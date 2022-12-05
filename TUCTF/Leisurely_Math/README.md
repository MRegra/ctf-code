# TUCTF 2022 (02 December 2022 to 04 December 2022)

## Leisurely Math

Category: Programming

Description:

    Too slow for rapid arithmetic? Want to take things a little more leisurely? Try this challenge!

    nc chals.tuctf.com 30202

Solution:

Once we connect to the provided host using netcat, we are presented with:

    tuctf$ nc chals.tuctf.com 30202
    1736 * 9585 * 8442 * 2261
    Answer:

Once we put in the response:

    You took too long to answer!

So we cannot do this manually.
I created a script to solve this operations.
One has to consider the mathematical rules behind this.

    - Multiplication is performed first

Script:

[My Solution Script](./leisurely_math.py)

Notes: There is, for sure, a more elegant and better code.
