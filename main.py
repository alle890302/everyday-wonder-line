"""Everyday Wonder entry — one sentence, at most 200 characters.

Pass 1 (chosen line):
"The elevator doors opened on a stranger humming my grandmother's song,
and for one floor the whole building felt like home."

Why it fits the judge's ordered criteria:
1. Small everyday wonder: a lift ride, a stranger humming — ordinary, one moment.
2. Fresh angle: the surprise is not the song itself but whose song it is —
   a stranger carrying the writer's grandmother's tune; the phrasing makes
   the ordinary strange.
3. Lands in one read: the turn arrives in the second clause ("for one floor
   the whole building felt like home") with no setup to decode.
4. Grounded and specific: elevator doors, humming, one floor, a building —
   concrete, real, not floating free.
5. Every word works: no filler, no worn phrase ("felt like home" is the
   payoff, earned by the grandmother's song).

Pass 2 challenger (tested, rejected):
"My kettle clicks off a second before it boils, as if it already knows I
have stopped listening for it."
Rejection: its turn is a gentle personification with no real surprise — the
kettle "knowing" is a familiar poetic move, and the wonder stays small
without the jolt of recognition the chosen line carries (a stranger holding
something intimately yours). The elevator line's angle is unmet; the kettle
line's is a commonplace.
"""

import os

TEXT = (
    "The elevator doors opened on a stranger humming my grandmother's song, "
    "and for one floor the whole building felt like home."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, f"length {len(TEXT)} outside gate"
    assert TEXT.count(".") == 1, "must be exactly one sentence"
    assert not TEXT.endswith("\n"), "no trailing newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
