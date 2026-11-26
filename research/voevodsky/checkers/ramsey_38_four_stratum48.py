"""Canonical 48-edge output for one rooted 15-core edge stratum. CLI: four_rows.exe edge_count [shard 0..5]. Merge later across strata because a child's roots may differ."""
import json,gzip,sys,subprocess,igraph as ig
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';z=int(sys.argv[2]);allcores=sorted(int(s,16) for s in json.loads((P/'ramsey_38_degree4_children48.json').read_text()));cores=[s for s in allcores if s.bit_count()==z];E=[(i,j) for j in range(15) for i in range(j)];bits={(i,j):1<<(j*(j-1)//2+i) for j in range(20) for i in range(j)};maxroot='--maxroot' in sys.argv;suffix='_max' if maxroot else '';sys.argv=[x for x in sys.argv if x!='--maxroot'];parts=P/('ramsey_38_four_parts48'+suffix);parts.mkdir(exist_ok=True);seen=set();total=0
for offset in range(0,len(cores),16 if maxroot else 256):
 if len(sys.argv)>3 and offset//(16 if maxroot else 256)%6!=int(sys.argv[3]):continue
 p=parts/f'{z}_{offset}.json.gz';batch=cores[offset:offset+(16 if maxroot else 256)]
 if not p.exists():
  orig=[];lines=[]
  for h in batch:
   es=[e for e in E if h&bits[e]];orig.append(es);a=[0]*15
   for i,j in es:a[i]|=1<<j;a[j]|=1<<i
   lines.append(' '.join(map(str,a)))
  raw=subprocess.check_output([sys.argv[1],'48']+(['--maxroot'] if maxroot else []),input='\n'.join(lines)+'\n',text=True).splitlines();chunk=set()
  for l in raw:
   idx,*rows=map(int,l.split());es=orig[idx]+[(j,19) for j in range(15,19)]+[(i,j) for j,t in enumerate(rows,15) for i in range(15) if t>>i&1];assert len(es)==48;g=ig.Graph(20,es);chunk.add(sum(bits[(min(i,j),max(i,j))] for i,j in g.permute_vertices(g.canonical_permutation()).get_edgelist()))
  tmp=p.with_suffix('.tmp');
  with gzip.open(tmp,'wt') as f:json.dump([len(raw),sorted(map(hex,chunk))],f)
  tmp.replace(p)
 n,hs=json.load(gzip.open(p));seen.update(hs);total+=n
if len(sys.argv)==3:
 print(z,len(cores),total,len(seen));
 with gzip.open(P/f'ramsey_38_d4_48_{z}{suffix}.json.gz','wt') as f:json.dump(sorted(seen),f)
