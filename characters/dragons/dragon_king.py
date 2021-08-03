from .scuba_thrower import ScubaThrower
from utils import terminators_win


class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    food_cost = 7
    kings = 0
    instantiated = False
    implemented = True  # Change to True to view in the GUI

    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        ScubaThrower.__init__(self,armor)
        if DragonKing.kings == 0:
            self.instantiated = True
        else:
            self.instantiated = False
        DragonKing.kings += 1
        self.temp_list = []
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.instantiated == False:
            self.reduce_armor(self.armor)
        else:
            temp= self.place.exit

            while(temp!= None):

                if temp.dragon is not None:
                    if temp.dragon not in self.temp_list:
                        temp.dragon.damage *= 2
                        self.temp_list.append(temp.dragon)
                    if temp.dragon.is_container is True:
                        if temp.dragon.contained_dragon is not None and temp.dragon.contained_dragon not in self.temp_list:
                            temp.dragon.contained_dragon.damage *= 2
                            self.temp_list.append(temp.dragon.contained_dragon)
                temp = temp.exit

            ScubaThrower.action(self,colony)

        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.instantiated==False:
            ScubaThrower.reduce_armor(self,amount)
        else:
            self.armor -= amount
            if self.armor <=0:
                terminators_win()





