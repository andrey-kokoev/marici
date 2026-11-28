"""Predecessor-only blue-seven coverage, before the nine removals. Score frozen choices against the previously verified pair only afterwards."""
from ramsey_retention_slice import CAT,D,decode
from itertools import islice,combinations
import gzip,json

def audit():
    record=262402;z=0
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,record,None)).strip())
    vs=[j for j in range(len(a)) if j!=z];cl=[0]
    for i in vs:cl.extend([s|1<<i for s in cl if not a[i]&s]);
    sevens={q for q in cl if q.bit_count()==7};assert max(map(int.bit_count,cl))==7
    es=[(i,j) for i,j in combinations(vs,2) if not a[i]>>j&1 and a[i]&a[j]==1<<z];assert len(es)==3
    hits={e:{s for s in sevens if s>>e[0]&s>>e[1]&1} for e in es};out=[]
    for e,f in combinations(es,2):
        assert set(e).isdisjoint(f);shared=hits[e]&hits[f];destroyed=hits[e]|hits[f];b=a[:]
        for i,j in (e,f):b[i]|=1<<j;b[j]|=1<<i
        # Independent count via unordered seven-subsets of the surviving vertex labels.
        remain=sum(all(b[v]&s==0 for v in c) for c in combinations(vs,7) for s in [sum(1<<v for v in c)]);assert remain==len(sevens)-len(destroyed);out.append(dict(pair=[e,f],individual=[len(hits[e]),len(hits[f])],shared=len(shared),destroyed=len(destroyed),remaining=remain))
    truth=json.loads((D.parent/'ramsey_forward_link_filter.json').read_text())['true_pairs'];best=[r['pair'] for r in out if r['destroyed']==max(v['destroyed'] for v in out)];success=len(best)==1 and [[list(e) for e in best[0]]] == truth;result=dict(record=record,deleted=z,total=len(sevens),pairs=out,unique_max_is_success=success);print(result);(D.parent/'ramsey_forward_blue_sevens.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
