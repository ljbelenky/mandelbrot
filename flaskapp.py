


import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for
from matplotlib.figure import Figure 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io 
import base64



'''A point is in the set if it remains below threshold 
for a given number of iterations. If this happens, it
is represented as 0

If a point exceedes the threshold value, we record how 
many iterations it takes for that to happen
'''

class Mandelbrot:
    def __init__(self):
        self.span = 3
        self.n = 500
        self.real_center = -.5
        self.imaginary_center = 0
        self.limit = 200
        self.threshold = 100

    def mandelbrot(self,z0):
        z = z0
        for t in range(self.limit):
            if abs(z) > self.threshold:
                return t
            z = z*z + z0
        return 0
    
    def plot(self):
        fig = Figure()
        ax = fig.subplots()
        
        plt.figure(figsize=(20,20))

        real = np.linspace(self.real_center - self.span/2, self.real_center+self.span/2, self.n)
        imaginary = np.linspace(self.imaginary_center - self.span/2, self.imaginary_center + self.span/2, self.n)
        X = np.array([[complex(r,i) for r in real] for i in imaginary]).flatten()
        
        x = np.vectorize(self.mandelbrot)(X).reshape(-1,self.n)[::-1,:]
        # x = x + x[x>0].min().astype('uint8')

        ax.imshow(x)
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])

        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String = 'data:iamge/png;base64,'
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

        return pngImageB64String


        
    def zoom_in(self):
        self.span /= 3

    def zoom_out(self):
        self.span *= 3
        
    def left(self):
        self.real_center += self.span/3
        
    def right(self):
        self.real_center -= self.span/3
        
    def up(self):
        self.imaginary_center -= self.span/3
        
    def down(self):
        self.imaginary_center += self.span/3


app = Flask(__name__)

@app.route('/home')
def reset():
    m.__init__()
    return home()

@app.route('/')
def home():
    return render_template('home.html', image = m.plot())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/in')
def zoom_in():
    m.zoom_in()
    return home()

@app.route('/out')
def zoom_out():
    m.zoom_out()
    return home()

@app.route('/up')
def up():
    m.up()
    return home()

@app.route('/down')
def down():
    m.down()
    return home()

@app.route('/left')
def left():
    m.left()
    return home()

@app.route('/right')
def right():
    m.right()
    return home()


if __name__ == '__main__':
    m = Mandelbrot()

    app.run(debug = True)


        
