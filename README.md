## Logic Gates and Bitwise Operators


Operator     Symbol   Description                              Example (`5 & 3`)           
-----------------------------------------------------------------------------------------
AND           `&`     1 if both bits are 1                     `0101 & 0011 → 0001 (1)`    
OR            `|`     1 if at least one bit is 1               `0101 | 0011 → 0111 (7)`    
XOR           `^`     1 if bits are different                  `0101 ^ 0011 → 0110 (6)`    
NOT           `~`     Flips all bits (one's complement)        `~0101 → -0110 (-6)`      
Left Shift    `<<`    Shifts bits left, filling with 0         `0101 << 1 → 1010 (10)`   
Right Shift   `>>`    Shifts bits right, dropping right bits   `0101 >> 1 → 0010 (2)`   

## Adder

a + b
5 (0101) + 3 (0011)

- First Iteration

Calculate no_carry:
a ^ b = 0101 ^ 0011 = 0110 (this is like adding without carries).

Calculate carry: (a & b) << 1:
0101 & 0011 = 0001
0001 << 1 = 0010
Update:
a = 0110 (no_carry)
b = 0010 (carry) 

- Second Iteration (b != 0)

a ^ b = 0110 ^ 0010 = 0100

(a & b) << 1 
0110 & 0010 = 0010
0010 << 1 = 0100

Update:
a = 0100
b = 0100 

- Third Iteration (b != 0)

a ^ b = 0100 ^ 0100 = 0

(a & b) << 1 
0100 & 0100 = 0100
0100 << 1 = 1000

Update:
a = 0000
b = 1000 

- Fourth Iteration (b != 0)

a ^ b = 0000 ^ 1000 = 1000

(a & b) << 1 
0000 & 1000 = 0000
0010 << 1 = 0000

Update:
a = 1000
b = 0 

- Result

1000 = 8


## Multiplier

Init:
a = 5 (101)
b = 3 (011)
result = 0

First iteration:
- b & 1 = 011 & 001 = 1 (last bit is 1)
- result = 0 + 101 = 101
- a = 101 << 1 = 1010
- b = 011 >> 1 = 001

Second iteration:
- b & 1 = 001 & 001 = 1 (last bit is1)
- result = 101 + 1010 = 1111
- a = 1010 << 1 = 10100
- b = 001 >> 1 = 000

Third iteration:
- b is 0, finish
- result = 1111 (15)