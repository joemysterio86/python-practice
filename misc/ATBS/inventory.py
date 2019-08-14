stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'radaway': 13, 'nukacola': 3, 'gatling gun': 1, 'ammo belt': 40}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInv(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory[addedItems[i]]+=1
        for i in addedItems:
            if i not in inventory:
                inventory[i]=0

addToInv(stuff,dragonLoot)
displayInventory(stuff)
