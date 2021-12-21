import json
from typing import List

letters_path = "uppercase-5pixels-by-5pixels.json"
with open(letters_path, "r") as f:
    letters = json.load(f)

text = "abcdefghijklmnopqrstuvwxyz"
char_msg: List[List[str]] = [letters[char] if char in letters else letters["UNKNOWN"] for char in text]
line_msg = []
for row_id in range(5):
    line_msg.append(" ".join(map(lambda x: x[row_id], char_msg)))

msg = "\n".join(line_msg)
print(msg)
