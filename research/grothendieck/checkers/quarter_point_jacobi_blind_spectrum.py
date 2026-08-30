"""Dependency-free numerical spectrum of the source-derived Jacobi compression."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
diag=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4']
off=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4']
diag=[sum(map(float,x))/2 for x in diag];off=[sum(map(float,x))/2 for x in off]
size=len(diag);matrix=[[0.0]*size for _ in range(size)]
for i,x in enumerate(diag):matrix[i][i]=x
for i,x in enumerate(off):matrix[i][i+1]=matrix[i+1][i]=math.sqrt(x)
for _ in range(100):
    p,q=max(((i,j) for i in range(size) for j in range(i+1,size)),key=lambda z:abs(matrix[z[0]][z[1]]))
    if abs(matrix[p][q])<1e-18:break
    phi=.5*math.atan2(2*matrix[p][q],matrix[q][q]-matrix[p][p]);c=math.cos(phi);s=math.sin(phi)
    app,aqq,apq=matrix[p][p],matrix[q][q],matrix[p][q]
    for k in range(size):
        if k not in (p,q):
            akp,akq=matrix[k][p],matrix[k][q]
            matrix[k][p]=matrix[p][k]=c*akp-s*akq;matrix[k][q]=matrix[q][k]=s*akp+c*akq
    matrix[p][p]=c*c*app-2*s*c*apq+s*s*aqq
    matrix[q][q]=s*s*app+2*s*c*apq+c*c*aqq;matrix[p][q]=matrix[q][p]=0.0
nodes=sorted(matrix[i][i] for i in range(size))
ordinates=[math.sqrt(1/u-.25) for u in reversed(nodes)]
assert all(0<u<4 for u in nodes)
result={'quadrature_nodes_u':nodes,'blind_ordinate_estimates':ordinates,
        'zero_locations_used_in_construction':False,'numerical_diagonalization_interval_certified':False,
        'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-jacobi-blind-spectrum.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
