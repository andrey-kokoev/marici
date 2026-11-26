"""Validate complete branch coverage for the previously open two-leaf graphs; classify the sole-leaf remainder. Re-run the weaker flexible-cell partial SAT without deficit slots or residual-label bounds on the last 236 branches for all candidates in exact quota-matching tails. This checks whether exclusion of these terminal tails depends on the strengthening. Partial support alone is not a witness."""
from ramsey_unsaturated_ten import *
from concurrent.futures import ProcessPoolExecutor
p=lambda s:json.loads((P/(s+'.json')).read_text());gs=graphs(9);degs=[ig.Graph(8,e).degree() for e in gs];prior=p('ramsey_nine_leaf_gate');two={i for i in prior['open'] if degs[i].count(1)==2};want={(r['i'],tuple(r['pr']+[s])) for r in p('ramsey_unsaturated_nine_2') if r['i'] in two for s in r['children']};st=[];unk=0
for j in range(3,7):
 rs=p('ramsey_unsaturated_nine_twoleaf_'+str(j));assert want=={(r['i'],tuple(r['pr'])) for r in rs} and len(want)==len(rs);st.append(len(want));unk+=sum(r.get('unknown',0) for r in rs);want={(r['i'],tuple(r['pr']+[s])) for r in rs for s in r.get('children',[])}
assert not any(r['complete'] for r in rs);B=collections.defaultdict(list)
for u,v in itertools.combinations_with_replacement(sizes,2):B[codes[u]+codes[v]].append((u,v))
def check(r):
 m=fixed(gs[r['i']])+tuple(r['pr']);target=7*codes[255]-sum(codes[x] for x in m);tails=[(x,y,z) for x in sizes for y,z in B.get(target-codes[x],[]) if x<=y];# Weaker symbolic test (no deficit slots or residual-label lower bounds) to measure what they add.
 domain=sorted({x for t in tails for x in t});ok,u=options_for(m,domain,residual=False,slots=False);old=[t for t in tails if set(ok).issuperset(t)];return (len(tails),len(old),u)
if __name__=='__main__':
 with ProcessPoolExecutor(8) as ex:ctrl=list(ex.map(check,rs,chunksize=2));
 left=sorted(set(prior['open'])-two);assert all(degs[i].count(1)==1 for i in left);out=dict(closed=sorted(two),stage_counts=st,unknown=unk,quota_possible=sum(x[0] for x in ctrl),without_boundary_cuts=sum(x[1] for x in ctrl),control_unknown=sum(x[2] for x in ctrl),with_boundary_cuts=0,excluded=len(gs)-len(left),open=left,signatures=collections.Counter(str(sorted(degs[i])) for i in left));print(out);(P/'ramsey_nine_twoleaf_audit.json').write_text(json.dumps(out)+'\n')
