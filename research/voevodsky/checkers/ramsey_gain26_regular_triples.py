"""All exact-three augmentations of the 62 sparse minima. First impose every vertex's quota locally, then global seven packing on all passing cases. Resolve any passing leaves separately. Parents/augmentations counted with labels and provenance, not distinct endpoint types."""
import json,concurrent.futures as cf,subprocess,sys,ast,collections
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_minimal.json').read_text());path=P/'ramsey_gain26_regular_triples.json';out=json.loads(path.read_text()) if path.exists() else [];done={x['idx'] for x in out};todo=[i for i,r in enumerate(R) if r['edges']==73 and i not in done]
def run(i):
 p=subprocess.run([sys.argv[1]],input=' '.join(map(str,R[i]['adj']))+'\n',text=True,capture_output=True,check=True);trace=ast.literal_eval(p.stderr.strip());ls=p.stdout.splitlines();assert len(ls)==trace[-1];vals=subprocess.check_output([sys.argv[2],'7','8'],input=p.stdout,text=True).splitlines();return dict(idx=i,trace=trace,passing=[list(map(int,s.split())) for s,z in zip(ls,vals,strict=True) if int(z)])
with cf.ThreadPoolExecutor(int(sys.argv[3])) as ex:
 for f in cf.as_completed([ex.submit(run,i) for i in todo]):out.append(f.result());path.write_text(json.dumps(out)+'\n');
print(len(out),sum(x['trace'][0] for x in out),sum(x['trace'][-1] for x in out),sum(len(x['passing']) for x in out))
