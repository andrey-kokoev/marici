"""Compare cyclic frames, a movable blue seam, and two meanings of quotient."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

def table(k):
    return {''.join('R' if j in rs else 'B' for j in range(k)) for rs in combinations(range(k),3) if min(rs[1]-rs[0],rs[2]-rs[1])>=2}
def rotations(s):return tuple(s[i:]+s[:i] for i in range(len(s)))
def orbit(s):return set(rotations(s))|set(rotations(s[::-1]))
def test(k):
    T=table(k);target=table(k+1);fixed=set();hist=Counter();rot_only=set()
    for s in T:
        fixed.update(rotations(s[::-1]+'B'))
        # Paths are retained separately; a frame is allowed to cross the old seam.
        for u in rotations(s[::-1]):
            hist.update(rotations(u+'B'))
        for u in rotations(s):rot_only.update(rotations(u+'B'))
    valid={s for s in hist if 'RR' not in s};assert valid==target and set(hist)==rot_only
    fixed_valid={s for s in fixed if 'RR' not in s};assert fixed_valid=={s for s in target if not s.startswith('R') or not s.endswith('R')}
    # Independent check: rooted, legal, one-blue insertion at every old gap.
    insertion={s[:i]+'B'+s[i:] for s in T for i in range(k+1)};assert insertion==target
    return dict(width=k,source=len(T),next=len(target),fixed_seam=len(fixed_valid),missing_fixed_example=min(target-fixed_valid),raw_words=len(hist),illegal_example=min(set(hist)-valid),valid_outputs=len(valid),distinct_legal_dihedral_classes=len({min(orbit(s)) for s in valid}),legal_frame_paths=sum(hist[s] for s in valid),reflection_adds_outputs=False)
if __name__=='__main__':
    result=[test(k) for k in range(6,13)];print(*result,sep='\n');p=Path(__file__).resolve().parents[1]/'results/ramsey_table_rotating_seam.json';text=json.dumps(result,indent=2)+'\n';assert not p.exists() or p.read_text()==text;p.write_text(text)
