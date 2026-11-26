"""Coverage audit distinguishing fully excluded nine-pair types from untested descendants of feasible prefixes. Count labeled triangle-free graphs independently and check every scoped child frontier."""
from ramsey_unsaturated_ten import *
from ramsey_eleven_coverage import count
p=lambda x:json.loads((P/(x+'.json')).read_text());gs=graphs(9);total=count(0,9,(0,)*8);assert total==sum(40320//ig.Graph(8,g).count_automorphisms() for g in gs);ds=[ig.Graph(8,e).degree() for e in gs];keys={(i,()) for i in range(len(gs))};L=[]
for j in range(7):
 data=p('ramsey_unsaturated_nine'+('_isolated' if j>=3 else '')+'_'+str(j));have={(r['i'],tuple(r['pr'])) for r in data};assert keys==have and len(have)==len(data);L.append(len(keys));keys={(r['i'],tuple(r['pr']+[s])) for r in data for s in r.get('children',[])}
 if j==2:live={i for i,t in keys};keys={k for k in keys if min(ds[k[0]])==0}
 if j==6:assert not any(r['complete'] for r in data)
iso={i for i in live if min(ds[i])==0};joined={r['i'] for r in p('ramsey_nine_domain_replay') if not any(z['r'][0] in ('higher','sat5') for z in r['win'])};left=sorted(live-iso-joined);assert all(1<=min(ds[i])<=max(ds[i])<=4 for i in left);summary=dict(labeled=total,total=len(gs),prefix_live=len(live),isolated=sorted(iso),scoped_layers=L,joined=sorted(joined),excluded=len(gs)-len(left),open=left,open_degree_signatures=dict(collections.Counter(str(sorted(ds[i])) for i in left)));print(summary);(P/'ramsey_nine_progress.json').write_text(json.dumps(summary)+'\n')
