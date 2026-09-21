"""Marked arithmetic paths in the forward graph OR its explicitly typed opposite."""
from dataclasses import dataclass

@dataclass(frozen=True)
class OrientedHistory:
    vertices: tuple
    events: tuple
    retained: tuple
    direction: int = 1

    def __post_init__(self):
        if self.direction not in (-1,1):raise ValueError('Expected graph orientation')
        if not self.vertices or len(self.vertices)!=len(self.events)+1:
            raise ValueError('Every arrow needs its endpoints')
        if len(self.retained)!=len(self.events) or any(type(b) is not bool for b in self.retained):
            raise ValueError('One Boolean mark per event')
        if any(type(v) is not int or not 0<=v<16 for v in self.vertices):
            raise ValueError('Invalid vertex')
        for s,t,j in zip(self.vertices,self.vertices[1:],self.events):
            if type(j) is not int or not 0<=j<4:raise ValueError('Invalid prime event')
            a,b=(s,t) if self.direction==1 else (t,s)
            if a>>j&1 or b!=a|1<<j:raise ValueError('Arrow violates its declared orientation')

    @classmethod
    def from_forward(cls,h):return cls(h.vertices,h.word,h.retained,1)

    def reverse(self):
        return OrientedHistory(self.vertices[::-1],self.events[::-1],self.retained[::-1],-self.direction)

    def join(self,other):
        if self.direction!=other.direction or self.vertices[-1]!=other.vertices[0]:
            raise ValueError('Typed attachment mismatch')
        return OrientedHistory(self.vertices+other.vertices[1:],self.events+other.events,
                               self.retained+other.retained,self.direction)

    def cut(self,j):
        if not 0<=j<=len(self.events):raise ValueError('Invalid cut')
        return (OrientedHistory(self.vertices[:j+1],self.events[:j],self.retained[:j],self.direction),
                OrientedHistory(self.vertices[j:],self.events[j:],self.retained[j:],self.direction))

    def gaps(self):
        starts=[j for j,b in enumerate(self.retained) if b]
        gaps=[];events=[];begin=0
        def piece(a,b):
            return OrientedHistory(self.vertices[a:b+1],self.events[a:b],self.retained[a:b],self.direction)
        for j in starts:
            gaps.append(piece(begin,j));events.append(piece(j,j+1));begin=j+1
        gaps.append(piece(begin,len(self.events)))
        return tuple(gaps),tuple(events)
