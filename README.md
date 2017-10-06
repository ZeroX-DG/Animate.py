# Animate.py [![Version](https://img.shields.io/badge/latest%20version-2-green.svg)](https://github.com/ZeroX-DG/Animate.py/tree/master/src/) [![PYversion](https://img.shields.io/badge/python-2.x-red.svg)](https://www.python.org/downloads/) 
*Just a python animations file*

## Installation
This module use for python 2.x.<br />
1. Just download animate.py from github and add the file to the same dir of your code.<br />
2. Import animate.py using this code: 
```
import animate
```
<br />
##Basic Usage
Use one of these effects<br />

  - Typing
  - Bounce
  - Frame
  - CharRun
  - slideInRight
  - slideInLeft
  - slideInTop
  - slideInBottom

Example:

mywork/ <br>
&nbsp;&nbsp;&nbsp;|-&nbsp;&nbsp;myfile.py<br>
&nbsp;&nbsp;&nbsp;|-&nbsp;&nbsp;animate.py<br>

myfile content:

```
import animate

animate.Typing("abc")
```

##Usage
Each effect duration can be modify by using this parameter:
```
duration=sec
```
Default duration will equal to 1 sec <br />
And you can change SlideIn effects distance which is the point in the console that the slideIn efftect will stop by using the parameter
```
distance=number
```
last but not least: the CharRun effect<br />
You can change the distance of this effect using distance parameter and remember the distance must greater than the text length ! Why ? try it, you will know why ;)

##Contact:
Facebook: https://www.facebook.com/profile.php?id=100010901431527
