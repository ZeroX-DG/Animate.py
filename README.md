# Animate.py [![Version](https://img.shields.io/badge/current%20version-1-red.svg)](https://github.com/ZeroX-DG/Animate.py/tree/master/src/ver_1)
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

  -Typing<br />
  -Bounce<br />
  -Frame<br />
  -CharRun<br />
  -slideInRight<br />
  -slideInLeft<br />
  -slideInTop<br />
  -slideInBottom<br />

Example:

mywork/ <br>
  myfile.py<br>
  animate.py<br>

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
