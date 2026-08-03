from typing import List

def read_integers() -> List[int]:
    result = input()
    str = result.split(",")
    int_list = []
    for s in str:
        int_list.append(int(s))

    return int_list
    
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
