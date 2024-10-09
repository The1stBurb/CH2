#bonus if include at least 1 class/static method
# The class for the order needs to have space for

# A drink
# An appetizer 
# A main course
# Two sides
# A dessert
# Please note that the user doesn't have to order an item for each category, they just need to be given the option

# The class needs to have methods that

# Prints out everything the user has ordered
# Gives the user a total for their order 
# Checks to see if ordered items are on the men (Tells user if what they ordered isn't on the menu)
# Makes sure that the user has ordered at least 1 item
# Allows user to place their order 
# Allows user to change an item in their order
itms={"drink":["water","wet water","soda"],"app":["salad","ice cream","apple"],"sid1":["sauce","apple sauce","frog soup"],"sid2":["icicles","food","beetles"],"dess":[]}
class order:
    def __init__(self):
        self.drnk=""
        self.app=""
        self.sid1=""
        self.sid2=""
        self.dess=""