#### Import class from module
##############################
from Classes import Planet 

# importing module Classes actually runs its code.
# This is not desirable. There should be a way around it.
p1 = Planet(2334,3324829842)
print(p1.getArea())
print(f'Planets radius is: {p1.getArea()} and Weight is {p1.getWeight()}')

###############################
#### Import modules from package
###############################
from Disney import Starwars
sw1=Starwars.Starwars_Objects()
print(sw1.getPlanet())
################################

###############################
#### Import modules from package
###############################
from Disney.Marvel import Marvel_Characters
mav1=Marvel_Characters()
print(mav1.getCharacters())
################################

###############################
#### Import methods from package module
###############################
from Disney.Marvel import Fliers,Runners
print(Fliers())
print(Runners())
################################

