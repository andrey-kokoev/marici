"""Intersect the 16 views of each arriving strip with the five row-compatible restarts. Test whether view-related *distinct* successors also diverge at the earliest possible visit. No ordering of strips as data."""
from itertools import takewhile
from ramsey_strip_frame_8_16 import first,swapped,ops,act
from ramsey_strip_next_row_restart import rows
tracks=sorted(first);closes={tuple(z['path']):z['closes'] for z in rows};hist=[]
for i,p in enumerate(tracks):
 views=[act(p,*op) for op in ops];images=[j for j,q in enumerate(tracks) if swapped(q) in views];overlap=lambda q:sum(1 for _ in takewhile(lambda v:v[0]==v[1],zip(p,q)))-1
 scores=list(map(overlap,tracks));early=[j for j,v in enumerate(scores) if v==min(scores)];alt=[j for j in images if j!=i];hist.append(images);print('track',i+1,'closes',closes[p],'views through prefix lengths 1..12',[len({v[:k] for v in views}) for k in range(1,13)],'other view-related successors',[j+1 for j in alt],'also earliest',[j+1 for j in alt if j in early]);assert i in images and len(alt)<=1
assert all(i in hist[j] for i,js in enumerate(hist) for j in js)
