308reedpipes
===

Time:       2 weeks

Team:       1

Language:   Python


The project
----
Having been a reed pipe enthusiast for a long time now, your cousin cobbled together a little numerically controlled machine that will enable him to carry out a serial production of reed pipes and make a business out of it. However, he would like a software so that he can design his pipes himself...

So, you have to create a program for him that, starting from the **pipe’s radius (in cm)** with abscissas 0, 5, 10, 15 and 20cm, and using **cubic splines**, displays the **radii of *n* points** that are evenly distributed along the pipe. In order to simplify the debugging process, you will also display the resolved linear system’s vector result in order to obtain the spline.


## USAGE:

```
>> ./308reedpipes -h
USAGE
    ./308reedpipes r0 r5 r10 r15 r20 n

DESCRIPTION
    r0      radius (in cm) of pipe at the 0cm abscissa
    r5      radius (in cm) of pipe at the 5cm abscissa
    r10     radius (in cm) of pipe at the 10cm abscissa
    r15     radius (in cm) of pipe at the 15cm abscissa
    r20     radius (in cm) of pipe at the 20cm abscissa
    n       number of points needed to display the radius
```

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)