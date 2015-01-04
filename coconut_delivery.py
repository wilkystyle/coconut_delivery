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
    next_stream = None
    flight = None

    def __init__(self, start, end, cost, flight):
        self.start = start
        self.end = end
        self.cost = cost
        self.flight = flight

    def ensure_base_score(self):
        """
        Set a base score is set for this jetstream, if we haven't already.
        """
        dist = self.flight.distance
        base_cost = self.flight.base_cost

        if self.score == 0:
            # No base score yet. Calculate one.
            cost_to_end = ((dist - self.end) * base_cost)
            self.score = self.cost + cost_to_end

    def update_score_maybe(self, other_stream):
        """
        Update the score and next_stream of this Jetstream if the other stream
        results in a better score for the this one.
        """
        # First, let's make sure this node has a base score.
        self.ensure_base_score()
        base_cost = self.flight.base_cost

        # See if using the other stream next would result in a better score.
        gap_cost = ((other_stream.start - self.end) * base_cost)
        additional_cost = other_stream.score + gap_cost
        new_score = self.cost + additional_cost

        if new_score < self.score:
            self.score = new_score
            self.next_stream = other_stream

    def enumerate_path(self):
        """
        List the jetstreams from the current stream to the end of the flight.
        """
        current_stream = self.next_stream
        while current_stream:
            yield (current_stream.start, current_stream.end)
            current_stream = current_stream.next_stream


def build_flight(data_file):
    """
    Build and return a flight object from a given input file. The jetstreams
    for the flight will be sorted by their ending position, in descending
    order.
    """
    the_flight = Flight()
    the_flight.base_cost = int(data_file.readline())  # First line is base cost
    distance = 0  # Also known as the end of the route.
    # Jetstreams list starts with a placeholder node for the starting position.
    jetstreams = [Jetstream(0, 0, 0, the_flight)]

    # Read in the remaining lines, creating a Jetstream object for each one.
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
