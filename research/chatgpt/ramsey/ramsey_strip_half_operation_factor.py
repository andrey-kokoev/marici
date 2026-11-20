"""Test whether the two quarter-turns arise by taking the forward half of one reciprocal identification and the return half of the other. Preserve full incidence, not only ports."""
from ramsey_strip_unmarked_frame_motion import maps,U,V,r,cross
reflections=[a for a in maps if all(a[a[x]]==x for x in a)];roots=[a for a in maps if all(a[a[x]]==r[x] for x in a)];s,t=reflections
assert all(s[t[x]]==t[s[x]]==r[x] for x in s)
for first,second in ((s,t),(t,s)):
 hybrid={x:(first[x] if x in V else second[x]) for x in U+V};print('hybrid is an admissible exchange',hybrid in maps,'hybrid square row swap',all(hybrid[hybrid[x]]==r[x] for x in hybrid),'matches root vertex counts',[sum(hybrid[x]==a[x] for x in hybrid) for a in roots])
 bad=[(x,y) for x in U for y in V if cross(x,y)!=cross(hybrid[y],hybrid[x])];print('cross-incidence violations',len(bad),'example',bad[:1]);assert bad and hybrid not in maps
print('same reciprocal rule twice gives identity; alternating whole reciprocal rules gives row swap')
