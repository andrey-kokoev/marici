"""Execute ramsey_37_interface_merge_protocol.md. No catalogue input."""
from itertools import product, combinations
from pathlib import Path
import json

cells = {'fixed': [(0,3),(1,2)], 'mixed1': [(0,1),(2,3)], 'mixed2': [(0,2),(1,3)]}
rows=[]
for a,b in product(('+','-','+-'), repeat=2):
    wa,aa,wb,bb = bits = ('-' in a, '-' not in b, '-' in b, '+' not in a)
    out={k:any(bits[i] and bits[j] for i,j in pairs) for k,pairs in cells.items()}
    # When A has both signs, mixed answers are complementary; otherwise identical.
    assert (out['mixed1'] != out['mixed2']) == (a=='+-')
    assert out['fixed']==bb
    rows.append(dict(A=a,B=b,**dict(zip(('wa','aa','wb','bb'),bits)),**out))
keys=['wa','aa','wb','bb',*cells];equal=[(x,y) for x,y in combinations(keys,2) if all(r[x]==r[y] for r in rows)]
assert equal==[('bb','fixed')];result=dict(rows=rows,identical_columns=equal)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(equal,[(r['A'],r['B']) for r in rows if r['mixed1']!=r['mixed2']])
