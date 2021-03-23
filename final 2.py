import turtle

#functions
def main_branch(branch,t): # this is the function for the green line
    branch_dup = branch #branch duplication
    branch_check = int(branch_dup - 20) #this check if the branch later is 10 behind the branch_dup
    if branch < 30:
        count_one = int(branch/10) - 3 #how many main lines are needed                     
    else:
        count_one = int(branch/10) 
        
    count_two = int(branch/10) - 1 #dup
    count_three = 0
    t.forward(branch)
    while branch > 30:
        t.right(20)
        branch_count = int(branch - 10)# every main branch are subtracted by 10
        t.forward(branch_count)
        branch -= 10
    branch -= 10
    t.right(20)
            
    while branch != branch_dup :
        count_three += 1
        branch = semi_branch(branch)
        if branch == branch_dup:
            t.backward(40)

        else:
            branch_fourthy(branch)
            if branch == 40:
                t.backward(branch)
                t.right(20)
                branch+= 10
                t.backward(branch)
        
            
def semi_branch(branch):
    while branch <= 40:    
        if branch == 20: #for branches that are equals to 20
            branch_twenty(branch)
            t.left(40)
            branch_twenty(branch)
            branch += 10
            return semi_branch(branch)
        elif branch == 30: #for branches that are equals to 30
            t.right(20)
            t.backward(branch)
            t.left(40)
            t.forward(branch)
            branch -= 10
            t.right(20)
            branch_twenty(branch)
            t.left(40)
            branch_twenty(branch)
            branch += 20
            if branch == 40:
                t.right(20)
                t.backward(branch - 10)
                t.right(20)
                return branch
        else:
            break

def branch_fourthy(branch):
    t.backward(branch)
    t.left(40)
    t.forward(branch)
    branch -= 10
    return thrity(branch)

def thrity(branch):
    t.right(20)
    t.forward(branch)
    branch -= 10
    t.right(20)
    return semi_branch(branch)

            
def branch_twenty(branch):
    t.forward(branch)
    sub_branch = int(branch - 10)
    t.color("blue")
    t.right(20)
    t.forward(sub_branch)
    t.color("red")
    t.backward(sub_branch)
    t.left(40)
    t.color("blue")
    t.forward(sub_branch)
    t.color("red")
    t.backward(sub_branch)
    t.right(20)
    t.backward(branch)
    branch += 10
    

#-----main t = turtle.Turtle() #identifies turtle
t = turtle.Turtle() #identifies turtle

myWin = turtle.Screen() #loads a screen

t.left(90) #sets up position of turtle,

t.up()

t.backward(100)                                   

t.down()

t.color("green")

main_branch(50,t) # this program only works if branch == 40 and branch == 50!

myWin.exitonclick()












