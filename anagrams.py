class Solve():
   def Anagrams( self, lst ):
       '''
       Function to Group Anagrams
       :param lst: list of words
       :return: list of grouped anagrams
       '''
       dictionary = {}
       for word in lst:
           sortedWord = ''.join(sorted(word))
           
           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]         
           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]
if __name__ == '__main__':
   lst = ['eat','tea','tan','ate','nat','bat']
   print(Solve().Anagrams(lst))
