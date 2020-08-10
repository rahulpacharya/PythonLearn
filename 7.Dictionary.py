############################################
## DICTIONARY
## Unordered collection of objects
## Key value pair
## Is mutable
############################################
print("Dictionary")
dict1 = {'John':15000,'Jane':34000}
print(dict1['John']) # 15000
dict1['John']=30000
print(dict1['John']) # 30000
print(dict1) # {'John': 30000, 'Jane': 34000}
del dict1['Jane'] 
print(dict1) # {'John': 30000}
dict1['Jacob'] = 45000  
print(dict1)  # {'John': 30000, 'Jacob': 45000}
print(dict1.keys()) # dict_keys(['John', 'Jacob'])
print(dict1.values()) # dict_values([30000, 45000])
print('*************************************')
d1=dict()
d2=dict(p="play",t="talk")
print(d2)  # {'p': 'play', 't': 'talk'}
d2.update(v="vibe",d="docs")
print(d2)  # {'p': 'play', 't': 'talk', 'v': 'vibe', 'd': 'docs'}
removed_value = d2.pop('v', 'No Key found')
print(removed_value) # vibe
print(d2) # {'p': 'play', 't': 'talk', 'd': 'docs'}
print('*************************************')
#############################################



inventory = {'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}
x = [i for i in inventory.values() if i < 0]
if len(x) != 0:
    print("error")
print(inventory)
#{'iPhone Model X': 100, 'Xiaomi Model Y': 1000, 'Nokia Model Z': 25}
new_stock = {'Redmi':34, 'MicroMax':334}
inventory.update(new_stock)

print("Inventory after addition: ", inventory)
# {'iPhone Model X': 100, 'Xiaomi Model Y': 1000, 'Nokia Model Z': 25, 
#  'Redmi': 34, 'MicroMax': 334}
requested_stock = {'Redmi':32,'Xiaomi Model Y':100}
print("requested_stock:", requested_stock)
# {'Redmi': 32, 'Xiaomi Model Y': 100}
modelFound=False
insufficientInventory=False

for r_k,r_v in requested_stock.items():
    for i_k,i_v in inventory.items():
        if r_k == i_k:
            modelFound=True
            if r_v > i_v:
                insufficientInventory=True
                break
            inventory[r_k] = int(i_v-r_v)
            break

print("Model Found: ",modelFound) #True
print("insufficientInventory: ",insufficientInventory) #False

print("Inventory: ", inventory)
# {'iPhone Model X': 100, 'Xiaomi Model Y': 900, 'Nokia Model Z': 25,
# 'Redmi': 2, 'MicroMax': 334}

# A way to check if atleast one key exists of type string
x=set(map(type, inventory.keys()))
print(x)
if x == {str}:
    print("in if where inventory matches")
    
inventory1  = {}
y = set(map(type, inventory1.keys()))
print(y)
if y == set():
    print("in empty set match if")

#############################################