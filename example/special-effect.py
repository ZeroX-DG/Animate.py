import animate
import time

"""
This file will show you how to use animate.py ! But just special effects !
slideIn effect is in the next file !
"""

"""
First one is the typing text effect !
It has a optional parameter is duration for adjusting the duration
"""
animate.Typing("Wow this text is typing\n");
#now try to slow the typing speed !
animate.Typing("Wow this one was slow ! It run in 5 sec\n",duration=5);

"""
Next one we have bounce text !
and it also has a optional parameter but it is power !
default power is 5
"""

animate.Bounce("let's bounce\n"); #power = 5
print "Try some stronger bounce !";
time.sleep(3);
animate.Bounce("This one bounce stronger !\n",power=15); #power = 15

"""
Next we will put the text into a box !
"""
multi_Line_Text = """
Yo ! this is the first line
Hi ! I'm the second line
Hey ! I'm the last line !
He lie to u ! I'm the last line !
"""
animate.Frame(multi_Line_Text);
time.sleep(3)

"""
This one is my favorite effect
CharRun ! (I named it so bad :'( I took it from stack overflow =))
I can't find the author of this def anymore :'( if anyone found him plz let me know !)
I make it better ! now you can adjust the distance !
the default distance will be length of the text
"""

animate.CharRun("\nYo ! let's run !\n",distance=50);

#The Blinktyping is the same as the typing text but will the '|' char behind (bad effect)
"""
FadeOut (It's typing text but reverse !)
"""

animate.FadeOut("animate's great !")

"""
And diamond text (It took me 2 hour the make this :'(
I'm getting old :'( 15 years old already :'( )
"""

animate.Diamond("Thisonedoesnothing!!");

"""
Old printer :3 (I don't know how this name was in my head hahaha)
You can add the duration parameter !
"""
logo = """
 _____    ____   _____    ____    _    _ 
|___  |  |  __| |  _  |  / __ \  | \  / |
   /  /  | |__  | |_| | | |  | |  \ \/ / 
  /  /   |  __| |    /  | |  | |   >  <  
 /  /_   | |__  | |\ \  | |__| |  / /\ \ 
|_____|  |____| |_| \_\  \____/  |_/  \_|
"""
animate.OldPrinter(logo,duration=5); #5 sec ! this printer is too old !

"""
End of special effect !
move on the the slideIn !
"""
