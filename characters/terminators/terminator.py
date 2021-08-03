from ..fighter import Fighter


class Terminator(Fighter):
    """A Terminator moves from place to place, following exits and stinging dragons."""

    name = 'Terminator'
    damage = 1
    is_watersafe = True

    # OVERRIDE CLASS ATTRIBUTES HERE
    def __init__(self,armor,place=None):
        Fighter.__init__(self,armor,place)
        self.is_scared = False

        self.count = 0

    def sting(self, dragon):
        """Attack a Dragon, reducing its armor by 1."""
        dragon.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Terminator's current Place to a new PLACE."""
        self.place.remove_fighter(self)
        place.add_fighter(self)

    def blocked(self):
        """Return True if this Terminator cannot advance to the next Place."""
        # BEGIN 2.4
        if self.place.dragon is None or self.place.dragon.blocks_path is False:
            return False
        else:
            return True

        # END 2.4

    def action(self, colony):
        """A Terminator's action stings the Dragon that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The DragonColony, used to access game state information.
        """

        # BEGIN 4.4
        "*** YOUR CODE HERE ***"
        if self.is_scared == False:
            destination = self.place.exit
        else:
            destination = self.place.entrance
            self.count +=1
            #if destination == skynet:
                #destination = self.place
        if self.count>2:
            destination = self.place.exit
        # END 4.4
        if self.blocked():
            self.sting(self.place.dragon)
        elif self.armor > 0 and destination is not None:
            self.move_to(destination)


        # For multiple stacking,start from the lastest action and if latest was slow_action then if colony.time is even then second last was
        #allowed to take it action but if colony.time is odd then inner does not get exicuted and get reserved for next time.