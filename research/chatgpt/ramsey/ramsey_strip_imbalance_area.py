"""Exact Gram nondegeneracy and ordered history area in coefficient space. No numerical eigenvectors or choice of next-cycle tie breaker."""
from ramsey_strip_imbalance_dynamics import run
from ramsey_strip_duality_imbalance import v,dot
ids=(2,3,5);G=[[dot(v[i,0],v[j,0]) for j in ids] for i in ids];a,b,c=G;det=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);assert det==9728
for start in (2,3):
    seq,*_=run(start);coeff=[0]*3;area=[0]*3;pairs=((0,1),(0,2),(1,2));cov=[[0]*3 for _ in range(3)]
    for i,bit in seq:
        u=[0]*3;u[ids.index(i)]=1-2*bit
        area=[z+coeff[j]*u[k]-coeff[k]*u[j] for z,(j,k) in zip(area,pairs)]
        cov=[[cov[j][k]+u[j]*u[k] for k in range(3)] for j in range(3)];coeff=[x+y for x,y in zip(coeff,u)]
    assert coeff==[0]*3 and cov==[[2,0,0],[0,2,0],[0,0,2]]
    print('start',start,'final coefficients',coeff,'ordered area (2^3,2^5,3^5)',area,'unordered covariance',cov)
print('Gram',G,'determinant',det,'eigenvalues 16, 25-sqrt(17), 25+sqrt(17)')
