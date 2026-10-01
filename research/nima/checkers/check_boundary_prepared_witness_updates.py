"""Boundary preparation and witness transport as retained affine updates.

The conjugation action follows a declared End(V) amplitude type and the faithful
S3 representation. Preparation increments remain explicit source inputs.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/boundary-prepared-witness-updates.json'
out.unlink(missing_ok=True)
V=tuple(range(4)); identity=V; G=tuple(g for g in permutations(V) if g[0]==0)
I=((F(1),F(0)),(F(0),F(1))); Z=((F(0),F(0)),(F(0),F(0)))
H=((F(0),F(1)),(F(0),F(0))); K=((F(0),F(0)),(F(1),F(0)))
def add(a,b): return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def scale(c,a): return tuple(tuple(c*x for x in row) for row in a)
def sub(a,b): return add(a,scale(-1,b))
def mul(b,a): return tuple(tuple(sum((b[i][k]*a[k][j] for k in range(2)),F(0)) for j in range(2)) for i in range(2))
def inverse(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det
    return ((a[1][1]/det,-a[0][1]/det),(-a[1][0]/det,a[0][0]/det))
def gm(b,a): return tuple(b[a[i]] for i in V)
def gi(a): return tuple(a.index(i) for i in V)
def rho(g): return tuple(tuple(F((g[j]==i)-(g[3]==i)) for j in (1,2)) for i in (1,2))
def conjugate(t,a): return mul(mul(t,a),inverse(t))
def act(h,a): return conjugate(rho(h),a)
def total(xs):
    result=Z
    for x in xs: result=add(result,x)
    return result

@dataclass(frozen=True)
class Update:
    source: int
    target: int
    witness: tuple
    kick: tuple
    parents: tuple=()
    def __post_init__(self):
        assert self.source in V and self.target in V and self.witness in G
    def apply(self,a): return add(act(self.witness,a),self.kick)
    def payload(self): return self.source,self.target,self.witness,self.kick

def compose(b,a):
    assert a.target==b.source
    return Update(a.source,b.target,gm(b.witness,a.witness),
                  add(b.kick,act(b.witness,a.kick)),(a,b))
def undo(a):
    h=gi(a.witness)
    return Update(a.target,a.source,h,scale(-1,act(h,a.kick)),(a,))
def prepare(i,b): return Update(i,i,identity,b)
def transport(i,j,h): return Update(i,j,h,Z)

states=(Z,I,H,K,add(H,scale(2,K)))
updates=[Update(i,j,h,add(scale(F(i,3),H),scale(F(j-1,5),K)))
         for i,j in product(V,repeat=2) for h in G]
for a in updates:
    restored=compose(undo(a),a)
    assert restored.payload()==(a.source,a.source,identity,Z)
    assert compose(prepare(a.target,Z),a).payload()==a.payload()
    assert compose(prepare(a.target,a.kick),transport(a.source,a.target,a.witness)).payload()==a.payload()
    for state in states: assert undo(a).apply(a.apply(state))==state
    for b in updates:
        if a.target!=b.source: continue
        for state in (Z,add(H,K)):
            assert compose(b,a).apply(state)==b.apply(a.apply(state))
        c=Update(b.target,0,G[3],I)
        left=compose(c,compose(b,a)); right=compose(compose(c,b),a)
        assert left.payload()==right.payload() and left.parents!=right.parents

# Passive changes of port coordinates transport the witness action, preparation
# and amplitude together; no output is adjusted afterward to force agreement.
frames={i:((F(1+i*i),F(i)),(F(i),F(1))) for i in V}
for a in updates:
    t=mul(mul(frames[a.target],rho(a.witness)),inverse(frames[a.source]))
    kick=conjugate(frames[a.target],a.kick)
    for state in states:
        lhs=add(conjugate(t,conjugate(frames[a.source],state)),kick)
        assert lhs==conjugate(frames[a.target],a.apply(state))
# The fixed reference remains explicit in decoding; preparation changes the
# response, not d4. Undoing an update restores the d4-relative response.
d4=scale(2,I)
decode=lambda state:mul(d4,add(I,state))
for a in updates:
    for state in states: assert decode(undo(a).apply(a.apply(state)))==decode(state)

# Witness/endpoint-only coherent kicks can be supplied by boundary potentials.
potentials={i:add(scale(F(i+1,3),H),scale(F(i*i-1,5),K)) for i in V}
coherent={(i,j,h):Update(i,j,h,sub(potentials[j],act(h,potentials[i])))
          for i,j in product(V,repeat=2) for h in G}
for a in coherent.values():
    for b in coherent.values():
        if a.target==b.source:
            assert compose(b,a).payload()==coherent[a.source,b.target,gm(b.witness,a.witness)].payload()
# Averaging incoming-arrow kicks recovers a potential for this cocycle. The
# accompanying note proves this formula for ANY cocycle on the finite groupoid.
recovered={j:scale(F(1,24),total(coherent[i,j,h].kick for i in V for h in G)) for j in V}
for a in coherent.values():
    assert a.kick==sub(recovered[a.target],act(a.witness,recovered[a.source]))
    for state in states:
        assert sub(a.apply(state),potentials[a.target])==act(a.witness,sub(state,potentials[a.source]))

# A supplied preparation word is more than its finite witness projection.
swap=(0,2,1,3)
pulse=compose(prepare(0,I),transport(0,0,swap))
twice=compose(pulse,pulse)
assert twice.witness==identity and twice.kick==scale(2,I)
assert twice.apply(Z)!=Z
assert undo(pulse).kick==scale(-1,I)
# Swapping operation order changes the prepared response, as predicted by the
# same conjugation law, with no new arbitrary interaction coefficient.
assert compose(transport(0,0,swap),prepare(0,H)).apply(Z)==K
assert compose(prepare(0,H),transport(0,0,swap)).apply(Z)==H

# Apply the common witness action and explicit preparations to primitive legs,
# not137 independent slot values. The original sharing/factorization survives.
legs={}
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        legs[tag,'x',i]=add(I,scale(F(i,3),H))
        legs[tag,'y',i]=add(I,scale(F(i,5),K))
assert len(legs)==30
b1={key:(H if key[1:] == ('x',0) else Z) for key in legs}
b2={key:(K if key[1:] == ('y',1) else Z) for key in legs}
h1=swap; h2=G[3]
def update_legs(values,h,preparation):
    return {key:add(act(h,value),preparation[key]) for key,value in values.items()}
def slots(values):
    return {(tag,i,j):mul(values[tag,'y',j],values[tag,'x',i])
            for tag,size in (('a',11),('s',4)) for i,j in product(range(size),repeat=2)}
first=update_legs(legs,h1,b1)
second=update_legs(first,h2,b2)
combined={key:add(b2[key],act(h2,b1[key])) for key in legs}
assert second==update_legs(legs,gm(h2,h1),combined)
old_slots=slots(legs); new_slots=slots(first)
assert len(new_slots)==137 and new_slots!=old_slots
for (tag,i,j),value in new_slots.items():
    x,y=legs[tag,'x',i],legs[tag,'y',j]
    bx,by=b1[tag,'x',i],b1[tag,'y',j]
    forced=total((act(h1,mul(y,x)),mul(act(h1,y),bx),mul(by,act(h1,x)),mul(by,bx)))
    assert value==forced
    rectangle=sub(add(value,new_slots[tag,0,0]),add(new_slots[tag,i,0],new_slots[tag,0,j]))
    assert rectangle==mul(sub(first[tag,'y',j],first[tag,'y',0]),
                          sub(first[tag,'x',i],first[tag,'x',0]))
assert slots(second)==slots(update_legs(legs,gm(h2,h1),combined))

result={
 'status':'passed',
 'classification':'retained_affine_preparation_transport_law_with_witness_only_cocycle_limit',
 'obligation':'source operation, attachment covariance and ordered composition before readout',
 'stratum':'Normalized rational End(V) responses; faithful S3 witness action; explicit additive preparation inputs; fixed d4=2I decoding',
 'checks':{'associative_payload_composition':True,'units_and_inverse_updates':True,
           'parent_histories_retained':True,'port_frame_covariance':True,
           'fixed_reference_decode':True,'coherent_boundary_potential_updates':True,
           'finite_cocycle_averaging':True,'preparation_word_not_just_finite_witness':True,
           'ordered_preparation_transport_control':True,
           'shared_leg_preparation_preserves_137_slot_factorization':True,
           'slot_cross_terms_derived_from_leg_updates':True},
 'unsupported':['physical selection of preparation increments',
                'physical time or dissipation','preservation of shared-leg factorization by arbitrary slot updates',
                'complete intended rung transport','physical amplitude metric'],
 'next_constructor':'Supply preparations as actual source operations or boundary data; do not identify their retained words with a finite witness alone.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
