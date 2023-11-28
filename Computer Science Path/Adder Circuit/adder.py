from gate import NAND_gate, XOR_gate, AND_gate, OR_gate, NOT_gate, ERROR_check_bulk


def half_adder(a: int, b: int) -> tuple[int, int]:
    ERROR_check_bulk([a, b])

    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return (s, c)


try:
    assert half_adder(0, 0) == (0, 0)
    assert half_adder(0, 1) == (1, 0)
    assert half_adder(1, 0) == (1, 0)
    assert half_adder(1, 1) == (0, 1)
    print("Half adder correct")
except Exception as e:
    print("ERROR: Half adder failed")


def full_adder(a: int, b: int, c: int) -> tuple[int, int]:
    ERROR_check_bulk([a, b, c])
    s_1, c_1 = half_adder(a, b)
    s, c_2 = half_adder(s_1, c)

    c_out = OR_gate(c_1, c_2)
    return (s, c_out)


try:
    assert full_adder(0, 0, 0) == (0, 0)
    assert full_adder(0, 0, 1) == (1, 0)
    assert full_adder(0, 1, 0) == (1, 0)
    assert full_adder(0, 1, 1) == (0, 1)
    assert full_adder(1, 0, 0) == (1, 0)
    assert full_adder(1, 0, 1) == (0, 1)
    assert full_adder(1, 1, 0) == (0, 1)
    assert full_adder(1, 1, 1) == (1, 1)
    print("Full adder correct")
except Exception as e:
    print("ERROR: Full adder failed")


def ALU(a: int, b: int, c: int, opcode: int):
    ERROR_check_bulk([a, b, c, opcode])
    if opcode == 0:
        s, c = half_adder(a, b)
    elif opcode == 1:
        s, c = full_adder(a, b, c)
    return (s, c)

try:
    assert ALU(0, 0, 1, 0) == half_adder(0, 0)
    assert ALU(0, 0, 1, 1) == full_adder(0, 0, 1)
    assert ALU(1, 1, 1, 0) == half_adder(1, 1)
    assert ALU(1, 1, 1, 1) == full_adder(1, 1, 1)
    print("ALU correct")

except Exception as e:
    print("ALU failed")
