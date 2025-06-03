import random 
size = random.randint(3,10)
arr_econ = [] #a list of all the coordinates

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def make_array(): #makes different sizes of array and randomly fills in X or O. X is unavailable and O is available
    arr = []
    for i in range(size):
        row = []
        for j in range(size):
            random_num = random.randint(0,1)
            if random_num == 0:
               row.append("X")
            else: 
                row.append("0")
        arr.append(row)
    return arr 
    
arr = make_array()
#makes a list of all the possible coordinate available for seating (for economy)    
def make_board_2():
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j] == "0"):
                arr_econ.append(str(i)+str(j))
#makes the plane seating 
def make_board():
    string = ""
    for i in range(len(arr)):
        string += "\n"
        for j in range(len(arr)):
            if arr[i][j] == "X":
                string += colors.RED + "X" + colors.END
            else:
                string += colors.GREEN + "0" + colors.END
    print(string)
    
#make sure that a place is not taken when requested for 
def place(row, col): #place an X or O if it can be placed (so if there is " ")
    if arr[row-1][col-1] == "0": #1 because we ask the customer from 1-3, not 0-2
        return True
    else:
        print("That spot is taken. Choose another spot.")
        return False
        
def display():
    make_array()
    print("Ta(N)^2: Niki Jiang, Tamiyyah Shafiq, and Nia Lam")
    start = input(colors.HEADER + "Welcome to Angry Bird airlines. " + colors.END + "Do you want to buy a seat?: yes/no ").lower()
    if start == "yes":
         run_sim() #while loop for continous running
    elif start == "no":
        print("We are sorry to hear that. You just missed out on a once-in-a-lifetime opportunity to receive a free flight from Angry Birds airlines.")
    else:
        print("Please type yes/no. ")

def run_sim():
    make_board()
    make_board_2()
    tier = input("\nWhat tier?: economy/regular ").lower()
    if(not tier == "economy" and not tier == "regular"): #error cases 
        print("Please enter a valid tier.")
        return
    seats = int(input("\nHow many seats do you want?: "))
    seats_dup = seats
    if seats < 1: #error cases 
        print("Sorry, please enter a valid number.")
        return
    if seats > len(arr_econ):
        print("Sorry, there are not enough seats available.")
        return
  #  if seats > len(arr) * len(arr[0]): #error cases 
  #      print("Sorry we do not have enough seats. Please try another airline.")
  #      return
    else: 
        if tier == "regular": #if the tier is regular, we let the user choose their spots and it runs for as many seats they want 
             while seats_dup > 0:
                row = int (input("\n You have " + str(seats_dup) + " seats remaining. \n" + "\nSelect your spot. First give us the row (1, 2, 3): "))
                col = int (input("Then give us the column (1, 2, 3): "))
                if(place(row,col)):
                    seats_dup -= 1
                    arr[row-1][col-1] = "X"
                    print("Seat " + str(row+1) + col_to_let(col) + " has been booked.")
        if tier == "economy": #if the user choose economy and the number of seats exceed the number of columns in a row, it will do random seating; otherwise it would do consecutive seating 
            if seats > len(arr[0]):
                for i in range(seats):
                    random_seating()
            else: 
                    econ_cor = consecutive_seating(seats)
                    if econ_cor == [-1, -1]:
                        for i in range(seats):
                            random_seating()
                    else:
                        econ_x = econ_cor[0]
                        econ_y = econ_cor[1]
                        for i in range(seats):
                            arr[econ_x][econ_y+i] = "X"
                            print("Seat " + str(econ_x+1) + col_to_let(econ_y+i) + " has been booked.")
                       
    make_board()
    print("\nThank you for flying with Angry Birds!")

def random_seating():
    random_coordinate = int(random.random() * len(arr_econ)) #give a random number to pick a random index of the list 
    x_cor = int(arr_econ[random_coordinate][0]) #store the xcor of the coordinate 
    y_cor = int(arr_econ[random_coordinate][1]) #store the ycor of the coordinate 
    if(place(x_cor+1,y_cor+1)): #using the place method to see if we can add a person at that place
        print("Seat " + str(x_cor+1) + col_to_let(y_cor) + " has been booked.")
        arr[x_cor][y_cor] = "X"
        arr_econ.remove(arr_econ[random_coordinate]) #we remove the coordinate from the list after putting a person at that place. This way it prevents from random getting the same location twice.

def consecutive_seating(seats):
    for i in range(len(arr)):#loop through the array and see if there is a row that has the correct number of consecutive spots for the number of seats the customer wants 
        count = 0
        for j in range(len(arr[0])):
            if arr[i][j] == "0":
                count += 1; 
            else:
                count = 0;
            if count >= seats: 
                return [i,j-seats+1] #return the coordinate of the x and y (row/col) of the first consecutive index 
    return [-1, -1]
            
def col_to_let(col):
    if col == 0:
        return "A"
    if col == 1:
        return "B"
    if col == 2:
        return "C"
    if col == 3:
        return "D"
    if col == 4:
        return "E"
    if col == 5:
        return "F"
    if col == 6:
        return "G"
    if col == 7:
        return "H"
    if col == 8:
        return "I"
    if col == 9:
        return "J"

    
display()
#make_board_2()
#print(arr_econ)
