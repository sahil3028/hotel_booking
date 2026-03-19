import json
import re

with open("rooms.json",'r')as file:
    data=json.load(file)

rooms=data.get("rooms",[])

def view_room(room=rooms,c=0):
    for r in room:
        c+=1
        print( f"\t{c} room")
        if not r['occupied']:
            print(f"{r["room_no"]} - {r["type"]}" + f"\nprice- {r["price"]}\navailable \n\n")
        else:
            print(f"{r["room_no"]} - {r["type"]}" + f"\nprice- {r["price"]}\nnot available \n\n")

def check_in():
    try:
        num=input("Enter the room number- ")
        num=int(num)
    except ValueError:
        print("The room number should be in num!!!")
        return()
    for r in rooms:
        if r["room_no"]== num:
            if r["occupied"]:
                print("That room is currently occupied")
                return()
            else:
                guest=input("Guest Name: ")
                try:
                    night = int(input("Enter the no of night stay: "))
                    if night <=0:
                        raise ValueError
                except ValueError:
                    print("the number of nights must be in number more than 0")
                    return check_in()
                c=input(f"your total will be {night*r["price"]} for {night} nights. \n do you confirm? (y/n)")
                if c.lower()=="y":
                    r["guest"]=guest
                    r["nights"]+=night
                    r["revenue"]+=night*r["price"]
                    r['occupied']=True
                    return
                elif c.lower()=="n":
                    print("ok")
                    return
                else:
                    print("Invalid Choice. canceling booking")
                    return
    print("Invalid RoomNo")
    return None


def check_out():
    try:
        num = int(input("Enter the room number- "))
    except ValueError:
        print("The room number should be in num!!!")
        return

    for r in rooms:
        if num==r["room_no"]:
            if r["occupied"]:
                r["occupied"]=False
                r['guest']=None
                r["nights"]=0
                print("check-out!!")
                return
            else:
                print("room is not occupied")
                return
    print("room doesnt exist")

def search_room():
    print("Describe your room:")
    prompt = input("Search: ").lower()

    avl = None
    rType = None
    price = []

    if "available" in prompt:
        avl = False

    if "deluxe" in prompt:
        rType = "Deluxe"
    elif "standard" in prompt:
        rType = "Standard"
    elif "suite" in prompt:
        rType = "Suite"

    price = re.findall(r'\d+', prompt)

    if price:
        pList = [int(x) for x in price]
        hP = None
        lP = None

        if len(pList) == 2:
            hP = max(pList)
            lP = min(pList)

        elif len(pList) == 1:
            if "under" in prompt or "less" in prompt or "below" in prompt:
                hP = pList[0]
                lP = 0
            elif "more" in prompt or "above" in prompt:
                lP = pList[0]
                hP = 999999
    else:
        hP = None
        lP = None

    count=0

    for r in rooms:
        if (
            (avl is None or r["occupied"] == avl) and
            (rType is None or r["type"] == rType) and
            (hP is None or lP <= r["price"] <= hP)
        ):
            pasvar=[r]
            view_room(pasvar,count)
            count += 1

def save():
    data= {"rooms":rooms}
    with open("rooms.json",'w') as file:
        json.dump(data,file,indent=4)

while True:
    ch=int(input("MENU\n1. View all rooms\n2. Check-in guest\n3. Check-out guest\n4. Search rooms\n5. Generate hotel report\n6. Save & Exit"))

    match ch:
        case 1:
            view_room()
        case 2:
            check_in()
        case 3:
            check_out()
        case 4:
            search_room()
        case 6:
            save()
            print("exit")
            break