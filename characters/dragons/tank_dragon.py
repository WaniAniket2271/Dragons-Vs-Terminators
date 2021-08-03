from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI
    food_cost = 6

    def __init__(self,armor=2):
        BodyguardDragon.__init__(self,armor)
        self.contained_dragon = None

    # END 3.3

    def action(self, colony):
        # BEGIN 3.3
        "*** YOUR CODE HERE ***"
        temp=self.place.terminators.copy()
        for i in temp:
            i.reduce_armor(self.damage)
        if self.contained_dragon is not None:
            self.contained_dragon.action(colony)

