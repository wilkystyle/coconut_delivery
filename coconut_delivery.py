import sys

DATA_FILE = "sample_paths.txt"


def build_flight(data_file):
    """
    Build and return a flight object from a given input file.
    """
    # TODO
    raise NotImplementedError(
        "You have not yet implemented the build_flight method!"
    )


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


if __name__ == '__main__':
    if len(sys.argv) == 2:
        DATA_FILE = sys.argv[1]

    with open(DATA_FILE) as f:
        build_flight(f)
