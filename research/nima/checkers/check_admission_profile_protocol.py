"""Finite operation contract and sufficient admission profiles.

Candidate active requests are S4 permutations with unit histories protected.
Passive changes transport history. A uniform family request must pass every
retained member. These policies are explicit, not inferred physical dynamics.
"""
from dataclasses import dataclass
from itertools import permutations, product
from math import factorial

G=tuple(permutations(range(4))); ID=tuple(range(4))

def compose(g,h): return tuple(g[h[i]] for i in range(4))
def inverse(g): return tuple(g.index(i) for i in range(4))
def transport(values,g): return tuple(values[inverse(g)[i]] for i in range(4))
def profile(values): return frozenset(g for g in G if transport(values,g)==values)

def conjugate(group,p): return frozenset(compose(compose(p,g),inverse(p)) for g in group)


@dataclass(frozen=True)
class State:
    # Diagonal degree1 maps in a zero-differential X->Y comparison frame.
    u: tuple
    v: tuple
    reference: tuple = ID

    def __post_init__(self):
        assert all(self.v[self.reference[i]]==self.u[i] for i in range(4))

    @property
    def admission(self): return profile(self.v)

    @property
    def observed(self):
        # Actual comparison equals the reference; return is its inverse.
        return self.reference,inverse(self.reference),(0,)*4


def active(state,g):
    if g not in state.admission: return False,state  # rejection is a no-op
    return True,State(state.u,state.v,compose(g,state.reference))


def passive(state,p):
    return State(state.u,transport(state.v,p),compose(p,state.reference))


states=[State(values,values) for values in product(range(4),repeat=4)]
buckets={}
for state in states: buckets.setdefault(state.admission,[]).append(state)
assert len(states)==256 and len(buckets)==15
for subgroup in buckets:
    assert ID in subgroup
    assert all(inverse(g) in subgroup for g in subgroup)
    assert all(compose(g,h) in subgroup for g,h in product(subgroup,repeat=2))
    representative=buckets[subgroup][0]
    multiplicities=[representative.v.count(value) for value in set(representative.v)]
    expected=1
    for size in multiplicities: expected*=factorial(size)
    assert len(subgroup)==expected

# Exact contextual sufficiency for the declared active/passive protocol.
for group,equivalent in buckets.items():
    a,b=equivalent[0],equivalent[-1]
    assert a.observed==b.observed
    for g,h in product(G,repeat=2):
        ok_a,aa=active(a,g); ok_b,bb=active(b,g)
        assert ok_a==ok_b and aa.observed==bb.observed
        assert aa.admission==bb.admission==group
        ok_aa,aaa=active(aa,h); ok_bb,bbb=active(bb,h)
        assert ok_aa==ok_bb and aaa.observed==bbb.observed
        # Transported presentation changes conjugate the admission profile.
        pa,pb=passive(a,g),passive(b,g)
        assert pa.admission==pb.admission==conjugate(group,g)
        assert active(pa,h)[0]==active(pb,h)[0]
# Distinct profiles are separated by a one-step active request.
profiles=tuple(buckets)
for i,a in enumerate(profiles):
    for b in profiles[i+1:]:
        witness=next(iter(a^b))
        assert active(buckets[a][0],witness)[0]!=active(buckets[b][0],witness)[0]


@dataclass(frozen=True)
class Family:
    label: str
    members: tuple

    @property
    def admission(self):
        out=frozenset(G)
        for member in self.members: out=out & member.admission
        return out

    @property
    def leaves(self):
        return tuple(leaf for member in self.members
                     for leaf in (member.leaves if isinstance(member,Family) else (member,)))


def promote_pairs(records,namespace):
    assert len(records)%2==0
    return tuple(Family(f'{namespace}:{i//2}',tuple(records[i:i+2])) for i in range(0,len(records),2))


pointed=[State(tuple(int(i==j) for i in range(4)),tuple(int(i==j) for i in range(4))) for j in range(4)]
assert [len(s.admission) for s in pointed]==[6]*4
first=promote_pairs(pointed,'one'); second=promote_pairs(first,'two')
assert [len(f.admission) for f in first]==[2,2]
assert len(second)==1 and len(second[0].admission)==1
assert second[0].leaves==tuple(pointed)
assert len({f.label for f in first+second})==3
assert second[0].admission==Family('flat',tuple(pointed)).admission
for g in G:
    assert (g in second[0].admission)==all(active(member,g)[0] for member in pointed)
# Intersection is a closed, associative summary operation on the15 profiles.
for a,b in product(profiles,repeat=2): assert a&b in buckets
for a,b,c in product(profiles,repeat=3): assert (a&b)&c==a&(b&c)
# Root-context covariance and family aggregation commute.
for p in G:
    transformed=Family('transported',tuple(passive(s,p) for s in pointed))
    assert transformed.admission==conjugate(second[0].admission,p)
# Summary discards amplitudes: costs or newly protected coordinates could split it.
assert profile((1,0,0,0))==profile((3,0,0,0))
assert sum(x*x for x in (1,0,0,0))!=sum(x*x for x in (3,0,0,0))
print('256 diagonal histories reduce to15 exact admission profiles for the declared S4 request family.')
print('Profiles are subgroups; passive relabelling conjugates them and admitted protected active steps preserve them.')
print('Equal profiles pass all two-request active/passive controls; distinct profiles have an explicit separating request.')
print('Uniform family promotion combines permissions by intersection; two retained pair-grouping rounds give profile sizes6->2->1.')
print('One fresh label per group and complete leaf recovery hold. Next-level endpoint fields are not invented by this profile rule.')
print('The summary is sufficient for this protocol, not for amplitude-sensitive costs or arbitrary history edits. Active use of S4 is a declared model choice.')
