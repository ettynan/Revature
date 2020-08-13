'''Defining loan behavior and attributes '''

class Loan():
    def __init__(self, loan_type=''):
        self.loan_type = loan_type
        self.status = 'pending'
        self.risk_score = 0.0
        self.credit_score = 0

        if loan_type == 'Mortgage':
            self.collateral_needed = 'Required'
            self.manager_approval = 'Risk Score'
            self.cosigner_needed = 'Optional'
        if loan_type == 'Car':
            self.collateral_needed = 'Required'
            self.manager_approval = 'Not Required'
            self.cosigner_needed = 'Optional'
        if loan_type == 'Personal':
            self.collateral_needed = 'Risk Score'
            self.cosigner_needed = 'Optional'
            self.manager_approval = 'Required'
        if loan_type == 'Student':
            self.collateral_needed = 'Not Required'
            self.manager_approval = 'Risk Score'
            self.cosigner_needed = 'Required'

    def set_cosigner_needed(self, info):
        '''Sets the cosigner  for the loan'''
        self.cosigner_needed = info

    def get_cosigner_needed(self):
        '''Returns the cosigner  for the loan'''
        return self.cosigner_needed

    def set_collateral_needed(self, info):
        '''Sets the collateral for the loan'''
        self.collateral_needed = info

    def get_collateral_needed(self):
        '''Returns the collateral  for the loan'''
        return self.collateral_needed

    def set_risk_score(self, info):
        '''Sets the risk score for the loan'''
        self.risk_score = info

    def get_risk_score(self):
        '''Returns the risk score for the loan'''
        return self.risk_score

    def set_credit_score(self, info):
        '''Sets the credit_score for the loan'''
        self.credit_score = info

    def get_credit_score(self):
        '''Returns the credit score for the user's loan'''
        return self.credit_score

    def set_status(self, status):
        '''Sets the status of the loan'''
        self.status = status

    def get_status(self):
        '''Returns the status of the loan'''
        return self.status

    def to_dict(self):
        '''Returns the dictionary representation of itself'''
        return self.__dict__

    def __str__(self):
        '''Returns a string representaion of an object'''
        string = self.loan_type + ' ' + self.cosigner_needed + ' '
        string += self.collateral_needed
        return string

    def __repr__(self):
        '''Returns representation of object'''
        return self.__str__()

    @classmethod
    def from_dict(cls, input_loan):
        '''Creates an instance of the class from a dictionary'''
        loan = Loan()
        loan.__dict__.update(input_loan)
        return loan