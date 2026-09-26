"""Returning to equal matrix bytes does not return to an old source generation."""
from hashlib import sha256
from pathlib import Path
import json
rows=('left','right','bottom','top');p=(2,0,3,1);q=(1,3,0,2)
step=lambda rs,perm:tuple(rs[i] for i in perm)
a=rows;b=step(a,p);c=step(b,q)
assert c==a and b!=a
H=lambda x:sha256(repr(x).encode()).hexdigest()
versions=[{'generation':i+1,'rows':rs,'issuer':None} for i,rs in enumerate((a,b,c))]
assert H(versions[0]['rows'])==H(versions[2]['rows']) and versions[0]['generation']!=versions[2]['generation']
cache_key=lambda v:(H(v['rows']),v['generation'])
assert cache_key(versions[0])!=cache_key(versions[2])
assert all(v['issuer'] is None for v in versions)
report={'passed':True,'generation_path':'1->2->3, source matrix1==matrix3','math_digest':'same at generation1 and3','scoped_cache_key':'different','issuer':'none at all generations; cannot inherit owner identity','scope':'Synthetic versions, no actual source mutation/authorization or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/permutation-generation-identity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
