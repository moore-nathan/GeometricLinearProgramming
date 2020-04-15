import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
# x = np.arange(0, 2*np.pi, 0.01)
x1 = np.linspace(0, 10, 1000)
# print(x1+1)
# line, = ax.plot(x, np.sin(x))
line2, = ax.plot([], [])


def init():  # only required for blitting to give a clean slate.
    # line.set_ydata([np.nan] * len(x))
    line2.set_data([],[])
    return line2,


def animate(i):
    # line.set_ydata(np.sin(x + i / 100))  # update the data.
    x1 = np.linspace(0, 10, 1000)
    y1 = x1 +i
    line2.set_data(x1,y1)
    return line2, #line


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1000, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
