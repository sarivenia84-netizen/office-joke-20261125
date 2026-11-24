"""Office Jokes entry for the make.fun bounty.

Writes a single-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt and prints it.
Standard library only, no network, no dependencies.

The contract: one UTF-8 line, 1-199 characters, not all whitespace. The
joke constant is 100 characters, so it fits with room to spare; a trailing
newline in the file is allowed and the writer adds exactly one.
"""

import os

# The joke is a constant so it stays the single source of truth; a few
# earlier drafts are kept below to document why the wording settled here.
#   Draft 1: "...so I initiated a meeting about it--now I'm leading four."
#   Draft 2: "...so I scheduled one; now I run a standing meeting about it."
#   Draft 3 repeated "meeting" needlessly, wasting the turn.
# Final: "initiative" becomes "recurring," so the punchline is a word the
# setup never used -- which is what makes it a twist rather than an echo.
JOKE = "My review said I need to show more initiative, so I scheduled a meeting about it\u2014now it's recurring."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
