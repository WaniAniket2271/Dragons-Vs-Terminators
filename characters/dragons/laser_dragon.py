from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    food_cost = 10
    damage = 2

    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        temp = self.place
        temp_dict={}
        counter = 0
        if temp.dragon.is_container is True:
            temp_dict[temp.dragon] = 0
        while(temp!=skynet):
            if len(temp.terminators) != 0:
                for i in temp.terminators:
                    temp_dict[i]=counter
            if counter!=0:
                if temp.dragon is not None:
                    if temp.dragon.is_container is False:
                        temp_dict[temp.dragon]=counter
                    else:
                        temp_dict[temp.dragon] = counter
                        if temp.dragon.contained_dragon is True:
                            temp_dict[temp.dragon.contained_dragon]=counter

            temp= temp.entrance
            counter+=1
        return temp_dict
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        damage= self.damage
        damage_due_distance = 0.2*distance
        additional_damage = self.fighters_shot*0.05
        damage = damage - damage_due_distance - additional_damage

        return damage
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
