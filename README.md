# RPI-Matrix-Player
Still a WIP, many globals need to be removed.
This Python script allows you to run small games on a 8x8 LED Matrix connected to your Raspberry Pi.
The Script Interfaces with Game modules via simple function calls, allowing you to easily Code your own Games without having to know the inner workings of everything.

## Playing a Game
To Start, you will need an 8x8 LED Matrix, a Raspberry Pi, two 75HC595 Shift Registers and three of those standard tactile buttons you get literally everywhere.

(Schematics go here)

Clone the repository and run the controller.py script. It will ask you for the name of the Game module you want to load. To test if everything is working, the repository comes with a (admittedly poorly coded) tetris clone. Just type "tetris" and hit Enter. A Virtual Matrix should also open, hopefully showing the same results as your real one. You should now be able to play tetris with the buttons.

## Making a Game
While you could theoretically already make a Game with help from the samplegame.py file, I don't recommend it as I'm still figuring out the interfacing between the controller script and game modules. So literally the whole thing might change in the future. If you do however decide to make one, get in contact with me and I will include it in a list here.
