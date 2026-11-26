"""Resumable per-catalogue-core paired-root search. CLI: compiled paired_roots executable, optional number of eligible records. Stats count search presentations, not isomorphism types."""
import sys,gzip,json,subprocess,concurrent.futures
from ramsey_retention_slice import CAT,D,decode
edge=int(sys.argv[3]) if len(sys.argv)>3 else 35;p=D.parent/f'ramsey_38_pair49_{edge}_parts';p.mkdir(exist_ok=True);rows=[]
for line in gzip.open(CAT.parent/'r36_16.g6.gz','rt'):
 s=line.strip();a=decode(s)
 if sum(v.bit_count() for v in a)==2*edge:rows.append((s,a))
def run(i):
 s,a=rows[i];path=p/f'{i}.json'
 if path.exists():r=json.loads(path.read_text());assert r['g6']==s;return r['stats']
 vals=list(map(int,subprocess.check_output([sys.argv[1]],input=' '.join(map(str,a))+'\n',text=True).split()));assert len(vals)==4;r=dict(g6=s,stats=vals);tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(r));tmp.replace(path);return vals
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(run,range(min(len(rows),int(sys.argv[2]) if len(sys.argv)>2 else len(rows)))))
print(len(out),len(rows),[sum(v[j] for v in out) for j in range(4)],flush=True)
