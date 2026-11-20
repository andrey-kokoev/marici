"""Exact normalized Cheeger constants on 16-vertex obstruction graphs and their complements."""
from fractions import Fraction
from pathlib import Path
import json
from ramsey_cell_decoder_polynomial import obstructions


def audit(dim,B):
    n=1<<dim;d=len(B);assert d and 0 not in B
    # Walsh halfspaces; normalized Laplacian eigenvalue is twice the cut fraction.
    cuts=[sum((h&b).bit_count()%2 for b in B) for h in range(1,n)]
    halfgap=Fraction(min(cuts),d)
    # Independent exhaustive edge-boundary computation by adding one vertex at a time.
    adj=[sum(1<<(x^b) for b in B) for x in range(n)];boundary=[0]*(1<<n);best=Fraction(1)
    for s in range(1,1<<n):
        bit=s&-s;t=s^bit;i=bit.bit_length()-1
        boundary[s]=boundary[t]+d-2*(t&adj[i]).bit_count()
        if s.bit_count()<=n//2:best=min(best,Fraction(boundary[s],d*s.bit_count()))
    assert best==halfgap
    return best,min(cuts),max(cuts)

if __name__=='__main__':
    for f in ['4bit_25','5bit_26','6bit_26','6bit_27_from_catalogue']:
        a=json.loads(Path(__file__).with_name('ramsey_38_cell_'+f+'.json').read_text())['rows'];dim,b=obstructions(a,3,3);bc=set(range(1,1<<dim))-b
        phi,lo,hi=audit(dim,b);other,clo,_=audit(dim,bc);assert hi+clo==1<<(dim-1)
        print(f,'degree',len(b),'phi',phi,'sparse vs best removed',lo,hi,'complement phi',other)
