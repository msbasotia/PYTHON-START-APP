content = open("test_python.csv","r").read()

lines = content.split("\n")

header_row = lines[0]
header = header_row.split(",")

record_set = lines[1:]

records = []

for x in record_set:
    y = x.split(",")
    records.append(y)


# Sum of GMV

sum = 0
for i in range(len(records)):
    sum += float(records[i][4])

print(f"Sum of {header[4]} = {sum}") 

# Filtering out records with gb_tag = 1

custom_set = []
for i in range(len(records)):
    if int(records[i][2]) == 0:
        custom_set.append(records[i])

print("Filtered Rows are....")
for items in custom_set[:5]:
    print(items)

# print only item_id and gb_tag and convert to csv
    
new_record_set = [[header[3],header[2]]]    

for record in records:
    item_id = record[3]
    gb_tag = record[2]
    new_record = [item_id,gb_tag]
    new_record_set.append(new_record)


'''
to convert it to csv, it has to be converted to very original format
'''

set1 = []
for new in new_record_set:
    x = ",".join(new)
    set1.append(x)


set2 = "\n".join(set1)

f = open("out_csv_ops.csv","w")
f.write(set2)

print("New file is generated.....")
