init python:
    class Stats(Enum):
        MONEY = 1
        FITNESS = 2
        LUST_ENERGY = 3
        HORNY = 4
        FIGHT = 5
        CONFIDENCE = 6

    class Protag:
        def __init__(self, name, money=0, fitness=0, lust_energy=None, fight=0, horny=None, confidence=0):
            self.name = name
            self.money = money
            self.fitness = fitness
            self.fitness_xp = 0
            self.fitness_xp_list = [0,2,5,8,12,16,20,25,30,35,42]
            self.lust_energy = lust_energy # starts as None
            self.confidence = confidence
            self.fight = fight
            self.horny = horny # starts as None
            self.stat_max = 10
            self.confidence_boosters = []

            if config.developer:
                if(self.name is None) or (self.name == ""):
                    raise Exception("Cannot create Protag object without a name!")


        def get_stat_name(self, stat) -> str:
            if(stat == Stats.FITNESS):
                return "Fitness"
            elif(stat == Stats.LUST_ENERGY):
                return "Lust Energy"
            elif(stat == Stats.HORNY):
                return "Horniness"
            elif(stat == Stats.FIGHT):
                return "Fighting Ability"
            elif(stat == Stats.CONFIDENCE):
                return "Self-Confidence"
            if config.developer:
                raise Exception("There is no stat " + str(stat))

        def got_lust_energy(self) -> bool:
            if(self.lust_energy is None) or (self.lust_energy <= 0):
                return False
            return True

        def get_stat(self, stat):
            if(stat == Stats.MONEY):
                return self.money
            elif(stat == Stats.FITNESS):
                return self.fitness
            elif(stat == Stats.LUST_ENERGY):
                if(self.lust_energy is None):
                    return 0
                return self.lust_energy
            elif(stat == Stats.HORNY):
                if(self.horny is None):
                    return 0
                return self.horny
            elif(stat == Stats.FIGHT):
                return self.fight
            elif(stat == Stats.CONFIDENCE):
                return self.confidence
            if config.developer:
                raise Exception("Stat: " + str(stat) + " does not exist!")


        def gain_fitness_xp(self, amount=1) -> None:
            self.fitness_xp += amount
            #xp_list = [0,2,5,8,12,16,20,25,30,35,42]
            new_level = 0
            for i in range(len(self.fitness_xp_list)):
                if(self.fitness_xp >= self.fitness_xp_list[i]):
                    new_level = i

            if(self.fitness < self.stat_max):
                fitness_xp_for_next_level = self.fitness_xp_list[self.fitness+1] - self.fitness_xp_list[self.fitness]
                fitness_xp_for_current_level = self.fitness_xp - self.fitness_xp_list[self.fitness]
                sections = proper_round((fitness_xp_for_current_level/fitness_xp_for_next_level)*10)
                if(new_level > self.fitness):
                    self.fitness += 1
                    if(self.fitness >= self.stat_max):
                        self.add_confidence_booster("fitness")
                renpy.show_screen("fitness_xp_bar", [sections, fitness_xp_for_current_level, fitness_xp_for_next_level])


        def add_confidence_booster(conf_type:str):
            if(conf_type in self.confidence_booster):
                return
            self.confidence_boosters.append(conf_type)
            self.confidence += 1


        def reset_stat(self, stat, silent=False):
            if(stat == Stats.HORNY):
                self.horny = 0
                if not silent:
                    renpy.notify("Horniness: 0")
            elif(stat == Stats.LUST_ENERGY):
                self.lust_energy = 0
                if not silent:
                    renpy.notify("Lust Energy: 0")


        def update_stat(self, stat, amount, silent=False):
            if(amount == 0):
                return
            statement = ""
            if(stat == Stats.MONEY):
                self.money += amount
                statement += "Money: "
            elif(stat == Stats.FITNESS):
                self.fitness = min(max(self.fitness+amount, 0), self.stat_max)
                statement += "Fitness: "
            elif(stat == Stats.LUST_ENERGY):
                if(self.lust_energy is None):
                    self.lust_energy = 0
                self.lust_energy = min(max(self.lust_energy+amount, 0), self.stat_max)
                statement += "Lust Energy: "
            elif(stat == Stats.HORNY):
                if(self.horny is None):
                    self.horny = 0
                self.horny = min(max(self.horny+amount, 0), self.stat_max)
                statement += "Horniness: "
            elif(stat == Stats.FIGHT):
                self.fight = min(max(self.fight+amount, 0), self.stat_max)
                statement += "Fighting Ability: "
            elif(stat == Stats.CONFIDENCE):
                self.confidence = min(max(self.confidence+amount, 0), self.stat_max)
                statement += "Confidence: "

            if(not silent):
                if(amount > 0):
                    if(stat == Stats.MONEY):
                        statement += "+$" + str(amount)
                    else:
                        statement += "+" + str(amount)
                else:
                    if(stat == Stats.MONEY):
                        statement += "-$" + str(amount * -1)
                    else:
                        statement += str(amount)

                renpy.notify(statement)

