#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Prints a single fortune-cookie message for a crypto trader who has
just been liquidated. One line, plain text, nothing else.
"""

print("A great fortune awaits you — unfortunately, it is currently sitting in your liquidator's wallet.")

try:
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write("A great fortune awaits you — unfortunately, it is currently sitting in your liquidator's wallet.\n")
except OSError:
    pass
