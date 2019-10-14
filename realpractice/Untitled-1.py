fruitList = ["kiwi","apple","banana","cherry","blueberry","strawberry","pamplemousse"]


otherList = {
    "1": {"color": "green", "fruit": "apple"},
    "2": {"color": "red", "fruit": "strawberry"},
    "3": {"color": "blue", "fruit": "blueberry"}
}

for fruit, fruit_info in otherList.items():
    print("\nID: " + fruit)
    for key in fruit_info:
        print(key + ": " + fruit_info[key])

def fruitLoop(arg):
    dot = ""
    for x in arg:
        dot += "."
        print(x + dot)

fruitLoop(fruitList)
# just a quick note





