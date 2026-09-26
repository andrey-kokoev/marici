"""Equal row math does not identify stable row occurrences or source ownership."""
from hashlib import sha256
from pathlib import Path
import json
H=lambda x:sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
a=[{'id':'synthetic-row-A','normal':['1','0'],'bound':'1'},{'id':'synthetic-row-B','normal':['0','1'],'bound':'1'}]
b=[dict(a[0],id='synthetic-row-A-new'),dict(a[1],id='synthetic-row-B-new')]
math=lambda rows:H({'schema':'ordered-matrix@1','rows':[(r['normal'],r['bound']) for r in rows]})
identity=lambda rows:H({'schema':'row-identity@1','rows':rows})
assert math(a)==math(b) and identity(a)!=identity(b)
assert math(a)!=math(list(reversed(a)))
report={'passed':True,'same_ordered_math':'same matrix digest across renamed synthetic row IDs','distinct_row_occurrences':'different identity commitment','reordered_rows':'different matrix digest','scope':'Identity commitment is not owner authentication or proof that a row occurrence happened; analytic map deferred.'}
out=Path(__file__).resolve().parents[1]/'results/row-matrix-vs-identity-digest.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
