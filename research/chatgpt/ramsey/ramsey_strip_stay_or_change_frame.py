"""Hold directed boundary map fixed; compare retaining versus changing the active ten-cycle. Construct both from local cycle orientation and unique spokes, not square tests."""
from ramsey_strip_local_reframe_extension import C,S,N,r,layers
maps=[]
for name,vertices in [('stay',set(C)),('change',S)]:
    Q=[29,7]
    while len(Q)<10:
        x,=(N[Q[-1]]&vertices)-{Q[-2]};Q.append(x)
    F={a:b for L,K in zip(layers(C),layers(Q)) for a,b in zip(L,K)};assert all({F[y] for y in N[x]}==N[F[x]] for x in range(30));maps.append(F)
    assert Q[2]!=Q[0] and Q[2] in N[Q[1]]
    print(name,'first three directed images',Q[:3],'square identity',all(F[F[x]]==x for x in range(30)),'square row swap',all(F[F[x]]==r[x] for x in range(30)))
a,b=maps;K={a[x]:b[x] for x in range(30)};assert K[29]==29 and K[7]==7
assert all(K[K[x]]==x for x in range(30));print('difference involution fixes directed exit flag and swaps its other neighbors',[(v,K[v]) for v in sorted(N[7]-{29})])
