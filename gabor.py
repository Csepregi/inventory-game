inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("inventory:")


def display_inventory():
    print("count", "item name\n""---------\n")
    for value in inv:
        print(inv[value], value)


def add_to_inventory(inv, dragon_loot):
    for i in dragon_loot:
        if i in inv:
            inv[i] = inv[i] + 1
        else:
            inv[i] = 1

def print_table(order=False):
   if not order:
       display_inventory()
   elif order == "count,desc" or order == "count,asc":
       if order == "count,asc":
           reverse = False
       elif order == "count,desc":
           reverse = True

       longest_key = max(inv.keys(), key=len)
       longest_value = str(max(map(str, inv.values()), key=len))
       item_name_length = len(max([longest_key, "item name"], key=len))
       count_length = len(max([longest_value, "count"], key=len))
       edge = item_name_length + count_length + 2 + 10

       print("Inventory:")
       print("count".rjust(count_length + 2) + "item name".rjust(edge - (count_length +  2)))
       print("~" * edge)
       for item in sorted(inv, key=inv.get, reverse=reverse):
           print("%s%s" % (str(inv[item]).rjust(count_length + 2), item.rjust(edge - (count_length + 2))))
       print("~" * edge)
       print("Total number of items: %d" % sum(inv.values()))  

def import_inventory(filename):
   filename = "import_inventory.csv"
   with open(filename) as text:        
       text_lines = text.readlines() 
   key_value_list = []                  
   for line_index in range(1, len(text_lines)): 
       if ',' in text_lines[line_index]:       
           text_lines[line_index] = text_lines[line_index][:-1] 
           key_value_list.append(text_lines[line_index].split(',',1)) 
           
   ext_dict=dict(key_value_list) 
   for key in ext_dict: 
       if key in inv:
           inv[key] += int(ext_dict[key])
       else:
           inv.update({key:int(ext_dict[key])})

def export_inventory(filename="export_inventory.csv"):
    with open(filename, "a") as text:
        text.write("item_name,count\n")
        for x in inv:
            line = x + "," + str(inv[x]) + "\n"
            text.write(line)

   


add_to_inventory(inv, dragon_loot)
display_inventory()
print_table("count,asc")
import_inventory(filename)