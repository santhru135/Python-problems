def comman_chars(list1, list2):
    for char in set(list1):
        if char in list2:
            count = min(list1.count(char), list2.count(char))
            for _ in range(count):
                list1.remove(char)
                list2.remove(char)
    return list1 + list2

if __name__ == "__main__":
    p1 = input("Enter 1st name: ").lower().replace(" ","")
    p2 = input("Enter 2nd name: ").lower().replace(" ","")
    
    p1_list = list(p1)
    p2_list = list(p2)
    remaining_elements = comman_chars(p1_list, p2_list)
    
    count = len(remaining_elements)
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >=0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames.pop()
            
    print(f"Relationship Status: {flames[0]}")