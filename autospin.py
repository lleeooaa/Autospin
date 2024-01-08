from tkinter import *
import timeit
import threading 

"""init"""
#runes={0:"heart",1:"water",2:"fire",3:"wood",4:"light",5:"dark"}
rows=[]
cols=[]
gameboard=""
count=[0,0,0,0,0,0]
max_score=0
max_combo=0
visited_list = {}
"""UI fun"""

def start1():
    global gameboard
    label_ans.delete("1.0","end")
    gameboard=""
    for i in rows:
        for j in i:
            gameboard+=j.get()
    gameboard="042334352451020123331302541452"
    count_max()
    a_star()

def thread():
    t1=threading.Thread(target=start1)
    t1.start()

def clearUI():
    for i in rows:
        for j in i:
            j.place_forget()

def count_max():
    global count
    global max_score
    global max_combo
    for i in gameboard:
        count[int(i)]+=1
    for i in count:
        x,y=divmod(i,3)
        if x>=1:
            max_score+=x*100+y*25
            max_combo+=x
    max_score*=1+(max_combo-1)*0.25   


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
    if(node[0]+1<5):
        neighbour.append(([node[0]+1,node[1]],'S'))
    if(node[1]-1>=0):
        neighbour.append(([node[0],node[1]-1],'W'))
    if(node[1]+1<6):
        neighbour.append(([node[0],node[1]+1],'E'))
    return neighbour
    
def compute(gameboard1):
    score=0
    combo_list=[]
    consecutive_list=[] #check 2x3 special case
    added=False
    for i in range(5):
        for j in range(6):
            #check row and column 2 by 2
            if j<5 and gameboard1[i*6+j]==gameboard1[i*6+j+1]:
                consecutive_list.append([(i,j),(i,j+1)])
            if i<4 and gameboard1[i*6+j]==gameboard1[(i+1)*6+j]:
                consecutive_list.append([(i,j),(i+1,j)])
            
            #check row and column 3 by 3
            if j<4 and gameboard1[i*6+j]==gameboard1[i*6+j+1]==gameboard1[i*6+j+2]:
                for combo in combo_list:
                    if (i,j) in combo or (i,j+1) in combo or (i,j+2) in combo:
                        combo_list.remove(combo)
                        combo_list.append(list(set(combo) | set([(i,j), (i,j+1), (i,j+2)])))
                        added=True
                if not added:    
                    combo_list.append([(i,j), (i,j+1), (i,j+2)])
                added=False

            if i<3 and gameboard1[i*6+j]==gameboard1[(i+1)*6+j]==gameboard1[(i+2)*6+j]:
                for combo in combo_list:
                    if (i*6,j) in combo or (i+1,j) in combo or (i+2,j) in combo:
                        combo_list.remove(combo)
                        combo_list.append(list(set(combo) | set([(i,j), (i+1,j), (i+2,j)])))
                        added=True
                if not added:
                    combo_list.append([(i,j), (i+1,j), (i+2,j)])
                added=False

    #check special case at the end
    for double in consecutive_list:
        a=b=None
        for combo in combo_list:
            if double[0] in combo:
                a=combo
            if double[1] in combo:
                b=combo
        if a and b and a!=b:
            combo_list.remove(a)
            combo_list.remove(b)
            combo_list.append(list(set(a)|set(b))) 
    for combo in combo_list:
        score+=(len(combo)+1)*25
    score*=1+(len(combo_list)-1)*0.25
    return score

def a_star():
    global queue
    global gameboard
    global curr
    queue=[]
    global visited_list 
    visited_list={}
    last_dir=None
    print(max_score)
    """
    for i in range(5):
        for j in range(6):
            queue.append([[i,j], [], gameboard, last_dir, 0])
    """
    queue.append([[0,0], [], gameboard, last_dir, 0])
    starting_time = timeit.default_timer()
    while len(queue)!=0:
        curr = queue.pop(0)
        if len(queue)>60000:
            for item in queue:
                score=compute(item[2])
                item[4]=score
            queue = sorted(queue, key=lambda tup: tup[4],reverse=True)[:1000]
            print(queue[0][4])
        if curr[4]>=max_score*0.65:
            label_ans.insert(END,f"visited nodes: {len(visited_list)}\n")
            label_ans.insert(END,f"time taken :{timeit.default_timer() - starting_time}\n")
            label_ans.insert(END,"path: "+str(curr[1]))
            break
        if curr[2] not in visited_list:
            visited_list[curr[2]]=1
            for coordinate, paths in get_neighbour(curr[0]):
                if (curr[3]=='N' and paths=='S') or (curr[3]=='S' and paths=='N') or (curr[3]=='E' and paths=='W') or (curr[3]=='W' and paths=='E'):
                   continue
                gameboard=swap(curr[2],curr[0],coordinate)
                queue.append([coordinate, curr[1] + [paths], gameboard, paths,curr[4]])

def num():
    print(len(visited_list),len(curr[1]),len(queue))

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
run=Button(root, text="Run", font=20, command=thread)
run.place(rely=0.6, relx=0.48)
visit=Button(root, text="Visited", font=20, command=num)
visit.place(rely=0.6,relx=0.7)
root.mainloop()
