def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        cijfer = False
        for c in newpassword:
            if c in '0123456789':
                cijfer = True
        return cijfer
    return False
res = new_password('vakProg17', 'python17')
# correct/true
print(res)
#zelfde/false
print(new_password('huProg17', 'huProg17'))
#Te kort/False
print(new_password('vakProg17', 'Pro17'))