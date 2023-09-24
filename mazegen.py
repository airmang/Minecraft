dirs: List[number] = []
index2 = 0
index = 0
right = 0
left = 0
forward = 0
temp = 0
moves: List[str] = []
tempArray: List[number] = []

def on_on_chat():
    blocks.fill(STONE, pos(-5, 0, -5), pos(5, 0, 5), FillOperation.REPLACE)
    agent.teleport_to_player()
    blocks.place(AIR, pos(0, 0, 0))
    agent.set_assist(DESTROY_OBSTACLES, False)
    player.teleport(pos(0, 5, 0))
    player.say("let's dig that maze!")
    dig()
player.on_chat("maze", on_on_chat)

def shuffle():
    global tempArray, index, index2, temp
    tempArray = [forward, left, right]
    for i in range(3):
        index = Math.random_range(0, 2)
        index2 = Math.random_range(0, 2)
        temp = tempArray[index]
        tempArray[index] = tempArray[index2]
        tempArray[index2] = temp
    k = 0
    while k <= 3 - 1:
        dirs.append(tempArray[k])
        k += 1
def dig():
    global temp
    player.say("dig deeper")
    shuffle()
    for j in range(3):
        player.say("try " + moves[dirs[len(dirs) - 1]])
        # turn towards the new direction
        if dirs[len(dirs) - 1] == left:
            agent.turn(TurnDirection.LEFT)
        elif dirs[len(dirs) - 1] == right:
            agent.turn(TurnDirection.RIGHT)
        # is this a wall?
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            # dig once
            agent.destroy(FORWARD)
            agent.move(FORWARD, 1)
            # did we dig through a wall?
            if not (agent.detect(AgentDetection.BLOCK, FORWARD)):
                player.say("oops, that was a wall")
                # move back and put the wall back
                agent.move(BACK, 1)
                agent.place(FORWARD)
            else:
                # yay! keep digging
                agent.destroy(FORWARD)
                agent.move(FORWARD, 1)
                # did we reach the end of the maze?
                if not (agent.detect(AgentDetection.BLOCK, FORWARD)):
                    # go back and place wall
                    player.say("oops, too far")
                    agent.move(BACK, 1)
                    agent.place(FORWARD)
                    agent.move(BACK, 1)
                else:
                    dig()
                    # start roll back
                    agent.move(BACK, 2)
        # turn back to the original direction
        if dirs[len(dirs) - 1] == left:
            agent.turn(TurnDirection.RIGHT)
        elif dirs[len(dirs) - 1] == right:
            agent.turn(TurnDirection.LEFT)
        temp = dirs.pop()
moves = ["forward", "left", "right"]
temp = 1
forward = 0
left = 1
right = 2
