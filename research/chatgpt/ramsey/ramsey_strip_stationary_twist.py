"""Toggle reciprocity while keeping the B and N fan images. Swap just the two stationary ground labels on the output; do not reverse rows or change H."""
from ramsey_strip_stationary_fan_extension import B,Q,via,D,H,act,permutations
from ramsey_strip_affine_star_dictionary import fixed
I=list(range(30));r=[H[x] for x in H];p=list(range(6));u,v=fixed;p[u],p[v]=p[v],p[u];K=act(p);assert all(K[H[x]]==H[K[x]] for x in I) and all(K[x]==x for x in (B,Q,29,via));n=0
for p in permutations(range(6)):
    A=act(p);d=[A[x] for x in D]
    if d[B]!=via or [d[x] for x in d]!=I:continue
    twisted=[K[x] for x in d];assert [twisted[x] for x in twisted]==r and twisted[B]==via and twisted[Q]==29
    for dictionary,square in ((d,r),(twisted,I)):
        f=[dictionary[x] for x in H];assert f[B]==29 and f[29]==B and [f[x] for x in f]==square
    n+=1
assert n==2;print('both reciprocal extensions acquire the other endpoint square under stationary-output twist')
