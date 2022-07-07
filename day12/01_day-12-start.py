############# Scope ################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength) <<<<<<< error


# Global Scope
player_health = 10

def drink_potions():
    potion_strength = 2
    print(player_health)

drink_potions()


# There is no BlockScope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


# Modifying Global Scope
enemy = 1

def increase_enemies():
    global enemy
    enemy += 1
    print(f"enemies inside unction: {enemy}")

increase_enemies()
print(f"enemies inside unction: {enemy}")


# Global Constants
PI = 3.141519
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"