# The World's Simplest Implementation of the Mandelbrot Set

This is intended as a starter for students to do further development.

Ideas:

1. Add ability to zoom in
1. Add ability to specify a center point
1. Make threshold a variable
1. Make limit (max number of iterations) a variable
1. Rescale values for plotting (perhaps use a log scale)
1. Experiment with different color maps
1. Explore the path a particular point follows as it converges or diverges

![Mandelbrot Set](images/mandelbrot.png)

## Instructions to get it running on AWS:

1. Spin up an EC2 instance. Nano or Micro works fine, and Ubuntu 18.04 AMI
1. Set inbound and outbound rules: ssh for my IP address, HTTP for all addresses
1. ssh in to instance
1. git clone this repo and cd to directory
1. sudo apt install docker.io
1. sudo docker build -t mandelbrot .
1. tmux
1. sudo docker run -p 80:5001 mandelbrot
1. ctrl-b, d
1. find IP address of EC2 and visit website (note: it's on http, not https)
