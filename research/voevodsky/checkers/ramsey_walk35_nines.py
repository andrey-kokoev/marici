"""Independent endpoint replay at every root; separate counts of genuine blue nines vs projected five-region score."""
from ramsey_incidence_walk35 import audit,a,P
import subprocess,json,sys,concurrent.futures as cf

def run(seed):
 s,n,adj=subprocess.check_output([sys.argv[1],str(seed),sys.argv[2]],input=' '.join(map(str,a)),text=True).strip().split(';');g=list(map(int,adj.split()));roots=[audit(g,i) for i in range(35)];assert all(r['nines']==int(s) for r in roots);best=min(range(35),key=lambda i:roots[i]['prof']);return dict(seed=seed,moves=int(n),adj=g,roots=roots,best_root=best)
with cf.ThreadPoolExecutor(8) as ex:out=list(ex.map(run,range(351710,351718)))
print([(r['roots'][0]['nines'],r['roots'][r['best_root']]['prof']) for r in out]);(P/'ramsey_walk35_nines.json').write_text(json.dumps(out)+'\n')
