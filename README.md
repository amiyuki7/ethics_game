# ethics_game

Recycled engine from my old account: https://github.com/dturnip/explorer

## Requirements

- Python 3.10+
- Terminal emulator is able to render 256 colors
- Terminal emulator is equipped with a font that can render Nerd Font glyphs. Recommended fonts are included in `fonts/`. Font sizes `16.0`〜`24.0` are recommended.

## macOS / Linux

## Kitty & Alacritty

- GPU accelerated terminals are great for this game as there will be less flickering and smoother performance. Both kitty and Alacritty will fail to render specific characters because `$TERM` is something other than `xterm-256color`. The below command fixes this problem (no need if you are using `./run.sh`):

```bash
export TERM=xterm-256color
```
