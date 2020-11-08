# VR-Drawing-Cutiehack
## Inspiration
The inspiration behind this VR Hand Painting project was a mix between making a covid friendly project (no touching required), as well as using a newly acquired VR Hand Sensor.

## What it does
It allows the user to draw any image they want while only using the motion of their hand. To start drawing, you simply put your thumb and index finger together. To stop drawing, simply separate your fingers. It also allows the user to choose a pencil width by moving your hand closer or further from the sensor.

## How we built it
By using a Leap Motion VR Hand Sensor, we were able to live feed of coordinates to a local WebSocket since our two files were coded in different versions of Python (python2.7 and python3). From there, we built a GUI using pygame in python and used a mixture of coordinate manipulation and different algorithms to successfully make this smooth running GUI. 

## Challenges we ran into
Our biggest challenge was being able to seamlessly transition from drawing to not drawing. It was hard because we didn't know how to make it so it still showed the painter's curser while not actively drawing. 

## Accomplishments that we're proud of
Overall, the websocket between the two files was a big accomplishment. Also we are really proud of overcoming the problem we ran into that was previously listed. However, overall, everything we accomplished in this project made us feel proud of the work we did today.

## What we learned
We learned how to utilize a Leap Motion VR Hand Sensor and actually be able to incorporate it into a larger project. We learned how to use a WebSocket in order to pipe data from one place to another in real time.

## What's next for VR Drawing
Next, would be more color options, more stability, and maybe different types of pens.

Credit to: Noah Allen, Sahil Patel, Tinghui Song
