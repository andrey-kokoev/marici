"""Endpoint-incidence lower bounds, retaining all seven tight-cover edges."""
from r312_nearmiss_cover import adj,n
cover=[(0,3),(38,43),(29,34),(18,23),(9,14),(25,47),(5,27)]
ends=set(sum((list(e) for e in cover),[])); assert len(ends)==14
seen=0; lower=0
for a,b in cover:
    centers=adj[a]&adj[b]; assert not centers&seen; seen|=centers
    c=centers.bit_count();lower+=max(4,c)
    print((a,b),'common centers',c)
assert seen==(1<<n)-1
# For each pair, at least two deletion incidences per endpoint for degree,
# and at least one at this pair per center for triangle destruction.
print('endpoint incidences >=',lower,'nonendpoint incidences >=',n-len(ends),
      'old deletions >=',(lower+n-len(ends)+1)//2)
