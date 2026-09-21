"""Typed marked prime paths. Forgotten events remain source arrows.

Marks select record letters, not deletion of arithmetic transitions.
"""
from dataclasses import dataclass
from itertools import product
from math import prod

PRIMES=(2,3,5,7)
def label(vertex):return 2*prod(p for j,p in enumerate(PRIMES) if vertex>>j&1)

@dataclass(frozen=True)
class History:
    start: int
    word: tuple
    retained: tuple

    def __post_init__(self):
        if not isinstance(self.start,int) or not 0<=self.start<16:
            raise ValueError('Invalid initial source vertex')
        if not isinstance(self.word,tuple) or not isinstance(self.retained,tuple):
            raise ValueError('Words and marks must be tuples')
        if len(self.word)!=len(self.retained) or any(type(b) is not bool for b in self.retained):
            raise ValueError('One Boolean mark per event is required')
        vertex=self.start
        for j in self.word:
            if type(j) is not int or not 0<=j<4 or vertex>>j&1:
                raise ValueError('Each event must add an unused source prime')
            vertex|=1<<j

    @property
    def vertices(self):
        out=[self.start]
        for j in self.word:out.append(out[-1]|1<<j)
        return tuple(out)

    @property
    def end(self):return self.vertices[-1]

    @property
    def labels(self):return tuple(label(v) for v in self.vertices)

    def join(self,other):
        if self.end!=other.start:raise ValueError('Arithmetic attachment mismatch')
        return History(self.start,self.word+other.word,self.retained+other.retained)

    def cut(self,j):
        if not 0<=j<=len(self.word):raise ValueError('Invalid cut')
        return (History(self.start,self.word[:j],self.retained[:j]),
                History(self.vertices[j],self.word[j:],self.retained[j:]))

    def gap_normal_form(self):
        """Alternating full forgotten paths and individual retained arrows."""
        gaps=[];events=[];begin=0
        for j,keep in enumerate(self.retained):
            if keep:
                gaps.append(History(self.vertices[begin],self.word[begin:j],self.retained[begin:j]))
                events.append(History(self.vertices[j],(self.word[j],),(True,)))
                begin=j+1
        gaps.append(History(self.vertices[begin],self.word[begin:],self.retained[begin:]))
        return tuple(gaps),tuple(events)

    @classmethod
    def from_gaps(cls,gaps,events):
        if len(gaps)!=len(events)+1 or not gaps:raise ValueError('Invalid gap arity')
        if any(any(g.retained) for g in gaps):raise ValueError('Gap contains retained event')
        if any(len(e.word)!=1 or e.retained!=(True,) for e in events):
            raise ValueError('Expected individual retained events')
        out=gaps[0]
        for e,g in zip(events,gaps[1:]):out=out.join(e).join(g)
        return out


def marked_lift(start,word):
    return tuple(History(start,tuple(word),tuple(bits)) for bits in product((False,True),repeat=len(word)))
