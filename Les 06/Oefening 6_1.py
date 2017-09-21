gewicht = eval(input('Wat is uw gewicht? '))
lengte = eval(input('Wat is uw lengte? '))
BMI = gewicht/lengte**2
if BMI< 18.5:
    print('U heeft ondergewicht')
elif BMI >18.5 and BMI <= 25:
    print('U heeft een nromaal gewicht')
else:
    print('U heeft overgewicht')