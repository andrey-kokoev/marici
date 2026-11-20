"""Catalogue-wide blue five-set coverage. Validate each input; independently test each missed pair by common-neighbor triangles."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import gzip,hashlib,json
H=Path(__file__).resolve().parents[1];src=H.parent/'chatgpt/ramsey/r36_16.g6.gz';U=(1<<16)-1

def cliques(blue,c,k,s=0):
    if not k:
        yield s;return
    while c.bit_count()>=k:
        v=c&-c;c^=v;yield from cliques(blue,c&blue[v.bit_length()-1],k-1,s|v)

def main():
    hist=Counter();bad=[];pair_count=0
    for idx,line in enumerate(gzip.open(src,'rt')):
        g=line.strip();assert ord(g[0])-63==16;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);red=[0]*16
        for j in range(16):
            for i in range(j):
                if bits[j*(j-1)//2+i]=='1':red[i]|=1<<j;red[j]|=1<<i
        blue=[U^(1<<i)^r for i,r in enumerate(red)];assert not any(cliques(red,U,3)) and not any(cliques(blue,U,6))
        covered=[0]*16
        for s in cliques(blue,U,5):
            z=s
            while z:
                b=z&-z;z^=b;covered[b.bit_length()-1]|=s
        missed=[]
        for i,j in combinations(range(16),2):
            if not blue[i]>>j&1:continue
            pair_count+=1
            if not covered[i]>>j&1:
                N=[v for v in range(16) if (blue[i]&blue[j])>>v&1];assert all((red[a]>>b&1) or (red[a]>>c&1) or (red[b]>>c&1) for a,b,c in combinations(N,3));missed.append([i,j])
        hist[len(missed)]+=1
        if missed:bad.append(dict(index_zero_based=idx,missing=missed))
    assert sum(hist.values())==2576
    out=dict(catalogue_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),records=sum(hist.values()),blue_pairs=pair_count,uncovered_pairs=sum(k*v for k,v in hist.items()),missing_per_graph_histogram=dict(sorted(hist.items())),exceptions=bad);print({k:v for k,v in out.items() if k!='exceptions'});(H/'results/ramsey_pair_coverage_census.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
