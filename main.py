"""The One-Liner Groan-Off: one original dad joke, written to /output/entry.txt.

The angle: sourdough. Not the tired dad-joke pantry of light bulbs,
elevators and chicken crossings, but the one kitchen resident that
genuinely behaves like a moody relationship partner. A sourdough
starter is alive, it needs feeding, it sulks when ignored, and every
home baker talks about it as if it had feelings and a calendar. That
is exactly the kind of everyday object a dad can point at across the
dinner table and turn into a breakup story, which is where the groan
lives: the joke treats a jar of fermented flour the way a teenager
treats a break-up text, and the listener realises halfway through
that the "partner" in the story is bread.

Why this line works, beat by beat. The setup, "My sourdough starter
dumped me", is a small absurdity delivered deadpan: a starter cannot
dump anyone, so the brain accepts the breakup frame before it
notices the frame is ridiculous, and that half-second of acceptance
is what makes the punchline land instead of flop. "Dumped" is doing
real work here rather than "left": it is the blunt, modern breakup
word, it makes the jar sound like a partner with standards, and it
sets up the excuse that follows as a text-message cliché instead of
a gentle drift apart. The middle,
"it said it needed space to rise", does double duty: it is a
plausible breakup excuse ("I need space") and, at the same time, a
literal description of what a starter actually does when it is fed
and left alone in a warm spot. The two meanings sit on top of each
other without a seam, so nothing in the line has to be explained
afterwards, and a joke that explains itself has already lost the
room. The closer, "and honestly, I kneaded that coming", is the
groan itself: "kneaded" sounds exactly like "needed", so the
sentence confesses that the break-up was foreseeable while smuggling
in the one word no sourdough joke can resist. Three short clauses,
one breath, no wasted words, and the pun arrives on the very last
word, which is where a one-liner's punchline belongs: the listener
cannot see it coming until it has already happened, and then cannot
unhear it.

The wording is deliberately plain and speakable. There is no jargon
beyond "starter", which any home baker knows and any non-baker can
guess from context, and the rhythm is conversational rather than
written: "dumped me", "it said", "and honestly". A dad joke has to
survive being said out loud in a kitchen, retold badly at work the
next day, and still work, and short declarative clauses survive
retelling far better than a clever sentence that depends on its
exact punctuation. The line is also fresh: sourdough had its
cultural moment, but the "starter as an ex" framing is not one of
the hundred-times-told dad jokes, and the "kneaded that coming"
turn is built for this sentence rather than borrowed from a joke
book.

The gate for this bounty is simple and strict: /output/entry.txt
must hold UTF-8 text of 1 to 140 characters, not only white space.
The program therefore validates its own line before writing it,
checking the character count (not the byte count, because the
em-dash is one character and three bytes in UTF-8) and refusing to
write a line that is blank or over the limit, so a bad line fails
loudly here instead of silently failing the sealed scorer.
"""

import os

# The entry: one line, one breakup, one pun. The em-dash separates
# the setup from the excuse the way a dad pauses for effect, and
# "dumped" keeps the breakup blunt: the starter did not drift away,
# it ended things.
LINE = (
    "My sourdough starter dumped me \u2014 it said it needed space to rise, "
    "and honestly, I kneaded that coming."
)

# The bounty gate, restated as code: 1 to 140 characters, not blank.
MAX_CHARS = 140


def validate(line):
    """Check a candidate line against the bounty gate.

    Returns the line unchanged when it passes. Raises ValueError
    with a plain explanation when it does not, so a bad line fails
    loudly here instead of failing the sealed scorer silently.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    # One line only: a stray newline would make the file two lines.
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    # Prove it encodes as UTF-8 before the scorer has to.
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # File permissions only: never chmod a directory. The grader runs
    # as an unprivileged user, and chmod on a directory it does not
    # own makes the whole program exit 1.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
