"""Replay strict weighted one-retained exclusions. For capacity-one rows use every eligible support, not the generator's minimal-pair list: find the inclusion-minimal eligible supports by cardinality, then check they pairwise intersect. Upward closure of intersection proves all eligible pairs intersect."""
from ramsey312_google_two_step import *
import numpy as np,gzip

def replay(z,s,d):
 h=F^d;assert h.bit_count()==44;X=np.array(s,np.uint64);high=np.array([v.bit_count()==11 for v in s]);cov=np.zeros(len(s),np.int64);total=0;n=0
 for b,t,c,w in z['cert']:
    assert w>0 and c>=0 and (b|t)&~h==0
    cond=(X&t)==0;bonus=False
    if b:
        assert b.bit_count()==1;cond&=(X&b)!=0
        if not t:assert c>=11-(adj[b.bit_length()-1]&h).bit_count()
        else:assert c>=11-t.bit_count() and all(adj[v]&t==0 for v in bits(t))
    elif c==1:
        n+=1;T=z['singles'][str(t)];assert T&t==T and T.bit_count()==10 and all(not adj[v]&T for v in bits(T));mins=[]
        for x in sorted(map(int,X[cond]),key=int.bit_count):
            if not any(y&x==y for y in mins):assert x and all(y&x for y in mins);mins.append(x)
    else:
        assert all(adj[v]&t==0 for v in bits(t)) and c>={10:2,9:5,8:8}[t.bit_count()];bonus=z.get('bonus',False) and t.bit_count()==10 and c==2
    total+=c*w;cov+=cond*w*(1+high if bonus else 1)
 assert int(cov.min())==z['den'] and total==z['cost'] and total<9*z['den'];return n

def main():
 f=sys.argv[1];cases=(D/'ramsey312_one_retained_targets.txt').read_text().splitlines();records={}
 for g in ['deeper_one29','warm_one29','warm_blocker29','warm_focus30','warm_wave30']:
    for p in D.glob('ramsey312_'+g+'_*.jsonl'):
        for z in map(json.loads,p.open()):
            if z['cert']:assert z['k'] not in records;records[z['k']]=z
 seen=set();ct=0
 for l in open(f):
    k,ar=l.split(' ',1);k=int(k)
    if k in records:
        z=records[k];assert cases[k].split()==z['case'];ct+=replay(z,list(map(int,ar.split())),int(z['case'][2]));seen.add(k)
 assert seen==set(records);ds={d for s,d in json.load(open(D/'ramsey312_all_nine_holes.json'))};rem={int(z.split()[2]) for k,z in enumerate(cases) if k not in seen};from collections import Counter
 hist=Counter(sum((d^(1<<v)) in rem for v in bits(d)) for d in ds);r=dict(weighted=len(seen),degree=23,remaining=len(rem),capacity_one_replayed=ct,core_remaining_hist=hist);print(r);(D/'ramsey312_one_retained_progress.json').write_text(json.dumps(dict(**r,remaining_masks=sorted(rem)),indent=1));
 with gzip.open(D/'ramsey312_one_retained_certs.json.gz','wt') as out:json.dump([records[k] for k in sorted(seen)],out,separators=(',',':'))
if __name__=='__main__':main()
