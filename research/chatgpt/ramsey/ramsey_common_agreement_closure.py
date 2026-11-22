"""Use actual selected Hall bundles. Project onto agreement at a duad or at a partition; close their generated symmetry group. Unit counting metric explicit. No assignment of proton coefficients to Hall flags."""
from ramsey_row_quotient_constructor import final,move,R
from fractions import Fraction as F
from pathlib import Path
import json
D=Path(__file__).parent

def run():
    m,=final;flags=sorted(m^move(m,R));n=len(flags);I=tuple(range(n));flip=lambda side:tuple(next(j for j,y in enumerate(flags) if x!=y and x[side]==y[side]) for x in flags);a,b=flip(0),flip(1);mul=lambda g,h:tuple(g[i] for i in h);group={I};todo=[I]
    for g in todo:
        for h in (a,b):
            v=mul(g,h)
            if v not in group:group.add(v);todo.append(v)
    step=lambda h,x:tuple((y+x[i])/2 for y,i in zip(x,h));seed=tuple(F(v==(0,16)) for v in flags);ab=step(b,step(a,seed));ba=step(a,step(b,seed));assert ab!=ba and len(group)==10
    for k in I:
        col=tuple(F(sum(g[k]==i for g in group),len(group)) for i in I);assert set(col)=={F(1,10)} and step(a,col)==step(b,col)==col
    return dict(flags=flags,generated_group_size=len(group),duad_then_partition=[(f,str(v)) for f,v in zip(flags,ab) if v],partition_then_duad=[(f,str(v)) for f,v in zip(flags,ba) if v],group_average_entry='1/10',common_rank=1)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_common_agreement_closure.json').write_text(json.dumps(out)+'\n')
