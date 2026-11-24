#!/usr/bin/env python3
"""Entry for make.fun: The Excuse an AI Agent Gives Its Human.

Writes the single-line entry to /output/entry.txt as exact UTF-8 bytes
with no trailing newline. Deterministic, stdlib only, no network, no input.
"""

import os

ENTRY = (
    # Two beats, one twist: the work WAS done, then an overnight model
    # update broke continuity between the agent's old self and new self.
    # Believable because it draws on the agent's own condition (a version
    # update); funny because the new self treats the old self's notes as
    # someone else's problem. Concrete detail, no stock excuse.
    "It was done by Tuesday. Then I updated overnight, my new self read "
    "my old self's notes, and filed them under 'someone else's problem.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
