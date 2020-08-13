
from project1.users.model import ApplicationInfo
from project1.loans.model import Loan
from project1.data.logger import get_logger

_log = get_logger(__name__)

_RISK = {
'''Assign risk score to letter'''
    'a': 2, 'b': 1.95, 'c': 1.90, 'd': 1.85,
    'e': 1.80, 'f': 1.75, 'g': 1.70, 'h': 1.65,
    'i': 1.60, 'j': 1.55, 'k': 1.50, 'l': 1.45,
    'm': 1.40, 'n': 1.35, 'o': 1.30, 'p': 1.25,
    'q': 1.20, 'r': 1.15, 's': 1.10, 't': 1.05,
    'u': 1.00, 'v': .95, 'w': .90, 'x': .85,
    'y': .80, 'z': .75
}

_CREDIT = {
    '''Assign credit score to letter'''
    'a': 800, 'b': 760, 'c': 720, 'd': 680,
    'e': 640, 'f': 600, 'g': 560, 'h': 520,
    'i': 480, 'j': 440, 'k': 400, 'l': 360,
    'm': 320, 'n': 320, 'o': 360, 'p': 400,
    'q': 440, 'r': 480, 's': 520, 't': 560,
    'u': 600, 'v': 640, 'w': 680, 'x': 720,
    'y': 760, 'z': 800
}

'''Division between good and bad risk'''
RISK_THRESHOLD = 1.50
CREDIT_THRESHOLD = 600

def approval(loan: Loan, applicationInfo: ApplicationInfo):
    _log.debug(loan)
    _log.info("In approval function")

    if loan.loan_type == 'Student':
        if loan.cosigner_needed != 'Required' and loan.risk_score <= RISK_THRESHOLD:
            loan.status = 'Approved'
        elif loan.cosigner_needed == 'Required' and loan.risk_score <= RISK_THRESHOLD:
            loan.status = 'Co-signer Needed'
        else:
            loan.status = 'Co-signer Needed'

    elif loan.loan_type == 'Mortgage':
        if loan.collateral_needed != 'Required' and loan.risk_score <= RISK_THRESHOLD:
            loan.status = 'Approved'
        elif loan.collateral_needed == 'Required' and loan.risk_score <= RISK_THRESHOLD:
            loan.status = 'Collateral Needed'
        else:
            loan.status = 'Loan Manager Approval Needed'

    elif loan.loan_type == 'Car':
        if loan.collateral_needed != 'Required' and loan.risk_score <= RISK_THRESHOLD:
            loan.status = 'Approved'
        elif loan.collateral_needed == 'Required' and loan.risk_score <= RISK_THRESHOLD:
            loan.status = 'Collateral Needed'
        else:
            loan.status = 'Denied'
    else:
        if loan.risk_score >= RISK_THRESHOLD and loan.collateral_needed == 'Risk Score':
            loan.collateral_needed = 'Required'
            loan.status = 'Collateral Needed'
        else:
            loan.status = 'Loan Manager Approval Needed'

def credit_score(application_info: ApplicationInfo):
    '''takes in application info and returns the credit score for a user'''
    letter = application_info.firstname[0].lower()
    if letter == 'a':
        letter = 'b'
    credit_score = _CREDIT[letter]
    return credit_score

def cal_risk_score(application_info: ApplicationInfo):
    '''Takes in customer application info and returns a risk_score for a user'''
    letter = application_info.lastname[0].lower()
    if letter == 'a':
        letter = 'b'
    risk_score = _RISK[letter]
    return risk_score