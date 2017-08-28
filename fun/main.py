def important_question():
    """Asks the most important question
    """
    resp = input('What is the best ice cream flavor? ').lower()
    while resp != 'coconut':
        if resp == 'fuck you':
            print('WELL FUCK YOU!')
        elif resp == 'tiramisu':
            print('Really? You like coffee in your ice cream? Weird.')
        elif resp == 'vanilla':
            print('SO BORING.')
        else:
            print('WRONG. YOU SUCK. TRY AGAIN.')
        resp = input('What is the best ice cream flavor? ').lower()
    print('YOU HAVE EXCELLENT TASTE. NICE.')
    exit() 
