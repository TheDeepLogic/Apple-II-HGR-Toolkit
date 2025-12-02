# Apple II HGR Toolkit

A Python-based code generator for creating Applesoft BASIC programs with HGR (High Resolution Graphics) text effects for the Apple II computer.

## Features

- **Bitmap Text Rendering**: Generates optimized HPLOT commands from a built-in 5x7 pixel font
- **Multiple Text Blocks**: Create multiple text elements at different positions with a single command
- **Scrolling Text**: Animated scrolling effects with configurable speed and direction
- **No DATA Statements**: Fast execution by using direct HPLOT commands instead of slow DATA/READ loops
- **Configurable Colors**: Full HCOLOR support (0-7)
- **Bootloader Generation**: Optional automatic setup code (HGR initialization, GOSUB calls, END)

## Requirements

- Python 3.x
- An Apple II emulator (AppleWin, Virtual II, MAME, etc.) or real hardware

## Installation

Clone or download this repository:

```bash
git clone https://github.com/yourusername/Apple-II-HGR-Toolkit.git
cd Apple-II-HGR-Toolkit
```

No additional dependencies required - uses only Python standard library.

## Usage

### Basic Syntax

```bash
python hgr-create.py [effect] [options] [effect] [options] ... [--bootloader]
```

### Effects

#### Static Text

```bash
python hgr-create.py text "HELLO WORLD" -x 80 -y 90 --bootloader
```

#### Scrolling Text

```bash
python hgr-create.py scroll "BREAKING NEWS" --scroll -2,0,140 -x 279 -y 12 --bootloader
```

### Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `-x NUM` | X coordinate (0-279) | 10 for text, 279 for scroll |
| `-y NUM` | Y coordinate (0-191) | 80 for text, 12 for scroll |
| `-s NUM` | Character spacing in pixels | 6 |
| `--hcolor NUM` | Color value (0-7) | 3 (white) |
| `--bootloader` | Include HGR setup and GOSUB calls | Off |
| `-o FILE` | Save output to file | Stdout |

### Scroll Parameters

Format: `--scroll X,Y,ITERATIONS`

- **X**: Horizontal speed (negative = left, positive = right)
- **Y**: Vertical speed (negative = up, positive = down)  
- **ITERATIONS**: Number of animation frames

Example: `--scroll -2,0,140` scrolls left at 2 pixels per frame for 140 frames

## Examples

### Example 1: Simple Title Screen

```bash
python hgr-create.py text "SUPER GAME" -x 90 -y 80 --bootloader -o title.bas
```

Then in your Apple II emulator, load and run the file.

### Example 2: Multiple Text Elements

```bash
python hgr-create.py text "SCORE" -x 10 -y 10 text "LIVES" -x 200 -y 10 --bootloader
```

### Example 3: Left-Scrolling Credits

```bash
python hgr-create.py scroll "CREDITS: CODE BY YOU" --scroll -1,0,300 -x 279 -y 90 --bootloader
```

### Example 4: Diagonal Scroll

```bash
python hgr-create.py scroll "DEMO" --scroll -2,-1,100 -x 279 -y 191 --bootloader
```

### Example 5: Custom Colors

```bash
python hgr-create.py text "PLAYER 1" -x 50 -y 50 --hcolor 3 text "PLAYER 2" -x 50 -y 100 --hcolor 6 --bootloader
```

## Apple II HGR Reference

### Screen Resolution
- **Text Mode**: 280×192 pixels (7 colors)
- **Coordinate System**: X: 0-279, Y: 0-191

### HCOLOR Values
| Value | Color (on color monitor) |
|-------|--------------------------|
| 0 | Black |
| 1 | Green |
| 2 | Violet |
| 3 | White |
| 4 | Black |
| 5 | Orange |
| 6 | Blue |
| 7 | White |

Note: Colors 0/4 and 3/7 are both white/black but affect adjacent pixel colors differently.

## Output Format

The tool generates Applesoft BASIC code that can be:
1. Typed directly into an Apple II
2. Pasted into an emulator
3. Saved to a `.bas` file for loading

Example output:
```basic
1 REM ** BOOTLOADER **
5 HGR
10 GOSUB 1000
100 END

1000 REM ** TEXT: HELLO **
1001 REM ** AT X=10, Y=80 **
1002 HCOLOR = 3
1003 HPLOT 10,80 TO 10,86: HPLOT 14,80 TO 14,86: HPLOT 11,83 TO 13,83
...
1030 RETURN
```

## Font Character Set

Supported characters:
- **Letters**: A-Z (automatically converted to uppercase)
- **Numbers**: 0-9
- **Punctuation**: `.` `,` `!` `?` `-` `:` `;` `'` `"` `/` `\` `(` `)`
- **Space**: ` `

## Tips & Tricks

1. **Faster Animation**: Reduce the number of HPLOT commands by increasing character spacing
2. **Line Length**: BASIC lines are limited to ~238 characters; the tool automatically splits long lines
3. **Memory**: Each text block uses approximately 500 line numbers; plan your layout accordingly
4. **Testing**: Use an emulator with paste functionality for rapid iteration
5. **Optimization**: Omit `--bootloader` if integrating into existing code

## Technical Details

- Font is rendered as optimized HPLOT commands with horizontal line optimization
- Scroll effects use DX/DY variables for position offsets, enabling dynamic positioning
- Line number allocation: 1-100 for bootloader, 1000+ for effect subroutines (500 lines per effect)
- Generated code is compatible with Applesoft BASIC on Apple II/II+/IIe/IIc/IIGS

## Limitations

- Maximum line length handled automatically (splits at ~230 chars)
- No lowercase text (Apple II typically uppercase only)
- Monochrome per text block (HGR color fringing applies)
- Font is fixed 5×7 pixels

## Version History

- **v3.0**: Complete rewrite with multi-effect support, scrolling, and bootloader
- **v2.x**: Added variable positioning  
- **v1.x**: Initial release with basic text rendering

## Contributing

Contributions welcome! Ideas for enhancement:
- Additional font styles (3×5, 7×9, etc.)
- Shape table generation
- Additional effects (fade, blink, etc.)
- Sprite support
- Color cycling

## License

MIT License - see LICENSE file for details

## Author

Created for the vintage computing community. Happy coding on your Apple II! 🍎
