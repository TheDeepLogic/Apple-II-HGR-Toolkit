# Examples

## Quick Start Examples

### 1. Hello World

The simplest example - display "HELLO WORLD" in the center of the screen:

```bash
python hgr-create.py text "HELLO WORLD" -x 80 -y 90 --bootloader
```

### 2. Game Title Screen

```bash
python hgr-create.py text "COSMIC FIGHTER" -x 70 -y 40 --hcolor 3 text "PRESS ANY KEY" -x 75 -y 120 --hcolor 5 --bootloader -o game-title.bas
```

### 3. Score Display

Multiple HUD elements:

```bash
python hgr-create.py text "SCORE:0" -x 5 -y 5 text "LEVEL:1" -x 200 -y 5 text "LIVES:3" -x 5 -y 185 --bootloader
```

### 4. Classic Left Scroller

News ticker style:

```bash
python hgr-create.py scroll "BREAKING NEWS - APPLE II STILL AWESOME IN 2025" --scroll -2,0,200 -x 279 -y 12 --bootloader -o newsticker.bas
```

### 5. Right Scroller

```bash
python hgr-create.py scroll "GAME OVER" --scroll 3,0,100 -x 0 -y 90 --bootloader
```

### 6. Vertical Scroll (Star Wars Style)

```bash
python hgr-create.py scroll "CREDITS" --scroll 0,-1,200 -x 120 -y 191 --bootloader
```

### 7. Diagonal Scroll

```bash
python hgr-create.py scroll "DEMO" --scroll -2,-1,150 -x 279 -y 191 --bootloader
```

## Advanced Examples

### 8. Multi-Color Display

```bash
python hgr-create.py text "RED" -x 50 -y 50 --hcolor 1 text "BLUE" -x 50 -y 70 --hcolor 6 text "WHITE" -x 50 -y 90 --hcolor 3 --bootloader
```

### 9. Tight Character Spacing

```bash
python hgr-create.py text "CONDENSED" -x 100 -y 90 -s 4 --bootloader
```

### 10. Wide Character Spacing

```bash
python hgr-create.py text "WIDE" -x 80 -y 90 -s 10 --bootloader
```

## Integration Examples

### 11. No Bootloader (For Integration)

Generate code without HGR setup for including in existing programs:

```bash
python hgr-create.py text "READY" -x 120 -y 90 -o ready-routine.bas
```

Then in your program:
```basic
100 HGR
110 REM ... your game code ...
500 GOSUB 1000: REM SHOW READY MESSAGE
510 REM ... continue ...
NEW
LOAD READY-ROUTINE.BAS
```

### 12. Multiple Scrollers

```bash
python hgr-create.py scroll "TOP LINE" --scroll -1,0,280 -x 279 -y 10 scroll "BOTTOM LINE" --scroll 1,0,280 -x 0 -y 180 --bootloader
```

## Creative Examples

### 13. Bouncing Text Effect

Generate multiple positions and use GOSUB in your main program:

```bash
python hgr-create.py text "BOUNCE" -x 100 -y 50 text "BOUNCE" -x 100 -y 100 text "BOUNCE" -x 100 -y 150 --bootloader
```

Then modify line 10-100 to alternate between GOSUBs in a loop.

### 14. Marquee Effect

```bash
python hgr-create.py scroll "     WELCOME TO THE SHOW     " --scroll -1,0,500 -x 279 -y 90 --bootloader
```

### 15. Copyright Notice

```bash
python hgr-create.py text "(C) 2025 YOUR NAME" -x 70 -y 180 --hcolor 3 -s 5 --bootloader
```

## Demo Programs

### 16. Simple Demo Sequence

```bash
python hgr-create.py text "APPLE II" -x 100 -y 80 --hcolor 3 text "FOREVER" -x 105 -y 100 --hcolor 5 --bootloader -o demo.bas
```

Modify to add delays:
```basic
10 GOSUB 1000
15 FOR I=1 TO 2000:NEXT I: REM DELAY
20 GOSUB 1500
25 FOR I=1 TO 2000:NEXT I
```

### 17. Animated Credits

```bash
python hgr-create.py scroll "PROGRAMMING: YOUR NAME" --scroll 0,-1,200 -x 80 -y 191 --bootloader -o credits.bas
```

## Command Line Tips

### Save All Output

```bash
python hgr-create.py text "SAVED" -x 100 -y 90 --bootloader -o output.bas
```

### Copy to Clipboard (Windows)

```bash
python hgr-create.py text "CLIPBOARD" -x 80 -y 90 --bootloader | clip
```

### Copy to Clipboard (Mac/Linux)

```bash
python hgr-create.py text "CLIPBOARD" -x 80 -y 90 --bootloader | pbcopy  # Mac
python hgr-create.py text "CLIPBOARD" -x 80 -y 90 --bootloader | xclip   # Linux
```

## Emulator-Specific Notes

### AppleWin
- Use Edit → Paste to paste generated code
- F2 resets, Ctrl+F2 reboots

### Virtual II (Mac)
- Command+V to paste
- Use "Type Clipboard" for better reliability

### MAME
- Use the built-in debugger console for pasting

## Common Patterns

### Center Text Calculation

For text of N characters with spacing S:
```
width = N × S
x_center = (280 - width) / 2
```

Example: "HELLO" (5 chars, spacing 6)
```
width = 5 × 6 = 30
x_center = (280 - 30) / 2 = 125
```

```bash
python hgr-create.py text "HELLO" -x 125 -y 90 --bootloader
```

### Bottom Aligned Text
```bash
python hgr-create.py text "BOTTOM" -x 100 -y 184 --bootloader
```

### Top Aligned Text
```bash
python hgr-create.py text "TOP" -x 100 -y 2 --bootloader
```

## Troubleshooting Examples

### Text Cut Off on Right
Reduce starting X or character spacing:
```bash
python hgr-create.py text "VERY LONG MESSAGE" -x 10 -y 90 -s 5 --bootloader
```

### Scroll Too Fast
Reduce scroll speed or increase iterations:
```bash
python hgr-create.py scroll "SLOW" --scroll -1,0,280 -x 279 -y 90 --bootloader
```

### Scroll Too Slow
Increase scroll speed:
```bash
python hgr-create.py scroll "FAST" --scroll -4,0,70 -x 279 -y 90 --bootloader
```

## Contributing Your Examples

Found a cool effect? Submit a pull request adding it to this file!
