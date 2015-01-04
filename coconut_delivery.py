import sys

DATA_FILE = "sample_paths.txt"


class Flight:
    """
    The delivery flight.

    Contains information about the jetstreams available along the delivery
    route, as well as the base cost for flying when not in a jetstream.
    """
    jetstreams = None
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
    score = 0

    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost


def build_flight(data_file):
    """
    Build and return a flight object from a given input file.
    """

    # Initialize the jetstreams list with placeholder for the start position.
    jetstreams = [Jetstream(0, 0, 0)]
    base_cost = int(data_file.readline())
    distance = 0  # Also known as the end of the route.

    for line in data_file.readlines():
        start, end, cost = [int(x) for x in line.split()]

        if end > distance:
            distance = end

        jetstreams.append(
            Jetstream(
                start,
                end,
                cost,
            )
        )

    # Add a placeholder for the end position.
    jetstreams.append(distance, distance, 0)

    return Flight(
        jetstreams,
        distance,
        base_cost,
    )


if __name__ == '__main__':
    if len(sys.argv) == 2:
        DATA_FILE = sys.argv[1]

    flight = None
    with open(DATA_FILE) as f:
        flight = build_flight(f)
