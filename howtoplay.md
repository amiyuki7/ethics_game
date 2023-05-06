# How to play

### Synopsis

1. Move in front of a group of three red heads
2. Interact with the middle one to answer a question
3. Correct? The red heads disappear and you can continue exploring
4. Incorrect? Lose 1 HP. Game ends when all 5 HP is lost.
5. Answer all reachable questions to win (there are 11)

### The Side Panel

<!-- There are 3 states: -->

1. **_Normal_** : Displays the player name, position, HP and progress
2. **_Command Log_** : Displays the command log
3. **_Command Prompt_** : Displays the command log and a green field at the bottom for command input

### Keybinds

| key       | action                                                                    |
| --------- | ------------------------------------------------------------------------- |
| w         | Move up 1 tile                                                            |
| a         | Move left 1 tile                                                          |
| s         | Move down 1 tile                                                          |
| d         | Move right 1 tile                                                         |
| e         | Interacts with a question                                                 |
| c         | Switches from normal to command log                                       |
| p         | Switches from normal to command prompt                                    |
| RETURN    | Switches from command prompt to command log if the prompt buffer is empty |
| SHIFT + q | Quits the game                                                            |

### Commands

| command                     | action                                          |
| --------------------------- | ----------------------------------------------- |
| open                        | Opens the question image in the default browser |
| answer \<a \| b \| c \| d\> | Submits the user's answer to a question         |
