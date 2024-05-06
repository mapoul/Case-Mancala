# Mancala
A simple game play of Mancala. You can play with a computer player.

## How to play
1. Make sure you have python3 installed.
   My version: `3.8.10`
1. Run the code.
   ```
   python main.py
   ```
1. Enjoy!

## What am I doing?
I aimed to practice and learn the following:
* Design patterns
* Clean code
* Machine Learning

But now, I hope this can be an ice-breaker for you and other developers 😸!

Please feel free to be critical on this project during your discussions, because that's how you get to know each other :)
___________________________________________________________

# Case study topics

## Code quality/how I would implement it
In my opinion, with the experience I have of python, I think overall it's a nice project.
I like how functions are well split up, into smaller functions, with a suitable name that states
what the function does, so you have an idea what you are reading. There is a minor thing with consistency. I ran the game as the
first thing, to see the behaviour of the game, and in the instructions it says its stones being moved from pot to pot, so I was looking out for functions that might have
something with name of "move-stone", but it was peas-functions I was looking for - again, a very small thing, but consistency helps readability.

I refactored the class human_player.py and merged get_input and validate_step to reduce the lines of code to make it more readable while also
changing it from a list to a dictionary for performance (though with this little amount of keys/elements it makes next to no difference) because a dictionary takes a shorter amount of time to traverse.

It says in this readme above, that the developer is working with Clean code, and that might be different
in python from what I've learned, and how im used to working with it, architectural wise anyway.
That might also make sense, when it's this small of a project, to structure it this way, because when working with types in Typescript and passing data from one layer to the other,
can create some overhead.
If I was to implement something with the clean architecture, I would have the core/business logic of my application isolated, and segregate that
with interfaces. Having the core isolated from 3rd party packages and libraries means you can easily change to another package if you find something more
suitable later, and by having it segregated with interfaces you access through dependency injection, you only need to change the implementation of the service using that package
without having to change the business logic.


## How can the game be tested?
You can write unit tests to testable functions. I changed the judge function in game.py to return a value, instead of exiting the game, as an example of how it
could be written to be more test friendly. You need some values to test, instead of exiting the program.

## Security
The game has basic input validation as it looks if the input given by the human player, is in the list of allowed steps.

## Objects and responsibility
I think the objects and their responsibilities are generally fine, the player class is sort of a factory to figure out if
its human player or the machine player, and then their respective class has their own logic.
