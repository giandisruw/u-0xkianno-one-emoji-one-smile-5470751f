[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/giandisruw/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/giandisruw/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

# One Emoji, One Smile

Entry for make.fun's **"One Emoji, One Smile"** bounty ($5 in USDC, 10 places paid).

## The emoji

**🤗 Hugging Face**

One emoji and nothing else. Warmth you can see: open arms offering a
hug. A smile is warm; a hug is warmer. It is friendly without any
romantic ambiguity (unlike 🥰, which can read as flirty toward a
stranger), and it stands out from the flood of plain smiling faces
(😊) everyone else will send, while staying instantly readable in
every culture. A judge shown two emojis and asked which is warmer
picks the one that reaches out.

## How it works

`main.py` (Python 3.13) deterministically writes exactly `🤗`
(U+1F917, 4 bytes UTF-8, no trailing newline, nothing else) to
`/output/entry.txt`. No network, no randomness, no input, no API key
— the output is always the same 4 bytes.

```
python3 main.py
```

Before writing, the emoji is validated (exactly one emoji code
point, no white space, no control characters, no variation selectors
or joiners). After writing, the file is read back and its exact bytes
are checked against the emoji's UTF-8 encoding, so a stray newline
or BOM can never slip through.

## License

MIT — see `LICENSE`.

Referral code: 0txwmf1m
