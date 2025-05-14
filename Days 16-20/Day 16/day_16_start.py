from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("cyan")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Names",["Dragonite", "Pikachu", "Squirtle", "Lucario"])
table.add_column("Types", ["Dragon", "Electric", "Water", "Fighting"])
table.align = "l"
print(table)