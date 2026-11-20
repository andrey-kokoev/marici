"""Read the B fan by composing literal opposite-port steps from alternating rows. No Hall pole, chart or half-step input. Compare to the locally allowed moves of the single-row colored seed."""
from itertools import combinations
from ramsey_brnn_seed_swap import seed
rows=('BRNN','BNRN');V=range(1,5);B=1;fs=[]
for w in rows:
    br=[i for i in V if w[i-1] in 'BR'];nn=[i for i in V if w[i-1]=='N'];fs.append({**dict(zip(br,br[::-1])),**dict(zip(nn,nn[::-1]))})
ed=lambda x,y:tuple(sorted((x,y)));E=set(combinations(V,2));blocks=[]
for i,f in enumerate(fs):
    u=f[B];q=fs[1-i][u];v=fs[1-i][B];assert f[u]==B and q==4
    direct=lambda j:seed(f)[frozenset(((u,B),(u,j)))];assert direct(v)==direct(q)=='R'
    blocks.append(frozenset([ed(B,u),ed(u,q)]));print('row',i+1,'outward',B,u,'single-row onward red choices',v,q,'other-row opposite',q)
blocks.append(frozenset(E-set.union(*map(set,blocks))));assert all(len(b)==2 for b in blocks);print('alternating blocks',sorted(sorted(b) for b in blocks))
