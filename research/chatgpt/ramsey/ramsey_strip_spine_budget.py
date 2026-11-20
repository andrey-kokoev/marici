"""Gate-to-gate length bound for fixed-spine excursions. Checked on the prism lift before deleting any outward path. Edges, not vertices, are counted."""
from collections import deque
from ramsey_strip_checkpoint_face_certificate import N
moving={v for v in N if isinstance(v,tuple)}
def dist(a,b,allowed):
 seen={a:0};q=deque([a]);
 while q:
    x=q.popleft()
    if x==b:return seen[x]
    for y in (N[x]&allowed)-seen.keys():seen[y]=seen[x]+1;q.append(y)
 return float('inf')
for start in 'AC':
 for end in 'BD':
    X,Y=sorted(set('ABCD')-{start,end});D=lambda a,b:min(dist((a,i),(b,j),moving) for i in (0,1) for j in (0,1));long=[];short=[]
    for x,y in [(X,Y),(Y,X)]:
        spine=dist((x,0),(y,0),(set(N)-moving-{start+'*',end+'*'})|{(x,0),(y,0)});assert spine==5
        long.append(D(start,x)+spine+D(y,end));short.append(D(start,x)+2+D(x,end))
    assert sorted(long)==[11,13] and short==[9,9];print(start,end,'through-spine minima (leg bounds)',sorted(long),'same-switch bounds',short)
