"""
Matienzo is a world-renowned caving region in Cantabria, Spain.
Di and Si are there for Christmas and have 5 caves with different prospects
they want to look at. However, after too many drinks at Bar German,
they can’t remember which caves are which! 
Help them to match the cave number with the area, the prospect and the current
length. No cheating by looking at the Matienzo caves website! 
¡Feliz navidad!

1. The cave in La secada is shorter in length than the cave with the bolt climb

2. The cave that is 25m long is in La Secada

3. 0603 is 25m long

4. The five caves are 1776, the dig with an echo, the bolt climb, the cave in La Secada and the shaft bash

5. 0099 isn’t in Mullir

6. Of the undescended shaft and the cave in Seldesuto, one is 1900 and the
other is 0m long ("undescended shaft" should read "shaft bash")

7. 1900 is longer than the cave in Las Calzadills

8. 0810 is either in La Collina or the shaft bash

"""
from itertools import permutations as perm

def dict_perms( category_list ):
  for p in perm(range(1,6)): yield {a:b for (a,b) in zip(category_list,p)}

def key(d, v): # find a key in dictionary d with value v
  return [name for name, val in d.items() if val == v][0]

lengths = [{0:1, 5:2, 25:3, 65:4, 954:5}]

lengths_caves = [ (length,cave) for length in lengths
                  for cave in dict_perms(['1900','1716','0810','0099','0603'])
                  if cave['0603'] ==  length[25]
                  and cave['1900'] != length[0] ]

 
lengths_caves_areas = [ (length,cave,area) for     length,cave in  lengths_caves
                        for area in dict_perms(['Mullir','Seldesuto','La Collina','Las Calzadillas','La Secada'])
                        if length[25] == area['La Secada']
                        and cave['1716'] != area['La Secada']
                        and cave['0099'] != area['Mullir']
                        and ( area['Seldesuto'] == cave['1900'] or area['Seldesuto'] == length[0] )
                        and cave['1900'] > area['Las Calzadillas']
                        ]

                                        
lengths_caves_areas_prospects = [(length,cave,area,prospect) for length,cave,area in lengths_caves_areas
                                 for prospect in dict_perms(['Dig-echo','Bolt climb','Undescended pitch',
                                                             'Unsupported dig','Shaft bash'])
                                 if prospect['Dig-echo'] != cave['1716']
                                 and prospect['Dig-echo'] != area['La Secada']
                                 and prospect['Bolt climb'] != cave['1716']
                                 and prospect['Bolt climb'] != area['La Secada']
                                 and prospect['Shaft bash'] != cave['1716']
                                 and prospect['Shaft bash'] != area['La Secada']
                                 and prospect['Shaft bash'] != area['Seldesuto']
                                 and ( ( prospect['Shaft bash'] == cave['1900']
                                       and area['Seldesuto'] == length[0])
                                       or
                                       ( prospect['Shaft bash'] == length[0] 
                                       and area['Seldesuto'] == cave['1900'] )
                                       )
                                 and (cave['0810'] == area['La Collina']
                                      or cave['0810'] == prospect['Shaft bash'] )
                                 and area['La Collina'] != prospect['Shaft bash']
                                 and area['La Secada'] < prospect['Bolt climb']
                                 ]

sols = set()       
for length,cave,area,prospect in lengths_caves_areas_prospects:
  sols.add( tuple( [(key(cave,pos),key(length,pos), key(area,pos),key(prospect,pos)) for pos in range(1,6)]) )
  for pos in range(1,6):
    print ( key(cave,pos), ",",key(length,pos), ",",key(area,pos),",",key(prospect,pos))
  print (" ")  

print ( len(sols) , "distinct solutions" )                                
                                       
