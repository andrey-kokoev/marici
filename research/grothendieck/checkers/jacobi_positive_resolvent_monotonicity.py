"""Numerical regression of nested positive-axis Jacobi resolvents."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4'];b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4'];m=json.loads((root/'quarter-point-order-four-interval.json').read_text())['moments_A0_through_A9']
a=[sum(map(float,x))/2 for x in a];b=[sum(map(float,x))/2 for x in b];A0=sum(map(float,m[0]))/2
def solve(M,y):
    n=len(y)
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(M[i][k]));M[k],M[p]=M[p],M[k];y[k],y[p]=y[p],y[k]
        for i in range(k+1,n):
            f=M[i][k]/M[k][k]
            for j in range(k,n):M[i][j]-=f*M[k][j]
            y[i]-=f*y[k]
    x=[0.0]*n
    for i in range(n-1,-1,-1):x[i]=(y[i]-sum(M[i][j]*x[j] for j in range(i+1,n)))/M[i][i]
    return x
def resolvent(n,h):
    M=[[float(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):M[i][i]+=h*a[i]
    for i in range(n-1):M[i][i+1]=M[i+1][i]=h*math.sqrt(b[i])
    return A0*solve(M,[1.0]+[0.0]*(n-1))[0]
heights=[1.0,10.0,100.0,1000.0]
values={str(h):[resolvent(n,h) for n in range(1,6)] for h in heights}
assert all(all(row[i]<=row[i+1] for i in range(4)) and row[-1]<=A0 for row in values.values())
result={'positive_h_values':heights,'resolvents_by_size':values,'nested_resolvents_nondecreasing':True,'uniform_upper_bound_A0':A0,'numerical_regression_interval_certified':False,'all_order_convergence_conditional_on_continued_positive_corners':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'jacobi-positive-resolvent-monotonicity.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
