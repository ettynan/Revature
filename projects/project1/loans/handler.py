''' A handler for Loan operations in our server '''
# External Modules
import json
from os import path
import urllib.parse
# Internal Modules
import project1.web.dispatch as dispatch
import project1.data.mongo as db
from project1.users.model import User, ApplicationInfo, ItemEncoder
from project1.loans.model import Loan
from project1.data.logger import get_logger
from project1.business.bank_operations import credit_score, cal_risk_score, approval

_log = get_logger(__name__)

class LoanDispatcher(dispatch.Dispatcher):
    '''Customer Dispatcher for Users'''
    def dispatch(self, path: list, method, r_body=None):
        '''dispatch takes in a path and request body and
           returns status code and response body as tuple'''
        _log.debug(r_body)
        if method == 'GET':
            return self.get_operations(path)
        if method == 'POST':
            return self.post_operations(path, r_body)

    def get_operations(self, path: list):
        '''Get operation for loans'''
        _log.debug('GET received on user dispatcher')
        if len(path) == 1:
            _log.debug('path[0]')
            _log.info('in path 1, show all loans for approval')
            loan_list = db.get_loans_needing_approval()
            _log.debug(loan_list)
            return (200, bytes(json.dumps(loan_list, cls=ItemEncoder), 'utf-8'))
        elif len(path) == 2:
            _log.info('Show a user\'s loans')
            _log.debug(path[1])
            user = db.get_user(path[1])
            user_loans = user.get_loans()
            return (200, bytes(json.dumps(user_loans, cls=ItemEncoder),
                               'utf-8'))

    def post_operations(self, path: list, r_body):
        '''POST operation for loan'''
        _log.debug('POST request received')
        _log.debug("len(path) = %s", len(path))

        if len(path) == 1:
            r_body_temp = json.loads(r_body.decode('utf-8'))
            _log.info("In loan handler. %s", r_body_temp)
            application = ApplicationInfo.from_dict(r_body_temp)

            loan = Loan(r_body_temp['loan_type'])
            value = r_body_temp['loan_type']
            if value == 'Car':
                loan.set_collateral_needed('Automobile')
            elif value == 'Personal':
                loan.set_collateral_needed('Real estate')
            elif value == 'Mortgage':
                loan.set_collateral_needed('House')

            risk = cal_risk_score(application)
            loan.set_risk_score(risk)
            credit = credit_score(application)
            loan.set_credit_score(credit)
            approval(loan, application)
            db.add_loan_application_to_user(r_body_temp['username'],
                                            application, loan)
            return (201, bytes(json.dumps(application, cls=ItemEncoder), 'utf-8'))

        if len(path) == 2:

            _log.info("in len equal 2 post")
            _log.debug(path)

            r_body_temp = json.loads(r_body.decode('utf-8'))
            loan = {'loan_type': r_body_temp['loan_type'],
                    'risk_score': r_body_temp['risk_score'],
                    'credit_score': r_body_temp['credit_score']}

            if r_body_temp['status'] == 'Approved':
                db.approve_loan(loan)
            elif r_body_temp['status'] == 'Denied':
                db.deny_loan(loan)
            return (200, bytes(json.dumps(loan, cls=ItemEncoder), 'utf-8'))

        return (401, b'Unauthorized')
