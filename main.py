"""Entry program for 'Fix Human Sleep: Funniest Patch Note'.

The whole entry is one patch-note line, under 160 characters: human
sleep now installs in a single uninterrupted session, with a warning
that waking up rested may feel unfamiliar at first. The joke is the
deadpan changelog voice treating a rested morning as a side effect
worth warning users about. The program asserts the 160-character
cap before writing, so the gate can never fail on length.
"""

import sys
from pathlib import Path

LINE = "Fixed: human sleep now installs in a single uninterrupted session. Warning: waking up rested may feel unfamiliar at first."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} characters, over the 160 limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
