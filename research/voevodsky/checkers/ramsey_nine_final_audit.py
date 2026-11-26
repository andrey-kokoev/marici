"""Reconcile all exact-nine type exclusions, check that every surviving hereditary prefix was tested, and count the final three-cell fillings before testing whether each member supports the fixed prefix. Repeat terminal member tests without the residual/deficit strengthening. Partial yes/no tests do not themselves assert that edge decisions on multiple branches coexist."""
from ramsey_unsaturated_ten import *
from ramsey_eleven_coverage import count
p=lambda name:json.loads((P/(name+'.json')).read_text());gs=graphs(9);ds=[ig.Graph(8,es).degree() for es in gs];src=p('ramsey_nine_twoleaf_audit');ids=src['open'];assert len(ids)==18 and all(ds[i].count(1)==1 for i in ids);n=count(0,9,(0,)*8);assert n==sum(40320//ig.Graph(8,e).count_automorphisms() for e in gs)
B=collections.defaultdict(list)
for u,v in itertools.combinations_with_replacement(sizes,2):B[codes[u]+codes[v]].append((u,v))
def replay(r):
 i=r['i'];m=fixed(gs[i])+tuple(r['pr']);h=7*codes[255]-sum(codes[s] for s in m);tail=[(s,x,y) for s in sizes for x,y in B.get(h-codes[s],[]) if s<=x];opts=sorted({x for t in tail for x in t});ok,unk=options_for(m,opts);ok=set(ok);return i,len(tail),sum(ok.issuperset(t) for t in tail),unk
if __name__=='__main__':
 # Check coverage union by graph IDs, not a mere sum of counts.
 want={(i,()) for i in range(len(gs))};stage=[];un=0
 for k in range(7):
  z=p('ramsey_unsaturated_nine'+('_oneleaf' if k>=3 else '')+f'_{k}');keys={(r['i'],tuple(r['pr'])) for r in z};assert len(keys)==len(z) and want==keys;stage.append(len(keys));un+=sum(r.get('unknown',0) for r in z);want={(r['i'],tuple(r['pr']+[s])) for r in z for s in r.get('children',[])}
  if k==2:live={i for i,t in want};want={v for v in want if v[0] in ids}
 assert not any(r['complete'] or r['win'] for r in z);joined={r['i'] for r in p('ramsey_nine_domain_replay') if not any(w['r'][0] in ('sat5','higher') for w in r['win'])};old=p('ramsey_nine_progress');leaf=p('ramsey_nine_leaf_gate');assert live==set(ids)|joined|set(old['isolated'])|set(leaf['closed_here'])|set(src['closed']);
 with ProcessPoolExecutor(8) as ex:ctl=list(ex.map(replay,z,chunksize=4));
 out=dict(total=len(gs),labeled=n,excluded=len(gs),open=[],final_scope=ids,stages=stage,unknown=un,low_degree_final=sum(max(ds[r['i']])==3 for r in z),high_degree_final=sum(max(ds[r['i']])==4 for r in z),quota_only=sum(x[1] for x in ctl),weaker_supported=sum(x[2] for x in ctl),weaker_unknown=sum(x[3] for x in ctl),supported=0);print(out);(P/'ramsey_unsaturated_nine_final.json').write_text(json.dumps(out)+'\n')
