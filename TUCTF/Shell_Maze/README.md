# TUCTF 2022 (02 December 2022 to 04 December 2022)

## Shell Maze

Category: Programming

Description:

    Not even maze runner could escape this maze...

    nc chals.tuctf.com 30204

Solution:

Once we connect to the provided host using netcat, we are presented with:

    Welcome to Shell Maze 1!
    Please navigate this maze for me!
    Controls: `<` to move left, '>' to move right, and 'V' to move down.
    XOOOOOOOOOOOOOOOOO##
    #################O##
    #################O##
    #####OOOOOOOOOOOOO##
    #####O##############
    #####OOOOOOOOOOOO###
    ##OOOOOOOOOOOOOOO###
    ##O#################
    ##O#################
    ##OOOOOOO###########
    OOOOOOOOOOOOOOOOOOOO
    Move:

Once we solve the maze, a new one pops up...
So we cannot do this manually.

I created a script to solve the challenges as they come:

[My Solution Script](./shell_maze.py)






