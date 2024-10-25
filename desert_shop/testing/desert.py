class dsrtItm:
    def __init__(self,nm):#,nm):
        self.nm=nm
    def __str__(self):
        return f"Type: {self.__class__.__name__}\nName: {self.nm}\nQuantity: {self.quan}\nPrice Per: {self.pp_}"
    def cost(self):
        return self.quan*self.pp_
    def gt_nm(self):
        return self.nm
    def get_quan(self):
        return self.quan
    
class candy(dsrtItm):#("candy")
    def __init__(self,nm,weg,ppp):
        super().__init__(nm)
        self.quan=weg
        self.pp_=1.5

class cookie(dsrtItm):#("cookie")
    def __init__(self,nm,quan,ppd):
        super().__init__(nm)
        self.quan=quan
        self.pp_=3.14

class iceCream(dsrtItm):#("ice cream")
    def __init__(self,nm,scps,pps):
        super().__init__(nm)
        self.quan=scps
        self.pp_=0.51

class sunday(iceCream):#("sunday")
    def __init__(self,nm,scps,pps,top,tpp):
        super().__init__(nm,scps,pps)
        self.tp=top
        self.quan=1
        self.pp_=0.15
