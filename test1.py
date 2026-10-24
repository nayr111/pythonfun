n = int(input())
m = int(input())
def chicken_nuggets(n, m):
    if n <= 0 and m <= 0:
        return "Please order a positive number of nuggets and indicate how many boxes of nuggets you would like to order."
    if n > 100 and m > 10: 
        return "We apologize, but we cannot fulfill orders of more than 100 nuggets and more than 10 boxes."
    elif n <= 0:
        return "Please order a positive number of nuggets."
    elif n > 100:
        return "We apologize, but we cannot fulfill orders of more than 100 nuggets."
    elif m <= 0:
        return "Please indicate how many boxes of nuggets you would like to order."
    elif m > 10:
        return "We apologize, but we cannot fulfill orders of more than 10 boxes."
    else:
        total_nuggets = n * m
        return f'You have ordered {total_nuggets} nuggets in total.'
print(chicken_nuggets(n, m))
