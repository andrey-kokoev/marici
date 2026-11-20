"""Frozen candidate: label retained projected cells by chord midpoint and length class. Exchange summands at fixed midpoint, independent of dilation. Compare labeled routes, not just cardinalities."""
from ramsey_pentagon_contrast_transport import L,orbits,neighborhood_tests,contrast
from pathlib import Path
import hashlib,json

def main():
    def label(i):
        a,b=L[i];return ((3*(a+b))%5,0 if (a-b)%5 in (1,4) else 1)
    labels=[label(i) for i in range(10)];assert len(set(labels))==10
    # The projected unit vectors (within-block mean subtracted) remain distinct.
    cols=[tuple(5*int(i==j)-int(i//5==j//5) for j in range(10)) for i in range(10)];assert len(set(cols))==10
    swap=[labels.index((m,1-t)) for m,t in labels];dilate=[L.index(tuple(sorted((2*a%5,2*b%5)))) for a,b in L]
    def rel(E,p):return {tuple(sorted((p[i],p[j]))) for i,j in E}
    def fam(S,p):return {sum(1<<p[i] for i in range(10) if s>>i&1) for s in S}
    cells=[dict(source=labels[i],via_input=labels[dilate[i]],via_output=labels[swap[i]]) for i in range(10) if swap[i]!=dilate[i]];assert len(cells)==8
    cases={}
    for mask in range(1<<len(orbits)):
        E=set().union(*(e for i,e in enumerate(orbits) if mask>>i&1));S=neighborhood_tests(E)
        if S is None:continue
        A,B=rel(E,dilate),rel(E,swap);X,Y=fam(S,dilate),fam(S,swap);assert X==neighborhood_tests(A) and Y==neighborhood_tests(B)
        cases[mask]=dict(unequal_incidence_entries=len(A^B),same_restricted_operator=contrast(A)==contrast(B),unequal_attachment_masks=len(X^Y))
    out=dict(scope='fixed-midpoint reduced exchange; cells retain midpoint and length',cell_mismatches=cells,decoder_cases=cases,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(cases,cells[0]);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_midpoint_exchange.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
