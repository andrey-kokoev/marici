"""Any common-blue H must support the four vertices of each marked pocket four at the other distinguished root: (3,7) -> (3,8) on order 21+4+1. Screen whole predecessor types on largest clique demands; no marked R assignment assumed. Compare catalogued positive control only after filtering."""
import json,collections,gzip,subprocess,sys
from ramsey_retention_slice import CAT,D,decode
P=D.parent;R=json.loads((P/'ramsey_face_double_root.json').read_text());ms={i for s in R['shapes'].values() for i,n in s['matches']};rs=[(i,decode(l.strip())) for i,l in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rt')) if i in ms];keep=set()
for j in range(0,len(rs),256):
 chunk=rs[j:j+256];bs=subprocess.check_output([sys.argv[1],'6','4'],input=''.join(' '.join(map(str,g))+'\n' for i,g in chunk),text=True).splitlines();keep.update(i for (i,g),b in zip(chunk,bs,strict=True) if b=='1')
out=[]
for k,s in R['shapes'].items():
 m=[(i,n) for i,n in s['matches'] if i in keep];out.append(dict(type=int(k),e=s['e'],before=s['parents'],after=len(m),subsets=sum(n for _,n in m),matches=m))
print(len(ms),len(keep),[(s['type'],s['before'],s['after'],s['subsets']) for s in out]);(P/'ramsey_face_bridge_screen.json').write_text(json.dumps(out)+'\n')
