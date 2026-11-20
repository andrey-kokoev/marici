"""Minimum nonadaptive on-route queries for deciding closure on the frozen 40 routes. Positions counted from the four-set pole, 1..10. No unused nodes or global counts queried."""
import json
from itertools import combinations
from pathlib import Path
from collections import Counter
H=Path(__file__).parent; rows=json.loads((H/'ramsey_strip_closure_control.json').read_text());rules=json.loads((H/'ramsey_strip_bridge_profiles.json').read_text())['whole']['examples'];out={}
for mode in ('profile','two_bits','one_bit','other_bit','nearest','distance_from_start','distance_from_end'):
    words=[]
    for row in rows:
        word=[]
        for p in row['profiles']:
            a,b=(int(p in rule) for rule in rules);word.append(dict(profile=tuple(p),two_bits=(a,b),one_bit=a,other_bit=b,nearest=min(p),distance_from_start=p[0],distance_from_end=p[-1])[mode])
        words.append((word,row['closes']))
    for k in range(11):
        fits=[]
        for I in combinations(range(10),k):
            values=[{tuple(w[i] for i in I) for w,y in words if y==target} for target in (False,True)]
            if values[0].isdisjoint(values[1]):fits.append(dict(positions=[i+1 for i in I],reject=sorted(values[0]),accept=sorted(values[1])))
        if fits:break
    out[mode]=fits;print(mode,len(fits),fits[:1])
(H/'ramsey_strip_local_access.json').write_text(json.dumps(out,indent=2)+'\n')
