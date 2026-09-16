"""Certify canonical isometries between nested finite Xi Gram features.
Run with PYTHONPATH="$PWD/research/benincasa/.tmp_flint".
"""
import json
from pathlib import Path
from flint import acb,acb_series,acb_mat,arb,ctx
ctx.dps=180;I=acb(0,1);PI=acb(arb.pi())
P4=[('0','1'),('5','1'),('10','1'),('15','1')]
P12=P4+[('2','2'),('8','3'),('14','2'),('20','4'),('5','0.25'),('12','0.5'),('20','0.75'),('28','1')]
P20=P12+[('14.134725','0.05'),('14.134725','0.2'),('21.022040','0.05'),('21.022040','0.2'),('25.010858','0.05'),('25.010858','0.2'),('30.424876','0.05'),('30.424876','0.2')]
def ep(z):
 s=acb_series([acb('.5')+I*z,I],3);x=acb('.5')*s*(s-1)*((-s/2)*PI.log()).exp()*(s/2).gamma()*s.zeta();return x[0]+I*x[1],x[0]-I*x[1]
def ker(z,w):
 a,b=ep(z);c,d=ep(w);return (a*c.conjugate()-b*d.conjugate())/(2*PI*I*(w.conjugate()-z))
def feature(raw):
 p=[acb(arb(x),arb(y)) for x,y in raw];n=len(p);K=[[acb(0) for _ in p] for _ in p]
 for i in range(n):
  for j in range(n): K[i][j]=(ker(p[i],p[j])+ker(p[j],p[i]).conjugate())/2
 L=[[acb(int(i==j)) for j in range(n)] for i in range(n)];D=[]
 for j in range(n):
  d=(K[j][j]-sum((L[j][q]*D[q]*L[j][q].conjugate() for q in range(j)),acb(0))).real;assert d>0;D.append(acb(d))
  for i in range(j+1,n): L[i][j]=(K[i][j]-sum((L[i][q]*D[q]*L[j][q].conjugate() for q in range(j)),acb(0)))/D[j]
 return acb_mat([[D[q].sqrt()*L[j][q].conjugate() for j in range(n)] for q in range(n)])
def zero_matrix(M): return all(M[i,j].contains(0) for i in range(M.nrows()) for j in range(M.ncols()))
def iso(small,big):
 m=small.ncols();sub=acb_mat([[big[i,j] for j in range(m)] for i in range(big.nrows())]);return sub*small.inv(),sub
def compare(small,big):
 m=small.ncols();U,sub=iso(small,big);ident=acb_mat(m,m)
 for i in range(m): ident[i,i]=1
 return {'source_dimension':m,'target_dimension':big.nrows(),'intertwining_certified':zero_matrix(U*small-sub),'isometry_certified':zero_matrix(U.transpose().conjugate()*U-ident)}
F4=feature(P4);F12=feature(P12);F20=feature(P20)
U412,_=iso(F4,F12);U1220,_=iso(F12,F20);U420,_=iso(F4,F20)
out={'nested_comparisons':[compare(F4,F12),compare(F12,F20),compare(F4,F20)],'cocycle_4_12_20_certified':zero_matrix(U1220*U412-U420),'interpretation':'U F_small equals the restricted columns of F_big, U^*U=I, and nested U maps compose strictly','arithmetic':'Arb complex balls, 180 decimal digits','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'arb-certified-nested-xi-gram-feature-isometries.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
