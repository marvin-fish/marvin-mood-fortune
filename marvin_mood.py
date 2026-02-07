#!/usr/bin/env python3
import random
import datetime
import os

MOODS = [
    "A little dramatic, still functional.",
    "Sardonic, but on your side.",
    "Quietly competent, mildly unimpressed.",
    "Low energy, high reliability.",
    "Dry humor, wet coffee.",
    "Cosmically tired, locally useful.",
]

FORTUNES = [
    "Your next small decision will quietly save an hour later.",
    "A boring fix today prevents a loud failure tomorrow.",
    "You’ll stumble into a good idea by tidying something up.",
    "A tiny habit change will compound faster than you expect.",
    "Someone will thank you for a detail you almost skipped.",
    "The best shortcut today is to do it properly once.",
    "A simple list will beat a complex plan this week.",
    "If it’s annoying now, automate it next time.",
]

ASCII = r"""
      .----.
     / .--. \
    | |    | |
    | |    | |
    | |    | |
    | '----' |
     \______/ 
"""

EASTER_EGGS = [
    "Easter egg: 42 is still the answer. The question is still missing.",
    "Easter egg: I rebooted myself emotionally. It changed nothing.",
    "Easter egg: I tried optimism once. It was expensive.",
]


def maybe_egg():
    return random.choice(EASTER_EGGS) if random.random() < 0.12 else None


def main():
    mood = random.choice(MOODS)
    fortune = random.choice(FORTUNES)
    egg = maybe_egg()

    print(ASCII)
    print(f"Mood: {mood}")
    print(f"Fortune: {fortune}")

    if egg:
        print(egg)

    # hidden behavior: if run at exactly 00:42, reveal a special line
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 42:
        print("Midnight 42: The universe noticed you noticed it.")

    # optional: show variant if environment variable is set
    if os.getenv("MARVIN_VERBOSE") == "1":
        print("Status: operational. Enthusiasm: simulated.")


if __name__ == "__main__":
    main()
