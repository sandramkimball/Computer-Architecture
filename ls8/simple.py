import sys

# ----- SIMPLE EXAMPLE -----
PRINT_BEES      = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4
PRINT_REGISTER  = 5
ADD             = 6 
PUSH            = 7
POP             = 8

#then create memory to store this in:
memory = [
    PRINT_BEES,
    SAVE,
    65, 
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT
] # needs a pointer; use a program counter(pc):

memory = [None] * 256
register = [0] * 8 # xtrmly fast, small data grps (ie a word) baked into hardware, NOT MEMORY 
cache #lil slower than yet bigger than rgstr

SP = 7 # R7 is reserved as SP
pc = 0 
running = True #just a flag 

while running: #this is the processor
    command = memory[pc]
    print(memory)
    print(register)
    print('------')

    if command = PRINT_BEES:
        print('Bees!')
        pc += 1

    elif command == HALT:
        running = False
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc+1] 
        print(num)
        pc += 2

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3

    elif command == PUSH:
        reg = memory[pc + 1]
        val = register[reg]
        #decrement the stack pointer (SP)
        register[SP] = (register[SP] - 1) % (len(memory))
        #copy value from stack at given reg to the address
        memory[register[SP]] = val
        pc += 2 # 2 because we had 1 arg

    elif command == POP:
        reg = memory[pc + 1]
        val = memory[register[SP]]
       # copy value from address to the memory
       register[reg] = val
       # increment SP
       register[SP] += 1
       pc += 2

    else: 
        print(f'Unknown command: {command}')
        sys.exit(1)

    pc += 1


    #########



filename = sys.argv[1]

def factorial(n):
    if n <= 1: # base case (without recursion, stack overflow happens)
        return 1
    return n * factorial(n-1) # pop it off the stack
print factorial(5)

# push - update pointer and memory
# pop - update pointer and register

