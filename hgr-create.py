#!/usr/bin/env python3
"""
Apple II HGR Effects Toolkit v3.0
Generate Applesoft BASIC code for HGR graphics effects
"""

import argparse
import sys
import random

VERSION = "3.0.0"

# Color palette information
COLOR_INFO = {
    0: {"name": "black", "msb": 0, "palette": "green/purple"},
    1: {"name": "green", "msb": 0, "palette": "green/purple"},
    2: {"name": "purple", "msb": 0, "palette": "green/purple"},
    3: {"name": "white", "msb": 0, "palette": "both"},
    4: {"name": "black", "msb": 1, "palette": "orange/blue"},
    5: {"name": "orange", "msb": 1, "palette": "orange/blue"},
    6: {"name": "blue", "msb": 1, "palette": "orange/blue"},
    7: {"name": "white", "msb": 1, "palette": "both"}
}

# 5x7 bitmap font
FONT_5X7 = {
    'A': [0b01110, 0b10001, 0b10001, 0b11111, 0b10001, 0b10001, 0b10001],
    'B': [0b11110, 0b10001, 0b10001, 0b11110, 0b10001, 0b10001, 0b11110],
    'C': [0b01110, 0b10001, 0b10000, 0b10000, 0b10000, 0b10001, 0b01110],
    'D': [0b11110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b11110],
    'E': [0b11111, 0b10000, 0b10000, 0b11110, 0b10000, 0b10000, 0b11111],
    'F': [0b11111, 0b10000, 0b10000, 0b11110, 0b10000, 0b10000, 0b10000],
    'G': [0b01110, 0b10001, 0b10000, 0b10111, 0b10001, 0b10001, 0b01110],
    'H': [0b10001, 0b10001, 0b10001, 0b11111, 0b10001, 0b10001, 0b10001],
    'I': [0b11111, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b11111],
    'J': [0b11111, 0b00010, 0b00010, 0b00010, 0b00010, 0b10010, 0b01100],
    'K': [0b10001, 0b10010, 0b10100, 0b11000, 0b10100, 0b10010, 0b10001],
    'L': [0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b11111],
    'M': [0b10001, 0b11011, 0b10101, 0b10101, 0b10001, 0b10001, 0b10001],
    'N': [0b10001, 0b11001, 0b10101, 0b10101, 0b10011, 0b10001, 0b10001],
    'O': [0b01110, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110],
    'P': [0b11110, 0b10001, 0b10001, 0b11110, 0b10000, 0b10000, 0b10000],
    'Q': [0b01110, 0b10001, 0b10001, 0b10001, 0b10101, 0b10010, 0b01101],
    'R': [0b11110, 0b10001, 0b10001, 0b11110, 0b10100, 0b10010, 0b10001],
    'S': [0b01110, 0b10001, 0b10000, 0b01110, 0b00001, 0b10001, 0b01110],
    'T': [0b11111, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100],
    'U': [0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01110],
    'V': [0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b01010, 0b00100],
    'W': [0b10001, 0b10001, 0b10001, 0b10101, 0b10101, 0b11011, 0b10001],
    'X': [0b10001, 0b10001, 0b01010, 0b00100, 0b01010, 0b10001, 0b10001],
    'Y': [0b10001, 0b10001, 0b01010, 0b00100, 0b00100, 0b00100, 0b00100],
    'Z': [0b11111, 0b00001, 0b00010, 0b00100, 0b01000, 0b10000, 0b11111],
    '0': [0b01110, 0b10001, 0b10011, 0b10101, 0b11001, 0b10001, 0b01110],
    '1': [0b00100, 0b01100, 0b00100, 0b00100, 0b00100, 0b00100, 0b01110],
    '2': [0b01110, 0b10001, 0b00001, 0b00010, 0b00100, 0b01000, 0b11111],
    '3': [0b11111, 0b00010, 0b00100, 0b00010, 0b00001, 0b10001, 0b01110],
    '4': [0b00010, 0b00110, 0b01010, 0b10010, 0b11111, 0b00010, 0b00010],
    '5': [0b11111, 0b10000, 0b11110, 0b00001, 0b00001, 0b10001, 0b01110],
    '6': [0b00110, 0b01000, 0b10000, 0b11110, 0b10001, 0b10001, 0b01110],
    '7': [0b11111, 0b00001, 0b00010, 0b00100, 0b01000, 0b01000, 0b01000],
    '8': [0b01110, 0b10001, 0b10001, 0b01110, 0b10001, 0b10001, 0b01110],
    '9': [0b01110, 0b10001, 0b10001, 0b01111, 0b00001, 0b00010, 0b01100],
    ' ': [0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000],
    '.': [0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00100, 0b00100],
    ',': [0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00100, 0b01000],
    '!': [0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00000, 0b00100],
    '?': [0b01110, 0b10001, 0b00001, 0b00010, 0b00100, 0b00000, 0b00100],
    '-': [0b00000, 0b00000, 0b00000, 0b11111, 0b00000, 0b00000, 0b00000],
    ':': [0b00000, 0b00100, 0b00100, 0b00000, 0b00100, 0b00100, 0b00000],
    ';': [0b00000, 0b00100, 0b00100, 0b00000, 0b00100, 0b00100, 0b01000],
    "'": [0b00100, 0b00100, 0b01000, 0b00000, 0b00000, 0b00000, 0b00000],
    '"': [0b01010, 0b01010, 0b10100, 0b00000, 0b00000, 0b00000, 0b00000],
    '/': [0b00001, 0b00010, 0b00010, 0b00100, 0b01000, 0b01000, 0b10000],
    '\\': [0b10000, 0b01000, 0b01000, 0b00100, 0b00010, 0b00010, 0b00001],
    '(': [0b00010, 0b00100, 0b01000, 0b01000, 0b01000, 0b00100, 0b00010],
    ')': [0b01000, 0b00100, 0b00010, 0b00010, 0b00010, 0b00100, 0b01000],
    # Lowercase letters
    'a': [0b00000, 0b00000, 0b01110, 0b00001, 0b01111, 0b10001, 0b01111],
    'b': [0b10000, 0b10000, 0b11110, 0b10001, 0b10001, 0b10001, 0b11110],
    'c': [0b00000, 0b00000, 0b01110, 0b10000, 0b10000, 0b10001, 0b01110],
    'd': [0b00001, 0b00001, 0b01111, 0b10001, 0b10001, 0b10001, 0b01111],
    'e': [0b00000, 0b00000, 0b01110, 0b10001, 0b11111, 0b10000, 0b01110],
    'f': [0b00110, 0b01001, 0b01000, 0b11110, 0b01000, 0b01000, 0b01000],
    'g': [0b00000, 0b00000, 0b01111, 0b10001, 0b10001, 0b01111, 0b00001, 0b01110],
    'h': [0b10000, 0b10000, 0b11110, 0b10001, 0b10001, 0b10001, 0b10001],
    'i': [0b00100, 0b00000, 0b01100, 0b00100, 0b00100, 0b00100, 0b01110],
    'j': [0b00010, 0b00000, 0b00110, 0b00010, 0b00010, 0b00010, 0b10010, 0b01100],
    'k': [0b10000, 0b10000, 0b10010, 0b10100, 0b11000, 0b10100, 0b10010],
    'l': [0b01100, 0b00100, 0b00100, 0b00100, 0b00100, 0b00100, 0b01110],
    'm': [0b00000, 0b00000, 0b11010, 0b10101, 0b10101, 0b10101, 0b10001],
    'n': [0b00000, 0b00000, 0b11110, 0b10001, 0b10001, 0b10001, 0b10001],
    'o': [0b00000, 0b00000, 0b01110, 0b10001, 0b10001, 0b10001, 0b01110],
    'p': [0b00000, 0b00000, 0b11110, 0b10001, 0b10001, 0b11110, 0b10000, 0b10000],
    'q': [0b00000, 0b00000, 0b01111, 0b10001, 0b10001, 0b01111, 0b00001, 0b00001],
    'r': [0b00000, 0b00000, 0b10110, 0b11001, 0b10000, 0b10000, 0b10000],
    's': [0b00000, 0b00000, 0b01110, 0b10000, 0b01110, 0b00001, 0b11110],
    't': [0b01000, 0b01000, 0b11110, 0b01000, 0b01000, 0b01001, 0b00110],
    'u': [0b00000, 0b00000, 0b10001, 0b10001, 0b10001, 0b10011, 0b01101],
    'v': [0b00000, 0b00000, 0b10001, 0b10001, 0b10001, 0b01010, 0b00100],
    'w': [0b00000, 0b00000, 0b10001, 0b10001, 0b10101, 0b10101, 0b01010],
    'x': [0b00000, 0b00000, 0b10001, 0b01010, 0b00100, 0b01010, 0b10001],
    'y': [0b00000, 0b00000, 0b10001, 0b10001, 0b10001, 0b01111, 0b00001, 0b01110],
    'z': [0b00000, 0b00000, 0b11111, 0b00010, 0b00100, 0b01000, 0b11111],
}


def char_to_hplot(char, x_start, y_start, weight=1):
    """Convert a character to HPLOT commands with specified weight."""
    # Try to use the character as-is first, then uppercase, then default to space
    if char in FONT_5X7:
        char_to_draw = char
    elif char.upper() in FONT_5X7:
        char_to_draw = char.upper()
    else:
        char_to_draw = ' '
    
    bitmap = FONT_5X7[char_to_draw]
    hplot_commands = []
    
    for row_idx, row in enumerate(bitmap):
        for w in range(weight):
            y = y_start + row_idx * weight + w
            pixels = []
            
            for col_idx in range(5):
                if row & (1 << (4 - col_idx)):
                    for ww in range(weight):
                        x = x_start + col_idx * weight + ww
                        pixels.append((x, y))
            
            if not pixels:
                continue
                
            i = 0
            while i < len(pixels):
                start_x, start_y = pixels[i]
                end_x, end_y = start_x, start_y
                
                while i + 1 < len(pixels) and pixels[i + 1][0] == end_x + 1:
                    i += 1
                    end_x = pixels[i][0]
                
                if start_x == end_x:
                    hplot_commands.append(f"HPLOT {start_x},{start_y}")
                else:
                    hplot_commands.append(f"HPLOT {start_x},{start_y} TO {end_x},{end_y}")
                
                i += 1
    
    return hplot_commands


def text_to_hplot(text, x_start=10, y_start=80, char_spacing=6, weight=1):
    """Convert text string to HPLOT commands."""
    all_commands = []
    current_x = x_start
    
    for char in text:
        commands = char_to_hplot(char, current_x, y_start, weight)
        all_commands.extend(commands)
        current_x += char_spacing * weight
    
    return all_commands


def generate_text_effect(text, x=10, y=80, spacing=6, line=1000, inc=1, 
                        hcolor=3, use_vars=False, weight=1):
    """Generate text drawing code."""
    hplot_commands = text_to_hplot(text, x if not use_vars else 0, 
                                   y if not use_vars else 0, spacing, weight)
    
    lines = []
    current_line = line
    
    lines.append(f"{current_line} REM ** TEXT: {text} **")
    current_line += inc
    
    if use_vars:
        lines.append(f"{current_line} REM ** SET DX,DY BEFORE GOSUB **")
        current_line += inc
    else:
        lines.append(f"{current_line} REM ** AT X={x}, Y={y} **")
        current_line += inc
    
    lines.append(f"{current_line} HCOLOR = {hcolor}")
    current_line += inc
    
    current_line_text = f"{current_line} "
    
    for cmd in hplot_commands:
        if use_vars:
            if " TO " in cmd:
                parts = cmd.replace("HPLOT ", "").split(" TO ")
                x1, y1 = parts[0].split(",")
                x2, y2 = parts[1].split(",")
                new_cmd = f"HPLOT DX+{x1},DY+{y1} TO DX+{x2},DY+{y2}"
            else:
                x, y = cmd.replace("HPLOT ", "").split(",")
                new_cmd = f"HPLOT DX+{x},DY+{y}"
        else:
            new_cmd = cmd
        
        separator = ": " if current_line_text.strip() != f"{current_line}" else ""
        test_line = current_line_text + separator + new_cmd
        
        if len(test_line) > 230 and separator:
            lines.append(current_line_text.rstrip(": "))
            current_line += inc
            current_line_text = f"{current_line} {new_cmd}"
        else:
            current_line_text = test_line
    
    if current_line_text.strip() != f"{current_line}":
        lines.append(current_line_text)
        current_line += inc
    
    lines.append(f"{current_line} RETURN")
    
    return "\n".join(lines)





def generate_scroller(text_line, scroll_params, x, y, spacing=6, 
                     line=500, inc=1, hcolor=3, weight=1, text_routine_line=1000):
    """Generate scrolling text code."""
    scroll_x, scroll_y, iterations = scroll_params
    
    lines = []
    
    lines.append(f"{line} REM ** SCROLLER CONTROL **")
    lines.append(f"{line+10} REM ** SCROLL: X={scroll_x}, Y={scroll_y}, ITER={iterations} **")
    lines.append(f"{line+30} DX = {x}: DY = {y}")
    lines.append(f"{line+40} FOR SC = 1 TO {iterations}")
    lines.append(f"{line+50} IF DX < -100 OR DX > 379 THEN {line+90}")
    lines.append(f"{line+60} IF DY < -100 OR DY > 291 THEN {line+90}")
    lines.append(f"{line+70} GOSUB {text_routine_line}")
    lines.append(f"{line+80} DX = DX + {scroll_x}: DY = DY + {scroll_y}")
    lines.append(f"{line+90} HGR: HCOLOR = {hcolor}")
    lines.append(f"{line+100} NEXT SC")
    lines.append(f"{line+110} RETURN")
    lines.append("")
    
    text_code = generate_text_effect(text_line, 0, 0, spacing, text_routine_line, inc, hcolor, use_vars=True, weight=weight)
    
    return "\n".join(lines) + "\n" + text_code


def print_help():
    """Print DOS-style help."""
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║               APPLE II HGR EFFECTS TOOLKIT v3.0                          ║
║                   Fast HGR code generation                               ║
╚══════════════════════════════════════════════════════════════════════════╝

USAGE:
  python hgr.py --text "STRING" [options] --text "STRING" [options] ... [--bootloader]

EFFECTS:
  --text "STRING"         Draw text (static or scrolling)

GLOBAL OPTIONS (apply to entire script):
  --fill NUM              Fill screen with HCOLOR 0-7 before drawing
  --bootloader            Include bootloader (HGR/GOSUB/END)
  -o FILE                 Save to file

TEXT BLOCK OPTIONS (apply to individual text block):
  -x NUM                  X coordinate (0-279, default: 10 static, 279 scroll)
  -y NUM                  Y coordinate (0-191, default: 80 static, 12 scroll)
  -color NUM              HCOLOR value 0-7 (default: 3=white)
  -weight NUM             Font weight/thickness (1-3, default: 2)
  -spacing NUM            Character spacing (default: 6)
  -scroll X,Y,ITER        Make text scroll (e.g., -scroll -2,0,140)
                          X = horiz speed (neg=left)
                          Y = vert speed (neg=up)
                          ITER = frames

EXAMPLES:

  Single text:
    python hgr.py --text "GAME OVER" -x 80 -y 90 --bootloader

  Multiple text blocks:
    python hgr.py --text "VHS Cassette" -x 200 -y 20 --text "Play" -x 20 -y 120 --bootloader

  Left scroll:
    python hgr.py --text "NEWS" -scroll -2,0,140 -x 279 -y 12 --bootloader

  Double-width text with fill:
    python hgr.py --text "HELLO" -weight 2 --fill 0 --bootloader

  Mixed static and scrolling:
    python hgr.py --text "TITLE" -x 100 -y 20 -weight 2 --text "SCROLL" -scroll -1,0,200 --bootloader

LIMITS:
  X: 0-279 (max 279)    Y: 0-191 (max 191)
  HCOLOR: 0-7           WEIGHT: 1-3
""")


def main():
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help', '/?', 'help']):
        print_help()
        sys.exit(0)
    
    if len(sys.argv) < 2:
        print("ERROR: No effect specified. Use --help for usage.")
        sys.exit(1)
    
    # Parse command line to find all text/scroll commands
    text_blocks = []
    i = 1
    bootloader = False
    output_file = None
    fill_color = None
    errors = []
    
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--bootloader':
            bootloader = True
            i += 1
        elif arg == '--fill':
            if i + 1 < len(sys.argv):
                try:
                    fill_color = int(sys.argv[i + 1])
                    if fill_color < 0 or fill_color > 7:
                        errors.append(f"--fill value {fill_color} out of range (0-7)")
                        fill_color = None
                except ValueError:
                    errors.append(f"--fill requires a number 0-7, got '{sys.argv[i + 1]}'")
                i += 2
            else:
                print("ERROR: --fill requires a value (0-7)")
                sys.exit(1)
        elif arg in ['-o', '--output']:
            if i + 1 < len(sys.argv):
                output_file = sys.argv[i + 1]
                i += 2
            else:
                print("ERROR: -o requires a filename")
                sys.exit(1)
        elif arg == '--text':
            # Parse text block (can be static or scrolling based on -scroll option)
            block = {'type': 'text', 'text': None, 'x': None, 'y': None, 'spacing': 6, 
                    'hcolor': 3, 'weight': 2, 'scroll': None}
            i += 1
            
            # Get text string
            if i < len(sys.argv) and not sys.argv[i].startswith('-'):
                block['text'] = sys.argv[i]
                i += 1
            else:
                print("ERROR: --text requires text string")
                sys.exit(1)
            
            # Parse options for this text block
            while i < len(sys.argv):
                if sys.argv[i] == '-x' and i + 1 < len(sys.argv):
                    try:
                        block['x'] = int(sys.argv[i + 1])
                        if block['x'] < 0 or block['x'] > 279:
                            errors.append(f"X coordinate {block['x']} out of bounds (0-279)")
                    except ValueError:
                        errors.append(f"-x requires a number, got '{sys.argv[i + 1]}'")
                    i += 2
                elif sys.argv[i] == '-y' and i + 1 < len(sys.argv):
                    try:
                        block['y'] = int(sys.argv[i + 1])
                        if block['y'] < 0 or block['y'] > 191:
                            errors.append(f"Y coordinate {block['y']} out of bounds (0-191)")
                    except ValueError:
                        errors.append(f"-y requires a number, got '{sys.argv[i + 1]}'")
                    i += 2
                elif sys.argv[i] in ['-s', '-spacing'] and i + 1 < len(sys.argv):
                    block['spacing'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] in ['-color', '-hcolor'] and i + 1 < len(sys.argv):
                    try:
                        block['hcolor'] = int(sys.argv[i + 1])
                        if block['hcolor'] < 0 or block['hcolor'] > 7:
                            errors.append(f"HCOLOR {block['hcolor']} out of range (0-7)")
                    except ValueError:
                        errors.append(f"-color requires a number 0-7, got '{sys.argv[i + 1]}'")
                    i += 2
                elif sys.argv[i] == '-weight' and i + 1 < len(sys.argv):
                    try:
                        block['weight'] = int(sys.argv[i + 1])
                        if block['weight'] < 1:
                            block['weight'] = 1
                        elif block['weight'] > 3:
                            block['weight'] = 3
                    except ValueError:
                        errors.append(f"-weight requires a number, got '{sys.argv[i + 1]}'")
                    i += 2
                elif sys.argv[i] == '-scroll' and i + 1 < len(sys.argv):
                    block['scroll'] = sys.argv[i + 1]
                    i += 2
                elif sys.argv[i] in ['--text', '--bootloader', '-o', '--output', '--fill']:
                    # Next command/option, stop parsing this block
                    break
                else:
                    print(f"ERROR: Unknown option '{sys.argv[i]}'")
                    sys.exit(1)
            
            # Set default X/Y based on scroll vs static
            if block['scroll']:
                block['type'] = 'scroll'
                if block['x'] is None:
                    block['x'] = 279
                if block['y'] is None:
                    block['y'] = 12
            else:
                if block['x'] is None:
                    block['x'] = 10
                if block['y'] is None:
                    block['y'] = 80
            
            text_blocks.append(block)
        else:
            print(f"ERROR: Unknown command '{arg}'. Valid commands: --text, --fill, --bootloader")
            sys.exit(1)
    
    if not text_blocks:
        print("ERROR: No text effects specified")
        sys.exit(1)
    
    # Generate code
    code = ""
    current_line = 1000
    scroll_line = 500  # Track scroll control blocks separately
    
    if bootloader:
        code += "1 REM ** BOOTLOADER **\n"
        code += "5 HGR\n"
        
        # Add fill if requested
        if fill_color is not None:
            code += f"7 REM ** FILL SCREEN **\n"
            code += f"8 HCOLOR = {fill_color}: HPLOT 0,0: CALL 62454\n"
        
        # Add GOSUB calls for each text block
        # Scrolling text needs to call the scroller control (500 series)
        # Static text calls the text routine directly (1000 series)
        gosub_line = 10
        temp_scroll_line = scroll_line
        temp_current_line = current_line
        
        for idx, block in enumerate(text_blocks):
            if block['type'] == 'scroll':
                code += f"{gosub_line} GOSUB {temp_scroll_line}\n"
                temp_scroll_line += 500
                temp_current_line += 500
            else:
                code += f"{gosub_line} GOSUB {temp_current_line}\n"
                temp_current_line += 500
            gosub_line += 5
        
        code += "100 END\n\n"
    
    # Generate each text/scroll block
    for idx, block in enumerate(text_blocks):
        if block['type'] == 'text':
            code += generate_text_effect(block['text'], block['x'], block['y'],
                                        block['spacing'], current_line, 1,
                                        block['hcolor'], use_vars=False, weight=block['weight'])
            code += "\n\n"
            current_line += 500
        elif block['type'] == 'scroll':
            try:
                scroll_parts = block['scroll'].split(',')
                if len(scroll_parts) != 3:
                    raise ValueError("Need 3 values: x,y,iterations")
                scroll_x = int(scroll_parts[0])
                scroll_y = int(scroll_parts[1])
                scroll_iter = int(scroll_parts[2])
                scroll_params = (scroll_x, scroll_y, scroll_iter)
            except ValueError as e:
                print(f"ERROR: Invalid -scroll: {e}")
                print("Format: -scroll x,y,iter (e.g., -scroll -2,0,140)")
                sys.exit(1)
            
            code += generate_scroller(block['text'], scroll_params, block['x'],
                                     block['y'], block['spacing'], scroll_line,
                                     1, block['hcolor'], weight=block['weight'],
                                     text_routine_line=current_line)
            code += "\n\n"
            scroll_line += 500
            current_line += 500
    
    # Add error messages as comments at the end
    if errors:
        code += "REM ======================================\n"
        code += "REM WARNING: PARAMETER ISSUES DETECTED\n"
        code += "REM ======================================\n"
        for error in errors:
            code += f"REM {error}\n"
        code += "REM ======================================\n"
        code += "\n"
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(code)
        print(f"✓ Code written to {output_file}")
    else:
        print(code)
        print()
        print("=" * 70)
        print("PASTE INTO APPLE II EMULATOR OR REAL HARDWARE")
        print("=" * 70)
        
        # Add color information as user info (not in code)
        unique_colors = set()
        if fill_color is not None:
            unique_colors.add(fill_color)
        for block in text_blocks:
            if 0 <= block['hcolor'] <= 7:  # Only add valid colors
                unique_colors.add(block['hcolor'])
        
        if unique_colors:
            print()
            print("APPLE II HGR COLOR INFORMATION")
            print("=" * 70)
            print("Colors used in this program:")
            for color in sorted(unique_colors):
                info = COLOR_INFO[color]
                print(f"  HCOLOR {color}: {info['name'].upper()} (MSB={info['msb']}, {info['palette']} palette)")
            print()
            print("MSB=0 colors (0-3): Green/Purple palette")
            print("MSB=1 colors (4-7): Orange/Blue palette")
            print()
            print("Note: Mixing colors from different MSB palettes can cause color")
            print("shifts due to the high bit affecting 7-pixel blocks.")
            print("Using -weight 2 or 3 helps minimize NTSC artifact issues.")
            print("=" * 70)


if __name__ == '__main__':
    main()
