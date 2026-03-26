def hanoi_solver(total_discs):
    """
    Solves the Tower of Hanoi puzzle for a given number of discs
    Args: total_discs: Number of discs to solve for
    Returns: A string representing each move taken to solve the puzzle
    """

    rod1, rod2, rod3 = [], [], [] # Setting up rods
    result = ''
    
    # initializing rod1 with total_discs from largest to smalled
    for n in range(total_discs, 0, -1):
        rod1.append(n) 
        
    current_state = f"{rod1} {rod2} {rod3}\n"
    result += current_state
    
    def move(n, source, target, aux):
        """Recursively moves n discs from source to target using aux"""
        
        nonlocal result # nonlocal so that the accumulated string isn't lost every time the function is recursively called
        
        # Recursion Base Case
        if n <= 0:
            return
        
        move(n - 1, source, aux, target) # Moves n - 1 disc out of the way
        disc = source.pop() # Taking disc off rod
        target.append(disc) # Adding it to next rod
        
        # Update current positions of rods
        current_state = f"{rod1} {rod2} {rod3}\n" 
        result += current_state
        
        move(n - 1, aux, target, source) # Move n-1 discs to target
        
    move(total_discs, rod1, rod3, rod2) 
        
    return result.rstrip('\n') # Get rid of trailing \n

# --> Example Usage <--
print(hanoi_solver(2))
print(hanoi_solver(3))
print(hanoi_solver(4))
print(hanoi_solver(5))