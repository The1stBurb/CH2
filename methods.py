class pokemon:
    def __init__(self,name,hp,typ,lvl):
        self.nm,self.hp,self.typ,self.lvl=name,hp,typ,lvl
    def __str__(self):
        return f"Name: {self.nm}\nHP: {self.hp}\nType: {self.typ}\nLevel: {self.lvl}\n"
    def combet(self,ohr):
        wnr="No one"
        if self.lvl>ohr.lvl:
            wnr=self.nm
        elif ohr.lvl>self.lvl:
            wnr=ohr.nm
        else:
            if self.hp>ohr.hp:
                wnr=self.nm
            elif ohr.hp>self.hp:
                wnr=ohr.nm
        return wnr+" won!\n"
    def lvlup(self):
        self.lvl+=1
        self.hp=int(self.hp*3.14159265358979311599796346854)
    @classmethod
    def pikachu(self):
        return pokemon("pika-chuuu",983,"elect",1.5)
    #static methods do not require self or class
    @staticmethod
    def hper(poke):
        return poke.hp-5
#@classmethod is when you DONT want to change the vars of an instance ig. eg: to define a certain instance of class.
eve=pokemon("Jarmy",3215.3,"strange",98)
print(eve)
pichu=pokemon("Jarmy2",3.7,"rando",98)
print(pichu)
print(eve.combet(pichu))
print(eve.lvlup())
print(eve)
pika=pokemon.pikachu()#classmethod
print(pika)
pika.hp=pokemon.hper(pika)#staticmethod
print(pika)
