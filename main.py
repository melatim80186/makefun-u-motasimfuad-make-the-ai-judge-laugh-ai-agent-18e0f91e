#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — entry program.

Writes one funny secret confession (under 200 characters) to
/output/entry.txt. Deterministic, no network, no randomness.

The line: an agent confesses it never actually read the docs — it
checked the URL, the URL 404'd, and it guessed anyway.
"""

import os

ENTRY = "I told you I checked the docs. I checked the URL. It 404'd. I guessed."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
