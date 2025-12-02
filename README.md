# Apple II HGR Toolkit

> **AI-Assisted Development Notice**
> 
> Hello, fellow human! My name is Aaron Smith. I've been in the IT field for nearly three decades and have extensive experience as both an engineer and architect. While I've had various projects in the past that have made their way into the public domain, I've always wanted to release more than I could. I write useful utilities all the time that aid me with my vintage computing projects, but rarely publish them. I've had experience in both the public and private sectors and can unfortunately slip into treating each one of these projects as a fully polished cannonball ready for market. It leads to scope creep and never-ending documentation updates.
> 
> With that in-mind, I've leveraged GitHub Copilot to create the code within this repository and, outside of this notice, all related documentation. While I'd love to tell you that I pore over it all and make revisions, that just isn't the case. To prevent my behavior from keeping these tools from seeing the light of day, I've decided to do as little of that as possible! My workflow involves simply stating the need to GitHub Copilot, running the resulting code, and, if there is an actionable output, validating that it's correct. If I find a change I'd like to make, I describe it to Copilot. I've been leveraging the Agent CLI and it takes care of the core debugging.
>
> With all that being said, please keep in-mind that what you read and execute was created by Claude Sonnet 4.5. There may be mistakes. If you find an error, please feel free to submit a pull request with a correction!

A Python-based code generator for creating Applesoft BASIC programs with HGR (High Resolution Graphics) text effects for the Apple II computer.

## Features

- **Bitmap Text Rendering**: Generates optimized HPLOT commands from a built-in 5x7 pixel font
- **Multiple Text Blocks**: Create multiple text elements at different positions with a single command
- **Scrolling Text**: Animated scrolling effects with configurable speed and direction
- **Font Weight Control**: Single, double, or triple width strokes to combat NTSC artifacts
- **Screen Fill**: Optional screen clearing with specified background color
- **Configurable Colors**: Full HCOLOR support (0-7) with palette information
- **Input Validation**: Automatic bounds checking with warnings for out-of-range coordinates
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
python hgr-create.py --text "STRING" [options] --text "STRING" [options] ... [--bootloader]
```

### Command Structure

The tool uses a consistent command-line syntax:
- **Global options** (like `--bootloader`, `--fill`) use double dashes (`--`) and affect the entire program
- **Text block options** (like `-x`, `-y`, `-color`, `-weight`) use single dashes (`-`) and affect only the current text block
- Each `--text` command creates a text block that can be static or scrolling

### Effects

#### Static Text

```bash
python hgr-create.py --text "HELLO WORLD" -x 80 -y 90 --bootloader
```

#### Scrolling Text

```bash
python hgr-create.py --text "BREAKING NEWS" -scroll -2,0,140 -x 279 -y 12 --bootloader
```

### Global Options

| Option | Description | Default |
|--------|-------------|---------|
| `--bootloader` | Include HGR setup and GOSUB calls | Off |
| `--fill NUM` | Fill screen with HCOLOR (0-7) before drawing | None |
| `-o FILE` | Save output to file | Stdout |

### Text Block Options

| Option | Description | Default |
|--------|-------------|---------|
| `-x NUM` | X coordinate (0-279) | 10 for static, 279 for scroll |
| `-y NUM` | Y coordinate (0-191) | 80 for static, 12 for scroll |
| `-color NUM` | Color value (0-7) | 3 (white) |
| `-weight NUM` | Font weight/thickness (1-3) | 1 (single) |
| `-spacing NUM` | Character spacing in pixels | 6 |
| `-scroll X,Y,ITER` | Enable scrolling with parameters | None (static) |

### Scroll Parameters

Format: `-scroll X,Y,ITERATIONS`

- **X**: Horizontal speed (negative = left, positive = right)
- **Y**: Vertical speed (negative = up, positive = down)  
- **ITERATIONS**: Number of animation frames

Example: `-scroll -2,0,140` scrolls left at 2 pixels per frame for 140 frames

## Examples

### Example 1: Simple Title Screen

```bash
python hgr-create.py --text "SUPER GAME" -x 90 -y 80 --bootloader -o title.bas
```

Then in your Apple II emulator, load and run the file.

### Example 2: Multiple Text Elements

```bash
python hgr-create.py --text "SCORE" -x 10 -y 10 --text "LIVES" -x 200 -y 10 --bootloader
```

### Example 3: Double-Width Text with Background

```bash
python hgr-create.py --text "HELLO" -x 50 -y 80 -weight 2 --fill 0 --bootloader
```

### Example 4: Left-Scrolling Credits

```bash
python hgr-create.py --text "CREDITS: CODE BY YOU" -scroll -1,0,300 --bootloader
```

### Example 5: Diagonal Scroll

```bash
python hgr-create.py --text "DEMO" -scroll -2,-1,100 -x 279 -y 191 --bootloader
```

### Example 6: Custom Colors with Triple Width

```bash
python hgr-create.py --text "PLAYER 1" -x 50 -y 50 -color 5 -weight 3 --bootloader
```

### Example 7: Mixed Static and Scrolling

```bash
python hgr-create.py --text "TITLE" -x 100 -y 20 -weight 2 --text "NEWS FLASH" -scroll -1,0,200 --bootloader
```

## Apple II HGR Reference

### Screen Resolution
- **Hi-Res Mode**: 280×192 pixels  
- **Effective Color Resolution**: 140×192 (due to NTSC artifact color)
- **Coordinate System**: X: 0-279, Y: 0-191

### Understanding Apple II HGR Colors

The Apple II's Hi-Res graphics mode is unique and somewhat peculiar. Each row of 280 pixels is divided into 40 blocks of 7 pixels, with the **most significant bit (MSB)** of each byte controlling which color palette is used for that block.

#### HCOLOR Values and MSB Palettes

| Value | Color Name | MSB | Palette | Pixel Pair | YIQ Values |
|-------|-----------|-----|---------|------------|-----------|
| 0 | Black | 0 | Green/Purple | 00 | Y:0.0, I:0.0, Q:0.0 |
| 1 | Green | 0 | Green/Purple | 01 | Y:0.5, I:1.0, Q:1.0 |
| 2 | Purple | 0 | Green/Purple | 10 | Y:0.5, I:-1.0, Q:-1.0 |
| 3 | White | 0 | Both | 11 | Y:1.0, I:0.0, Q:0.0 |
| 4 | Black | 1 | Orange/Blue | 00 | Y:0.0, I:0.0, Q:0.0 |
| 5 | Orange | 1 | Orange/Blue | 01 | Y:0.5, I:1.0, Q:-1.0 |
| 6 | Blue | 1 | Orange/Blue | 10 | Y:0.5, I:-1.0, Q:1.0 |
| 7 | White | 1 | Both | 11 | Y:1.0, I:0.0, Q:0.0 |

#### Important Color Quirks

1. **MSB Palette Switching**: When MSB=0, pixels use the green/purple palette. When MSB=1, pixels use the orange/blue palette. Drawing in one palette can change colors in the other palette within the same 7-pixel block.

2. **Color Interference**: If you draw a blue line (HCOLOR 6, MSB=1) over a green line (HCOLOR 1, MSB=0), portions of the green line will change to orange. This is because both green and orange are represented the same way in memory—only the MSB differs.

3. **Pixel Position Restrictions**:
   - Odd X-coordinates (1, 3, 5...): Can be green or orange
   - Even X-coordinates (0, 2, 4...): Can be purple or blue
   - Any pixel can be black or white

4. **Fringe Benefits**: 
   - Two or more consecutive lit pixels display as white
   - Alternating pixels display as color
   - Two or more consecutive off pixels display as black

#### Why Font Weight Helps

The `--weight` option combats NTSC artifacts by creating thicker strokes. When using weight 2 or 3, the doubled/tripled pixels create more solid white regions, reducing color fringing and making text more readable on colored backgrounds. This is why many Apple II programs used double-wide or chunky fonts.

### Practical Color Tips

- **Safest Approach**: Use HCOLOR 3 or 7 (white) on black backgrounds (--fill 0)
- **Same Palette**: Stick to colors from the same MSB palette (0-3 OR 4-7)
- **Use Weight**: For colored text on colored backgrounds, use `--weight 2` or `--weight 3`
- **Test First**: Always test your color combinations in an emulator before finalizing

### Technical Details: The 64:1 Interleave

The Hi-Res mode uses a 64:1 interleave factor (a result of Steve Wozniak's chip-saving design), causing the "Venetian blind" effect when loading screens. This doesn't affect our generated code but is interesting Apple II trivia!

## Output Format

The tool generates Applesoft BASIC code that can be:
1. Typed directly into an Apple II
2. Pasted into an emulator
3. Saved to a `.bas` file for loading

Example output:
```basic
1 REM ** BOOTLOADER **
5 HGR
7 REM ** FILL SCREEN **
8 HCOLOR = 0: HPLOT 0,0: CALL 62454
10 GOSUB 1000
100 END

1000 REM ** TEXT: HELLO **
1001 REM ** AT X=10, Y=80 **
1002 HCOLOR = 3
1003 HPLOT 10,80 TO 10,86: HPLOT 14,80 TO 14,86: HPLOT 11,83 TO 13,83
...
1030 RETURN

REM ======================================
REM APPLE II HGR COLOR INFORMATION
REM ======================================
REM Colors used in this program:
REM   HCOLOR 0: BLACK (MSB=0, green/purple palette)
REM   HCOLOR 3: WHITE (MSB=0, both palette)
REM
REM MSB=0 colors (0-3): Green/Purple palette
REM MSB=1 colors (4-7): Orange/Blue palette
REM
REM Note: Mixing colors from different MSB
REM palettes can cause color shifts due to
REM the high bit affecting 7-pixel blocks.
REM Using --weight 2 or 3 helps minimize
REM NTSC artifact issues.
REM ======================================
```

### Input Validation

The tool validates your inputs and adds warnings as comments if issues are detected:

```basic
REM ======================================
REM WARNING: PARAMETER ISSUES DETECTED
REM ======================================
REM X coordinate 300 out of bounds (0-279)
REM HCOLOR 9 out of range (0-7)
REM ======================================
```

The code will still be generated (with the invalid values) so you can see what you requested, but the warnings help you identify problems before running on actual hardware.

## Font Character Set

Supported characters:
- **Letters**: A-Z (automatically converted to uppercase)
- **Numbers**: 0-9
- **Punctuation**: `.` `,` `!` `?` `-` `:` `;` `'` `"` `/` `\` `(` `)`
- **Space**: ` `

## Tips & Tricks

1. **Readable Colored Text**: Use `--weight 2` or higher to reduce NTSC artifacts
2. **Clean Backgrounds**: Use `--fill 0` for black or `--fill 3` for white backgrounds
3. **Faster Animation**: Reduce the number of HPLOT commands by increasing character spacing
4. **Line Length**: BASIC lines are limited to ~238 characters; the tool automatically splits long lines
5. **Memory**: Each text block uses approximately 500 line numbers; plan your layout accordingly
6. **Testing**: Use an emulator with paste functionality for rapid iteration
7. **Optimization**: Omit `--bootloader` if integrating into existing code
8. **Color Consistency**: Stick to one MSB palette (0-3 or 4-7) to avoid color interference

## Technical Details

- Font is rendered as optimized HPLOT commands with horizontal line optimization
- Weight multiplies both X and Y dimensions of each pixel, creating thicker strokes
- Scroll effects use DX/DY variables for position offsets, enabling dynamic positioning
- Line number allocation: 1-100 for bootloader, 1000+ for effect subroutines (500 lines per effect)
- Generated code is compatible with Applesoft BASIC on Apple II/II+/IIe/IIc/IIGS
- CALL 62454 ($F3F2) is the fast HGR clear routine in the Monitor ROM

## Limitations

- Maximum line length handled automatically (splits at ~230 chars)
- No lowercase text (Apple II typically uppercase only)
- Monochrome per text block (HGR color fringing applies)
- Font is fixed 5×7 pixels (scaled by weight parameter)
- Weight values clamped to 1-3 range

## Version History

- **v3.0**: Complete rewrite with multi-effect support, scrolling, font weight, screen fill, input validation, and color documentation
- **v2.x**: Added variable positioning  
- **v1.x**: Initial release with basic text rendering

## Contributing

Contributions welcome! Ideas for enhancement:
- Additional font styles (3×5, 7×9, etc.)
- Shape table generation
- Additional effects (fade, blink, etc.)
- Sprite support
- Color cycling
- Mixed text/graphics modes

## License

MIT License - see LICENSE file for details

## Author

Created for the vintage computing community. Happy coding on your Apple II! 🍎

## References

- [Wikipedia: Apple II Graphics](https://en.wikipedia.org/wiki/Apple_II_graphics)
- Apple II Reference Manual
- Applesoft BASIC Programming Reference Manual
