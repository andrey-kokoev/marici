"""Protected active-frame admission and compositional triangle transport."""
from pathlib import Path
from fractions import Fraction as F
from dataclasses import dataclass
import runpy
from biclique_complex import rank

p=runpy.run_path(str(Path(__file__).with_name('check_coherent_return_history_policy.py')))
m=p['m']; Map,add,mul,delta=p['Map'],p['add'],p['mul'],p['delta']


def prod(*maps):
    out=maps[0]
    for a in maps[1:]: out=mul(out,a)
    return out


def comm(g,v): return add(mul(g,v),mul(v,g),-1)


@dataclass(frozen=True)
class Frame:
    d: Map
    r: Map
    u: Map
    v: Map
    triangle: Map

    def __post_init__(self):
        assert delta(self.u)==add(mul(self.r,self.d),m['identity']('A'),-1)
        assert delta(self.v)==add(mul(self.d,self.r),m['identity']('B'),-1)
        assert delta(self.triangle)==add(mul(self.d,self.u),mul(self.v,self.d),-1)


def active(frame,g,gi,K):
    assert not delta(g).entries and not delta(gi).entries
    assert mul(g,gi)==mul(gi,g)==m['identity']('B')
    assert not comm(g,delta(frame.v)).entries
    assert delta(K)==comm(g,frame.v)
    return Frame(mul(g,frame.d),mul(frame.r,gi),frame.u,frame.v,
                 add(mul(g,frame.triangle),mul(K,frame.d)))


def diagonal(a,b):
    return Map('B','B',0,{(i,i):F(1 if i==0 else a if i<5 else b) for i in range(9)})


base=Frame(p['d'],p['r'],p['fixed'].u,p['fixed'].v,p['fixed'].triangle)
g,gi=diagonal(2,3),diagonal(F(1,2),F(1,3))
h,hi=diagonal(5,7),diagonal(F(1,5),F(1,7))
Kg=Map('B','B',2,{(5,1):F(-1),(6,2):F(-1)})
Kh=Map('B','B',2,{(5,1):F(-2),(6,2):F(-2)})
first=active(base,g,gi,Kg); second=active(first,h,hi,Kh)
K_hg=add(mul(h,Kg),mul(Kh,g))
direct=active(base,mul(h,g),mul(gi,hi),K_hg)
assert second==direct
K_inv=Map('B','B',2,{key:-v for key,v in prod(gi,Kg,gi).entries.items()})
assert active(first,gi,g,K_inv)==base
# Exact changes of unit history leave admission unchanged, with transported
# admission certificates. Parent history can still be retained separately.
Z=Map('B','B',2,{(5,1):F(1),(6,2):F(1)})
new_v=add(base.v,delta(Z))
changed=Frame(base.d,base.r,base.u,new_v,add(base.triangle,mul(Z,base.d),-1))
K_changed=add(Kg,comm(g,Z))
assert active(changed,g,gi,K_changed).v==new_v
# Conversely, any admitted triangle yields the commutator certificate: if
# T*d=delta(Q), then T=delta(Q*r+T*v), using delta(v)=d*r-1.
T=comm(g,base.v)
Q=add(first.triangle,mul(g,base.triangle),-1)
recovered=add(mul(Q,base.r),mul(T,base.v))
assert delta(recovered)==T
# In this full-support fixture H1(End B)=0. Its closed unit-history edits do
# not produce distinct admission profiles; the earlier counterexample used a
# different zero-differential space with nontrivial degree1 homology.
b1=p['basis']('B','B',1); b2=p['basis']('B','B',2)
r1=rank([delta(a).entries for a in b1]); r2=rank([delta(a).entries for a in b2])
assert len(b1)-r1-r2==0
print('Protected request g admits exactly when [g,delta(v)]=0 and [g,v] has a degree2 filler (full candidate frame).')
print('Triangle update W_new=g*W+K_g*d passes two steps, direct composition and inverse return.')
print('Certificates compose as K_hg=h*K_g+K_h*g; exact history changes preserve the admission profile.')
print('The singular-reference fixture has H1=0: its closed unit edits share admission profiles in the full-support frame.')
print('History-sensitive admission in the earlier counterexample requires its nontrivial H1 or an added support/readout/cost restriction.')
