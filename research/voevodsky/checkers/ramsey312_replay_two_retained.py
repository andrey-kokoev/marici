"""Merge and integer-replay every successful two-retained fractional exclusion. Locate unresolved labeled partial graphs in the 51 original cores."""
from ramsey312_google_two_step import *
import numpy as np,gzip

def main():
 cases=[l.split() for l in (D/'ramsey312_release26_two_targets.txt').open()];best={}
 for pat in ('ramsey312_deeper_two26*','ramsey312_deeper_tail26*','ramsey312_oracle_*26*'):
    for f in D.glob(pat):
        for r in map(json.loads,f.open()):
            if r['cert'] and (r['k'] not in best or len(r['cert'])<len(best[r['k']]['cert'])):best[r['k']]=r
 passed=0;mx=0;fail=[];ds=sorted({d for _,d in json.loads((D/'ramsey312_all_nine_holes.json').read_text())});affected=set()
 for l in open(sys.argv[1]):
    k,*s=map(int,l.split());z=cases[k];free=int(z[2]);h=F^free;assert int(z[4])==len(s);g=adj.copy();flipped=0
    for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i;flipped|=(1<<i)|(1<<j)
    if k not in best:
        loc=[d for d in ds if (free|flipped)&~d==0];affected.update(loc);fail.append(dict(k=k,free=list(bits(free)),flips=z[5:],cores=loc,n=len(s)));continue
    r=best[k];X=np.array(s,dtype=np.uint64);coverage=np.zeros(len(s),dtype=np.int64);cost=0
    for b,t,c,w in r['cert']:
        assert w>0 and b.bit_count()<=1 and not (b|t)&~h and all(not t&g[i] for i in bits(t))
        if b and t:assert c==11-t.bit_count()
        elif b:assert c==11-(g[b.bit_length()-1]&h).bit_count()
        else:assert c=={10:2,9:5,8:8}[t.bit_count()]
        scale=1+np.array([int(x.bit_count()==11) for x in s]) if r.get('bonus') and not b and t.bit_count()==10 else 1
        coverage+=w*(((X&b!=0) if b else True)&(X&t==0))*scale;cost+=c*w
    assert coverage.min()>=r['den'] and cost==r['cost']<8*r['den'];passed+=len(s);mx=max(mx,cost/r['den'])
 print('weighted exclusions',len(best),'supports',passed,'max cost',mx,'residual',fail,'affected',len(affected));(D/'ramsey312_two_retained_remaining.json').write_text(json.dumps(fail));
 with gzip.open(D/'ramsey312_two_retained_certs.json.gz','wt') as o:json.dump(list(best.values()),o,separators=(',',':'))
if __name__=='__main__':main()
