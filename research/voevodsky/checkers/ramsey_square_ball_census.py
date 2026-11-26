"""Scan predecessor catalogues only. Distinguish no addable edges, no disjoint balls, sufficient size test, and exact exterior test. Compare full degree sequences for passing vs failing types."""
import sys,json,itertools,collections,subprocess,gzip,hashlib
from ramsey_retention_slice import CAT,D
P=D.parent;out={}
for n,k in [(22,7),(27,8),(35,9)]:
 path=CAT/('r37_22.g6' if n==22 else 'r38_27.g6.gz');f=([r['graph6'] for r in json.loads(D.read_text()) if r['l']==3 and r['k']==9] if n==35 else gzip.open(path,'rt') if n==27 else path.open());profiles=collections.defaultdict(collections.Counter);tot=collections.Counter();examples={};edgecounts=collections.defaultdict(collections.Counter)
 it=iter(f)
 while True:
  batch=[s.strip() for s in itertools.islice(it,8192)]
  if not batch:break
  vals=subprocess.check_output([sys.argv[1],str(k)],input='\n'.join(batch)+'\n',text=True).splitlines();assert len(vals)==len(batch)
  for s,l in zip(batch,vals):
   *v,ds=l.split();e,add,pairs,short,passes=map(int,v);state='guaranteed_by_size' if short else 'exterior_only' if passes else 'all_exteriors_fail' if pairs else 'no_disjoint_pair' if add else 'saturated';tot[state]+=1;tot['graphs']+=1;tot['pairs']+=pairs;tot['short_pairs']+=short;tot['passing_pairs']+=passes;profiles[ds][bool(passes)]+=1;edgecounts[e][state]+=1;examples.setdefault(state,s)
 mixed=sum(bool(c[True] and c[False]) for c in profiles.values());out[n]=dict(counts=tot,degree_profiles=len(profiles),mixed_profiles=mixed,edge_counts=edgecounts,examples=examples);print(n,tot,'profiles',len(profiles),mixed,flush=True)
(P/'ramsey_square_ball_census.json').write_text(json.dumps(out)+'\n')
