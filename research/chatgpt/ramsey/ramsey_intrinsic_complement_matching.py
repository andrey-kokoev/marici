"""Recover intermediate matchings from edge exclusion alone. Test whether old row order plus the marked exit & apex duad (entry 0) breaks the symmetry of the two reconstructions, using type-preserving incidence automorphisms on six edge letters."""
from itertools import permutations
from ramsey_antipode_extension import run as polarity,m,mate,D,json
from ramsey_history_matching_provenance import enum,P,T
from ramsey_row_quotient_constructor import action,move

def run():
    pol,=polarity();absf=set(pol['absolute_flags']);flags={(P.index(d),j) for j,t in enumerate(T,15) for d in t};ms=list(enum());rem=flags-(m|mate|absf);c=[s for s in ms if s<=rem];assert len(c)==2 and c[0]|c[1]==rem and flags-(rem|absf)==m|mate;out=[]
    for p in permutations(range(6)):
        h=action(p)
        if move(m,h)!=m or move(mate,h)!=mate or h[29]!=29 or h[0]!=0:continue
        out.append(dict(letters=p,swaps_candidates=move(c[0],h)==c[1],fixes_absolute=move(absf,h)==absf))
    at=[next(i for i,j in s if j==26) for s in c];linked={d:[i for i in at if set(P[0])&set(P[d])&set(P[i])] for d in (7,4)};assert linked=={7:[8],4:[3]};return dict(common_entry_letter=linked,forced_common=sorted(c[0]&c[1]),alternating=sorted(c[0]^c[1]),at26=[next(i for i,j in s if j==26) for s in c],stabilizer=out)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_intrinsic_complement_matching.json').write_text(json.dumps(out)+'\n')
