"""Decode labeled pair colors from blue-five incidence alone; exhaustive exact leaves if unit reconstruction stalls."""
from ramsey_pair_coverage_census import cliques,H,src,U
import gzip,json,hashlib
from collections import Counter
from pathlib import Path
from itertools import combinations
pairs=list(combinations(range(16),2))
def decode(index):
    B=[0]*16;R=[0]*16
    def add(adj,i,j):adj[i]|=1<<j;adj[j]|=1<<i
    for s in index:
        for i in range(16):
            if s>>i&1:B[i]|=s^(1<<i)
    sols=[];branches=0
    def search(b,r):
        nonlocal branches
        while True:
            moved=False;unknown=[]
            for i,j in pairs:
                if ((b[i]|r[i])>>j)&1:continue
                # Unknown ij belongs to no recorded five-set. Making ij blue
                # cannot complete any blue five-set containing it.
                cant_blue=bool(next(cliques(b,b[i]&b[j],3),0));cant_red=bool(r[i]&r[j])
                if cant_red and cant_blue:return
                if cant_red or cant_blue:add(b if cant_red else r,i,j);moved=True
                else:unknown.append((i,j))
            if not moved:break
        if unknown:
            branches+=1;i,j=unknown[0]
            for blue in [True,False]:
                bb=b[:];rr=r[:];add(bb if blue else rr,i,j);search(bb,rr)
        elif not any(cliques(r,U,3)) and not any(cliques(b,U,6)) and set(cliques(b,U,5))==index:sols.append(tuple(r))
    search(B,R);return sols,branches

def main():
    hist=Counter();ambiguous=[];n=0
    for i,line in enumerate(gzip.open(src,'rt')):
        g=line.strip();assert ord(g[0])-63==16;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);r=[0]*16
        for a,b in pairs:
            if bits[b*(b-1)//2+a]=='1':r[a]|=1<<b;r[b]|=1<<a
        b=[U^(1<<v)^x for v,x in enumerate(r)];idx=set(cliques(b,U,5));sols,branches=decode(idx);assert tuple(r) in sols;hist[branches]+=1;n+=1
        if len(sols)>1:ambiguous.append(dict(record=i,red_adjacencies=sols))
    assert n==2576
    out=dict(graphs=n,unique=n-len(ambiguous),ambiguous=ambiguous,branch_count_histogram=dict(hist),catalogue_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(n,out['unique'],dict(hist));(H/'results/ramsey_joint_incidence_decode.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
