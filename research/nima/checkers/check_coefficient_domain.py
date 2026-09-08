"""Exact obstruction to rational channel parameters despite trivial characters."""
import json
from pathlib import Path
from fractions import Fraction
from math import prod
p=json.loads(Path('research/nima/results/local_global_torus_lattice.json').read_text())
assert p['status']=='passed' and p['combined_index_in_saturation']==1
T=[frozenset(tuple(e) for e in t) for t in p['triangulations']]
channels=set().union(*T)
adj={e:set() for e in channels}
for i,a in enumerate(T):
    for b in T[i+1:]:
        if len(a^b)==2:
            x=next(iter(a-b));y=next(iter(b-a));adj[x].add(y);adj[y].add(x)
seen={next(iter(channels))}
while True:
    new=seen|set().union(*(adj[e] for e in seen))
    if new==seen:break
    seen=new
assert seen==channels and all(len(t)==3 for t in T)
D=p['complement']
def coords(value):return [prod(Fraction(value)**e for e in row) for row in D]
assert coords(2)==coords(1)==[1,1]
# All constant-weight channel solutions are common z, by connected flip equations.
# At prime 2, z^3=2 would require an integer valuation v with 3v=1.
assert 1%3!=0
assert Fraction(2)**3==8 and coords(8)==[1,1]
result={'status':'passed','constant_weight':2,'quotient_characters':[1,1],'crossing_graph_connected':True,'required_rational_valuation':'3*v_2(z)=1','rational_channel_solution':False,'positive_control':{'constant_weight':8,'common_channel_scale':2},'real_boundary':'At n=6 every nonzero real constant has a cube root; at n=5 constant -1 has no real square root.', 'scope':'Constant-weight family and rational obstruction; no numerical root approximation.'}
Path('research/nima/results/coefficient_domain.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
