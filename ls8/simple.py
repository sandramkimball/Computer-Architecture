import sys

# ----- SIMPLE EXAMPLE -----
PRINT_BEES      = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4
PRINT_REGISTER  = 5
ADD             = 6 

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
pc = 0 
running = True #just a flag 

while running: #this is the processor
    command = memory[pc]

    if command = PRINT_BEES:
        print('Bees!')

    elif command == HALT:
        running = False

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

    else: 
        print(f'Unknown command: {command}')
        sys.exit(1)

    pc += 1


    # ########



filename = sys.argv[1]

def load_memory(filename):
    address = 0

    if len(sys.argv) != 2:
        print('usage: file.py filename')
        sys.exit(1)
    
    try: 
        with open(filename) as f:
            for line in f:
                # want to ignore comments
                comment_split = line.split('#')
                # stip out whitespace
                num = comment.split[0].strip()
                # ignore blank lines
                if num == '':
                    continue
                print(line)

                val = int(num)
                memory[address] = val
                address += 1
                
    except FileNotFoundError:
        print('File not found')
        sys.exit(2)