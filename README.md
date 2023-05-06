# ethics_game

- [Requirements](#requirements)
- [Installation](#installation)
- [Building From Source (macOS/Linux)](#building-from-source-macoslinux)
- [Note: Kitty & Alacritty](#note-kitty-alacritty)
- [Known Issues](#known-issues)

A 2D CLI adventure game where the enemies are multiple choice questions regarding social and ethical issues in software design and development.

![](./images/preview.png)

☆ Recycled engine from my old account: https://github.com/dturnip/explorer

### Requirements

- Python 3.11+
- Terminal emulator can render 256 colors
- Terminal emulator is equipped with a font that can render Nerd Font glyphs. Recommended fonts are included in `fonts/`. Font sizes `16.0`〜`24.0` are recommended.

### Installation

Download the latest [release](https://github.com/amiyuki7/ethics_game/releases) binary

### Building From Source (macOS/Linux)

Python 3.11.3 is recommended as this is the version used to create and compile this project.

```sh
$ git clone https://github.com/amiyuki7/ethics_game.git
$ cd ethics_game
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pyinstaller cli.spec
```

The binary is in `./dist/cli`

### Note: Kitty & Alacritty

GPU accelerated terminals are great for this game as there will be less flickering and overall smoother performance. Both kitty and/or Alacritty are excellent choices, but will fail to render specific characters because `$TERM` is something other than `xterm-256color`. The below command fixes this issue:

```bash
$ export TERM=xterm-256color
```

For developer convenience, this is included in `run.sh`

### Known Issues

- Resizing the terminal window to a smaller size will crash the program
