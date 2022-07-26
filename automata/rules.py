POSSIBLE_CONFIGURATIONS = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
][::-1]

def int2bin(integer):
    binary = bin(integer).split("b")[1]
    return ("0" * (8 - len(binary))) + binary

def get_rule(rule_numer):
    rule_bin = int2bin(rule_numer)
    rules = {}

    for index, value in enumerate(rule_bin):
        configuration = POSSIBLE_CONFIGURATIONS[index]
        rules[configuration] = int(value)
    
    return rules