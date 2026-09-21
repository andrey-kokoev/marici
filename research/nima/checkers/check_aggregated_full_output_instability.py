"""Exact source-norm and vertical-packet identities; no finite-rank inference."""
from pathlib import Path
from fractions import Fraction as Q
import json
import sympy as s


def main():
    n=s.symbols('n',positive=True)
    c,cp=s.symbols('c cp',real=True)
    derivative=s.I*c+cp/n
    squared=s.expand(s.conjugate(derivative)*derivative+c*c/n**2)
    assert s.simplify(squared-(c*c+(c*c+cp*cp)/n**2))==0
    A0,A1=s.symbols('A0 A1',positive=True)
    norm2=A0+(A0+A1)/n**2
    assert s.limit(norm2,n,s.oo)==A0
    u,v=s.symbols('u v',real=True)
    assert s.simplify(s.exp(-s.I*(v-n)*u)-s.exp(s.I*n*u)*s.exp(-s.I*v*u))==0
    moments=logs=0
    for k in range(1,31):
        for j in range(-50,51):
            assert Q(1+abs(j-k),k)<=1+Q(1+abs(j),k)
            moments+=1
            assert 1+abs(j-k)<=(1+k)*(1+abs(j))
            logs+=1
    result={'passed':True,'checks':['oscillating_graph_norm_identity',
        'positive_limiting_graph_norm','vertical_fourier_density_shift'],
        'first_moment_majorants':moments,'logarithmic_frequency_majorants':logs,
        'scope':'The analytic gamma/prime estimates are supplied by Voevodsky. These checks do not infer compactness or nonclosed range from finite matrices.'}
    out=Path(__file__).resolve().parents[1]/'results/aggregated-full-output-instability.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
