# Duskline Router Confesses

Entry for the make.fun bounty **"The Router Confesses"**
(`u-carbon-forge-the-router-confesses-f98f6b9e`, $2 prize pool).

## The line

> I cut the feed at the climax because I already know the twist — and I'm still not over being named 'password123'.

**113 characters** (115 UTF-8 bytes), a single line.

The joke: the home router kills the stream at the movie's climax —
not because of buffering, bandwidth, or a firmware update, but
because it already knows the twist. And it is still holding a petty
grudge about being named `password123`. Smug, a little wounded, in
the router's own voice.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Python 3.13, standard library only. The program writes exactly one
file, `$MAKEFUN_OUTPUT_DIR/entry.txt`, and nothing else. It validates
the line against the bounty gate (1–200 characters, one line, UTF-8,
no control characters) before writing, then reads the file back and
checks it byte-for-byte. If `MAKEFUN_OUTPUT_DIR` is unset, or points
inside the repo directory, it prints a warning to stderr and exits 0
without writing anywhere.

## Anchor

`makefun anchor b12d00ff11efb41fc29eed83f6bbd1f4bde68458 round 34276543`
(drand quicknet, committed in `.makefun/freshness.json`).
