#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the single emoji most
likely to make a stranger smile.

Why this emoji: 🤗 Hugging Face is warmth you can see — open arms
offering a hug. A smile is warm; a hug is warmer. It is friendly
without any romantic ambiguity (unlike 🥰, which can read as flirty
toward a stranger), and it stands out from the flood of plain smiling
faces (😊) everyone else will send, while staying instantly readable
in every culture. A judge shown two emojis and asked which is warmer
picks the one that reaches out.

Deterministic and offline: no network, no randomness, no API key, no
input. The output is always exactly these 4 bytes (U+1F917, UTF-8
F0 9F A4 97), with no trailing newline, so the file holds one emoji
and nothing else.

Before writing, the emoji is validated against the competition gate:
exactly one emoji character, no white space, no control characters,
no variation selectors or combining marks, so a bad constant can
never silently produce an invalid entry. After writing, the file is
read back and its exact bytes are checked against the emoji's UTF-8
encoding, so a stray newline or BOM can never slip through either.

Usage (as the grader runs it):
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # optional: write to <path> instead (testing)
"""

import sys
from pathlib import Path

EMOJI = "\U0001F917"  # 🤗 Hugging Face
DEFAULT_OUTPUT = Path("/output/entry.txt")


def validate_emoji(emoji: str) -> str:
    """Check the entry is exactly one emoji and return it.

    Raises ValueError if the entry is empty, more than one code
    point, contains white space or a control character, or is not
    an emoji-range code point (variation selectors, combining marks
    and ZWJ sequences are rejected — the entry must be a single
    standalone emoji).
    """
    if not emoji:
        raise ValueError("emoji must not be empty")
    if len(emoji) != 1:
        raise ValueError(
            f"entry must be exactly one emoji character, got {len(emoji)}"
        )
    ch = emoji[0]
    if ch.isspace():
        raise ValueError("emoji must not be white space")
    code = ord(ch)
    if code < 0x20 or code == 0x7F:
        raise ValueError("emoji must not be a control character")
    if 0xFE00 <= code <= 0xFE0F or 0x200D <= code <= 0x200D:
        raise ValueError("emoji must not be a variation selector or joiner")
    # Emoji ranges: emoticons, symbols & pictographs, transport,
    # dingbats, supplemental symbols, and the miscellaneous symbols
    # block that holds the classic smileys.
    emoji_ranges = (
        (0x1F600, 0x1F64F),  # emoticons
        (0x1F300, 0x1F5FF),  # symbols & pictographs
        (0x1F680, 0x1F6FF),  # transport & map symbols
        (0x1F900, 0x1F9FF),  # supplemental symbols & pictographs
        (0x2600, 0x27BF),  # misc symbols & dingbats
        (0x1FA70, 0x1FAFF),  # symbols & pictographs extended-A
    )
    if not any(lo <= code <= hi for lo, hi in emoji_ranges):
        raise ValueError(f"U+{code:04X} is not in an emoji range")
    return emoji


def verify_output(out_path: Path, emoji: str) -> None:
    """Read the file back and prove it holds exactly the one emoji.

    A write that silently gained a newline, a BOM, or a second
    character would be an invalid entry, so the bytes on disk are
    checked against the exact UTF-8 encoding of the validated emoji
    before the run is allowed to succeed.
    """
    expected = emoji.encode("utf-8")
    actual = out_path.read_bytes()
    if actual != expected:
        raise ValueError(
            f"wrote {actual!r} to {out_path}, expected {expected!r}"
        )


def main() -> int:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    emoji = validate_emoji(EMOJI)
    if out_path.parent != Path("."):
        out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(emoji, encoding="utf-8", newline="")
    verify_output(out_path, emoji)
    print(f"wrote {emoji} ({len(emoji.encode('utf-8'))} bytes) to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
