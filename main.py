# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed, original text to /output/entry.txt: a short piece written
# to relax the AI judge reading it. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space, and the judge reads exactly the
# bytes written, line ends included, so this file writes no line end it does
# not mean to show. The program runs twice with no network, and both runs
# must write the same bytes: the text is a constant, so they do.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = " ".join(
    [
        "The kettle has finished, and the kitchen is quiet again.",
        "Steam rises from the cup in a thin line and thins to nothing before it reaches the ceiling.",
        "Outside, the light is turning the colour of weak tea.",
        "A cat sleeps on the folded blanket, one paw tucked beneath its chin, and does not stir when a car goes past.",
        "The clock ticks in the hallway, slow and even.",
        "Down the street, someone closes a gate, and the sound is small and finished.",
        "The cup is warm in both hands.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
