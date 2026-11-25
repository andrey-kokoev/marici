"""Independent five-colorability classification on a deterministic held-out shard of full compatibility graphs."""
from ramsey312_google_two_step import *
import gzip

def main():
 out=[];bad=[]
 for l,e in zip(open(sys.argv[1]),open(sys.argv[2]),strict=True):
    z=l.split();d=list(map(int,z[:5]));s=list(map(int,z[7:]));n=len(s);assert z[6]=='RAW' and n==int(z[5]);h=F^sum(1<<v for v in d);A=[s.index(adj[v]&h) for v in d];r=e.split();assert z[:5]==r[:5];edges=[tuple(map(int,t.split(':')[:2])) for t in r[5:]];p=lambda i,k:1+i*5+k
    with Solver(name='g4') as sl:
        for i in range(n):sl.add_clause([p(i,k) for k in range(5)])
        for k,a in enumerate(A):sl.add_clause([p(a,k)])
        for i,j in edges:
            for k in range(5):sl.add_clause([-p(i,k),-p(j,k)])
        if sl.solve():
            m=set(sl.get_model());col=[next(k for k in range(5) if p(i,k) in m) for i in range(n)];assert all(col[i]!=col[j] for i,j in edges)
        else:col=None;bad.append(d)
    out.append(dict(d=d,s=s,color=col))
 with gzip.open(D/'ramsey312_held3000_color.json.gz','wt') as f:json.dump(out,f,separators=(',',':'))
 print('tested',len(out),'not five-colorable',len(bad),bad[:30]);(D/'ramsey312_held3000_bad.json').write_text(json.dumps(bad))
if __name__=='__main__':main()
