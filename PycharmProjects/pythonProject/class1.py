lang=input('whats is your language?')
time_zone=input('what is the time?')
if lang == 'en':
    if time_zone == "mo":
        print("Good morning")
    elif time_zone == 'evening':
        print('Good evening')
    else:
        print('Hello')
elif lang == 'french':
    if time_zone == 'mo':
        print("Bonjour")
    elif time_zone == 'evening':
        print('Bonsoir')
    else:
        print('salut')
else:
    print('this language is not available')














