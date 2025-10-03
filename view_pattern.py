view=["login","login","login","view","logout","view","view"]
position=[]
for i in range(1,len(view)):
    if view[i]== view[i-1]:
        if  not position:
              position.append(i-1)
        position.append(i)
    else:
          if len(position)>1:   
                print(f"consecutive duplicate found:{view[position[0]]} "f"at {position}")
                position=[]
                
if len(position)>1:   
                print(f"consecutive duplicate found:{view[position[0]]} "f"at {position}")
                


               
