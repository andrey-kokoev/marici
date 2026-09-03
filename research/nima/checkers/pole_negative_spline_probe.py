"""Exploratory prime-orbit shift signatures; not interval certificates."""
import math
S=(4*math.sinh(.25))**4;L=math.log(2);c=(3/S,-2*math.sqrt(2)/S)
def k(x):return sum((-1)**j*math.comb(8,j)/math.factorial(7)*max(0.,x+4-j)**7 for j in range(9))
def signatures(y):
 ys=(0.,y)
 def h(x):return sum(c[i]*c[j]*k(x+ys[i]-ys[j]) for i in range(2) for j in range(2))
 limit=int(math.exp(4+y));out={}
 for p in range(2,limit+1):
  if all(p%d for d in range(2,int(p**.5)+1)):
   n=p;v=0.;powers=[]
   while n<=limit:
    term=-2*math.log(p)/math.sqrt(n)*h(math.log(n));v+=term;powers.append((n,term));n*=p
   out[p]=(v,powers)
 return out
D=1e-4;m=signatures(L-D);z=signatures(L);p=signatures(L+D)
rows=[]
for prime in z:
 der=(p[prime][0]-m[prime][0])/(2*D);rows.append((abs(der),prime,der,z[prime][0],z[prime][1]))
rows.sort(reverse=True)
print({'delta':D,'total_prime_derivative':sum(r[2] for r in rows),'ranked_prime_orbits':rows,'p2_deleted_completed_derivative':-6-8.09727156129103+sum(r[2] for r in rows if r[1]!=2),'status':'exploratory_not_certified'})
