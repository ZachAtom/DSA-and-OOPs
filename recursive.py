def countdown(i):
    print(i)
    if i > 1:
         countdown(i-1)
    else:
         return
countdown(3)