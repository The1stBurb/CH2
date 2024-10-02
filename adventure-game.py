from random import choice,randint,random
import sys
from time import sleep,perf_counter
from math import floor
def sm(n):
    n=int(n)
    ks={"1":"st","2":"nd","3":"rd"}
    return str(n)+(ks[str(n)]if str(n)in ks else"th")
def txtr(txt):
    s="qωєятуυισραѕ∂ƒgнנкℓzχ¢νвηмqωєятуυισραѕ∂ƒgнנкℓzχ¢νвηм"#ϘWƎЯTYUIOꟼAƧႧꟻӘHႱﻼ⅃ZXƆV𐐒ИMpwɘɿtγυioqɒƨbʇϱʜįʞlzxɔvdnm"#ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃ℤ𝕏ℂ𝕍𝔹ℕ𝕄𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞"#𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"#"𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷𝖅𝖃𝕮𝖁𝕭𝕹𝕸𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒"
    s2="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    st=""
    for i in txt:
        ind=s2.find(i)
        # print(ind,i,s[ind],"}")
        if ind!=-1:
            st+=s[ind]
            # if i=="m"or i=="w":
            #     st+=" "
        else:
            st+=i
    return st#txt
def tprint(*text,sp=False):
    sp=10**-15
    # print(type(text))
    # if isinstance(text[0],tuple):
    #     text=text[0]
    if isinstance(text,tuple):
        txt=[]
        for i in text:
            txt.append(str(i))
        text=" ".join(txt)
    text=txtr(text)
    punctuation = {
    "." : 0.25,
    "!" : 0.15,
    "?" : 0.15,
    "," : 0.05,
    ":" : 0.1,
    "\n":0,
    }
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in punctuation:
            sleep(0)#punctuation[char])
        else:
            r=random()/2+0.5
            sleep(r*(0.05 if sp==False else sp))
    print()
    # time.sleep(0.25)
def intput(*txt,sp=0.005,inp=""):
    tprint(*txt,sp=sp)
    # print(txt)
    return input(inp+" >> ")

def gt():
    # print(perf_counter_ns())
    return perf_counter()
tme=[gt(),gt(),2]
def tmr():
    global tme
    pt,ct=tme[1],gt()
    cpt=((ct-pt))//34
    if cpt>34:
        cpt=cpt-34
    cpt+=tme[2]
    return [round(pt),round(ct),[cpt,cpt/2]]
p=[0,0,[["Handbook",1]]]
mp=[[[randint(1,4),[0]]]]
def upMp(d):
    global mp,p
    #types 0-none,1-field,2-forest,3-river,4-mount
    if d==1:
        p[1]-=1
    elif d==2:
        p[0]+=1
    elif d==3:
        p[1]+=1
    elif d==4:
        p[0]-=1
    if p[0]<0:
        for i in range(len(mp)):
            mp[i].insert(0,[randint(1,4),[0]])
        p[0]=0
    elif p[0]>len(mp[0])-1:
        for i in range(len(mp)):
            mp[i].append([randint(1,4),[0]])
        p[0]=len(mp[0])-1
    elif p[1]<0:
        mp.insert(0,[[randint(1,4),[0]]for i in range(len(mp[0]))])
        p[1]=0
    elif p[1]>len(mp)-1:
        mp.append([[randint(1,4),[0]]for i in range(len(mp[0]))])
        p[1]=len(mp)-1
def bfix():
    global p
    inv={}
    for i in p[2]:
        # print(i)
        if i[0] in inv:
            inv[i[0]]+=i[1]
        else:
            inv[i[0]]=i[1]
    p[2]=[]
    for i in inv:
        p[2].append([i,inv[i]])
mater={
    "nothing":["None"],
    "handbook":["read"],
    "grass":["eat","burn"],
    "hemp":["eat","burn"],
    "seed":["eat","throw","burn"],
    "wood":["build","throw","burn"],
    "leaf":["eat","burn"],
    "apple":["eat","throw"],
    "water":["drink"],
    "rock":["build","throw"],
    "fish":["eat","throw"],
    "coal":["throw","burn"],
    "iron":["throw","build"],}
craft={
    "fire":[[["wood","coal"],5],1],
    "house":[["wood",50],2],
    "pickaxe":[[["rock","iron"],[4,2]],["wood",2],3],
}
def build():
    global craft,mater,p
    print("You have:")
    bbl={}
    for a,i in enumerate(p[2]):
        if "build" in mater[i[0].lower()]:
            print("  ",str(i[1])+"x",i[0])
            bbl[i[0]]=[i[1],a]
    print()
    # bld={}
    for a,i in enumerate(craft):
        c=craft[i]
        print(str(a+1)+".",i+":")
        # bld[i]=[]
        for j in range(len(c)-1):
            k=c[j]
            mx=[]
            nal=True if isinstance(k[0],list) else False
            nul=True if isinstance(k[1],list) else False
            if nal and nul:
                for l in range(len(k[0])):
                    mx.append(str(k[1][l])+"x "+k[0][l])
                    # bld[i].append([k[0][l],k[1][l]])
            elif nal:
                for l in range(len(k[0])):
                    mx.append(str(k[1])+"x "+k[0][l])
                    # bld[i].append([k[0][l],k[1]])
            print("  ",(" or ".join(mx)if nal else str(k[1])+"x "+k[0]))
            # print("  ",str(c[j][1])+"x",(" or ".join(c[j][0])if isinstance(c[j][0],list)else c[j][0]))
    while True:
        bld=intput("What would you like to build")
        if not bld in craft:
            print("Whoops! You can't build that!")
        else:
            break
    rsc=craft[bld]
    # mx={}
    for i in rsc:
        mx={}
        nal=True if isinstance(i[0],list) else False
        nul=True if isinstance(i[1],list) else False
        if nal and nul:
            for l in range(len(i[0])):
                # mx.append(str(k[1][l])+"x "+k[0][l])
                mx[i[0][l]]=i[1][l]
        elif nal:
            for l in range(len(k[0])):
                mx[i[0][l]]=i[1]
                # mx.append(str(k[1])+"x "+k[0][l])
        if nal:
            gd=False
            for j in mx:
                if j in bbl and bbl[i][0]>=mx[j]:
                    p[2][bbl[i][1]][1]-=mx[j]
        else:
            if i in bbl and bbl[i][0]>=rsc[i]:
                p[2][bbl[i][1]][1]-=rsc[i]
    # for i in mx:
    #     if i in bbl:
    #         if 
def res(tl):
    rs=[["nothing!"],["grass","hemp","seed"],["wood","leaf","apple"],["water","rock","fish"],["rock","rock","coal","iron","rock","wood","rock"]][tl]
    fnd=[]
    for i in range(randint(2,5)):
        fnd.append([choice(rs),randint(1,3)])
    return fnd
def action():
    tle=mp[p[0]][p[1]][0]
    tme=tmr()
    # print(tme)
    tprint("Its the",sm(tme[2][1]),"day.")
    tprint("You are on a",["None","field","forest","river","moustain"][tle],"tile!")
    inp=intput("You can:\n 1. Explore\n 2. Build\n 3. Eat\n 4. Rest\n 5. Look for resources\n 6. Open your backpack",sp=0.001)
    match inp:
        case "1":
            inp=intput("What direction? 1-Up, 2-Right, 3-Down, 4-Left")
            if inp.isdigit()and int(inp)in range(1,5):
                upMp(int(inp))
                print(mp)
            else:
                tprint("Can't go that direction!")
        case "2":
            build()
            # b=input("Sorry but building isn't availible!",inp="Press enter to continue!")
            # continue
        case "3":
            b=input("Sorry but eating isn't availible!",inp="Press enter to continue!")
        case "4":
            tprint("You decide the nearest spot of ground looks comfy!")
            for i in ["z","Z","z","z","Z"]:
                print(i)
                sleep(random()/2)
            tprint("You wake up feeling very refreshed!\nYou gain 0HP!")
        case "5":
            fnd=res(tle)
            for i in fnd:
                tprint(str(i[1])+"x",i[0])
                p[2].append(i)
            bfix()
        case "6":
            for i in p[2]:
                tprint(str(i[1])+"x",i[0])
            intput("")
            # print("6")
        case _:
            tprint("Woops! Not an action!")
    sleep(0.5)
# tprint("Welcome to this world! If you don't remember, like most, you have been selected to test thois newly found world! Explore, because we are using YOU to find out if humans can live here! The country thanks you for your work!")
# tprint("PS. if you are in trouble we won't rescue you!",sp=10**-15)
# intput("You should find a handbook in your backpack!",sp=False,inp="Press enter to continue!")
while True:
    print("\033c")
    action()