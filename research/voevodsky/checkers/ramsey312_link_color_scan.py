"""Color maximal common-link facets; on failure, extract a vertex-critical four-chromatic subgraph. Inputs output by center_link_scan.rs."""
from ramsey312_google_two_step import *
import gzip

def main():
 for f in sys.argv[1:]:
    summary=[];links=[];bad=[]
    for line in open(f):
        if line.startswith('S'):summary.append(list(map(int,line.split()[1:])));continue
        a,b=line.split(';');d,x,y,n,*s=map(int,a.split()[1:]);assert n==len(s);E=[tuple(map(int,t.split(':'))) for t in b.split()];V=set(range(n))
        def solve(V):
            with Solver(name='g4') as sl:
                for i in V:sl.add_clause([3*i+k for k in (1,2,3)])
                for i,j in E:
                    if i in V and j in V:
                        for k in (1,2,3):sl.add_clause([-3*i-k,-3*j-k])
                if not sl.solve():return None
                m=set(sl.get_model());c={i:next(k for k in (1,2,3) if 3*i+k in m) for i in V};assert all(c[i]!=c[j] for i,j in E if i in V and j in V);return c
        c=solve(V);w=None
        if c is None:
            for i in sorted(V):
                if solve(V-{i}) is None:V.remove(i)
            w=[s[i] for i in sorted(V)];bad.append(dict(d=d,end=[x,y],kernel=w))
        links.append(dict(d=d,end=[x,y],facets=s,color=list(c.values()) if c is not None and list(c)==list(range(n)) else c,kernel=w))
    name=Path(f).stem;print(name,'cores',len(summary),'pairs',sum(z[2] for z in summary),'domains',sum(z[3] for z in summary),'maximal',len(links),'bad cores',len({r['d'] for r in bad}),'bad links',len(bad),'sizes',sorted(set(len(r['kernel']) for r in bad)));(D/f'ramsey312_{name}_link_summary.json').write_text(json.dumps(dict(cores=len(summary),pairs=sum(z[2] for z in summary),unique_domains=sum(z[3] for z in summary),maximal_domains=len(links),bad=bad))); 
    with gzip.open(D/f'ramsey312_{name}_link_cert.json.gz','wt') as out:json.dump(dict(summary=summary,links=links),out,separators=(',',':'))
if __name__=='__main__':main()
