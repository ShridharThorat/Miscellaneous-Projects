# Adder Circuit
At the most basic level, the computer you are typing on right now is a complex combination of the gates you have already learned how to construct. But how do we go from having a NAND gate, for example, to having an entire processor that runs Mac OS?

One step we can take towards this goal is to create an ALU, or an Arithmetic Logic Unit. An ALU can perform a bunch of bitwise operations like adding, subtracting, and shifting.

For this project, we are going to focus on creating one part of the ALU, the adder.

A full adder is normally comprised of two half adders. A half adder takes in two inputs, `a` and `b`, and returns a sum bit, `s`, and a carry bit, `c`. The truth table looks like this:
    
    | a | b | s | c |
    | 0 | 0 | 0 | 0 |
    | 0 | 1 | 1 | 0 |
    | 1 | 0 | 1 | 0 |
    | 1 | 1 | 0 | 1 |

When we add `0` to `0`, we should get a sum of `0` with a carry of `0`. When we add `0` to `1`, we should get a sum of `1`, with a carry of `0`. And so on.

The full adder takes in `a`, `b`, and a carry-in bit `c`. It returns a sum bit `s` and a carry-out bit `c_out`. The truth table looks like this:

    | a | b | c | s | c_out |
    |---|---|---|---|-------|
    | 0 | 0 | 0 | 0 |   0   |
    | 0 | 0 | 1 | 1 |   0   |
    | 0 | 1 | 0 | 1 |   0   |
    | 0 | 1 | 1 | 0 |   1   |
    | 1 | 0 | 0 | 1 |   0   |
    | 1 | 0 | 1 | 0 |   1   |
    | 1 | 1 | 0 | 0 |   1   |
    | 1 | 1 | 1 | 1 |   1   |

## Instructions

### Building a Half-Adder
- [x] **1.** Create a function called half_adder() that will take in a and b. For now, we’re just going to calculate the sum bit s and return it.</br>
    We have provided all of the logic gates you have been working with so far: `NAND`, `NOT`, `AND`, `OR`, and `XOR`.
    </br>

    Use logic gates to calculate the sum bit from `a` and `b`, store it in the variable `s` and return it.
</br>

- [x] **2.** Now, we are going to calculate the carry-bit. Create a variable called c, and in it, use a combination of gates to determine the carry-bit from the sum of a and b.</br>    
    Return both the s and the c bit from the half_adder():
    `return (s, c)`
</br>

- [x] **3.** Test out your half-adder by printing out the output when:
    - a is 0 and b is 0
    - a is 0 and b is 1
    - a is 1 and b is 0
    - a is 1 and b is 1

    Does it produce the results you expect?


### Building the Full Adder
- [x] **4.** Nice! Now we have a half adder that can sum two bits. We can use two of these half adders to create a full adder that can take in a, b, and a carry-bit c and produce a sum and carry. </br>
    Create a function called `full_adder()` that takes in inputs `a`, `b` and `c`. For now, just create variables `s` and `c_out`, set them to `0`, and return `(s, c_out)`. 
</br>

- [x] **5.** Use a combination of two half adders to create the sum bit `s`. One of the outputs of one half adder should go into the next one. Can you figure out which?
</br>

- [x] **6.** To produce the carry-out bit, use a combination of an OR gate and the two half adders you used to create the sum bit `s`.
</br>

- [x] **7.** Test out your full adder by printing the output from a bunch of different inputs, like:

    - a is 0, b is 0, and c is 0
    - a is 1, b is 1, and c is 1
    - a is 0, b is 1, and c is 1
    - a is 1, b is 1, and c is 0

    Does it produce the results you expect? Refer to the truth table to see what we expect the output of the full adder to be.


### Make the Structure of the ALU
- [x] **8.** At this point, we can make an ALU that takes in inputs and either produces output from a half adder or from a full adder. <br>
    The ALU will take in a bit called the `opcode`, which determines what operation the ALU should perform. For our purposes, if the `opcode` is `0`, we will return the output from the `half_adder()` you wrote. If the opcode is `1`, we will return the output from the `full_adder()` you wrote. <br>
    For now, just define a function called `ALU()` and have it take in `a`, `b`, `c`, and `opcode`.
<br>

- [x] **9.** Inside the `ALU()`, we need two branches to decide which function to call. 
    <br>

    When the opcode is `0`, `s` and `c` should equal the return values of `half_adder(a, b)`.
    <br>

    When the opcode is 1, s and c should equal the return values of `full_adder(a, b, c)`

    Create this logic and return `s` and `c` from `ALU()`.
<br>

- [x] **10.** Test out your ALU by printing the output from a bunch of different inputs, like:

    - a is 0, b is 0, c is 1 and opcode is 0 (we want a half-add)
    - a is 0, b is 0, c is 1 and opcode is 1 (we want a full-add)
    - a is 1, b is 1, c is 1 and opcode is 0 (we want a half-add)
    - a is 1, b is 1, c is 1 and opcode is 1 (we want a full-add)
    
    Does your ALU produce the results you expect?
<br>

- [x] **11.** Wow! You have a basic Arithmetic Logic Unit that can produce different outputs with the same inputs. <br>

    Most ALUs also allow for incrementing, decrementing, and subtraction. Can you figure out how to implement incrementation (adding 1 to a) in your ALU? You will probably need a bigger opcode!