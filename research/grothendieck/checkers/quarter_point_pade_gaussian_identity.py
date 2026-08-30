"""Numerical regression: fifth Jacobi quadrature matches moments through A9."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4'];b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4'];mom=json.loads((root/'quarter-point-order-four-interval.json').read_text())['moments_A0_through_A9']
a=[sum(map(float,x))/2 for x in a];b=[sum(map(float,x))/2 for x in b];mom=[sum(map(float,x))/2 for x in mom];n=5
A=[[0.0]*n for _ in range(n)];V=[[float(i==j) for j in range(n)] for i in range(n)]
for i in range(n):A[i][i]=a[i]
for i,x in enumerate(b):A[i][i+1]=A[i+1][i]=math.sqrt(x)
for _ in range(200):
    p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda z:abs(A[z[0]][z[1]]))
    if abs(A[p][q])<1e-18:break
    phi=.5*math.atan2(2*A[p][q],A[q][q]-A[p][p]);c=math.cos(phi);s=math.sin(phi);app,aqq,apq=A[p][p],A[q][q],A[p][q]
    for k in range(n):
        if k not in (p,q):
            x,y=A[k][p],A[k][q];A[k][p]=A[p][k]=c*x-s*y;A[k][q]=A[q][k]=s*x+c*y
        x,y=V[k][p],V[k][q];V[k][p]=c*x-s*y;V[k][q]=s*x+c*y
    A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[q][q]=s*s*app+2*s*c*apq+c*c*aqq;A[p][q]=A[q][p]=0
nodes=[A[i][i] for i in range(n)];weights=[mom[0]*V[0][i]**2 for i in range(n)]
reconstructed=[sum(w*u**k for w,u in zip(weights,nodes)) for k in range(10)]
relative=[abs(x-y)/abs(y) for x,y in zip(reconstructed,mom)]
assert max(relative)<3e-15
poles_h=sorted(-1/u for u in nodes)
result={'quadrature_nodes_u':nodes,'quadrature_weights':weights,'reconstructed_A0_through_A9':reconstructed,'relative_moment_residuals':relative,'maximum_relative_residual':max(relative),'pade_poles_in_h':poles_h,'gaussian_degree_nine_matching_passed':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-pade-gaussian-identity.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
