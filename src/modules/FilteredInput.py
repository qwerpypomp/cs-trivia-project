from enum import Enum

class _FreeInput():
    def __contains__(self,idc):
        return True
_FreeInputSingleton = _FreeInput()
def Input(Prompt, *args):
    if len(args) > 0 and type(args[0]) == Enum:
        ExpectedValues = tuple(x.value for x in args[0]) # ts syntax lowkey tuff
    elif len(args)==1:
        ExpectedValues = args[0]
    elif len(args)==0:
        ExpectedValues = _FreeInputSingleton
    else:
        ExpectedValues = args
            
    while(True):
        Check = input(Prompt).lower().strip()
        if(Check.isnumeric()):
            Check = int(Check)
        if(Check in ExpectedValues or len(ExpectedValues) < 1):
            return Check
        else:
            print("Invalid answer")