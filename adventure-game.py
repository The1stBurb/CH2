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
            sleep(punctuation[char])
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
tme=[gt(),gt(),0]
def tmr():
    global tme
    pt,ct=tme[1],gt()
    cpt=((ct-pt))#//34
    if cpt>34:
        cpt=cpt-34
    cpt+=tme[2]
    return [round(pt),round(ct),[cpt,cpt/2]]
def action():
    tme=tmr()
    # print(tme)
    tprint("Its the",sm(tme[2][1]),"day.")
    inp=intput("You can:\n 1. Explore\n 2. Build\n 3. Eat\n 4. Rest\n 5. Open your backpack",sp=0.00000001)
    match inp:
        case "1":
            print("1")
        case "2":
            print("2")
        case "3":
            print("3")
        case "4":
            print("4")
        case "5":
            print("5")
        case _:
            tprint("Woops! Not an action!")
            sleep(0.5)
# tprint("Welcome to this world! If you don't remember, like most, you have been selected to test thois newly found world! Explore, because we are using YOU to find out if humans can live here! The country thanks you for your work!")
# tprint("PS. if you are in trouble we won't rescue you!",sp=10**-15)
# intput("You should find a handbook in your backpack!",sp=False,inp="Press enter to continue!")
while True:
    action()