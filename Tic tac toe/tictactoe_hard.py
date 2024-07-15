                  #Player vs Computer(AI) hard level
                    #a bit incomplete 
import random
array =["1","2","3","4","5","6","7","8","9"]
Number_left = [1,2,3,4,5,6,7,8,9]
def setup():
    global array
    print(array[0]," | " ,array[1], " | ", array [2])
    print(array[3]," | " ,array[4], " | ", array [5])
    print(array[6]," | " ,array[7], " | ", array [8])
# Use X for player
# Use O for Computer
def firstmove():
    global array, Number_left
    print("Wanna go first or give me chance")
    print("If you wanna go first enter 1")
    print("If u want to challenge me press 2")
    turn = int(input())
    while turn != 1 and turn != 2:
        print("You entered wrong value, please enter again")
        turn= int(input())
    if turn ==  1:
        print("which value u wanna go first")
        Value1 = int(input())
        Number_left.remove(Value1)
        Value1 -=1
        array[Value1] = "X"
    else:
        array[0] = "O"
    setup()
    print("___________________")
    return turn
def X_checker(location):
    for x in range(len(array)):
        if array[x] == ("X"):
            location.append(x)
    return location
def O_checker(location):
    for x in range(len(array)):
        if array[x] == ("O"):
            location.append(x)
    return location
def completed_algorithm(location):
    check = False
    diff = []
    if len(location) >= 3:
        for x in range(len(location) -1):
            d = location[x +1] -location[x]
            diff.append(d) 
        x = 1
        check = False
        while x <= len(location) -2 and check == False:
            if diff[x-1] == 1 and diff[x] == 1 and location[x] %3 ==0:
                check = True
            elif diff[x- 1] == 2 and diff[x] == 2 and location[0] %2 == 0:
                check = True
            elif diff[x-1] ==3 and diff[x] == 3:
                check = True
            elif diff[x-1] == 4 and diff[x] ==4:
                check = True
            x +=1
    return check
def check_if_completed():
    global array
    location_player = []
    check_player = False
    X_checker(location_player)
    check_player = completed_algorithm(location_player)
    location_comp = []
    check_computer = False
    O_checker(location_comp)
    check_computer = completed_algorithm(location_comp)
    return check_player, check_computer
def main_algorithm(location, rand_value):
    global array
    diff = []
    change = False
    change_loc = 0
    count_change = 0
    done = []
    if len(location) >= 2:
        for x in range(len(location) - 1):
            for y in range(1,len(location)):
                diff.append(location[y] - location[x])
        for x in range(len(diff)):  
            z = 0
            while z<= len(diff) and z<= count_change and len(done) != 0:
                y = 0
                while y<= len(done) and y<= count_change:
                    if diff[z] == done[y]:
                        diff.remove(done[y])
                    y +=1
                z +=1 
            change = True       
            if diff[x] % 4 == 0:                                      
                if diff[x]/4 ==2:                                      
                    change_loc = 4                                
                if location[1]/4 ==1 and location[0] == 0:        
                    change_loc = 8
                if location[1]/4 ==2 and location[0] == 4:
                    change_loc = 0    
                else: 
                    change_loc = 4                            
            elif diff[x] == 2:
                if location[1] == 4 and location[0] == 2:
                    change_loc =6
                elif location[1] == 6 and location[0] == 4:
                    change_loc = 2  
                match location[1]:
                    case 2:
                        change_loc =1
                    case 5:
                        change_loc =4
                    case 8:
                        change_loc = 7
            elif diff[x] ==1:
                if location[1] +1 % 3 == 0:
                    change_loc =location[0] -1
                else:
                    change_loc =location[1] +1
            elif diff[x] % 3 == 0:
                if diff[x]/3 ==2:
                    change_loc = location[0] +3
                elif location[0] <= 2:
                    change_loc = location[1] +3
                else: change_loc = location[0] -3 
            else:
                change = False
            if change == True:
                done.append(change_loc)
                count_change +=1
    return change, change_loc
        
def computer_play(rand_value):
    global array, Number_left
    location_player = []
    X_checker(location_player)
    location_comp = [] 
    O_checker(location_comp)    
    change, change_loc =main_algorithm(location_comp, rand_value)
    for x in range(len(location_player)):
        if change_loc == location_player[x] and len(location_player) != 1:
            change = False
    if change == False:
        change,change_loc = main_algorithm(location_player, rand_value) 
        if change == False:
            Com_Val = Number_left[rand_value]
            Number_left.remove(Com_Val)
            Com_Val -=1
            array[Com_Val]= "O" 
    if change == True:
        array[change_loc] = "O"
        change_loc += 1
        Number_left.remove(change_loc)
def verication_user_imput(value):
    location =[]
    X_checker(location)
    for x in range(len(location)):
        location[x] +=1
        while value == location[x]:
            print("You have entered already present value, Please enter again")
            value = int(input())
    return value
#main
setup()
turn = firstmove()
check_player = False
check_computer = False
while check_player == False and check_computer == False and len(Number_left) != 0:
    if turn == 1:
        rand_value = random.randint(1, len(Number_left) -1)
        computer_play(rand_value)
        setup()
        print("Please enter next move")
        check_player,check_computer = check_if_completed()
        if check_computer == False and check_player == False:
            value = int(input())
            value =verication_user_imput(value)
            Number_left.remove(value)
            value -= 1
            array[value] = "X"
            print("___________________")
            setup()
            check_player,check_computer = check_if_completed()
    if turn == 2:
        print("Please enter next move")
        value = int(input())         
        value =verication_user_imput(value)
        Number_left.remove(value)
        value -= 1
        array[value] = "X"
        setup()
        rand_value = random.randint(1, len(Number_left) -1)
        computer_play(rand_value)
        setup()
        check_player,check_computer = check_if_completed()         
if check_player == True:
    print("Congratulations u have won")
elif check_computer == True:
    print("Unlucky computer has won.. Make sure to Try Again")
else: print("Unlucky You have drawn ")  
