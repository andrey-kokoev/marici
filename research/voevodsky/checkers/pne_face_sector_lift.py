"""Conditional dual reading: use actual transfer faces in their recorded orders; sector=(face centroid, tail, head) for each cyclic side. No particle interpretation of a dual step assumed."""
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';r=json.loads((D/'pne_neutron_face_readout.json').read_text());a,b=r['entry'],r['exit'];assert a==r['window'] and a[1:]==b[:2][::-1]
def sector(face,i):return ('F:'+','.join(sorted(face)),face[i],face[(i+1)%3])
s=[sector(a,0),sector(a,1),sector(b,0),sector(b,1)];assert len(set(s))==4
moves=[]
for x,y in zip(s,s[1:]):
 seam=set(x)&set(y);assert len(seam)==2
 moves.append(next(name for name,(i,j) in [('centroid-tail',(0,1)),('outer',(1,2)),('head-centroid',(2,0))] if {x[i],x[j]}==seam))
assert moves==['head-centroid','outer','head-centroid'];print(moves);(D/'pne_face_sector_lift.json').write_text(json.dumps(dict(sectors=s,moves=moves),indent=2)+'\n')
