"""Exhaustive local identities on the six-vertex cross-panel diagram."""
from itertools import combinations
from ramsey_point_panel_basis import T,bits
# Positions u,v,U,V,X,Y, where U,V are extended labels and X,Y the ef twins.
E=[(0,1),(0,3),(1,2),(2,3),(0,4),(0,5),(1,4),(1,5)]
for p in ['ac','bd','ad','bc']:
    pool=[i for i,t in enumerate(T) if not set(t)&set(p)];vertices=pool[:6];diag=len(pool)==7
    assert set(e for e in combinations(pool,2) if e in bits)=={(vertices[i],vertices[j]) for i,j in E}
    checked=0
    for mask in range(256):
        uv,uV,vU,UV,uX,uY,vX,vY=[bool(mask>>j&1) for j in range(8)]
        both_touch=(uX or uY) and (vX or vY);covered=(uX or vX) and (uY or vY)
        if not diag and not both_touch:continue # guaranteed by the two diagonal panels jointly
        pred=(UV and both_touch and (covered or uv or (uV and vU))) if diag else (covered or uv or uV or vU or UV)
        edges=[(vertices[i],vertices[j]) for j0,(i,j) in enumerate(E) if mask>>j0&1]
        actual=all(any(i in U and j in U for i,j in edges) for U in combinations(pool,5));assert pred==actual;checked+=1
    print(p,'diagonal' if diag else 'off-diagonal','local patterns verified',checked)
