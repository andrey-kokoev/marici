"""Build the three marked permutations without a reference wiring. Only then compare the two square-coordinate conventions at every root."""
import json,itertools
from pathlib import Path
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());W=src['wirings'];S=src['address_masks'];edges=list(map(tuple,src['edge_order']))
def move(swaps):
 p=list(range(7))
 for i,j in swaps:p[i],p[j]=p[j],p[i]
 m=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];perm=[edges.index(tuple(sorted((m[i],m[j])))) for i,j in edges];return lambda w:sum(((w>>i)&1)<<j for i,j in enumerate(perm))
A=move([(0,1),(2,3)]);B=move([(0,1),(4,5)]);C=move([(2,4),(3,5)])
assert all(C(w) in W and C(w)!=w and C(C(w))==w and C(A(C(w)))==B(w) for w in W)
# Competing exchange obtained by conjugating the named C by A. Keep the actual named bridge table fixed for the address test.
alt=move([(2,5),(3,4)])
assert all(alt(w)==A(C(A(w)))==A(B(C(w))) and alt(w)!=C(w) and alt(alt(w))==w and alt(A(alt(w)))==B(w) for w in W)
# Test ordered *transitions* of named wirings, rather than pairs of bare labels.
af={(w,A(w)) for w in W};bf={(w,B(w)) for w in W};push=lambda g,p:(g(p[0]),g(p[1]))
assert len(af)==len(bf)==8 and af.isdisjoint(bf)
assert all(push(A,p)==p[::-1] for p in af)
assert {push(C,p) for p in af}==bf and {push(C,p) for p in bf}==af
assert all(push(C,p[::-1])==push(C,p)[::-1] for p in af|bf)
flags=dict(A_flags=len(af),A_reversed=sum(push(A,p)==p[::-1] for p in af),C_preserves_A_family=sum(push(C,p) in af for p in af),combined_flags=len(af|bf),A_reversed_on_union=sum(push(A,p)==p[::-1] for p in af|bf));print(flags);(D/'results/ramsey_transition_reversal.json').write_text(json.dumps(flags,indent=2)+'\n')
keys=list(itertools.product(range(2),repeat=3));ident=lambda x:x
for w in W:
 bridge={};local={}
 for i,j,t in keys:
  a,b,c=(A if i else ident),(B if j else ident),(C if t else ident);bridge[i,j,t]=c(a(b(w)));local[i,j,t]=a(b(c(w)))
 assert set(bridge.values())==set(local.values())==set(W)
 assert all(C(bridge[i,j,t])==bridge[i,j,1-t] and C(local[i,j,t])==local[j,i,1-t] for i,j,t in keys)
 assert all(alt(bridge[i,j,t])==bridge[1-i,1-j,1-t] for i,j,t in keys)
out=dict(alternative='(25)(34)',alternative_on_fixed_bridge='(1-i,1-j,1-t)',named_C_on_fixed_bridge='(i,j,1-t)',named_states=len(W),roots_checked=len(W),fixed_named_states=sum(C(w)==w for w in W),fixed_square_addresses_after_local_fold=2,root_free_pairs=sorted([w,C(w)] for w in W if w<C(w)));print(out);(D/'results/ramsey_exchange_reference.json').write_text(json.dumps(out,indent=2)+'\n')
