import random

def random_color(base = (None, None, None)):
    r = base[0] or random.randint(0, 255)
    g = base[1] or random.randint(0, 255)
    b = base[2] or random.randint(0, 255)

    return r, g, b

def random_int2color_map(range_start, range_end):
    return {integer: get_random_color() for integer in range(range_start, range_end + 1)}

def get_random_color(base = (None, None, None), no_greys =False):
    r, g, b = random_color(base)
    
    if no_greys:    
        while r == b == g:
            r, g, b = random_color(base)
        return r, g, b
    else:
        return r, g, b
    
        
    