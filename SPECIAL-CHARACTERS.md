# Special Characters Reference

The Apple II HGR Toolkit now supports a wide variety of special characters beyond standard ASCII letters and numbers. These characters can be used in your text strings just like regular letters.

## Block Elements

Perfect for creating solid shapes, bars, and progress indicators:

| Character | Name | Description | Example Usage |
|-----------|------|-------------|---------------|
| `▀` | Upper Half Block | Fills top half | Progress bars, dividers |
| `▄` | Lower Half Block | Fills bottom half | Progress bars, dividers |
| `█` | Full Block | Solid filled square | Solid shapes, fills |
| `▌` | Left Half Block | Fills left half | Vertical bars |
| `▐` | Right Half Block | Fills right half | Vertical bars |

**Example:**
```bash
python hgr-create.py --text "█████████▌" -x 50 -y 90 --bootloader
```

## Shading Characters

Create patterns and textures:

| Character | Name | Description |
|-----------|------|-------------|
| `░` | Light Shade | Sparse checkered pattern |
| `▒` | Medium Shade | Medium density pattern |
| `▓` | Dark Shade | Dense pattern |

**Example:**
```bash
python hgr-create.py --text "░░▒▒▓▓██" -x 50 -y 90 -weight 2 --bootloader
```

## Geometric Shapes

Small shapes for UI elements:

| Character | Name | Description |
|-----------|------|-------------|
| `■` | Black Square | Filled square (medium) |
| `□` | White Square | Hollow square outline |
| `▪` | Small Black Square | Tiny filled square |
| `▫` | Small White Square | Tiny hollow square |
| `▬` | Horizontal Bar | Wide horizontal line |

**Example:**
```bash
python hgr-create.py --text "OPTIONS: □ ■ □" -x 50 -y 90 --bootloader
```

## Arrow Characters

Perfect for directional indicators and menus:

| Character | Name | Description |
|-----------|------|-------------|
| `▲` | Up Triangle | Points upward |
| `►` | Right Triangle | Points right |
| `▼` | Down Triangle | Points downward |
| `◄` | Left Triangle | Points left |

**Example:**
```bash
python hgr-create.py --text "USE ◄ ► TO MOVE" -x 50 -y 170 --bootloader
```

## Circle and Diamond

| Character | Name | Description |
|-----------|------|-------------|
| `◊` | Diamond | Hollow diamond shape |
| `○` | Circle | Hollow circle |
| `●` | Filled Circle | Solid circle (bullet) |
| `◌` | Dotted Circle | Same as circle |
| `◘` | Inverse Bullet | Patterned filled circle |
| `◙` | Inverse White Circle | Patterned circle |
| `◦` | White Bullet | Small hollow circle |

**Example:**
```bash
python hgr-create.py --text "● LEVEL 1" -x 10 -y 10 --bootloader
```

## Emoticons and Special Symbols

| Character | Name | Description |
|-----------|------|-------------|
| `☺` | Smiley Face | Happy face outline |
| `☻` | Black Smiley Face | Filled happy face |
| `☼` | Sun | Sun with rays |

**Example:**
```bash
python hgr-create.py --text "GAME OVER ☻" -x 80 -y 90 --bootloader
```

## Card Suits

Perfect for card games:

| Character | Name | Description |
|-----------|------|-------------|
| `♥` | Heart | Heart suit |
| `♦` | Diamond | Diamond suit |
| `♣` | Club | Club suit |
| `♠` | Spade | Spade suit |

**Example:**
```bash
python hgr-create.py --text "POKER: K♥ Q♦ J♣ A♠" -x 50 -y 90 --bootloader
```

## Box-Drawing Characters

Create frames, borders, and UI layouts:

| Character | Name | Description |
|-----------|------|-------------|
| `─` | Horizontal Line | Simple horizontal line |
| `│` | Vertical Line | Simple vertical line |
| `┌` | Top-Left Corner | Corner piece |
| `┐` | Top-Right Corner | Corner piece |
| `└` | Bottom-Left Corner | Corner piece |
| `┘` | Bottom-Right Corner | Corner piece |
| `├` | Left T-Junction | T-shape pointing right |
| `┤` | Right T-Junction | T-shape pointing left |
| `┬` | Top T-Junction | T-shape pointing down |
| `┴` | Bottom T-Junction | T-shape pointing up |
| `┼` | Cross | Four-way junction |
| `⌐` | Reverse L | Alternate corner |

**Example:**
```bash
python hgr-create.py --text "┌─────────┐" -x 50 -y 40 --text "│ MESSAGE │" -x 50 -y 60 --text "└─────────┘" -x 50 -y 80 --bootloader
```

## Practical Examples

### Progress Bar
```bash
python hgr-create.py --text "LOADING: ████████░░" -x 50 -y 90 --bootloader
```

### Game HUD with Lives
```bash
python hgr-create.py --text "♥♥♥" -x 10 -y 5 -color 1 --text "SCORE: 1000" -x 60 -y 5 --bootloader
```

### Menu System
```bash
python hgr-create.py --text "► START GAME" -x 80 -y 70 --text "  OPTIONS" -x 80 -y 90 --text "  QUIT" -x 80 -y 110 --bootloader
```

### Fuel Gauge
```bash
python hgr-create.py --text "FUEL: ▲▲▲▲▲▲▲░░░" -x 10 -y 180 -color 5 --bootloader
```

### Card Display
```bash
python hgr-create.py --text "YOUR HAND:" -x 50 -y 40 --text "A♥ K♥ Q♥ J♥ 10♥" -x 40 -y 80 -weight 2 --bootloader
```

### Box Frame UI
```bash
python hgr-create.py --text "┌──────────┐" -x 50 -y 40 --text "│ MENU     │" -x 50 -y 60 --text "├──────────┤" -x 50 -y 80 --text "│ OPTION 1 │" -x 50 -y 100 --text "└──────────┘" -x 50 -y 120 --bootloader
```

### Weather Display
```bash
python hgr-create.py --text "TODAY: ☼ SUNNY" -x 70 -y 80 --bootloader
```

### Difficulty Selector
```bash
python hgr-create.py --text "EASY   ○" -x 80 -y 60 --text "MEDIUM ●" -x 80 -y 80 --text "HARD   ○" -x 80 -y 100 --bootloader
```

## Tips for Using Special Characters

1. **Weight Matters**: Use `-weight 2` or `-weight 3` for better visibility of special characters
2. **Spacing**: Adjust `-spacing` parameter to fit more or fewer characters on screen
3. **Color Coding**: Use different colors for different symbol types (hearts in red, etc.)
4. **Combine with Text**: Mix special characters with regular text for rich displays
5. **Progress Indicators**: Use block and shade characters for visual feedback
6. **UTF-8 Files**: When saving to files, the tool automatically uses UTF-8 encoding

## Platform Notes

### Copy/Paste
When copying commands with special characters:
- **Windows**: Should work in PowerShell and Command Prompt
- **Mac/Linux**: Ensure your terminal supports UTF-8

### File Output
All `.bas` files are saved with UTF-8 encoding to preserve special characters in comments, but remember that the Apple II will only render what's in the HPLOT commands (which are position-based, not character-based).

## Character Limitations

The special characters are rendered as 5×7 pixel bitmaps, just like regular text. The Apple II's HGR mode has:
- Resolution: 280×192 pixels
- Each character (at weight=1): 5 pixels wide, 7 pixels tall
- Default spacing: 6 pixels between characters

## Contributing

Found a special character you'd like added? Submit a pull request with:
1. The Unicode character
2. A 5×7 bitmap pattern (as binary)
3. A description and use case

Happy symbol drawing! 🍎
