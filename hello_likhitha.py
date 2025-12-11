#!/usr/bin/env python3
"""Hello Likhitha — prints a friendly greeting and some great things about you."""

import argparse
import random

GOOD_THINGS = [
    "Creative problem-solver",
    "Hardworking and persistent",
    "Curious and always learning",
    "Empathetic and kind",
    "Great communicator and team player",
    "Quick learner who adapts fast",
]


def print_all():
    print("Hello, Likhitha! 👋\n")
    print("Here are some great things about you:\n")
    for i, thing in enumerate(GOOD_THINGS, 1):
        print(f"{i}. {thing}")


def print_random():
    print("Hello, Likhitha! 👋\n")
    print("A random great thing about you:\n")
    print(f"- {random.choice(GOOD_THINGS)}")


def main():
    parser = argparse.ArgumentParser(description="Hello Likhitha — a small compliment script")
    parser.add_argument("-r", "--random", action="store_true", help="Show one random compliment")
    args = parser.parse_args()

    if args.random:
        print_random()
    else:
        print_all()


if __name__ == "__main__":
    main()
