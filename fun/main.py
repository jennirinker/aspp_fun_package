def important_question():
    """Asks the most important question
    """
    
    
    with open('db.json', 'r') as fp:
        data = json.load(fp)
            
    resp = input('What is the best ice cream flavor? ').lower()
    while resp != 'coconut':
        if resp == 'fuck you':
            print('WELL FUCK YOU!')
        elif resp == 'chocolate':
            print('You are trying to be original, I guess?')
        elif resp == 'strawberry':
            print('Well I guess that is a fruit. But your taste still sucks.')
        elif resp == 'tiramisu':
            print('Really? You like coffee in your ice cream? Weird.')
        elif resp == 'vanilla':
            print('SO BORING.')
        elif resp == 'fuck zou':
            print("Oh you're german!")
        else:
            print('WRONG. YOU SUCK. TRY AGAIN.')
       
       )
       resp = input('What is the best ice cream flavor? ').lower()
        
    print('YOU HAVE EXCELLENT TASTE. NICE.')
    exit() 
