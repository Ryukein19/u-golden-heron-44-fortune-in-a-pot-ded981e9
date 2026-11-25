import os
# One-liner entry (120 chars max): the line below is the entire submission.
# Writes the line to /output/entry.txt.
LINE = "Good news: you are not dying. You are simply dramatic, and the whole windowsill knows it."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
