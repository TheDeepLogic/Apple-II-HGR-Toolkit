#!/usr/bin/env python3
"""
Apple II HGR Effects Toolkit v3.0
Generate Applesoft BASIC code for HGR graphics effects

Focus: Speed and flexibility - no slow DATA statements!
"""

import argparse
import sys
import random

VERSION = "3.0.0"

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
}


def char_to_hplot(char, x_start, y_start):
    """Convert a character to HPLOT commands."""
    char_upper = char.upper()
    if char_upper not in FONT_5X7:
        char_upper = ' '
    
    bitmap = FONT_5X7[char_upper]
    hplot_commands = []
    
    for row_idx, row in enumerate(bitmap):
        y = y_start + row_idx
        pixels = []
        
        for col_idx in range(5):
            if row & (1 << (4 - col_idx)):
                x = x_start + col_idx
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


def text_to_hplot(text, x_start=10, y_start=80, char_spacing=6):
    """Convert text string to HPLOT commands."""
    all_commands = []
    current_x = x_start
    
    for char in text:
        commands = char_to_hplot(char, current_x, y_start)
        all_commands.extend(commands)
        current_x += char_spacing
    
    return all_commands


def generate_text_effect(text, x=10, y=80, spacing=6, line=1000, inc=1, 
                        hcolor=3, use_vars=False):
    """Generate text drawing code."""
    hplot_commands = text_to_hplot(text, x if not use_vars else 0, 
                                   y if not use_vars else 0, spacing)
    
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
                     line=5000, inc=1, hcolor=3):
    """Generate scrolling text code."""
    scroll_x, scroll_y, iterations = scroll_params
    
    lines = []
    
    lines.append("500 REM ** SCROLLER CONTROL **")
    lines.append(f"510 REM ** SCROLL: X={scroll_x}, Y={scroll_y}, ITER={iterations} **")
    lines.append(f"530 DX = {x}: DY = {y}")
    lines.append(f"540 FOR SC = 1 TO {iterations}")
    lines.append(f"550 IF DX < -100 OR DX > 379 THEN 590")
    lines.append(f"560 IF DY < -100 OR DY > 291 THEN 590")
    lines.append(f"570 GOSUB {line}")
    lines.append(f"580 DX = DX + {scroll_x}: DY = DY + {scroll_y}")
    lines.append(f"590 HGR: HCOLOR = {hcolor}")
    lines.append("600 NEXT SC")
    lines.append("610 RETURN")
    lines.append("")
    
    text_code = generate_text_effect(text_line, 0, 0, spacing, line, inc, hcolor, use_vars=True)
    
    return "\n".join(lines) + "\n" + text_code


def print_help():
    """Print DOS-style help."""
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║               APPLE II HGR EFFECTS TOOLKIT v3.0                          ║
║                   Fast HGR code generation                               ║
╚══════════════════════════════════════════════════════════════════════════╝

USAGE:
  python hgr.py [effect] [options] [effect] [options] ... [--bootloader]

EFFECTS:
  text "STRING"           Draw static text
  scroll "STRING"         Animated scrolling text

COMMON OPTIONS:
  -x NUM                  X coordinate (0-279, default: varies)
  -y NUM                  Y coordinate (0-191, default: varies)
  --hcolor NUM            HCOLOR value 0-7 (default: 3=white)
  --bootloader            Include bootloader (HGR/GOSUB/END)
  -o FILE                 Save to file

TEXT OPTIONS:
  -s NUM                  Character spacing (default: 6)

SCROLL OPTIONS:
  --scroll X,Y,ITER       e.g., --scroll -2,0,140
                          X = horiz speed (neg=left)
                          Y = vert speed (neg=up)
                          ITER = frames

EXAMPLES:

  Single text:
    python hgr.py text "GAME OVER" -x 80 -y 90 --bootloader

  Multiple text blocks:
    python hgr.py text "VHS Cassette" -x 200 -y 20 text "Play" -x 20 -y 120 --bootloader

  Left scroll:
    python hgr.py scroll "NEWS" --scroll -2,0,140 -x 279 -y 12

LIMITS:
  X: 0-279 (max 279)    Y: 0-191 (max 191)
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
    
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--bootloader':
            bootloader = True
            i += 1
        elif arg in ['-o', '--output']:
            if i + 1 < len(sys.argv):
                output_file = sys.argv[i + 1]
                i += 2
            else:
                print("ERROR: -o requires a filename")
                sys.exit(1)
        elif arg == 'text':
            # Parse text block
            block = {'type': 'text', 'text': None, 'x': 10, 'y': 80, 'spacing': 6, 'hcolor': 3}
            i += 1
            
            # Get text string
            if i < len(sys.argv) and not sys.argv[i].startswith('-'):
                block['text'] = sys.argv[i]
                i += 1
            else:
                print("ERROR: text effect requires text string")
                sys.exit(1)
            
            # Parse options for this text block
            while i < len(sys.argv):
                if sys.argv[i] == '-x' and i + 1 < len(sys.argv):
                    block['x'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == '-y' and i + 1 < len(sys.argv):
                    block['y'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] in ['-s', '--spacing'] and i + 1 < len(sys.argv):
                    block['spacing'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == '--hcolor' and i + 1 < len(sys.argv):
                    block['hcolor'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] in ['text', 'scroll', '--bootloader', '-o', '--output']:
                    # Next command/option, stop parsing this block
                    break
                else:
                    print(f"ERROR: Unknown option '{sys.argv[i]}'")
                    sys.exit(1)
            
            text_blocks.append(block)
            
        elif arg == 'scroll':
            # Parse scroll block
            block = {'type': 'scroll', 'text': None, 'x': 279, 'y': 12, 'spacing': 6, 
                    'hcolor': 3, 'scroll': None}
            i += 1
            
            # Get text string
            if i < len(sys.argv) and not sys.argv[i].startswith('-'):
                block['text'] = sys.argv[i]
                i += 1
            else:
                print("ERROR: scroll effect requires text string")
                sys.exit(1)
            
            # Parse options for this scroll block
            while i < len(sys.argv):
                if sys.argv[i] == '-x' and i + 1 < len(sys.argv):
                    block['x'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == '-y' and i + 1 < len(sys.argv):
                    block['y'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] in ['-s', '--spacing'] and i + 1 < len(sys.argv):
                    block['spacing'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == '--hcolor' and i + 1 < len(sys.argv):
                    block['hcolor'] = int(sys.argv[i + 1])
                    i += 2
                elif sys.argv[i] == '--scroll' and i + 1 < len(sys.argv):
                    block['scroll'] = sys.argv[i + 1]
                    i += 2
                elif sys.argv[i] in ['text', 'scroll', '--bootloader', '-o', '--output']:
                    break
                else:
                    print(f"ERROR: Unknown option '{sys.argv[i]}'")
                    sys.exit(1)
            
            if not block['scroll']:
                print("ERROR: scroll effect requires --scroll parameter")
                sys.exit(1)
            
            text_blocks.append(block)
        else:
            print(f"ERROR: Unknown command '{arg}'. Valid: text, scroll")
            sys.exit(1)
    
    if not text_blocks:
        print("ERROR: No text or scroll effects specified")
        sys.exit(1)
    
    # Generate code
    code = ""
    current_line = 1000
    
    if bootloader:
        code += "1 REM ** BOOTLOADER **\n"
        code += "5 HGR\n"
        
        # Add GOSUB calls for each text block
        gosub_line = 10
        for idx, block in enumerate(text_blocks):
            code += f"{gosub_line} GOSUB {current_line}\n"
            gosub_line += 5
            current_line += 500  # Reserve 500 lines per block
        
        code += "100 END\n\n"
    
    # Generate each text/scroll block
    current_line = 1000
    for idx, block in enumerate(text_blocks):
        if block['type'] == 'text':
            code += generate_text_effect(block['text'], block['x'], block['y'],
                                        block['spacing'], current_line, 1,
                                        block['hcolor'], use_vars=False)
            code += "\n\n"
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
                print(f"ERROR: Invalid scroll: {e}")
                print("Format: --scroll x,y,iter (e.g., --scroll -2,0,140)")
                sys.exit(1)
            
            code += generate_scroller(block['text'], scroll_params, block['x'],
                                     block['y'], block['spacing'], current_line,
                                     1, block['hcolor'])
            code += "\n\n"
        
        current_line += 500  # Reserve 500 lines per block
    
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


if __name__ == '__main__':
    main()
