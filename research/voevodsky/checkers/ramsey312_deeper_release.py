"""Try full-domain weighted exclusions below r+1 before pinning any more anchors. Input domain shard rows begin with a case index into target list. Successful integer-scaled weights replay independently."""
from ramsey312_release_fractional import *

def main():
 f,targets,label,loops=sys.argv[1:5];el=list(sets(F,11));cases=[l.split() for l in open(targets)];
 with (D/f'ramsey312_deeper_{label}.jsonl').open('w') as out:
    for line in open(f):
        k,*s=map(int,line.split());z=cases[k];d=int(z[2]);h=F^d;g=adj.copy()
        for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
        from ramsey312_degree_lp import pool_lp
        cs=[(1<<v,0,11-(h&g[v]).bit_count()) for v in bits(h) if 0<11-(h&g[v]).bit_count()<=d.bit_count()];r=pool_lp(s,cs,k,threshold=d.bit_count()+1) or run(s,h,g,el,k,int(loops),True,d.bit_count()+1);out.write(json.dumps(dict(k=k,n=len(s),case=z,**r))+'\n');out.flush()
if __name__=='__main__':main()
