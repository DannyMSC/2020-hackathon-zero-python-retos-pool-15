#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    pasw=""
    for n in range(passLen):
        pasw += "".join([random.choice(string.ascii_letters + string.digits) ]) 
    
    return pasw