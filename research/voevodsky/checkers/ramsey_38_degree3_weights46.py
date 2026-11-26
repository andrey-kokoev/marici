"""Fresh integer dual certificates for every resistant minimum-degree-3 core at 46 edges."""
import json,sys
from threadpoolctl import threadpool_limits
from ramsey_38_layer46_fresh import P,E,fit
degree=4 if '--degree4' in sys.argv else 3
rows=json.loads((P/('ramsey_38_degree4_inventory46.json' if degree==4 else 'ramsey_38_degree3_inventory_0_37_46.json')).read_text())['resistant'];shard=int(sys.argv[1]);out=P/f'ramsey_38_degree{degree}_weights46_{shard}.jsonl';done={json.loads(s)['core'] for s in out.read_text().splitlines()} if out.exists() else set()
with threadpool_limits(limits=1),out.open('a') as f:
 for a in rows[shard::4]:
  h=hex(sum(1<<k for k,(i,j) in enumerate(E) if a[i]>>j&1));
  if h in done:continue
  r=fit(h);f.write(json.dumps(r)+'\n');f.flush()
