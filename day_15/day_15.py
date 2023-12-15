import sys
from collections import defaultdict
input = open(sys.argv[1]).read().strip().split(',')

def hash_f(input_val: str) -> int:
    result = 0
    for char in input_val:
        result += ord(char)
        result *= 17
        result %= 256
    return result

result = [hash_f(value) for value in input] 
print(f"Part 1: {sum(result)}")

boxes = defaultdict(dict)

def insert_lens(label : str, lens :int) -> None:
    box = hash_f(label)
    boxes[box][label] = lens

for val in input:
    code = val.split('=')
    if len(code) > 1:
        insert_lens(code[0],int(code[1]))
    else:
        boxes[hash_f(code[0][:-1])].pop(code[0][:-1], None)

result = 0
for box, label_lenses in boxes.items():
    for pos, label in enumerate(label_lenses):
        result += (1 + box) * (pos + 1) * label_lenses[label]

print(f"Part 2: {result}")
