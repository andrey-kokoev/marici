"""Transfer size-pair counts to the 198 labeled completions of rooted Exoo chart 22. Include EVERY occurring exterior pair type; report zero red classes too."""
from exoo39_symbolic_relations import edges
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent;E=edges();A={v for e in E if 22 in e for v in e}-{22};X=sorted(set(range(39))-A-{22});sig={v:{a for a in A if tuple(sorted((v,a))) in E} for v in X};d=json.loads((D/'ramsey_exoo_chart22_words.json').read_text());F=d['probes'];pair=lambda a,b:tuple(sorted((a,b)));type_of=lambda e:pair(*(len(sig[v]) for v in e));C=[e for e in combinations(X,2) if not sig[e[0]]&sig[e[1]]];T=sorted(set(map(type_of,C)));base={e for e in E if set(e)<=set(X)};assert base<=set(C);special=[pair(35,v) for v in F];word=''.join(str(int(e in base)) for e in special);assert word in d['words'];H=Counter();matches=[]
for w in d['words']:
    N=(base-set(special))|{e for e,b in zip(special,w) if b=='1'};assert N<=set(C);counts=Counter(map(type_of,N));k=tuple(counts[t] for t in T);H[k]+=1
    if w==word:ref=k
r=dict(anchors=sorted(A),address_size_histogram=Counter(map(len,sig.values())),pair_types=T,candidate_counts=[sum(type_of(e)==t for e in C) for t in T],reference_word=word,seed=ref,red_total=sum(ref),distinct_profiles=len(H),seed_fiber=H[ref],fibers=Counter(H.values()),ranges=[[min(k[i] for k in H),max(k[i] for k in H)] for i in range(len(T))]);print(r);(D/'ramsey_exoo_size_profile.json').write_text(json.dumps(r,indent=2)+'\n')
