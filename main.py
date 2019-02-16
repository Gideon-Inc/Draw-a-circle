from matplotlib import pyplot as plt
import time

f = plt.figure(1, figsize=(8, 8))
ax = f.gca()
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
f.show()


r = 25
x = 0
y = r

d = 3 - 2 * r

'''
colors (( bo, go, etc... ))
‘b’	blue 
‘g’	green
‘r’	red
‘c’	cyan
‘m’	magenta
‘y’	yellow
‘k’	black
‘w’	white
'''

def plot(_x, _y, _radius):
    ax.plot(_x, _y, 'bo')
    ax.plot(-_x, _y, 'bo')
    ax.plot(_x, -_y, 'bo')
    ax.plot(-_x, -_y, 'bo')

    ax.plot(_y, _x, 'bo')
    ax.plot(_y, -_x, 'bo')
    ax.plot(-_y, _x, 'bo')
    ax.plot(-_y, -_x, 'bo')
    f.canvas.draw()


while y >= x:
    plot(x, y, r)
    x = x + 1
    if d > 0:
        y = y - 1
        d = d + 4 * (x - y) + 10
    else:
        d = d + 4 * x + 6

time.sleep(10)
