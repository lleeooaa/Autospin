from tkinter import *
import timeit
import threading 

"""init"""

n=0
ans=""
rows=[]
cols=[]
gameboard=""
runes={0:"heart",1:"water",2:"fire",3:"wood",4:"light",5:"dark"}
count=[0,0,0,0,0,0]
visited_list = {}

"""UI fun"""

def start1():
    global gameboard
    label_ans.delete("1.0","end")
    gameboard=""
    for i in rows:
        for j in i:
            gameboard+=runes[int(j.get())]

def threading():
    t1=threading.Thread(target=start1)
    t1.start()

def clearUI():
    for i in rows:
        for j in i:
            j.place_forget()

def count_runes():
    global count
    for i in gameboard:
        count[int(i)]+=1


"""main"""

def swap(gameboard1,node1,node2):
    gameboard1=list(gameboard1)
    gameboard1[5*node1[0]+node1[1]],gameboard1[5*node2[0]+node2[1]]=gameboard1[5*node2[0]+node2[1]],gameboard1[5*node1[0]+node1[1]]
    gameboard1=''.join(gameboard1)
    return gameboard1

def get_neighbour(node):
    neighbour=[]
    if(node[0]-1>=0):
        neighbour.append(([node[0]-1,node[1]],'N'))
    if(node[0]+1<n):
        neighbour.append(([node[0]+1,node[1]],'S'))
    if(node[1]-1>=0):
        neighbour.append(([node[0],node[1]-1],'W'))
    if(node[1]+1<n):
        neighbour.append(([node[0],node[1]+1],'E'))
    return neighbour

def compute(gameboard1):
    combo_list=[]
    for i in range(3):
        for j in range(4):
            if gameboard1[i*5][j]==gameboard[i*5][j+1]==gameboard[i*5][j+2]:
                combo_list.append([gameboard1[i*5][j],gameboard1[i*5][j+1],gameboard1[i*5][j+2]])

def a_star():
    global queue
    global gameboard
    global curr
    queue=[]
    global visited_list 
    visited_list={}
    last_dir=None
    for i in range(5):
        for j in range(6):
            queue.append(([i,j], [], gameboard, last_dir, compute(gameboard)))
    starting_time = timeit.default_timer()
    while len(queue)!=0:
        curr = queue.pop(0)
        if len(queue)>60000:
            queue = sorted(queue, key=lambda tup: tup[4])[:1000]
        if curr[2]==ans:
            label_ans.insert(END,f"visited nodes: {len(visited_list)}\n")
            label_ans.insert(END,f"time taken :{timeit.default_timer() - starting_time}\n")
            label_ans.insert(END,"path: "+str(curr[1]))
            break
        if curr[2] not in visited_list:
            visited_list[curr[2]]=1
            for coordinate, paths in get_neighbour(curr[0]):
                if (curr[3]=='N' and paths=='S') or (curr[3]=='S' and paths=='N') or (curr[3]=='E' and paths=='W') or (curr[3]=='W' and paths=='E'):
                   continue
                gameboard=swap(curr[2],curr[0],coordinate,curr[4])
                queue.append((coordinate, curr[1] + [paths], gameboard, paths))

root=Tk()
root.geometry("800x800")
for i in range(5):
    cols = []
    for j in range(6):
        e = Entry(width=10,font=20)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, 0)
        e.place(rely=0.1+i/16*1.5,relx=0.25+j/16*1.5,height=75,width=75)
        cols.append(e)
    rows.append(cols)
label_ans=Text(root,font=20)
label_ans.place(width=800,height=150,rely=0.7)
run=Button(root, text="Run", font=20, command=threading)
run.place(rely=0.6, relx=0.48)


root.mainloop()
