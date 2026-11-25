"""Check the combined certificates against every enumerated support and independently validate every capacity and rewiring on its own graph."""
from ramsey312_google_two_step import *
import numpy as np,gzip

def main():
 certs=json.loads((D/'ramsey312_degree_fraction25.json').read_text())+[r for f in D.glob('ramsey312_release_frac25_*.jsonl') for r in map(json.loads,f.open()) if r['cert']];out={}
 for r in certs:
    if r['k'] not in out or len(r['cert'])<len(out[r['k']]['cert']):out[r['k']]=r
 cases=[l.split() for l in (D/'ramsey312_bounded24_6.txt').open() if l.startswith('L ')];assert len(cases)==len(out)==302;total=0;maxcost=(0,None);rows=[]
 for idx,line in enumerate(open(sys.argv[1])):
    k,*s=map(int,line.split());z=cases[k];free=int(z[2]);h=F^free;assert len(s)==int(z[4]) and k==idx;g=adj.copy();total+=len(s)
    for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
    r=out[k];X=np.array(s,dtype=np.uint64);coverage=np.zeros(len(s),dtype=np.int64);cost=0
    for b,t,c,w in r['cert']:
        assert b.bit_count()<=1 and not (b|t)&~h and all(not t&g[i] for i in bits(t)) and w>0
        if t and b:assert c==11-t.bit_count()
        elif t:assert t.bit_count()==10 and c==2
        else:assert b and c==11-(h&g[b.bit_length()-1]).bit_count()
        coverage+=w*(((X&b!=0) if b else True)&(X&t==0));cost+=w*c
    assert coverage.min()>=r['den'] and cost==r['cost'] and cost<7*r['den'];maxcost=max(maxcost,(cost/r['den'],k));rows.append(dict(case=z,**r))
 with gzip.open(D/'ramsey312_release25_final.json.gz','wt') as f:json.dump(rows,f,separators=(',',':'))
 print('verified',len(rows),'domains',total,'max budget',maxcost)
if __name__=='__main__':main()
