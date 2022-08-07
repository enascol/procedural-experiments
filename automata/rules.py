import sys
sys.path.append("./")

import automata_rules

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

def get_rule(rule_number):
    return automata_rules.get_rule(rule_number, POSSIBLE_CONFIGURATIONS)
