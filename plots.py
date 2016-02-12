import argparse
from collections import defaultdict
import re
import logging
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser('analysis for a game of catan')

    parser.add_argument('filename')
    args = parser.parse_args()

    filename = args.filename
    with open(filename, 'r') as fp:
        lines = fp.readlines()

    plot_rolls(lines)
    plot_robbers(lines)
    plot_dev_cards(lines)
    plot_points(lines)

    plt.show()


def plot_rolls(lines):
    rolls = defaultdict(int)
    for line in lines:
        match = re.match(r'[a-z]+ rolls (\d+)', line)
        if match:
            rolls[match.group(1)] += 1

    f = plt.figure()
    plt.bar(rolls.keys(), rolls.values())
    plt.title('Rolls')
    f.show()


def plot_robbers(lines):
    thieves = defaultdict(int)
    victims = defaultdict(int)
    for line in lines:
        match = re.match(r'([a-z]+) moves robber to \d+, steals from ([a-z]+)', line)
        if match:
            thieves[match.group(1)] += 1
            victims[match.group(2)] += 1

    f = plt.figure()
    plt.subplot(121)
    plt.bar(range(len(thieves)), thieves.values())
    plt.xticks(range(len(thieves)), thieves.keys())
    plt.title('Thieves')
    plt.subplot(122)
    plt.bar(range(len(victims)), victims.values())
    plt.xticks(range(len(victims)), victims.keys())
    plt.title('Victims')
    f.show()


def plot_points(lines):
    points = defaultdict(int)
    for line in lines:
        match = re.match(r'([a-z]+) buys (settlement|city)', line)
        if match:
            points[match.group(1)] += 1

    f = plt.figure()
    plt.bar(range(len(points)), points.values())
    plt.xticks(range(len(points)), points.keys())
    plt.title('Points from settlements and cities')
    f.show()


def plot_dev_cards(lines):
    buyers = defaultdict(int)
    players = defaultdict(int)
    for line in lines:
        match = re.match('([a-z]+) buys dev card', line)
        if match:
            buyers[match.group(1)] += 1
        match = re.match('([a-z]+) plays', line)
        if match:
            players[match.group(1)] += 1

    f = plt.figure()
    plt.subplot(121)
    plt.bar(range(len(buyers)), buyers.values())
    plt.xticks(range(len(buyers)), buyers.keys())
    plt.title('Dev Cards Bought')
    plt.subplot(122)
    plt.bar(range(len(players)), players.values())
    plt.xticks(range(len(players)), players.keys())
    plt.title('Dev Cards Played')
    f.show()

if __name__ == '__main__':
    main()