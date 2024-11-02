from time import sleep
from random import choice,randint
# Make a superclass called monster that instantiates a name and where the monster is from and has a method for attack

# Make sub classes for at least 4 different monsters that specify how that particular monster attacks
class monster:
    def __init__(self,name,hom,hp,atk):
        self.nm,self.hm,self.hp,self.atk=name,hom,hp+randint(-2,5),atk+randint(-3,4)
    def atc(self):
        return "burb"
    def __str__(self):
        return f"{self.nm} from {self.hm} has {self.hp} health and {self.hp} attack!"
class nomNom(monster):
    def __init__(self,nm,hm):
        super().__init__(nm,hm,10,2)
        self.at="noms on"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class burb(monster):
    def __init__(self,nm,hm):
        super().__init__(nm,hm,15,3)
        self.at="pecks"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class frog(monster):
    def __init__(self,nm,hm):
        super().__init__(nm,hm,10,2)
        self.at="hops over"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class angee(monster):
    def __init__(self,nm,hm):
        super().__init__(nm,hm,5,10)
        self.at="screams at"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class ber(monster):
    def __init__(self,nm,hm):
        super().__init__(nm,hm,20,5)
        self.at="potatos"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class squarle(monster):
    def __init__(self,nm,hm):
        super().__init__(nm,hm,1,2)
        self.at="runs from"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class mak:
    def __init__(self,nm,frm):
        self.c=None
        n=randint(0,5)
        if n==0:
            self.c=nomNom(nm,frm)
        elif n==1:
            self.c=burb(nm,frm)
        elif n==2:
            self.c=frog(nm,frm)
        elif n==3:
            self.c=angee(nm,frm)
        elif n==4:
            self.c=ber(nm,frm)
        elif n==5:
            self.c=squarle(nm,frm)
    def gv(self):
        return self.c
nams=["greg","burb","tree","%$#^*!@","ber","frog","alexander hamilton","nonagon","coler than u","hey u","u hey"]
frm=["alabama, new jersey","eigth foot house","a tree","your soul","georges packback","also tree","rocks","the pits","[REDACTED]","a scientist's house"]
bobs=[]#nomNom("greg","alabama, new jersey"),burb("burb","eight foot house"),frog("tree","a tree"),angee("%$#^*!@","your soul"),]#ber("ber","georges packback"),squarle("frog","also tree"),]
for i in range(8):
    bobs.append(mak(choice(nams),choice(frm)).gv())
con=[]
def conCon(bbs):
    bbs=bbs.copy()
    cn=[]
    for i in range(0,len(bbs)-1,2):
        o=choice(bbs)
        bbs.remove(o)
        op=choice(bbs)
        bbs.remove(op)
        cn.append([o,op])
    return cn
con=conCon(bobs)
print(con)
def prBr(br):
    for i in br:
        print(i[0].nm,"vs",i[1].nm)
    print("\n")
print("Heres your guys!")
for i in bobs:
    print("  ",i)
while True:
    prBr(con)
    input("Press enter to continue!")
    bobs=[]
    for i in con:
        op=i[0]
        o=i[1]
        print(op.nm,"vs",o.nm)
        sleep(1)
        fg=True
        while fg:
            print(op.atc(o))
            if o.hp<=0:
                print(o.nm,"has died!")
                bobs.append(op)
                fg=False
                continue
            print(o.atc(op))
            if op.hp<=0:
                print(op.nm,"has died!")
                bobs.append(o)
                fg=False
                continue
            sleep(0.1)
            print("\n")
        print("\n")
    if len(bobs)==1:
        break
    con=conCon(bobs)
print("The winner is: ",bobs[0].nm)