import os

# Verified count: exactly 5 characters ("moist"), no trailing newline.
WORD = "moist"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
output_path = os.path.join(output_dir, "entry.txt") if output_dir else "/output/entry.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(WORD)
