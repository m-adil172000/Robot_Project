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


def take_input():

    name = input("What is the name of your robot?: ")
    id = int(input("Please provide the robot id: "))
    grid_size = 10
    row = int(input("Enter the row-coordinate of the robot: "))
    col = int(input("Enter the column-coordinate of the robot: "))
    dirc = input("What is its initial direction [n|s|e|w]?: ")

    if row<0:
        row = 0
    if row > grid_size -1 :
        row = grid_size - 1
    if col<0:
        col = 0
    if col > grid_size -1 :
        col = grid_size - 1
    
    return name, id, grid_size, row, col, dirc

def moving(row,col,grid_size,dirc):

    if dirc=='n':
        print("I am facing North")
        if row!=0:
            row = row - 1
    elif dirc=='s':
        print('I am facing South')
        if row!=grid_size-1:
            row = row + 1
    elif dirc=='e':
        print('I am facing East')
        if col != grid_size-1:
            col += 1
    else:
        print("I am facing West")
        if col!=0:
            col -= 1
    print("Moving one step forward.")
    return row,col




def main():
    
    name, id, grid_size, row, col, dirc = take_input()

    loc = quadrant(row,col,grid_size)
    print(f"Hello. My name is {name}. My ID is {id}.")
    print(f"My current location is {(row,col)}.I am in the {loc}")
    row,col = moving(row,col,grid_size,dirc)
    loc = quadrant(row,col,grid_size)
    print(f"My current location is {(row,col)}.I am in the {loc}")





if __name__ == "__main__":
    main()

