class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.current = -1
    
    def __contains__(self,members):
        if members in self.__myTeam:
            return True
        else:
            return False


    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.last = self.__myTeam[-1]
        self.lastIndex = self.__myTeam.index(self.last)
        self.current += 1
        if self.current <= self.lastIndex:
            return self.__myTeam[self.current]   
        else:
            raise StopIteration
    
    def __len__(self):
        return len(self.__myTeam)
            
class rIterator:
    def __init__(self, classmates):
        self.__Class = classmates

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])

    print("Tim" in classmates)
    print("Sam" in classmates)
    for x in classmates:
        print (x)
    try:
        print("There is a len method, and the length of classmates is: ", len(classmates))
    except:
        print("No Len method")
main()