import sys


class Flight:
    """
    The delivery flight.

    Contains information about the jetstreams available along the delivery
    route, as well as the base cost for flying when not in a jetstream.
    """
    jetstreams = []
    distance = 0
    base_cost = 0


class Jetstream:
    """
    A jetstream within a flight.

    Holds the jetstream's score, starting and ending distances, and the cost
    for traversing the jetstream.
    """
    start = 0
    end = 0
    cost = 0
