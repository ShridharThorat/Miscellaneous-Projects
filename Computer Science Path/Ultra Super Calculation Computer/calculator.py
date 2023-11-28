# -------------------------------------------
# USCC Headquarter's Instruction Set Architecture
#  System Design:
#   - Four function calculator
#   - Can only operate on numbers stored in registers
#   - Processor receives binary data as 32-bit strings
#   - Returns results to the terminal
#   - Can operate on 10-bit numbers (0 thru 1023)
#   - Results can be negative (5 - 10 = -5)
#  Instruction format:
#   - 32 bit's in length
#   - Binary data will come to the CPU as a string
#   - Registers (32 total on CPU, 0-indexed)
#      - 0 thru 21:  Available for number storage
#        - 0: Constant 0
#      - 22 thru 31: Available for history storage
# +=======+=======+=======+=======+=======+=======+=======+=======+
# | 0: 0  | 1:    | 2:    | 3:    | 4:    | 5:    | 6:    | 7:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# | 8:    | 9:    |10:    |11:    |12:    |13:    |14:    |15:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |16:    |17:    |18:    |19:    |20:    |21:    |22: H0 |23: H1 |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |24: H2 |25: H3 |26: H4 |27: H5 |28: H6 |29: H7 |30: H8 |31: H9 |
# +=======+=======+=======+=======+=======+=======+=======+=======+
#   - Bits 0-5 are OPCODEs
#     - use variable 'opcode' in program
#   - Bits 6-10 & 11-15 are source register locations
#     - use variables 'source_one' and 'source_two' in program
#   - Bits 16-25 are reserved for adding a new value to the registers
#     - use variable 'store' in program
#   - Bits 26-31 are functions
#     - use variable 'function_code' in program
#   - 000000   00000       00000      0000000000      000000
#     opcode   source_1   source_2      store     function_code
# +--------+----------+-------------------------------------+
# | OPCODE | FUNCTION | Definition                          |
# | 000000 |  100000  | Add two numbers from registers      |
# | 000000 |  100010  | Subtract two numbers from registers |
# | 000000 |  011000  | Multiply two numbers from registers |
# | 000000 |  011010  | Divide two numbers from registers   |
# | 000001 |  000000  | Store value to next register        |
# | 100001 |  000000  | Return previous calculation         |
# +--------+----------+-------------------------------------+

# Your code below here:
from typing import Union


class UltraSuperCalculator:

    def __init__(self, name: str) -> None:
        self.name = name
        # given R0-R21 are for numbers
        self.number_registers = [0 for _ in range(22)]
        self.history_registers = [0 for _ in range(
            22, 32)]  # given R22-R31 are history

        # The index for the number register. Starts at 1 since R0 = 0.
        self.numbers_index = 1
        self.history_index = 0  # Index for the history registers
        # Index of the register after the latest used history register
        self.temp_history_index = 0

        self.user_display = ""  # Data to display to the user later
        self.update_display(f"Welcome to {self.name}'s Ultra Super Calculator")

    def update_display(self, to_update: str) -> None:
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store: str) -> None:
        # 1. Never overwrite the constant 0 stored at index 0
        # 2. If all your registers are full, begin overwriting the oldest registers
        if (self.numbers_index > 21):
            self.numbers_index = 1

        converted_value = int(value_to_store, base=2)
        self.number_registers[self.numbers_index] = converted_value
        print(
            f"Value: '{converted_value}' stored in Register_{self.numbers_index}")
        self.numbers_index += 1

    def load_value_from_register(self, register_address: int) -> int:
        index = int(register_address, base=2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store:int):
        if (self.history_index > 9):
            self.history_index = 0

        # Convert result to a binary and store it in a history register
        result_to_store = int(result_to_store)
        self.history_registers[self.history_index] = bin(result_to_store)
        # self.history_registers[self.history_index] = result_to_store
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2) -> int:
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

        calculated_value = num1 + num2
        return calculated_value

    def subtract(self, address_num1, address_num2) -> int:
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

        calculated_value = num1 - num2
        return calculated_value

    def multiply(self, address_num1, address_num2) -> int:
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

        calculated_value = num1 * num2
        return calculated_value

    def divide(self, address_num1, address_num2) -> int:
        """
        Divides the number in address_num1 by the number in address_num2. 

        Prints an error if the number in address_num2 is 0
        """
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0
        if num2 != 0:
            calculated_value = num1 / num2
        else:
            print(f"ERROR: Division by 0: {num1}/{num2}.")
        return calculated_value

    def get_last_calculation(self) -> None:
        self.temp_history_index -= 1  # Go back to the latest used history register number
        history_int_val = int(
            self.history_registers[self.temp_history_index],base=2)
        last_value = f"Last calculation was: {str(history_int_val)}"
        self.update_display(last_value)

    def binary_reader(self, instruction: str) -> None:
        """Reads 32-bit long string instructions"""
        if (len(instruction) != 32):
            self.update_display(
                "ERROR: Invalid Instruction Length\n\tInstructions must be 32-bits long")
            return
        # Based on ISA
        opcode = instruction[0:6]
        source_one = instruction[6:11]
        source_two = instruction[11:16]
        store = instruction[16:26]
        function_code = instruction[26:32]
        
        if opcode == '000001':
            self.store_value_to_register(store)
            return
        elif opcode == '100001':
            self.get_last_calculation()
            return
        elif opcode != '000000':
            self.update_display(f"ERROR: Invalid opcode: {opcode}")
            return

        result = 0
        if (function_code == '100000'):
            result = self.add(source_one, source_two)
        elif (function_code == '100010'):
            result = self.subtract(source_one,source_two)
        elif (function_code == '011000'):
            result = self.multiply(source_one, source_two)
        elif (function_code == '011010'):
            result = self.divide(source_one, source_two)
        else:
            self.update_display(f"ERROR: Invalid funcion_code: {function_code}")
            return
        
        # Store result
        self.store_to_history_register(result)
        self.update_display(f"The result is: {result}")


test = UltraSuperCalculator("bob")
# Adds 5 and 10 to number registers
test.binary_reader("00000100000000000000000101000000")
test.binary_reader("00000100000000000000001010000000")

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
test.binary_reader("00000000001000100000000000100000")
test.binary_reader("00000000001000100000000000100010")
test.binary_reader("00000000001000100000000000011000")
test.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
test.binary_reader("10000100000000000000000000000000")
test.binary_reader("10000100000000000000000000000000")
test.binary_reader("10000100000000000000000000000000")
