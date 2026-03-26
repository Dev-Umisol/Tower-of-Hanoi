def hanoi_solver(total_discs):
    rod1, rod2, rod3 = [], [], [] # Setting up rods
    result = ''
    
    for n in range(total_discs, 0, -1):
        rod1.append(n) # Adds the disc to the first rod
        
    current_state = f"{rod1} {rod2} {rod3}\n"
    result += current_state
    
    def move(n, source, target, aux):
        nonlocal result # nonlocal so that the accumulated string isn't lost every time the function is recursively called
        
        # Recursion Base Case
        if n <= 0:
            return
        
        move(n - 1, source, aux, target)
        disc = source.pop() # Taking disc off rod
        target.append(disc) # Adding it to next rod
        
        current_state = f"{rod1} {rod2} {rod3}\n"
        result += current_state
        
        move(n - 1, target, aux, source)
        
        
        
        
        