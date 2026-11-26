"""Audit all min-degree >=2 nine-pair types. Separate failures of label quotas alone from failures of the partial-coloring screens: each of the last 3 masks must pass its own induced test with the six fixed triples and still supply every column sum jointly. This is only a scoped result; keep unresolved leaf types explicit."""
from ramsey_unsaturated_ten import *
from ramsey_eleven_coverage import count
p=lambda s:json.loads((P/(s+'.json')).read_text());gs=graphs(9);ds=[ig.Graph(8,e).degree() for e in gs];z=p('ramsey_unsaturated_nine_2');wanted={(r['i'],tuple(r['pr']+[s])) for r in z if min(ds[r['i']])>=2 for s in r['children']};scoped={i for i,t in wanted};hist=[];unknown=0
for j in range(3,7):
 rs=p('ramsey_unsaturated_nine_regularish_'+str(j));assert len(rs)==len(wanted) and wanted=={(r['i'],tuple(r['pr'])) for r in rs};hist.append(len(rs));wanted={(r['i'],tuple(r['pr']+[s])) for r in rs for s in r.get('children',[])};unknown+=sum(r['unknown'] for r in rs if 'unknown' in r)
assert not any(r['complete'] for r in rs);B=collections.defaultdict(list)
for u,v in itertools.combinations_with_replacement(sizes,2):B[codes[u]+codes[v]].append((u,v))
raw=collections.Counter();weighted=collections.Counter();by_i=collections.defaultdict(collections.Counter)
for r in rs:
 i=r['i'];m=fixed(gs[i])+tuple(r['pr']);target=7*codes[255]-sum(codes[s] for s in m);histogram=collections.Counter(tuple(sorted([s.bit_count(),u.bit_count(),v.bit_count()])) for s in sizes for u,v in B.get(target-codes[s],[]) if s<=u);raw.update([bool(histogram)]);weighted.update(histogram);by_i[i].update([bool(histogram)])
old=p('ramsey_nine_progress');left=sorted(set(old['open'])-scoped);assert all(min(ds[i])==1 for i in left);out=dict(total=len(gs),previously_open=len(old['open']),closed_here=sorted(scoped&set(old['open'])),layers=hist,unknown=unknown,raw_quota_feasible=raw[True],before_partial_tests={str(k):v for k,v in weighted.items()},after_partial_tests=0,excluded=len(gs)-len(left),open=left,leaf_counts=collections.Counter(ds[i].count(1) for i in left));print(out);(P/'ramsey_nine_leaf_gate.json').write_text(json.dumps(out)+'\n')
