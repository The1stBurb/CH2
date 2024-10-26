class movie:
    def __init__(self,title,releaseYear,director,rating,genre,cast):
        self.tit,self.ry,self.dir,self.rat,self.gr,self.ct=title,releaseYear,director,rating,genre,cast
        #titles, release year, director, rating, genre and cast
    def __str__(self):
        return f"Title: {self.tit}\nRelease Year: {self.ry}\nDirector: {self.dir}\nRating: {self.rat}\nGenre: {self.gr}\nCast: "+(", ".join(self.ct))+"\n"
    def __lt__(self, other):
        return self.tit < other.tit
    def alphSort(self,g1,otr):
        m="abcdefghijklmnopqrstuvwxyz"
        frst=0
        for i in range(min(len(self.tit),len(otr.tit))):
            fl=[m.find(self.tit[i]),m.find(otr.tit[i])]
            if fl[0]==-1 or fl[0]<fl[1]:
                return otr,self
                break
            elif fl[1]==-1 or fl[0]>fl[1]:
                break
        return self,otr
    def chrnSort(self,otr):
        if self.ry>otr.ry:
            return otr,self
        return self,otr
    def dirSrch(self,dir):
        return self.dir.lower()==dir.lower()
    def cstSrch(self,cstMbr):
        inr=cstMbr in self.ct
        return inr
    def inGnr(self,gnr):
        return self.gr==gnr
movies=[
    movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),
    movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),
    movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),
    movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),
    movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),
    movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),
    movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"]),
    movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),
    movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),
    movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]),
    movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),
    movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),
    movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"]),
    movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),
    movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),
    movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),
    movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"])
]
def alphaSort():
    global movies
    # srt=[]
    movies=sorted(movies, key=lambda x: x.tit)
    return
    for i in range(len(movies)):
        for j in range(len(movies)):
            movies[i],movies[j]=movies[i].alphSort(movies[i],movies[j])
def getGnr(gnr):
    # inGnr=[]
    for i in movies:
        if i.inGnr(gnr):
            print(i)
def getCst(gnr):
    # inGnr=[]
    for i in movies:
        if i.cstSrch(gnr):
            print(i)
def getDir(gnr):
    # inGnr=[]
    for i in movies:
        if i.dirSrch(gnr):
            print(i)
def chronSort():
    global movies
    # srt=[]
    movies=sorted(movies, key=lambda x: x.ry,reverse=True)
    return
    for i in range(len(movies)):
        for j in range(i+1,len(movies)):
            movies[i],movies[j]=movies[i].chrnSort(movies[i],movies[j])
def pra():
    for i in movies:
        print(i)
while True:
    ac=input("1-Alphabetical sort\n2-Chronological Order\n3-Of Genre\n4-Director Search\n5-Cast Search\n >>")
    # match ac:
    if ac=="1":
        alphaSort()
        pra()
    elif ac=="2":
        chronSort()
        pra()
    elif ac=="3":
        wht=input("What genre? ")
        getGnr(wht)
    elif ac=="4":
        wht=input("Director: ")
        getDir(wht)
    elif ac=="5":
        wht=input("Cast Member: ")
        getCst(wht)
    print()
# Needs the init method yauygsalkjgjds
# -Needs string methods that will print out all the information for the movies kjashgdkjgdsadsg
# -Method that sorts the movies in alphabetical order kjaskjgdhdsag
# -Method that sorts the movies in chronological order yr 0-yr 2000 kjsaddsag
# -List genre AKJSGFLKJsdg
# -Search director lksa;lkdjhadsh
# -search cast alkjdshdsas
