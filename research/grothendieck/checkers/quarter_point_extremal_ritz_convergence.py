"""Numerical regression of nested extremal Ritz nodes."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4'];b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4']
a=[sum(map(float,x))/2 for x in a];b=[sum(map(float,x))/2 for x in b]
def eigenvalues(size):
    A=[[0.0]*size for _ in range(size)]
    for i in range(size):A[i][i]=a[i]
    for i in range(size-1):A[i][i+1]=A[i+1][i]=math.sqrt(b[i])
    for _ in range(100):
        pairs=[(i,j) for i in range(size) for j in range(i+1,size)]
        if not pairs:break
        p,q=max(pairs,key=lambda z:abs(A[z[0]][z[1]]))
        if abs(A[p][q])<1e-18:break
        phi=.5*math.atan2(2*A[p][q],A[q][q]-A[p][p]);c=math.cos(phi);s=math.sin(phi);app,aqq,apq=A[p][p],A[q][q],A[p][q]
        for k in range(size):
            if k not in (p,q):
                x,y=A[k][p],A[k][q];A[k][p]=A[p][k]=c*x-s*y;A[k][q]=A[q][k]=s*x+c*y
        A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[q][q]=s*s*app+2*s*c*apq+c*c*aqq;A[p][q]=A[q][p]=0
    return sorted(A[i][i] for i in range(size))
max_nodes=[max(eigenvalues(n)) for n in range(1,6)];ordinate_bounds=[math.sqrt(1/u-.25) for u in max_nodes]
assert all(max_nodes[i]<max_nodes[i+1] for i in range(4));assert all(ordinate_bounds[i]>ordinate_bounds[i+1] for i in range(4))
result={'compression_sizes':[1,2,3,4,5],'largest_u_ritz_nodes':max_nodes,'transformed_ordinate_upper_estimates':ordinate_bounds,'largest_nodes_strictly_increase':True,'ordinate_estimates_strictly_decrease':True,'numerical_eigensolve_interval_certified':False,'measure_interpretation_conditional':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-extremal-ritz-convergence.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
