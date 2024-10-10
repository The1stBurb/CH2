#bonus if include at least 1 class/static method
# The class for the order needs to have space for

# A drink donfkdsnkgds
# An appetizer akjsdgnkjdsgakgsdnak
# A main coursealkdgslsg
# Two sides aksjdgndsg
# A dessert askjgnkdsag
# Please note that the user doesn't have to order an item for each category, they just need to be given the option askjddasg

# The class needs to have methods that

# Prints out everything the user has ordered ans dgasgasdg
# Gives the user a total for their order  akjsgasdklgdsg
# Checks to see if ordered items are on the men (Tells user if what they ordered isn't on the menu)
# Makes sure that the user has ordered at least 1 item kjasdgksadgkjdsg
# Allows user to place their order jknsdkjlgskga
# Allows user to change an item in their orderkjasdgkjdsg
itms={"drink":["water","wet water","soda","none"],"app":["salad","ice cream","apple","none"],"sid1":["sauce","apple sauce","frog soup","none"],"sid2":["icicles","food","beetles","none"],"dess":["salamanders","forks","spinach","walruses","none"]}
prc={"water":1,"wet water":2,"soda":5,"none":0.01,"salad":1,"ice cream":5,"apple":2,"sauce":1,"apple sauce":3,"frog soup":7,"icicles":2,"food":1,"beetles":4.99,"salamanders":9.99,"forks":1,"spinach":5,"walruses":170,}
class order:
    def __init__(self,drnk="",app="",sid1="",sid2="",dess=""):
        self.drnk=drnk
        self.app=app
        self.sid1=sid1
        self.sid2=sid2
        self.dess=dess
    def __str__(self):
        return f"Drink: {self.drnk}\nAppateizer: {self.app}\nFirst Side: {self.sid1}\nSecond Side: {self.sid2}\nDessert: {self.dess}\nPrice: {prc[self.drnk]+prc[self.app]+prc[self.sid1]+prc[self.sid2]+prc[self.dess]}₪\n"
    def ord1(self):
        return self.drnk=="none"and self.app=="none"and self.sid1=="none"and self.sid2=="none"and self.dess=="none"
    @classmethod
    def dllr(self):
        return order("water","salad","sauce","food","forks")
    @classmethod
    def gt(inr):
        while True:
            inp=input("What would you like to get thats an "+{"drink":"drink","app":"appetizer","sid1":"first side","sid2":"second side","dess":"dessert"}[inr]+"? ")
            if inp in itms[inr]:
                print()
                return inp
            else:
                print("Thats not an option!")
    @classmethod
    def get():
        for a,i in enumerate(itms):
            print(["Drink","Appetizer","First Side","Second Side","Dessert"][a]+":")
            for j in itms[i]:
                print("  ",j+":",str(prc[j])+"₪")
            print()
        ord=order()
        while True:
            inp=input("WOuld you like to get the dollar menu?(y/n) ")
            if inp=="y":
                ord=order.dllr()
                return ord
            ord.drnk=order.gt("drink")
            ord.app=order.gt("app")
            ord.sid1=order.gt("sid1")
            ord.sid2=order.gt("sid2")
            ord.dess=order.gt("dess")
            if ord.ord1():
                print("You have to order something!")
            else:
                break
        return ord
    @classmethod
    def hppy(self):
ord=order.get()
print(ord)
inp=input("Are you happy with your order?(y/n) ")
if inp!="y":
    ord=order.get()
