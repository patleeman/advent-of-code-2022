import copy
from collections import OrderedDict
c = copy.deepcopy


def part1(stacks, instructions):
    for instruction in instructions:
        parts = instruction.split(" ") 
        num_moved = int(parts[1])
        from_column = int(parts[3])
        to_column = int(parts[5])
        
        for _ in range(num_moved):
            item = stacks[from_column].pop(0);
            stacks[to_column].insert(0, item)
            print(instruction, item, stacks)

    stacks = [s[0] for _, s in stacks.items()]

    return "".join(stacks) 


if __name__ == "__main__":
    with open('exercise.txt') as f:
        data = f.read()
    
    data = data.split('\n')
    stacks = OrderedDict()
    for x in range(8):
        line = data[x]
        
        line = [line[i:i+4] for i in range(0, len(line), 4)]
        for i, crate in enumerate(line):
            num = i + 1
            if num not in stacks:
                stacks[num] = []
            
            crate = crate.strip()
            if not len(crate) <= 1:
                crate = crate[1]
                stacks[num].append(crate) 

    with open('data.txt') as f:
        data = f.read();
    instructions = data.split('\n')
    del instructions[-1]

    test_data = {
        1: ["A", "B"],
        2: ["C", "D"]
    }
    
    test_instructions = [
        "move 1 from 1 to 2",
        "move 2 from 2 to 1"
    ]
    output = part1(test_data, test_instructions)
    print(output)
    assert output == "CD"


    print(part1(c(stacks), c(instructions))) 
    
