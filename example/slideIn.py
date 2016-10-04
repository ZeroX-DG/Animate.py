import animate
import time


"""
This file show some great help on how to use slideIn and other effect
"""

"""
First we will try to use slideIn
every slideIn effect has distance and duration parameter !
"""

#right
animate.slideInRight("bro! Im slide in from the right");
time.sleep(2)

#left
animate.slideInLeft("Yeah I see you bro ! I'm from the left",distance=10);
time.sleep(2)

#top
animate.slideInTop("Left and Right ! I'm coming down in 3sec",duration=3);
time.sleep(2)

#bottom
animate.slideInBottom("Hey I'm too old ! I'm just go up 15 line ok? wait 2s",distance=15,duration=2);
time.sleep(2)

"""
And next we will try some other effect in version 2
"""

animate.TopToBottomRight("ahihi");
animate.TopToBottomLeft("hohoo");

animate.VBounce("HEHEHEHE");
animate.HBounce("HOHOHOHO");

"""
And that's the end of example !
"""
