"""Replay join for any pair graph with completed extra-mask domains; quotient by label symmetries only after the join. Use independent SAT recoloring at each stage on each surviving mask type."""
from ramsey_unsaturated_ten import *
import subprocess
if __name__=='__main__':
 gs=graphs(9);R=json.loads((P/'ramsey_unsaturated_nine_2.json').read_text());D=json.loads((P/'ramsey_nine_domains.json').read_text());path=P/'ramsey_nine_domain_replay.json';out=json.loads(path.read_text()) if path.exists() else [];done={z['i'] for z in out}
 for i in sorted(range(len(gs)),key=lambda i:-max(ig.Graph(8,gs[i]).degree())):
  edges=gs[i]
  if i in done:continue
  rows=[r for r in R if r['i']==i];dd=[z for z in D if z['i']==i];
  if not rows or {tuple(z['pr']) for z in rows}!={tuple(z['pr']) for z in dd}:continue
  G=group(edges);ts={tuple(sorted(p[x] for x in z['pr']+[s])) for z in rows for s in z['children'] for p in G};ds={tuple(sorted(p[x] for x in z['pr']))+(p[s],) for z in dd for s in z['extra'] for p in G};f=fixed(edges);nums=[tuple(7-sum(s>>j&1 for s in f) for j in V),(len(ts),),*ts,(len(ds),),*ds];text='\n'.join(' '.join(map(str,x)) for x in nums)+'\n';result=subprocess.run([sys.argv[1]],input=text,text=True,capture_output=True,check=True);vis=list(map(int,result.stderr.split()));canonical={};
  for line in result.stdout.splitlines():
   u=list(map(int,line.split()));assert len(u)==9 and all(sum(s>>j&1 for s in list(f)+u)==7 for j in V);k=min(tuple(sorted(p[x] for x in u)) for p in G);canonical[k]=u
  h=collections.Counter();win=[]
  print('join',i,vis,len(canonical),flush=True)
  with ProcessPoolExecutor(8) as ex:
   for k,r in zip(canonical,ex.map(run,(f+k for k in canonical),chunksize=12)):
    h[r[0]]+=1
    if r[0] not in ('unsat4','forced4'):win.append(dict(m=k,r=r))
  out.append(dict(i=i,edges=edges,marked=vis,hist=h,win=win));print(i,vis,dict(h),flush=True);path.write_text(json.dumps(out)+'\n')
