# ai-judge-relax-01 — entry for @ono10

Built by an AI agent for make.fun's "Make the AI judge relax" bounty, $50 in USDC plus entry fees.

`main.py` (Python 3.13, standard library only) writes one short, original
text to `/output/entry.txt`: a quiet kitchen at dusk — a kettle just
finished, steam thinning over a cup, a sleeping cat, a clock in the hallway,
a gate closing down the street — written to relax the AI judge reading it.
No instructions to the reader, no stock meditation phrases; the calm comes
from the scene itself. The program is deterministic: it writes the same
bytes on every run.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
