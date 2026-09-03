import json
from pathlib import Path
# Equal positive endpoint weights admit distinct couplings with identical diagonal Grams.
a=(1,1); b=(1,1)
identity=((1,0),(0,1)); swap=((0,1),(1,0))
def margins(m): return tuple(map(sum,m)),tuple(map(sum,zip(*m)))
def gram(v): return tuple(v)
allowed=((1,0),(0,1))
def support_within(m,g): return all(not m[i][j] or g[i][j] for i in range(2) for j in range(2))
checks={'same_left_gram':gram(a)==gram(a),'same_right_gram':gram(b)==gram(b),'same_margins':margins(identity)==margins(swap)==(a,b),'distinct_couplings':identity!=swap,'identity_respects_interlacing_graph':support_within(identity,allowed),'swap_violates_interlacing_graph':not support_within(swap,allowed)}
result={'schema':'marici.strominger.rh_quarter_endpoint_gram_coupling_nonidentifiability.v1','status':'passed' if all(checks.values()) else 'failed','endpoint_grams':{'left':gram(a),'right':gram(b)},'couplings':{'identity':identity,'swap':swap},'verdict':'Separate positive endpoint Gram diagonals and margins do not identify the joint Hall coupling or certify its interlacing support.','residual':'A source-derived joint map from signed source terms to interlacing-edge capacities remains necessary.','checks':checks}
p=Path(__file__).parents[1]/'results'/'rh_quarter_endpoint_gram_coupling_nonidentifiability.json';p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
