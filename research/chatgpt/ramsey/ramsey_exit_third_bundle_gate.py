"""Locate the third incidence at 29 in the source quotient and test what using it costs among the eight actual invariant perfect matchings."""
from ramsey_row_quotient_constructor import final,frame_records,move,R,flags,P
from collections import Counter
from pathlib import Path
import json
D=Path(__file__).parent

def run():
    m,=final;n=move(m,R);_,H,ms=next(z for z in frame_records if m in z[2]);E=m-n;F=n-m;third,={s for s in flags if s[1]==29}-(E|F);B=set();s=third
    while s not in B:B.add(s);s=(H[s[0]],H[s[1]])
    dom=lambda q:{i for i,j in q};cod=lambda q:{j for i,j in q};assert len(B)==5 and cod(B)==cod(E)==cod(F) and dom(B).isdisjoint(dom(E)) and move(B,R)==B
    counts=Counter(next(i for i,j in t if j==29) for t in ms);alts=[t for t in ms if B<=t];costs=[(len(m-t)//5,len(n-t)//5) for t in alts];assert all(third not in t for t in [m,n]);return dict(third=third,bundle=sorted(B),domain_duads=[P[i] for i in sorted(dom(B))],choices_at_exit=dict(counts),replaced_bundle_counts=costs)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_exit_third_bundle_gate.json').write_text(json.dumps(out)+'\n')
