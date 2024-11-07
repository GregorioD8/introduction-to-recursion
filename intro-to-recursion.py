def recursive_count(count):
    if count < 10: 
        print(count)
        recursive_count(count + 1) # Recursive call with incrementated count

recursive_count(6) # Expected return: 6 7 8 9