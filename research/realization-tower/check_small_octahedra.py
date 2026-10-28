"""Small exact FCC graph intervals; no particle labels enter the construction."""
from itertools import product
from collections import Counter
from pathlib import Path
import json
from check_six_step_octahedron import interval, distance, add


def main():
    reports=[]
    directions={d for d in product((-1,0,1),repeat=3) if sum(abs(x) for x in d)==2}
    for radius in (1,2,3):
        # Select even-parity endpoints; shift the centre when radius is odd.
        centre=(radius%2,0,0)
        start=(centre[0]-radius,0,0);end=(centre[0]+radius,0,0)
        points=interval(start,end)
        assert points=={p for p in product(range(centre[0]-radius,centre[0]+radius+1),range(-radius,radius+1),range(-radius,radius+1))
                       if sum(p)%2==0 and sum(abs(p[i]-centre[i]) for i in range(3))<=radius}
        edges={tuple(sorted((p,add(p,d)))) for p in points for d in directions if add(p,d) in points}
        tets=[];octs=[]
        for c in product(range(centre[0]-radius-1,centre[0]+radius+1),range(-radius-1,radius+1),range(-radius-1,radius+1)):
            tet=tuple(sorted(p for d in product((0,1),repeat=3) if sum(p:=add(c,d))%2==0))
            if set(tet)<=points:tets.append(tet)
            if sum(c)%2:
                octa=tuple(sorted(add(c,tuple(s if i==axis else 0 for i in range(3))) for axis in range(3) for s in (-1,1)))
                if set(octa)<=points:octs.append(octa)
        assert len(tets)+4*len(octs)==4*radius**3
        grades=dict(sorted(Counter(distance(start,p) for p in points).items()))
        reports.append({'steps':2*radius,'start':start,'end':end,'grades':grades,
                        'vertices':len(points),'edges':len(edges),'tetrahedra':len(tets),'octahedra':len(octs),
                        'points':sorted(points)})
    small=reports[0]
    assert small['grades']=={0:1,1:4,2:1}
    assert (small['vertices'],small['edges'],small['tetrahedra'],small['octahedra'])==(6,12,0,1)
    belt=[p for p in small['points'] if distance(small['start'],p)==1]
    assert len(belt)==4
    # Each equatorial site joins both poles; the equator is a four-cycle.
    for p in belt: assert distance(small['start'],p)==distance(p,small['end'])==1
    assert sum(distance(p,q)==1 for i,p in enumerate(belt) for q in belt[i+1:])==4
    result={'status':'pass','candidate':'Smallest octahedral interval as a helium candidate; radius chosen for minimality, not derived from isotope data.',
            'cases':reports,'small_case':'Two poles and a four-site equatorial grade. Four paths of length two. No 2-proton/2-neutron assignment or helium identification derived.'}
    target=Path(__file__).with_name('results')/'small-octahedra-v1.json'
    target.parent.mkdir(exist_ok=True);target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','cases':[{k:v for k,v in c.items() if k!='points'} for c in reports]}))


if __name__=='__main__':main()
