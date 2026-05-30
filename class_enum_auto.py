from enum import Enum,auto
damage=0
class DifficultyType(Enum):
    EASY=auto()
    MEDIUM=auto()
    HARD=auto()

class EnemyDamage:
    def __init__ (self,easy,medium,hard):
        self.easy=easy
        self.medium=medium
        self.hard=hard
        
        
    def enemy_damage(self,difficulty):
        if difficulty==DifficultyType.EASY:
            return self.easy
        elif difficulty==DifficultyType.MEDIUM:
            return self.medium
        elif difficulty==DifficultyType.HARD:
            return self.hard
    
        
zombie=EnemyDamage(10,20,30)
creeper=EnemyDamage(75,50,100)


print(zombie.enemy_damage(DifficultyType.HARD))





















