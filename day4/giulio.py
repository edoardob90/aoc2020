good_ids = 0
with open("input.txt") as f:
    for line in f:
        ll = line.split()
        current_id = []
        field_list = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]  # For now this is commented ,"cid"]
        while len(ll) != 0:
            for field in ll:
                current_id.append(field.split(":")[0])
            line = f.readline()
            ll = line.split()
        
        result =  all(elem in current_id  for elem in field_list)
        if result:
            good_ids += 1

print("There are", good_ids, "good IDs")
