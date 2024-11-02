from time import sleep
# Make a superclass called monster that instantiates a name and where the monster is from and has a method for attack

# Make sub classes for at least 4 different monsters that specify how that particular monster attacks
class monster:
    def __init__(self,name,hom,hp,atk):
        self.nm,self.hm,self.hp,self.atk=name,hom,hp,atk
    def atc(self):
        return "burb"
    def __str__(self):
        return f"{self.nm} from {self.hm} has {self.hp} health and {self.hp} attack!\n"
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
bobs=[nomNom("greg","alabama, new jersey"),burb("burb","eight foot house"),frog("tree","a tree"),angee("%$#^*!@","your soul"),]#ber("ber","georges packback"),squarle("frog","also tree"),]
con=[]
def conCon(bbs):
    cn=[]
    for i in range(0,len(bbs)-1,2):
        cn.append([bbs[i],bbs[i+1]])
    return cn
con=conCon(bobs)
print(con)
def prBr(br):
    for i in br:
        print(i[0].nm,"vs",i[1].nm)
    print("\n")
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
            sleep(0.5)
        print("\n")
    if len(bobs)==1:
        break
    con=conCon(bobs)
print("The winner is: ",bobs[0].nm)