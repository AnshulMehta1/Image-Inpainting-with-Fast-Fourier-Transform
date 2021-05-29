from PIL import Image
import os, sys

def red(r,g,b):
    newr=r
    newg=0
    newb=0
    return(newr,newg,newb)

def blue(r,g,b):
    newr=0
    newg=0
    newb=b
    return(newr,newg,newb)

def green(r,g,b):
    newr=0
    newg=g
    newb=0
    return(newr,newg,newb)

def yellow(r,g,b):
    newr=r
    newg=g
    newb=0
    return(newr,newg,newb)

def purple(r,g,b):
    newr=r
    newg=0
    newb=b
    return(newr,newg,newb)

def cyan(r,g,b):
    newr=0
    newg=g
    newb=b
    return(newr,newg,newb)

def grey(r,g,b):
    newr=r+g+b//3
    newg=r+g+b//3
    newb=r+g+b//3
    return(newr,newg,newb)

def orange(r,g,b):
    newr=r+r
    newg=g
    newb=0
    return(newr,newg,newb)


img= Image.open("imageG.jfif").convert("RGB")

width,height = img.size
pixels= img.load()

for py in range(height):
    for px in range(width):
        r,g,b=img.getpixel((px,py))
        pixels[px,py]=orange(r,g,b)

outfile=img.show()
outfile= img.save("output.jpg") 
