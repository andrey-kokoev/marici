"""Exact rational verifier for finite physical common-edge defect certificates."""
import itertools,json,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def mat(x):return [[F(v) for v in r] for r in x]
def add(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def det(a):
 n=len(a)
 if n==0:return F(1)
 return sum(((-1)**j)*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))
def hermitian(a):return all(a[i][j]==a[j][i] for i in range(len(a)) for j in range(len(a)))
def psd(a):
 n=len(a)
 return hermitian(a) and all(det([[a[i][j] for j in idx] for i in idx])>=0 for k in range(1,n+1) for idx in itertools.combinations(range(n),k))
def verify(d):
 GT,G0,Dp,B=map(mat,(d['G_T'],d['G_0'],d['D_plus'],d['graph_control_B']));eps=F(d['epsilon']);C=sub(GT,Dp);st=add(C,scale(eps,B));D=sub(GT,G0)
 checks={'dimensions_match':len({len(GT),len(G0),len(Dp),len(B),len(d['basis'])})==1,'G_T_positive':psd(GT),'G_0_positive':psd(G0),'D_plus_positive':psd(Dp),'graph_control_positive':psd(B),'alignment_consistent':hermitian(D),'stabilized_common_remainder_positive':psd(st),'epsilon_nonnegative':eps>=0}
 return {'schema':'marici.voevodsky.physical-common-edge-defect-certificate-check.v1','regulator':d['regulator'],'epsilon':str(eps),'checks':checks,'passed':all(checks.values()),'forced_common_remainder':[[str(x) for x in r] for r in C]}
def main():
 p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'fixtures'/'physical-common-edge-defect-example.json';d=json.loads(p.read_text());out=verify(d);target=ROOT/'results'/'physical-common-edge-defect-certificate.json';target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
