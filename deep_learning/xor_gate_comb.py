import numpy as np
import nand_gate as NAND
import or_gate as OR
import percept_bias as AND

def XOR(x1, x2):
    r1 = NAND.NAND(x1, x2)
    r2 = OR.OR(x1, x2)
    return AND.AND(r1, r2)

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))
