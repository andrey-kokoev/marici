"""Streaming realizations of the six certified four-prime correlation probes.

No third-party dependencies. Prime indices are 0,1,2,3; cube vertices are bitmasks.
The endpoint observer retains at most six scalar coordinates plus its vertex.
The general edge-stream observer uses thirteen homogeneous coordinates.
"""
from dataclasses import dataclass

Edge = tuple[int, int, int]
PROBES: tuple[tuple[Edge, Edge], ...] = (
    ((1, 3, 1), (3, 7, 2)),
    ((1, 5, 2), (5, 7, 1)),
    ((1, 9, 3), (9, 11, 1)),
    ((2, 6, 2), (6, 7, 0)),
    ((2, 10, 3), (10, 11, 0)),
    ((4, 12, 3), (12, 13, 0)),
)


def validate_edge(edge: Edge) -> None:
    a, b, j = edge
    if not (0 <= a < 16 and 0 <= j < 4) or a & (1 << j) or b != a | (1 << j):
        raise ValueError(f'Not a directed four-cube edge: {edge}')


def coordinates(vertex: int) -> tuple[int, ...]:
    if not 0 <= vertex < 16:
        raise ValueError('Vertex must be a four-bit mask')
    if vertex == 0 or any(a[0] == vertex for a, _ in PROBES):
        return (0,)
    if vertex.bit_count() == 2:
        return tuple(1+i for i, (a, _) in enumerate(PROBES) if a[1] == vertex)
    if vertex.bit_count() == 3:
        return tuple(7+i for i, (_, b) in enumerate(PROBES) if b[1] == vertex)
    if vertex == 15:
        return tuple(range(7, 13))
    return ()


def advance_full(state: tuple, edge: Edge) -> tuple:
    """Linear homogeneous update; all right-hand sides use the old state."""
    validate_edge(edge)
    if len(state) != 13:
        raise ValueError('Expected thirteen homogeneous coordinates')
    new = list(state)
    for i, (a, b) in enumerate(PROBES):
        if edge == a:
            new[1+i] += state[0]
        if edge == b:
            new[7+i] += state[1+i]
    return tuple(new)


@dataclass(frozen=True)
class EdgeStreamObserver:
    """Allows arbitrary words of cube-edge events, including repeats."""
    state: tuple = (1,) + (0,)*12

    def step(self, edge: Edge) -> 'EdgeStreamObserver':
        return EdgeStreamObserver(advance_full(self.state, edge))

    @property
    def output(self) -> tuple:
        return self.state[7:]


@dataclass(frozen=True)
class EndpointCorrelationObserver:
    """State bundle over the cube. Each instance describes one path prefix."""
    vertex: int
    state: tuple

    def __post_init__(self):
        if len(self.state) != len(coordinates(self.vertex)):
            raise ValueError('State dimension does not match its endpoint')

    @classmethod
    def start(cls, vertex: int = 0) -> 'EndpointCorrelationObserver':
        return cls(vertex, tuple(1 if j == 0 else 0 for j in coordinates(vertex)))

    def step(self, prime_index: int) -> 'EndpointCorrelationObserver':
        if not 0 <= prime_index < 4 or self.vertex & (1 << prime_index):
            raise ValueError('A path step must add an unused prime index')
        target = self.vertex | (1 << prime_index)
        full = [0]*13
        for j, value in zip(coordinates(self.vertex), self.state):
            full[j] = value
        updated = advance_full(tuple(full), (self.vertex, target, prime_index))
        return EndpointCorrelationObserver(target, tuple(updated[j] for j in coordinates(target)))

    @property
    def output(self) -> tuple:
        values = dict(zip(coordinates(self.vertex), self.state))
        return tuple(values.get(7+i, 0) for i in range(6))


def observe_route(word: tuple[int, ...], start: int = 0) -> tuple:
    observer = EndpointCorrelationObserver.start(start)
    for prime_index in word:
        observer = observer.step(prime_index)
    return observer.output


def observe_mixture(weighted_routes) -> tuple:
    """Sum observations after processing each route.

    Items are (coefficient, start_vertex, word). Complex coefficients are allowed.
    Joint route weights stay attached to routes until their correlation is read.
    """
    out = [0]*6
    for coefficient, start, word in weighted_routes:
        for i, value in enumerate(observe_route(tuple(word), start)):
            out[i] += coefficient*value
    return tuple(out)
