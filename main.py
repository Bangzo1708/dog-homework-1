"""The Dog Ate My Homework: Funniest Excuse -- entry program.

Writes one line (the dog's excuse, in the dog's own voice) to
$OUTPUT_DIR/entry.txt (default /output), with no trailing newline.
Deterministic: no network, no randomness, no clock. Pure stdlib.

Three candidate excuses, scored against the judge's five criteria
(in order of importance):
  1. An excuse a dog gives after being caught eating the homework,
     in the dog's own voice.
  2. The bigger laugh: a twist / piece of dog logic landing in one line.
  3. Sounds like a real dog: dog priorities, none of a person's shame.
  4. Stands alone, no setup, nothing needing a second line.
  5. Fresh: no cat, no taste of paper, no "good boy".

Candidate A:
  "It said 'chew on this problem' right at the top, so I did.
   Problem solved -- you're welcome."
  1: yes, first-person dog voice. 2: good twist, the instruction
     taken literally -- but the joke leans on a written instruction
     the dog somehow read, which is slightly human. 3: confident,
     no shame. 4: standalone. 5: fresh. Strong, but the "I can read"
     premise is a small crack.

Candidate B:
  "The homework was sitting on MY couch, in MY house, unguarded.
   That's not eating, that's rent collection."
  1: yes, dog claiming territory. 2: "rent collection" is a funny
     twist, but it is a human concept -- the laugh comes from a
     human idea in a dog's mouth, not from dog logic itself.
  3: territorial, no shame. 4: standalone. 5: fresh. Good, but the
     punchline is borrowed from human economics.

Candidate C (CHOSEN):
  "I didn't eat your homework. I graded it, it failed, and I
   disposed of the evidence."
  1: yes -- an excuse offered the moment it is caught, first person.
  2: best twist of the three: a three-beat escalation (graded it,
     it failed, disposed of the evidence) where each beat reframes
     the crime as a duty. The dog is not sorry; it is the authority.
  3: pure dog priorities -- the homework's fate matters less than
     the dog's verdict, and there is zero embarrassment.
  4: fully self-contained; the first sentence even denies the act
     before confessing it in a better light. 5: fresh -- no cat,
     no taste, no good boy, no begging for forgiveness.

Candidate C wins: its twist is dog logic all the way down (a dog
who believes grading homework is its job), it has the tightest
three-beat structure, and it is the line most clearly spoken by a
dog who believes it has done nothing wrong.
"""

import os
import sys

# The chosen excuse -- candidate C.
EXCUSE = (
    "I didn't eat your homework. "
    "I graded it, it failed, and I disposed of the evidence."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    text = EXCUSE

    # Hard guard: the gate requires 1-200 characters of UTF-8 text.
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "excuse must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )

    # The entry must be exactly one line and not whitespace-only:
    # a stray newline would break the "single line" requirement and
    # a whitespace-only file fails the gate outright.
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line, no line breaks")
    if not text.strip():
        raise ValueError("excuse must not be whitespace only")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # No trailing newline: exactly one line of text.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
