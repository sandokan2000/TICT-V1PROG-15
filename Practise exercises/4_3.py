def lang_genoeg(lengte):
    if lengte >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Helaas, je bent te klein!')
    return lengte
lengte = eval(input('Wat is uw lengte in centimeters? '))
lang_genoeg(lengte)