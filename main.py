
name = input("What is the name of your robot?: ")
id = int(input("Please provide the robot id: "))
grid_size = 10
row = int(input("Enter the row-coordinate of the robot: "))
col = int(input("Enter the column-coordinate of the robot: "))


if row<0:
    row = 0
if row > grid_size -1 :
    row = grid_size - 1
if col<0:
    col = 0
if col > grid_size -1 :
    col = grid_size - 1

def quadrant(row,col,grid_size):
    mid = grid_size//2 - 1

    if row<=mid and col <=mid:
        return "Top-left quadrant"
    elif row<=mid and col>mid:
        return "Top-right quadrant"
    elif row>mid and col<=mid:
        return "Bottom-left quadrant"
    elif row>mid and col>mid:
        return "Bottom-right quadrant"
    
    return "Space"
    
loc = quadrant(row,col,grid_size)

print(f"Hello. My name is {name}. My ID is {id}. My current location is {(row,col)}.I am in the {loc}" )

