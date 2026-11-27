"""Terminal truth-function audit of a scoped binding, not probabilities or stored Booleans."""
from itertools import permutations,product
from collections import Counter
from pathlib import Path
import json

D=Path(__file__).resolve().parents[1]/'results'

def run():
    rows=('BRNN','BNRN');s=[{i for i,c in enumerate(row) if c!='N'} for row in rows];U=set(range(4));Y,=[p for p in permutations(range(4)) if all({p[i] for i in a}==U-a for a in s)];r=(0,2,1,3);G=[tuple(range(4)),r,Y,tuple(r[i] for i in Y)]
    # Observe the physical responder addresses 2 (R/N) and 1 (B/N).
    # Do not use these marks to disable a requester. Each occurrence is keyed by route.
    marks=[(rows[0][p[1]],rows[0][p[0]]) for p in G];assert marks==[('R','B'),('N','B'),('N','N'),('R','N')]
    together=(0,2);apart=(1,3)
    def evaluation(law,routes):
        # Each route supplies two continuations. Until observation the comparison
        # holds references to the responders, not resolved reply bits.
        def reply(side,route):
            def at_resolution(net):
                target,opposite=(net[route] if side==0 else net[route][::-1]);return target!='N' and law[side][int(opposite!='N')]
            return at_resolution
        fs=[[reply(side,t) for t in routes] for side in range(2)]
        def at_resolution(net):
            absent=[not any([f(net) for f in group]) for group in fs];return (*absent,any(absent))
        return at_resolution
    laws=list(product((False,True),repeat=2));counts=Counter();symmetric=Counter();examples={}
    for lr,lb in product(laws,repeat=2):
        law=(lr,lb);a=evaluation(law,together)(marks);b=evaluation(law,apart)(marks);diff=tuple(x!=y for x,y in zip(a,b));assert diff[:2]==(lr[0]!=lr[1],lb[0]!=lb[1]);counts['lower_different']+=int(any(diff[:2]));counts['OR_different']+=int(diff[2]);counts['laws']+=1
        if lr==lb:symmetric['laws']+=1;symmetric['OR_different']+=int(diff[2]);examples[str(lr)]=dict(together=a,apart=b)
    out=dict(assumptions='Each color responder may depend on the opposite binding at the same route only; N has the stipulated terminal negation response. Absence means no positive terminal reply. Law counts are not probabilities.',marks=marks,together=together,apart=apart,law_counts=counts,mirror_symmetric_counts=symmetric,symmetric_examples=examples);print(out);(D/'ramsey_literal_negation_readout.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
