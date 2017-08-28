def important_question():
    """Asks the most important question
    """
    resp = input('What is the best ice cream flavor? ').lower()
    while resp != 'coconut':
        print('WRONG. YOU SUCK. TRY AGAIN.')
        resp = input('What is the best ice cream flavor? ').lower()
        if resp == 'fuck you':
            print('WELL FUCK YOU!')
    print('YOU HAVE EXCELLENT TASTE. NICE.')
    return
