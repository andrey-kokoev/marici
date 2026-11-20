"""Check the finite edge-budget obstruction at 36 against the complete 27-vertex (3,8) catalogue. Inputs for the mathematical conclusion: R(3,8)=28 and catalogue completeness (or the published e(3,8;27)=85). No cyclic or window hypothesis."""
from pathlib import Path
from collections import Counter
import gzip,hashlib,json
H=Path(__file__).resolve().parents[1];F=H.parent/'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz'
def main():
    hist=Counter();n=27;bits=n*(n-1)//2;chunks=(bits+5)//6;pad=6*chunks-bits;weights=bytes([(x-63).bit_count() if 63<=x<=126 else 255 for x in range(256)])
    with gzip.open(F,'rb') as f:
        for row in f:
            g=row.rstrip(b'\r\n');assert len(g)==1+chunks and g[0]-63==n and not ((g[-1]-63)&((1<<pad)-1));vals=g[1:].translate(weights);assert 255 not in vals;hist[sum(vals)]+=1
    total=36*8//2;root_edges=8;cross_edges=8*(8-1);required=total-root_edges-cross_edges;assert sum(hist.values())==477142 and min(hist)==85 and required==80
    out=dict(catalogue_sha256=hashlib.sha256(F.read_bytes()).hexdigest(),records=sum(hist.values()),edge_histogram=dict(sorted(hist.items())),required_edges=required,minimum_edges=min(hist),minimum_attainers=hist[min(hist)]);print(out);(H/'results/ramsey_39_root_edge_budget.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
