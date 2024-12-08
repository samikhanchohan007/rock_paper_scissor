import random
def game():
    print("You are playing rock paper scissor...\n")
    print("r for rock\n")
    print("s for scissor\n")
    print("p for paper\n")
    dict={"r":1,"p":0,"s":-1}
    with open("HS_redo.txt","w") as f:
        pass
    
    computer=random.choice(["r","p","s"])
    score=0
    with open("HS_redo.txt","r") as f:
        data=f.read()
        if data!="":
            data=int(data)
        else:
            data=0

                                   
    
    
    
    while(0<1):
        you=input("Your choice: ")
        if dict[computer]==dict[you]:
            print(f"computer choose {computer}\n")
            print("its draw")
        else:
            if dict[computer]-dict[you]==-1 or dict[computer]-dict[you]==2:
                print(f"computer choose {computer}")
                print("you loose")
                break
            else:
                print(f"computer choose {computer}")
                print("you win")
                score+=1
    if score>data:
        data=score

    with open("HS_redo.txt","w") as f:
        f.write(f"highscore is {str(data)}")
game()


    