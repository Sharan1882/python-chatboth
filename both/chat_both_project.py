from random import randrange


def add_controls():    
    while 1:
        qs=open('chatboth.txt','a')
        qus=[]
        cu=1
        x=input('\nAsk/Questions ')
        if x=='':
            break
        qus.append(x)

        while x:
            x=input('ans'+str(cu)+':')
            qus.append(x)
            cu+=1
            
        aa=",nx,".join(qus)
        print(aa,file=qs)
        #qus.clear()        
        qs.close()
    
    #main()


        
def load_chat():
    chat={}
    qs=open('chatboth.txt','r')
    a=qs.readline()
    while a:
        ans=[]
        spl=a.split(',nx,')
        for x in range(1,len(spl)-1):
            ans.append(spl[x])

        chat[spl[0]]=ans  
        a=qs.readline()
    #print(chat)
    return chat
    qs.close()


def rand_get(lists):
    num=randrange(len(lists))
    r=lists[num]
    return r
    


def check_chat(inpt):
    chats=load_chat()
    point=[]
    ques=[]
    res=""

    sy=inpt.lower().split(' ')
    for x in chats:
        c=0
        ques.append(x)
        xx=x.lower().split(' ')
        for y in xx:            
            if y in sy:
                c+=1
        point.append(c)

    
    mx=max(point)
    if mx!=0:
        ind=point.index(mx)
        res=rand_get(chats[ques[ind]])

    return res

    

def chat_both():
    print("CHAT BOT")
    
    while True:
        get=input("\nME:")
        if get=="":
            continue
        else:
            result=check_chat(get)
            if result=="":
                print("bot:i can't undersatant")
            else:
                print("bot:"+str(result))


#add_controls()   
#chat_both()

def main():
    if __name__=="__main__":
        print('''

    ##############################################

               CHAT BOT MAIN MENU

    ##############################################

    1. Add Question
    2. chat both
    ''')
        inp=input('Enter the option:')
        if inp=="1":
            add_controls()
        elif inp=="2":
            chat_both()
        else:
            main()



main()


