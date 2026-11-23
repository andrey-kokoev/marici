"""Use the unique maximum pair-degree label and the incident address among the three published probes. Compare transporting that address with reselecting it from the fixed probes. Test the two previously supplied path bindings separately."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';load=lambda n:json.loads((D/(n+'.json')).read_text());q=load('ramsey_probe_address_roles');profiles=q['profiles'];h,=[i for i,p in enumerate(profiles) if p[0]==max(t[0] for t in profiles)];a,={tuple(a) for sides in q['probes'].values() for a in sides if h in a};c=[0,1,4,5,2,3,6];step=lambda a:tuple(sorted(c[i] for i in a));s=[a,step(a),step(step(a))];assert c[h]==h and s[0]==s[2]!=s[1];binds=[]
for r in load('ramsey_probe_path_seed_actions'):
 b=r['binding'];binds.append([b[str(next(i for i in t if i!=h))] for t in s]);
o=dict(anchor=h,address_trace=s,partners_as_seed_sites=binds,after_one_in_original_probe_endpoints=s[1] in {tuple(a) for sides in q['probes'].values() for a in sides});print(o);(D/'ramsey_fixed_label_context.json').write_text(json.dumps(o,indent=2)+'\n')
