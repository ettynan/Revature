''' Maps requests to dispatcher '''
import project1.loans.handler as loans
import project1.users.handler as users
_MAP = {
    'loans': loans.LoanDispatcher(),
    'users': users.UserDispatcher(),

}
_CONTENT = {
    'home': ['static', 'login.html'],
    'apply':['static', 'apply.html'],
    'index':['static', 'index.html'],
}

def get_dispatcher(context: str):
    '''This function takes in a string "context" and returns the dispatcher associated with it.'''
    if context in _MAP:
        return _MAP[context]
    else:
        return None

def get_static_location(context: str):
    ''' This function takes in a string "context" and returns the file associated with it.'''
    if context in _CONTENT:
        return _CONTENT[context]
    else:
        return None