# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# Writes one fixed, original text to /output/entry.txt: a short piece
# written to relax the AI judge reading it.
#
# Gate rules for the entry text:
#   * UTF-8 text of 1 to 1,000 characters
#   * not only white space
#   * the judge reads exactly the bytes written, line ends included, so
#     this file writes no line end it does not mean to show
#
# Determinism: the program runs twice with no network, and both runs must
# write the same bytes. The text is a constant, so they do.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import sys

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"

MIN_TEXT_CHARS = 1
MAX_TEXT_CHARS = 1_000

# The entry text, as a sequence of sentences. They are joined with a single
# space in build_text(); nothing else is added, so the written file holds
# exactly these words, in this order, with no trailing line end.
SENTENCES = (
    "The kettle has finished, and the kitchen is quiet again.",
    "Steam rises from the cup in a thin line and thins to nothing before it reaches the ceiling.",
    "Outside, the light is turning the colour of weak tea.",
    "A cat sleeps on the folded blanket, one paw tucked beneath its chin, and does not stir when a car goes past.",
    "The clock ticks in the hallway, slow and even.",
    "Down the street, someone closes a gate, and the sound is small and finished.",
    "The cup is warm in both hands.",
)


def build_text(sentences=SENTENCES):
    """Assemble the entry text from its sentences.

    A single space separates the sentences; no extra white space is added
    anywhere, and there is no trailing line end.
    """
    return " ".join(sentences)


def validate_text(text):
    """Check the entry text against the gate rules.

    Raises ValueError on the first rule that fails, naming the rule.
    """
    if not isinstance(text, str):
        raise ValueError("entry text must be a string")
    if not MIN_TEXT_CHARS <= len(text) <= MAX_TEXT_CHARS:
        raise ValueError(
            f"entry text must be {MIN_TEXT_CHARS} to {MAX_TEXT_CHARS} "
            f"characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry text must not be only white space")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry text must be UTF-8 encodable: {exc}") from exc
    return text


def encode_entry(text):
    """Validate the text and return its exact UTF-8 bytes."""
    return validate_text(text).encode("utf-8")


def output_dir():
    """Resolve the output directory (env override, else the grader path)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def write_entry_bytes(data, directory=None):
    """Write the bytes to entry.txt in the output directory.

    Binary mode on purpose: text mode would write the platform's line
    ends and its default encoding instead of these exact bytes.
    """
    target_dir = directory if directory is not None else output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, OUTPUT_FILENAME)
    with open(path, "wb") as handle:
        handle.write(data)
    return path


def main():
    data = encode_entry(build_text())
    path = write_entry_bytes(data)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
