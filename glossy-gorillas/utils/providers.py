import random
from itertools import cycle
from typing import Generator, List, Tuple


def random_permutations(list_1: List[str], list_2: List[str]) -> List[Tuple[str, str]]:
    permutations = [(x, y) for x in set(list_1) for y in set(list_2)]
    random.shuffle(permutations)
    return permutations


def _spice() -> Generator[str, None, None]:
    SPICES = [
        "cumin",
        "turmeric",
        "oregano",
        "salt",
        "sugar",
        "saffron",
        "pepper",
        "paprika",
    ]
    COLOR = ["black", "brown", "yellow", "blue", "orange", "pink", "white", "green"]
    while True:
        for color, spice in cycle(random_permutations(SPICES, COLOR)):
            yield f"{color} {spice}".title()


def _service() -> Generator[str, None, None]:
    SERVICES = [
        "piracy",
        "protection",
        "entertainment",
        "companionship",
        "catering",
        "appraisal",
        "maintenance",
    ]
    ADJECTIVES = [
        "happy",
        "nervous",
        "brave",
        "cowardly",
        "sad",
        "bombastic",
        "loud",
        "quiet",
        "angry",
    ]
    while True:
        for (adj, job) in cycle(random_permutations(SERVICES, ADJECTIVES)):
            yield f"{adj} {job}".capitalize()


def _object() -> Generator[str, None, None]:
    OBJECTS = [
        "plate",
        "vase",
        "fork",
        "sword",
        "statue",
        "knife",
        "mallet",
        "shield",
    ]
    ADJECTIVES = [
        "bronze",
        "gold",
        "porcelain",
        "marble",
        "silver",
        "iron",
        "brittle",
        "sturdy",
    ]
    while True:
        for adj, obj in cycle(random_permutations(OBJECTS, ADJECTIVES)):
            yield f"{adj} {obj}".capitalize()


SpiceGenerator = _spice()
ServiceGenerator = _service()
ObjectGenerator = _object()
