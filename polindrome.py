
def polindrome(func):
    def pol(text):
        dec=func(text)
        
        if dec == dec[::-1]:
              return "this is polidrome"
        else:
            return 'Its not a polindrome'
    return pol    
        







@polindrome
def polin(word):
    return word


print(polin("dad"))
