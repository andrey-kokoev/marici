"""Streaming highest-Walsh-mode observer on consecutive positional pairs.

For an even number of distinct prime indices, a completed route yields one
ordered tuple of unordered pairs and its internal-order parity. Coefficient
1/2 is the balanced six-prime normalization. On route mixtures, summing these
sparse outputs implements K^T/2 before additive history aggregation.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class BlockParityObserver:
    prime_count: int
    vertex: int = 0
    blocks: tuple = ()
    pending: int | None = None
    sign: int = 1

    def __post_init__(self):
        if self.prime_count < 2 or self.prime_count % 2:
            raise ValueError('An even prime count of at least two is required')
        if self.sign not in (-1, 1):
            raise ValueError('The pathwise parity must be +1 or -1')
        flat = []
        for pair in self.blocks:
            if len(pair) != 2 or pair[0] >= pair[1]:
                raise ValueError('Completed pairs must be sorted and distinct')
            flat.extend(pair)
        if self.pending is not None:
            flat.append(self.pending)
        if len(set(flat)) != len(flat) or any(not 0 <= x < self.prime_count for x in flat):
            raise ValueError('State contains repeated or invalid prime indices')
        if self.vertex != sum(1 << x for x in flat):
            raise ValueError('Endpoint mask must match the retained state')

    def step(self, prime_index: int) -> 'BlockParityObserver':
        if not 0 <= prime_index < self.prime_count or self.vertex & (1 << prime_index):
            raise ValueError('A step must add an unused prime index')
        vertex = self.vertex | (1 << prime_index)
        if self.pending is None:
            return BlockParityObserver(self.prime_count, vertex, self.blocks, prime_index, self.sign)
        orientation = 1 if self.pending < prime_index else -1
        pair = tuple(sorted((self.pending, prime_index)))
        return BlockParityObserver(self.prime_count, vertex, self.blocks+(pair,), None,
                                   self.sign*orientation)

    def output(self, scale=Fraction(1, 2)) -> tuple:
        if self.vertex != (1 << self.prime_count)-1:
            raise ValueError('The output contract requires a completed route')
        return self.blocks, scale*self.sign


def observe_mixture(prime_count: int, weighted_words, scale=Fraction(1, 2)) -> dict:
    """Linear extension of the pathwise sparse readout.

    Each item is (coefficient, full_word). Prime counts and endpoint typing are
    external control information, as in the typed linear-state realization.
    """
    outputs = {}
    for coefficient, word in weighted_words:
        observer = BlockParityObserver(prime_count)
        for j in word:
            observer = observer.step(j)
        key, value = observer.output(scale)
        outputs[key] = outputs.get(key, 0)+coefficient*value
    return {key: value for key, value in outputs.items() if value != 0}
