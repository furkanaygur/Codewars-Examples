'''
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

Return True if yes, False otherwise :)

8kyu

'''
# def hero(bullets=0, dragons=0):
#     return (bullets/2 >= dragons)

# print(hero(4,5))


'''
I'm afraid you're in a rather unfortunate situation. You've injured your leg, and are unable to walk, and a number of zombies are shuffling towards you, intent on eating your brains. Luckily, you're a crack shot, and have your trusty rifle to hand.

The zombies start at range metres, and move at 0.5 metres per second. Each second, you first shoot one zombie, and then the remaining zombies shamble forwards another 0.5 metres.

If any zombies manage to get to 0 metres, you get eaten. If you run out of ammo before shooting all the zombies, you'll also get eaten. To keep things simple, we can ignore any time spent reloading.

Write a function that accepts the total number of zombies, a range in metres, and the number of bullets you have.

If you shoot all the zombies, return "You shot all X zombies." If you get eaten before killing all the zombies, and before running out of ammo, return "You shot X zombies before being eaten: overwhelmed." If you run out of ammo before shooting all the zombies, return "You shot X zombies before being eaten: ran out of ammo."

(If you run out of ammo at the same time as the remaining zombies reach you, return "You shot X zombies before being eaten: overwhelmed.".)

Good luck! (I think you're going to need it.)

7kyu

'''

def zombie_shootout(zombies=0.0, distance=0.0, ammo=0):
    killCount = 0
    if ammo == 0:
        return (f'You shot {killCount} zombies before being eaten: ran out of ammo.')
    while distance != 0.0:
        distance = distance - 0.5
        if (zombies == 0.0 and ammo == 0) and distance >= 0:
            return (f'You shot all {killCount} zombies.')
        if ammo > 0:
            ammo = ammo - 1
            if zombies > 0.0:
                zombies = zombies - 1
                killCount = killCount + 1
            else:
                return (f'You shot all {killCount} zombies.')
                break
        else:
            return (f'You shot {killCount} zombies before being eaten: ran out of ammo.')
            break
        
    if zombies>0.0:
        return (f'You shot {killCount} zombies before being eaten: overwhelmed.')
    return (f'You shot all {killCount} zombies.')

print(zombie_shootout(19.1,10,20))

