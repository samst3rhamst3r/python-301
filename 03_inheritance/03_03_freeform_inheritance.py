# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Business:

    def __init__(self, sq_ft, num_rooms, owner) -> None:
        self.sq_ft = sq_ft
        self.num_rooms = num_rooms
        self.owner = owner

class Restaurant(Business):

    def __init__(self, sq_ft, num_rooms, owner, num_tables, num_kitch_emps, menu, oper_hrs, mgr) -> None:
        super().__init__(sq_ft, num_rooms, owner)
        self.num_tables = num_tables
        self.num_kitch_emps = num_kitch_emps
        self.menu = menu 
        self.oper_hrs = oper_hrs
        self.mgr = mgr

class Gourmet(Restaurant):

    def __init__(self, sq_ft, num_rooms, owner, num_tables, num_kitch_emps, menu, oper_hrs, mgr, num_bus_emps, num_waiters) -> None:
        super().__init__(sq_ft, num_rooms, owner, num_tables, num_kitch_emps, menu, oper_hrs, mgr)
        self.num_bus_emps = num_bus_emps
        self.num_waiters = num_waiters

class FastFood(Restaurant):

    def __init__(self, sq_ft, num_rooms, owner, num_tables, num_kitch_emps, menu, oper_hrs, mgr, drive_thru, fry_machine) -> None:
        super().__init__(sq_ft, num_rooms, owner, num_tables, num_kitch_emps, menu, oper_hrs, mgr)
        self.drive_thru = drive_thru
        self.fry_machine = fry_machine