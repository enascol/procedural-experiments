def int2bin(possible_configurations, integer):
    bin_string_max_size = len(possible_configurations)
    binary = bin(integer).split("b")[1]
    
    return ("0" * (bin_string_max_size - len(binary))) + binary

def get_rule(rule_numer, possible_configurations):
    rule_bin = int2bin(possible_configurations, rule_numer)
    rules = {}

    for index, value in enumerate(rule_bin):
        configuration = possible_configurations[index]
        rules[configuration] = int(value)
    
    return rules

def get_rule_size(possible_configurations):
    config_set_size = len(possible_configurations)
    
    return 2 ** config_set_size