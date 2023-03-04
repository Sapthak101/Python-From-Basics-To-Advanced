#type pip install package_name in the terminal of the visual studio
import prettytable as pt

table=pt.PrettyTable()
print(table) #prints the object
#after the creation of the object the module referece to access the member attribute or metods are not needed
#but in case the object is directly used from the module then while using it module name with dot operator must be used
table.add_column("Poke name", ["wuegf", "wefiu", "wekf"])
table.add_column("Type", ["wug", "efiu", "wek"])

table.align="l"
print(table)
#printing objects sometimes gives thir type or sometimes their overall output
a=10
print(type(a)) #works for only user objects
print(type())
