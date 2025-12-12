# Apple II HGR/GR Toolkit

A Python-based code generator for creating Applesoft BASIC programs with HGR (High Resolution Graphics) and GR (Low Resolution Graphics) text effects for the Apple II computer.

> **AI-Assisted Development Notice**
> 
> Hello, fellow human! My name is Aaron Smith. I've been in the IT field for nearly three decades and have extensive experience as both an engineer and architect. While I've had various projects in the past that have made their way into the public domain, I've always wanted to release more than I could. I write useful utilities all the time that aid me with my vintage computing and hobbyist electronic projects, but rarely publish them. I've had experience in both the public and private sectors and can unfortunately slip into treating each one of these as a fully polished cannonball ready for market. It leads to scope creep and never-ending updates to documentation.
> 
> With that in-mind, I've leveraged GitHub Copilot to create or enhance the code within this repository and, outside of this notice, all related documentation. While I'd love to tell you that I pore over it all and make revisions, that just isn't the case. To prevent my behavior from keeping these tools from seeing the light of day, I've decided to do as little of that as possible! My workflow involves simply stating the need to GitHub Copilot, providing reference material where helpful, running the resulting code, and, if there is an actionable output, validating that it's correct. If I find a change I'd like to make, I describe it to Copilot. I've been leveraging the Agent CLI and it takes care of the core debugging.
>
> With all that being said, please keep in-mind that what you read and execute was created by Claude Sonnet 4.5. There may be mistakes. If you find an error, please feel free to submit a pull request with a correction!

## Features

- **Dual Graphics Modes**: Support for both HGR (280×192) and GR (40×48) modes
- **Bitmap Text Rendering**: Generates optimized HPLOT/PLOT commands from built-in fonts
- **Multiple Font Styles**: Choose from default, tiny, bold, or bubble fonts
- **Multiple Text Blocks**: Create multiple text elements at different positions with a single command
- **Scrolling Text**: Animated scrolling effects with configurable speed and direction
- **Dithered Colors** (HGR only): Create additional colors (yellow, pink, lime, gray, etc.) using checkerboard dithering
- **Full Color Palettes**: HGR (8 colors + 10 dithered), GR (16 colors)
- **Font Weight Control**: Single, double, or triple width strokes to combat NTSC artifacts
- **Screen Fill**: Optional screen clearing with specified background color
- **Configurable Colors**: Full HCOLOR support (0-7 + dithered 100-109) for HGR, COLOR support (0-15) for GR
- **Input Validation**: Automatic bounds checking with warnings for out-of-range coordinates
- **Bootloader Generation**: Optional automatic setup code (HGR/GR initialization, GOSUB calls, END)

## Requirements

- Python 3.x
- An Apple II emulator (AppleWin, Virtual II, MAME, etc.) or real hardware

## Installation

Clone or download this repository:

```bash
git clone https://github.com/TheDeepLogic/Apple-II-HGR-Toolkit.git
cd Apple-II-HGR-Toolkit
```

No additional dependencies required - uses only Python standard library.

## Usage

### Basic Syntax

```bash
python hgr-create.py [--gr] --text "STRING" [options] --text "STRING" [options] ... [--bootloader]
```

The `--gr` flag switches from HGR (High Resolution) mode to GR (Low Resolution) mode.

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
| `--gr` | Use GR (Low-Res) mode instead of HGR (Hi-Res) | HGR mode |
| `--bootloader` | Include graphics mode setup and GOSUB calls | Off |
| `--fill NUM` | Fill screen before drawing (HGR: 0-7, GR: 0-15) | None |
| `-o FILE` | Save output to file | Stdout |

### Text Block Options

| Option | Description | Default |
|--------|-------------|---------|
| `-x NUM` | X coordinate (HGR: 0-279, GR: 0-39) | HGR: 10, GR: 5 (static)<br>HGR: 279, GR: 39 (scroll) |
| `-y NUM` | Y coordinate (HGR: 0-191, GR: 0-47) | HGR: 80, GR: 20 (static)<br>HGR: 12, GR: 5 (scroll) |
| `-color NUM` | Color value<br>HGR: 0-7 (solid), 100-109 (dithered)<br>GR: 0-15 (solid only) | 3 (white in both modes) |
| `-weight NUM` | Font weight/thickness (1-3) | HGR: 2, GR: 1 |
| `-size NUM` | Text size multiplier (1-5) | HGR: 2, GR: 1 |
| `-font NAME` | Font style (default, tiny, bold, bubble) | default |
| `-spacing NUM` | Character spacing in pixels | 6 |
| `-scroll X,Y,ITER` | Enable scrolling with parameters | None (static) |

**Note**: GR mode defaults to `-weight 1 -size 1` to maximize text capacity on the 40-block-wide screen.

### Scroll Parameters

Format: `-scroll X,Y,ITERATIONS`

- **X**: Horizontal speed (negative = left, positive = right)
- **Y**: Vertical speed (negative = up, positive = down)  
- **ITERATIONS**: Number of animation frames

Example: `-scroll -2,0,140` scrolls left at 2 pixels per frame for 140 frames

## Examples

### HGR Mode Examples

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

### Example 7: Large Title Text

```bash
python hgr-create.py --text "GAME OVER" -x 40 -y 80 -size 3 -weight 1 --bootloader
```

### Example 8: Tiny Font for Status Display

```bash
python hgr-create.py --text "SCORE 1000 LIVES 3" -font tiny -x 10 -y 10 -weight 1 --bootloader
```

### Example 9: Bold Font for Emphasis

```bash
python hgr-create.py --text "WARNING" -font bold -x 80 -y 90 -color 5 --bootloader
```

### Example 10: Bubble Font with Size

```bash
python hgr-create.py --text "HELLO" -font bubble -size 2 -x 60 -y 70 --bootloader
```

### Example 11: Yellow Lemon with Dithering

```bash
python hgr-create.py --text "LEMON" -color 100 -x 80 -y 80 -size 2 --bootloader
```

### Example 12: Multiple Dithered Colors

```bash
python hgr-create.py --text "YELLOW" -color 100 -x 10 -y 10 --text "PINK" -color 106 -x 10 -y 30 --text "LIME" -color 108 -x 10 -y 50 --bootloader
```

### Example 13: Mixed Static and Scrolling

```bash
python hgr-create.py --text "TITLE" -x 100 -y 20 -weight 2 --text "NEWS FLASH" -scroll -1,0,200 --bootloader
```

### GR Mode Examples

**Important**: GR mode has only 40 blocks of horizontal resolution. Use short text (single words or labels) for best results.

### Example 14: Simple GR Label

```bash
python hgr-create.py --gr --text "SCORE" -x 2 -y 2 -color 13 --bootloader
```

Renders yellow "SCORE" label in GR mode. Default settings (weight=1, size=1) used automatically.

### Example 15: GR Numeric Display

```bash
python hgr-create.py --gr --text "1000" -x 15 -y 10 -color 15 --fill 0 --bootloader
```

White numbers on black background - perfect for score displays.

### Example 16: GR Scrolling Ticker

```bash
python hgr-create.py --gr --text "NEWS" -scroll -1,0,50 -x 39 -y 10 -color 9 --bootloader
```

Short word scrolling in orange - GR is better for single-word tickers.

### Example 17: GR Status Label

```bash
python hgr-create.py --gr --text "READY" -x 5 -y 20 -color 12 --bootloader
```

Single-word status in bright green.

### Example 18: GR Tiny Font (Maximum Text)

```bash
python hgr-create.py --gr --text "HI SCORE" -font tiny -x 2 -y 2 -color 15 -spacing 4 --bootloader
```

Using tiny font with reduced spacing to fit more text (~8-10 characters possible).

### Example 19: GR Multiple Labels

```bash
python hgr-create.py --gr --text "P1" -x 2 -y 5 -color 1 --text "P2" -x 35 -y 5 -color 6 --text "GO" -x 18 -y 20 -color 13 --bootloader
```

Multiple short labels in different colors for game UI.

## Apple II Graphics Modes Reference

### HGR (High-Resolution Graphics) Mode

#### Screen Resolution
- **Hi-Res Mode**: 280×192 pixels  
- **Effective Color Resolution**: 140×192 (due to NTSC artifact color)
- **Coordinate System**: X: 0-279, Y: 0-191
- **Memory**: 8KB at $2000-$3FFF

### Understanding Apple II HGR Colors

The Apple II's Hi-Res graphics mode is unique and somewhat peculiar. Each row of 280 pixels is divided into 40 blocks of 7 pixels, with the **most significant bit (MSB)** of each byte controlling which color palette is used for that block.

#### Solid HCOLOR Values and MSB Palettes

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

#### Dithered Colors (100-109)

Dithered colors use a checkerboard pattern to alternate between two colors, creating the illusion of a third color:

| Value | Color Name | Pattern Colors | Visual Effect |
|-------|------------|----------------|---------------|
| 100 | Yellow | White + Orange | Bright yellow tone |
| 101 | Light Blue | White + Blue | Sky blue |
| 102 | Light Green | White + Green | Pale green |
| 103 | Light Purple | White + Purple | Lavender |
| 104 | Brown | Orange + Black | Dark brown |
| 105 | Gray | White + Black | Medium gray |
| 106 | Pink | White + Purple | Light pink |
| 107 | Aqua | White + Blue | Cyan/aqua |
| 108 | Lime | White + Green | Bright lime |
| 109 | Tan | Orange + White | Light tan |

The dithering uses a checkerboard pattern where pixels alternate based on their screen position, creating smooth color blending when viewed from a distance or on a composite monitor.

**Important Dithering Limitations**: Dithered colors generate significantly more code than solid colors. While solid colors can render efficiently using `HPLOT TO` commands, dithered patterns require individual plotting for each alternating pixel. A dithered text block can generate 100-200+ lines of BASIC code (compared to typical 50-line estimates for solid colors), consuming substantially more memory. For large graphics or tight memory constraints, prefer solid colors (0-7) over dithered colors (100-109). Dithering works best for small text or accent elements.

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

The `-weight` option combats NTSC artifacts by creating thicker strokes. When using weight 2 or 3, the doubled/tripled pixels create more solid white regions, reducing color fringing and making text more readable on colored backgrounds. This is why many Apple II programs used double-wide or chunky fonts.

#### Text Size Scaling

The `-size` option (values 1-5, default 1) scales the entire character by multiplying both the pixel positions and the font weight. This creates larger text while maintaining proportions:
- **Size 1**: Normal 5×7 font with specified weight (default)
- **Size 2**: 10×14 characters (double size)
- **Size 3**: 15×21 characters (triple size)
- **Size 4**: 20×28 characters (quadruple size)
- **Size 5**: 25×35 characters (quintuple size)

Note: Larger sizes may require adjusting spacing to prevent character overlap. The size multiplier affects both the character dimensions and the stroke weight.

### Font Styles

The toolkit includes four font styles that can be selected with the `-font` option:

- **default**: Standard 5×7 bitmap font with good readability
- **tiny**: Compact 3×5 font for fitting more text on screen
- **bold**: 5×7 font with thicker strokes built into the bitmap
- **bubble**: 5×7 rounded, friendly style font

All fonts support uppercase letters, lowercase letters, numbers, and basic punctuation. Special characters (blocks, arrows, symbols, card suits, box-drawing) automatically use the default font regardless of the font selected, ensuring consistent rendering of these elements across all font styles.

### GR (Low-Resolution Graphics) Mode

#### Screen Resolution
- **Lo-Res Mode**: 40×48 blocks (or 40×40 with text window)
- **Physical Display**: Each block is approximately 7×8 pixels on screen
- **Coordinate System**: X: 0-39, Y: 0-47 (full screen) or 0-39 (with bottom 4 text lines)
- **Memory**: 1KB at $400-$7FF (page 1) or $800-$BFF (page 2)
- **Color System**: Direct 16-color palette (no NTSC artifacts)

#### GR Color Palette (0-15)

GR mode provides 16 solid colors without the complexity of HGR's NTSC color system:

| Value | Color Name | Description |
|-------|-----------|-------------|
| 0 | Black | Pure black |
| 1 | Magenta | Bright magenta/pink |
| 2 | Dark Blue | Deep blue |
| 3 | Purple | Purple/violet |
| 4 | Dark Green | Forest green |
| 5 | Gray 1 | Dark gray |
| 6 | Medium Blue | Medium blue |
| 7 | Light Blue | Sky blue |
| 8 | Brown | Brown |
| 9 | Orange | Bright orange |
| 10 | Gray 2 | Light gray |
| 11 | Pink | Light pink |
| 12 | Light Green | Bright green |
| 13 | Yellow | Bright yellow |
| 14 | Aqua | Aqua/cyan |
| 15 | White | Pure white |

#### GR Mode Advantages

1. **Simpler Color System**: No MSB palettes or color interference - each block is independently colored
2. **True 16 Colors**: All 16 colors available without dithering
3. **Faster Rendering**: Larger blocks mean less memory access and faster drawing
4. **No NTSC Artifacts**: Colors are solid and don't depend on pixel positioning
5. **Less Memory**: GR screens use only 1KB vs HGR's 8KB

#### GR Mode Limitations

1. **Lower Resolution**: 40×48 blocks vs HGR's 280×192 pixels
2. **Blocky Appearance**: Each "pixel" is actually a large colored block
3. **No Dithering Support**: The toolkit doesn't support dithered colors in GR mode (not needed with 16 colors)
4. **Limited Text Width**: With only 40 blocks horizontally, text capacity is severely limited:
   - **Default settings (weight=1, size=1)**: ~6-7 characters per line
   - **Tiny font (weight=1, size=1)**: ~8-10 characters per line
   - **Bold/larger text**: Only 3-4 characters per line
   - **Recommendation**: Use `-weight 1 -size 1` for readable text in GR mode

**IMPORTANT**: GR mode is best suited for **very short text** (single words, labels, scores) rather than full sentences. The 40-block width makes it impractical for most text display purposes. Consider using HGR mode if you need to display more than a few characters.

#### When to Use GR Mode

- **Single-word labels** or **very short text** (3-7 characters)
- **Numeric scores/counters** in games
- **Simple icons or symbols** using block characters
- **Color-coded status indicators**
- **Fast animations** requiring quick screen updates
- **Memory-constrained programs** needing smaller graphics buffers

**NOT recommended for:**
- Full sentences or paragraphs (use HGR mode instead)
- Detailed text displays
- Multiple lines of readable text

**Pro tip**: For GR mode, always use `-weight 1 -size 1` (which is now the default for GR) to maximize text capacity. Even with these settings, you'll only fit about 6-7 characters across the screen.

### Practical Color Tips

**For HGR Mode:**
- **Safest Approach**: Use HCOLOR 3 or 7 (white) on black backgrounds (--fill 0)
- **Same Palette**: Stick to colors from the same MSB palette (0-3 OR 4-7)
- **Use Weight**: For colored text on colored backgrounds, use `-weight 2` or `-weight 3`
- **Dithering for More Colors**: Use dithered colors (100-109) to create yellow, pink, lime, gray, and other tones
- **Test First**: Always test your color combinations in an emulator before finalizing

**For GR Mode:**
- **Keep text SHORT**: Maximum 6-7 characters with default settings
- **Single words work best**: "SCORE", "READY", "GO", "LIVES", etc.
- **Use for labels, not sentences**: GR excels at UI labels and counters
- **Tiny font gains ~3-4 more characters**: Use `-font tiny -spacing 4` for "HI SCORE" etc.
- **No palette restrictions**: Mix any of the 16 colors freely
- **High Contrast**: Use high-contrast combinations for readability (e.g., 13/0 yellow on black, 15/2 white on dark blue)
- **Fast Updates**: GR mode is ideal for frequently updated displays due to smaller memory footprint
- **Color Testing**: Test on composite displays - colors may appear different than on RGB monitors
- **Consider HGR instead**: If you need more than 5-6 characters, use HGR mode

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
- **Letters**: A-Z, a-z
- **Numbers**: 0-9
- **Punctuation**: `.` `,` `!` `?` `-` `:` `;` `'` `"` `/` `\` `(` `)`
- **Space**: ` `
- **Special Characters**:
  - **Block Elements**: `▀` (upper half) `▄` (lower half) `█` (full block) `▌` (left half) `▐` (right half)
  - **Shading**: `░` (light shade) `▒` (medium shade) `▓` (dark shade)
  - **Shapes**: `■` (black square) `□` (white square) `▪` (small black square) `▫` (small white square) `▬` (horizontal bar)
  - **Arrows**: `▲` (up) `►` (right) `▼` (down) `◄` (left)
  - **Symbols**: `◊` (diamond) `○` (circle) `●` (filled circle) `◘` `◙` `◦`
  - **Emoticons**: `☺` (smiley) `☻` (filled smiley) `☼` (sun)
  - **Card Suits**: `♥` (heart) `♦` (diamond) `♣` (club) `♠` (spade)
  - **Box Drawing**: `─` (horizontal) `│` (vertical) `┌` `┐` `└` `┘` (corners) `├` `┤` `┬` `┴` (T-junctions) `┼` (cross) `⌐` (reverse L)

## Tips & Tricks

1. **Readable Colored Text**: Use `-weight 2` or higher to reduce NTSC artifacts
2. **Clean Backgrounds**: Use `--fill 0` for black or `--fill 3` for white backgrounds
3. **Faster Animation**: Reduce the number of HPLOT commands by increasing character spacing
4. **Line Length**: BASIC lines are limited to ~238 characters; the tool automatically splits long lines
5. **Memory**: Each solid-color text block uses approximately 50 line numbers; dithered colors (100-109) can use 100-200+ lines depending on size
6. **Testing**: Use an emulator with paste functionality for rapid iteration
7. **Optimization**: Omit `--bootloader` if integrating into existing code
8. **Color Consistency**: Stick to one MSB palette (0-3 or 4-7) to avoid color interference
9. **Dithering Memory Cost**: Dithered colors require significantly more memory than solid colors—use them for small decorative elements rather than large graphics

### Saving and Loading Graphics Screens

The generated BASIC programs can use significant memory. Once you've run your program and created the graphics screen, you can save just the graphics buffer as a binary file and load it instantly without re-executing the BASIC code:

**To save HGR screens:**
```basic
BSAVE MYGRAPHIC,A$2000,L$2000
```

This saves 8KB (8192 bytes = $2000 hex) starting at memory address $2000 (8192 decimal), which is where HGR Page 1 resides.

**To load HGR screens:**
```basic
HGR : BLOAD MYGRAPHIC,A$2000
```

**To save GR screens:**
```basic
BSAVE MYGRAPHIC,A$400,L$400
```

This saves 1KB (1024 bytes = $400 hex) starting at memory address $400 (1024 decimal), which is where GR Page 1 resides.

**To load GR screens:**
```basic
GR : BLOAD MYGRAPHIC,A$400
```

The `HGR` command switches to Hi-Res graphics mode, then `BLOAD` loads the binary data directly into the graphics memory.

**Why this is useful:**
- **Memory savings**: BASIC programs with all the HPLOT/PLOT commands can be 10-20KB or more, but final screens are always 8KB (HGR) or 1KB (GR)
- **Instant display**: Loading a binary screen file is nearly instantaneous compared to executing hundreds of HPLOT/PLOT commands
- **Title screens**: Perfect for game title screens or splash screens that don't need to be regenerated
- **Disk space**: Save multiple screen variants and load them as needed
- **GR advantage**: GR screens are only 1KB, making them 8x smaller than HGR screens!

**HGR Page 2 (if using second page):**
```basic
BSAVE MYGRAPHIC2,A$4000,L$2000
BLOAD MYGRAPHIC2,A$4000
```

**Pro tip**: After generating your graphics with this toolkit, run the program once, verify it looks correct, save it with BSAVE, then you can delete the large BASIC program and just keep the small 8KB binary file!

## Technical Details

- Fonts rendered as optimized HPLOT (HGR) or PLOT (GR) commands
- HGR uses horizontal line optimization with `HPLOT TO` for efficiency
- GR plots individual blocks (no line drawing optimization available)
- Weight multiplies stroke thickness (1=single, 2=double, 3=triple pixel width)
- Size multiplies both character dimensions and weight for proportional scaling
- Scroll effects use DX/DY variables for position offsets, enabling dynamic positioning
- Line number allocation: 1-100 for bootloader, 500+ for scrollers, 1000+ for text subroutines
- Generated code is compatible with Applesoft BASIC on Apple II/II+/IIe/IIc/IIGS
- HGR: CALL 62454 ($F3F2) is the fast HGR clear routine in the Monitor ROM
- GR: Screen fill uses nested FOR loops to plot all 1920 blocks (40×48)

## Limitations

- Maximum line length handled automatically (splits at ~230 chars)
- HGR: Monochrome per text block (HGR color fringing applies)
- GR: True color per block (no fringing)
- Font is fixed 5×7 or 3×5 pixels (scaled by weight and size parameters)
- Weight values clamped to 1-3 range
- **HGR dithered colors (100-109) generate significantly more code**: A typical dithered text block produces 100-200+ lines of BASIC code versus the usual 50 lines for solid colors. This is due to the checkerboard pattern requiring more granular HPLOT statements. Use dithering sparingly for small text or decorative elements where memory permits.
- **GR mode does not support dithering**: With 16 solid colors available, dithering is not implemented in GR mode

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
