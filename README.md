# mandelbrot_pygame

A (slow) Mandelbrot renderer (no scaling) for python3 with pygame.

## I made a YouTube video about this project in German language.
Feel free to watch and support.
* Link 1: https://www.youtube.com/watch?v=uh9IYDHR6vw
* Link 2: https://www.youtube.com/watch?v=JrF2L--X9z8

## Dependencies
* **pygame** is used for drawing pixels to the screen
* **colorsys** is used for conversion from the HSV color model to the RGB color model

## Explanation
Pixels on the screen are transformed into complex numbers. The initial coordinate system goes somewhere from -2 to 1 on x, from -1 to 1 on y.
Each complex number is used in a mathematical series.
Over the course of that, the number either
* diverges to infinity.
In that case we detect how fast this happens and paint the pixel in an according color. For that, we use different Hue values to make a color in the HSV color model, which we will later transform.
* converges to 2.0.
In this case the number (the pixel) is part of the Mandelbrot set and we paint it black.
