"""Use reciprocal frame exchanges as elementary moves. Show that nonbacktracking forces their alternation, with directed edges encoding phase. These are move-graph edges, not Hall incidences."""
from ramsey_strip_phase_moving_frame import S,T,r
N={x:{S[x],T[x]} for x in S};assert all(len(v)==2 for v in N.values());arcs={(x,y) for x in N for y in N[x]};nextarc={}
for x,y in arcs:
 z,=N[y]-{x};nextarc[x,y]=(y,z);assert z==r[x]
seen=set();orbits=[]
for a in sorted(arcs):
 if a in seen:continue
 path=[a];b=nextarc[a]
 while b!=a:path.append(b);b=nextarc[b]
 assert len(path)==4;seen.update(path);orbits.append(path)
assert len(orbits)==8 and len(seen)==32
print('move graph: 16 vertices, four squares; directed-edge dynamics: 32 states, eight four-cycles')
a=(16,7);path=[a]
for _ in range(4):a=nextarc[a];path.append(a)
print('marked directed orbit',path)
# Every directed edge uniquely identifies which reciprocal operation was just used.
assert all((S[x]==y)!=(T[x]==y) for x,y in arcs)
print('phase recoverable from previous and current frame states; no schedule table needed')
