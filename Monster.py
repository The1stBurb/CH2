# Make a superclass called monster that instantiates a name and where the monster is from and has a method for attack

# Make sub classes for at least 4 different monsters that specify how that particular monster attacks
class monster:
    def __init__(self,name,hom,hp,atk):
        self.nm,self.hm,self.hp,self.atk=hame,hom.hp,atk
    def atc(self):
        return "burb"
    def __str__(self):
        return f"{self.nm} from {self.hm} has {self.hp} health and {self.hp} attack!\n"
class nomNom(monster):
    def __init__(self,nm,hm):
        super.__init__(nm,hm,10,2)
        self.at="noms on"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class burb(monster):
    def __init__(self,nm,hm):
        super.__init__(nm,hm,15,3)
        self.at="pecks"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class frog(monster):
    def __init__(self,nm,hm):
        super.__init__(nm,hm,10,2)
        self.at="hops over"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class angee(monster):
    def __init__(self,nm,hm):
        super.__init__(nm,hm,5,10)
        self.at="screams at"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class ber(monster):
    def __init__(self,nm,hm):
        super.__init__(nm,hm,20,5)
        self.at="potatos"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
class squarle(monster):
    def __init__(self,nm,hm):
        super.__init__(nm,hm,1,2)
        self.at="runs from"
    def atc(self,other):
        other.hp-=self.atk
        return f"{self.nm} {self.at} {other.nm} for {self.atk} damage"
bobs=[nomNom("greg","alabama, new jersey"),burb("burb","eight foot house"),frog("tree","a tree"),angee("%$#^*!@","your soul"),ber("ber","georges packback"),squarle("frog","also tree"),]
con=[]
for i in range(0,len(bobs)-1,2):
    con.append([bobs[i],bobs[i+1]])
print(con)