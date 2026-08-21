"""Blind Gaussian-weight estimate of the top atom multiplicity."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4'];b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4'];mom=json.loads((root/'quarter-point-order-four-interval.json').read_text())['moments_A0_through_A9']
a=[sum(map(float,x))/2 for x in a];b=[sum(map(float,x))/2 for x in b];A0=sum(map(float,mom[0]))/2
def top_node_weight(n):
    A=[[0.0]*n for _ in range(n)];V=[[float(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):A[i][i]=a[i]
    for i in range(n-1):A[i][i+1]=A[i+1][i]=math.sqrt(b[i])
    for _ in range(200):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        if not pairs:break
        p,q=max(pairs,key=lambda z:abs(A[z[0]][z[1]]))
        if abs(A[p][q])<1e-18:break
        phi=.5*math.atan2(2*A[p][q],A[q][q]-A[p][p]);c=math.cos(phi);s=math.sin(phi);app,aqq,apq=A[p][p],A[q][q],A[p][q]
        for k in range(n):
            if k not in (p,q):
                x,y=A[k][p],A[k][q];A[k][p]=A[p][k]=c*x-s*y;A[k][q]=A[q][k]=s*x+c*y
            x,y=V[k][p],V[k][q];V[k][p]=c*x-s*y;V[k][q]=s*x+c*y
        A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[q][q]=s*s*app+2*s*c*apq+c*c*aqq;A[p][q]=A[q][p]=0
    index=max(range(n),key=lambda i:A[i][i]);u=A[index][index];weight=A0*V[0][index]**2
    return u,weight,weight/u
rows=[top_node_weight(n) for n in range(1,6)]
result={'compression_sizes':[1,2,3,4,5],'top_node_u':[x[0] for x in rows],
        'top_quadrature_mass':[x[1] for x in rows],'blind_multiplicity_estimate_mass_over_u':[x[2] for x in rows],
        'fifth_estimate_distance_from_one':abs(rows[-1][2]-1),'numerical_not_interval_certified':True,
        'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-blind-multiplicity.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
