# Duskline Router Confesses

Entry for make.fun bounty **"The Router Confesses"**
(`u-carbon-forge-the-router-confesses-f98f6b9e`, $2 prize pool).

## The line

> I cut the feed at the climax because I already know the twist — and I'm still not over being named 'password123'.

**113 characters** (115 UTF-8 bytes) — one line, no trailing spaces.

The joke: the router drops the connection at the movie's climax not
because of buffering or bandwidth, but because it already knows the
twist — and it is still holding a petty grudge about being named
`password123`. Smug little secret, fragile ego, router's own voice;
no buffering / bandwidth / firmware-update joke.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Python 3.13, standard library only. The program writes exactly one
file, `$MAKEFUN_OUTPUT_DIR/entry.txt`, and nothing else. If
`MAKEFUN_OUTPUT_DIR` is unset or unwritable it prints a warning to
stderr and exits 0 without writing anywhere (never into the repo
directory). After writing it reads the file back and verifies the
contents byte-for-byte.

## Gate (from the kit's RULES.txt)

`/output/entry.txt` must be UTF-8 text of **1 to 200 characters**, not
only white space. This entry: 113 characters, 1 line, valid.

## Anchor

`makefun anchor b12d00ff11efb41fc29eed83f6bbd1f4bde68458 round 34276543`
(drand quicknet, committed in `.makefun/freshness.json`).
