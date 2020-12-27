'''
************************************************* First KATA **************************************************

Story
There are four warriors, they need to go through a dark tunnel. Tunnel is very narrow, every time only can let two warriors through, and there are lot of dangerous traps. Fortunately, they have a lamp that can illuminate the tunnel to avoid being trapped by the trap.

In order to pass this tunnel, they need five steps:

Two people go through the tunnel with the lamp
And then one people come back with the lamp
And then two people go through the tunnel with the lamp
And then one people come back with the lamp
And then two people go through the tunnel with the lamp
Each warrior has his own walking speed, we need to calculate the shortest time they have to cross the tunnel.

For example:

Four warriors is a,b,c,d. Their speed are [3,4,5,6]. It means they need 3 minutes, 4 minutes, 5 minutes and 6 minutes to cross the tunnel. The shortest crossing time should be 21 minutes, the method is as follows:

a and b go through the tunnel  ---> Spend 4 minutes
(Time spent should be calculated by the person who is slow)
a come back                    ---> Spend 3 minutes
a and c go through the tunnel  ---> Spend 5 minutes
a come back                    ---> Spend 3 minutes
a and d go through the tunnel  ---> Spend 6 minutes
Do you have any other better way?

Task
Complete function shortestTime() that accepts 1 argument: speed that are the spent time of four warriors. Returns the shortest time that all warriors go through the tunnel.

Note: The method in example above is not always the best way.

Example
shortestTime([3,4,5,6])  === 21

shortestTime([3,7,10,18])  === 41

shortestTime([5,5,6,7])  === 27

shortestTime([5,6,30,40])  === 63

'''

'''
************************************************* Second KATA *************************************************

Problem Description
The story continues.

After the great success of the Four Warriors, a whole army of n warriors have reached the entrance of the dreaded tunnel, which is still narrow and full of traps. Now the n warriors want to pass the tunnel, but the same rules apply:

At most two warriors can pass the tunnel at once.
There is still one lamp (probably due to stupid leader :P), so one person has to come back carrying the lamp before other people can pass the tunnel.
Each warrior has his own walking speed, which is given as the time to pass the tunnel in minutes.
The walking speed of two people is the slower one.
Your task is to find the shortest possible time for the warriors to pass the tunnel, given the passing times of the warriors times.

Examples
Four warriors a, b, c, d with speed [3, 4, 5, 6] will take 21 minutes:

a and b go through the tunnel  ---> Spend 4 minutes
a come back                    ---> Spend 3 minutes
a and c go through the tunnel  ---> Spend 5 minutes
a come back                    ---> Spend 3 minutes
a and d go through the tunnel  ---> Spend 6 minutes
More examples:

shortest_time([10]) == 10
shortest_time([10, 11]) == 11
shortest_time([5, 10, 15]) == 30

shortest_time([3, 4, 5, 6]) == 21
shortest_time([5, 5, 6, 7]) == 27
shortest_time([3, 7, 10, 18]) == 41
shortest_time([5, 6, 30, 40]) == 63

shortest_time([1, 2, 4, 8, 16]) == 28
shortest_time([4, 5, 6, 7, 8, 9]) == 49
shortest_time([1, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 109


'''


def shortest_time(speed):
    lenght = len(speed)
    result = []
    if lenght == 4:
        minn = min(speed)
        speed.remove(minn)
        result.append(2*minn+sum(speed))
        speed.append(minn)
    if len(speed)<= 2: return max(speed)
    else:
        bridge,cross,total = [],[],0
        flag,flag2 = False,False
        while len(speed) != 0:
            if flag2 == False:
                if len(bridge) < 2:
                    if flag:
                        bridge.append(max(speed))
                        speed.remove(max(speed))
                    elif flag == False:
                        bridge.append(min(speed))
                        speed.remove(min(speed))
                elif len(bridge) == 2:
                    if flag:
                        total += max(bridge)
                        [cross.append(i) for i in bridge]
                        [bridge.remove(bridge[0]) for i in range(2)]
                        speed.append(min(cross))
                        total += min(cross)
                        cross.remove(min(cross))
                        flag2 = True
                    else:
                        total += max(bridge)
                        cross += max(bridge),
                        bridge.remove(max(bridge))
                        total += bridge[0]
                        speed.append(bridge[0])
                        bridge.remove(bridge[0])
                        flag = True
            else:
                if bridge == []: 
                    bridge.append(min(speed))
                    speed.remove(min(speed))
                else:
                    bridge.append(max(speed))
                    speed.remove(max(speed))
                    total += max(bridge)
                    bridge.remove(max(bridge))
                    if len(speed) != 0: total += min(bridge)
        if len(bridge) == 2: total += max(bridge)
        if lenght == 4:
            result.append(total)
            return min(result)
        return total

print(shortest_time([3,7,10,18]))
