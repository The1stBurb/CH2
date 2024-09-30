from random import choice,randint,random
import sys,time
from math import floor
# from collections import Counter

# def get_21_combinations():
#     cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#     valid_combinations = []

#     def backtrack(combination, total, start):
#         if total == 21:
#             counter = Counter(combination)
#             if (counter[10] <= 12 and 
#                 counter[1] + counter[11] <= 4 and 
#                 all(counter[i] <= 4 for i in range(2, 10))):
#                 valid_combinations.append(tuple(sorted(combination)))
#             return
#         if total > 21:
#             return

#         for i in range(start, len(cards)):
#             combination.append(cards[i])
#             backtrack(combination, total + cards[i], i)
#             combination.pop()

#     backtrack([], 0, 0)
#     return sorted(set(valid_combinations))

# # Get and tprint the combinations
# combinations = get_21_combinations()
# with open("comb.txt","w")as c:
#     c.write("[")
#     for i, combo in enumerate(combinations, 1):
#         tprint(f"{i}. {combo}")
#         c.write(f"{combo},")
#     c.write("]")

# tprint(f"\nTotal number of combinations: {len(combinations)}")
def txtr(txt):
    s="ﺈઊ⧥ֆ៖߮＆꘎⟬〕▁☩Ⴓ₩𝝽®ㄒ￥ມ𝕀ዑᎮ⦃｜❵𝓐ﻛ𝓓ꘘ𝓖ⴼਹ𝓚╚ⵓ\"ɀӼƇᏤβℿღ≼⋟ᕉ⥠ഉਡᔦちϬ𐒇ზፃ𝞱–𝍡Ⴓ₩𝝽®ㄒ￥ມ𝕀ዑᎮ⟦⦎╲ઊકԂ𝖋ဌ𐒅ژꝄไ⨾ʾʑ𝖝ር√Ꙏกጢ⸒ⴰ⟋_"
    s2="~!@#$%^&*()_+QWERTYUIOP{|}ASDFGHJKL:\"ZXCVBNM<>?`1234567890-=QWERTYUIOP[]\asdfghjkl;'zxcvbnm,./ "
    st=""
    for i in txt:
        ind=s2.find(i)
        print(ind,i)
        if ind!=-1:
            st+=s[ind]
        else:
            st+=i
    return st
def nmr(nm):
    nm=str(nm)
    s="𝞱⥠ഉਡᔦちϬ𐒇ზፃ"
    nnm=""
    for i in nm:
        # prin(nm)
        nnm+=s[int(i)]
    return nnm
def tprint(*text,sp=False):
    # print(type(text))
    # if isinstance(text[0],tuple):
    #     text=text[0]
    if isinstance(text,tuple):
        txt=[]
        for i in text:
            # if isinstance(i,int):
            #     txt.append(nmr(i))
            # else:
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
            time.sleep(punctuation[char])
        else:
            time.sleep((0.005 if sp==False else sp))
    print()
    # time.sleep(0.25)
def intput(*txt):
    tprint(*txt,sp=10**-15)
    # print(txt)
    return input(" >> ")
#⥠
def chnc(tttl):
    td=21-tttl
    p=[]
    if td>0 or td>10:
        p.append("𝓐")
    if td>9:
        p.append("⥠𝞱")
        p.append("ਹ")
        p.append("Ⴓ")
        p.append("𝓚")
    if td>8:
        p.append("ፃ")
    if td>7:
        p.append("ზ")
    if td>6:
        p.append("𐒇")
    if td>5:
        p.append("Ϭ")
    if td>4:
        p.append("ち")
    if td>3:
        p.append("ᔦ")
    if td>2:
        p.append("ਡ")
    if td>1:
        p.append("ഉ")
    gd=0
    bd=0
    for i in crs:
        if i in p:
            gd+=crs[i]
        else:
            bd+=crs[i]
    tt=gd+bd
    gdc=round((gd/tt)*100)
    bdc=round((bd/tt)*100)
    return (gdc,bdc)
scr=[0,0]
mon=[100,100]
bt=0
while True:
    tprint("\033c")
    crs={"𝓐":4,"ഉ":4,"ਡ":4,"ᔦ":4,"ち":4,"Ϭ":4,"𐒇":4,"ზ":4,"ፃ":4,"⥠𝞱":4,"ਹ":4,"Ⴓ":4,"𝓚":4}
    crds={"𝓐":[1,11],"ഉ":2,"ਡ":3,"ᔦ":4,"ち":5,"Ϭ":6,"𐒇":7,"ზ":8,"ፃ":9,"⥠𝞱":10,"ਹ":10,"Ⴓ":10,"𝓚":10}
    cards=[]
    for i in ["𝓐","ഉ","ਡ","ᔦ","ち","Ϭ","𐒇","ზ","ፃ","⥠𝞱","ਹ","Ⴓ","𝓚"]:
        for j in range(4):
            cards.append(i)
    ttl=52
    yr=0
    ur=0
    t=1
    s=[False,False]
    #Ƈઊ𝓻Ԃ_ဌ𝜽եⵓ_   
    # bt=0
    m="ღ𝜽กᕦუ "
    tprint("You have",mon[0],m+"while your opponent has",mon[1],m+"!")
    while True:
        mn=intput("How much would you like to bet?",10,"-",(mon[0]))
        if mn.isdigit() and int(mn)in range(10,mon[0]+1):
            mon[0]-=int(mn)
            bt+=int(mn)
            break
        if mn.isdigit()and int(mn)<10:
            tprint("Too low!")
    mn=randint(10,floor(mon[1]/2))
    mon[1]-=mn
    bt+=mn
    while True:
        if s==[True,True]:
            break
        if t==1:
            if s[0]==True:
                t*=-1
                continue
        else:
            if s[1]==True:
                t*=-1
                continue
        # tprint(ur,yr)
        # tprint(crds)
        # tprint(crs)
        # tprint(yr)
        if t==1:
            # s[0]=
            tprint("Your total:",yr)
            gdc,bdc=chnc(yr)
            # tprint("Chance of dying next:",str(bdc)+"% chance!")
            tprint("Your chance of living is",gdc,"%!")
            tprint("I would do it!" if gdc>bdc else "I wouldn't draw!")
            dor=intput("Hit? (y/n) ")
            if dor!="y":
                s[0]=True
                tprint("Skip!\n")
                t*=-1
                continue
        else:
            # s[1]=False
            gdc,bdc=chnc(ur)
            # tprint(ur,gdc,bdc)
            if gdc<bdc:
                s[1]=True
                tprint("Opponent skips!\n")
                t*=-1
                continue
            else:
                tprint("Opponent drew!")
        crd=choice(cards)
        cards.remove(crd)#intput("Card got ").upper()
        # if not crd in crs or crs[crd]<=0:
        #     tprint("Woops! not possible")
        #     continue
        # y=intput("u (y/n) ")
        # if y=="y":
        if t==1:
            tprint("Card got: "+crd)
            if crd=="𝓐":
                oe=intput("1 or 11: ")
                n=0 if oe=="1" else 1
                yr+=crds[crd][n]
            else:
                yr+=crds[crd]
        else:
            if crd=="𝓐":
                ur+=crds[crd][0]
            else:
                ur+=crds[crd]
        crs[crd]-=1
        t*=-1
        tprint()
        if yr>21 or ur>21:
            break
    w=2
    if s==[True,True]:
        tprint("You won!" if yr>ur else("You Lost!" if ur>yr else"You Tied!"))
        if yr!=ur:
            if yr>ur:
                w=0
                # scr[0]+=1
            else:
                w=1
                # scr[1]+=1
    else:
        tprint("You won!" if ur>21 else"You Lost!")
        if ur>21:
            w=0
            # scr[0]+=1
        else:
            w=1
            # scr[1]+=1
    if w==0:
        scr[0]+=1
        mon[0]+=bt
        bt=0
    elif w==1:
        mon[1]+=bt
        bt=0
        scr[1]+=1
    tprint("You:",yr)
    tprint("Opponent:",ur)
    intput("Score:\n  You: ",str(scr[0]),"\n  Opp: ",str(scr[1]))
