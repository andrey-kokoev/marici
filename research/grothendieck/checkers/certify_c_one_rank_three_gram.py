"""Directed coarse-tail certificate for the coherent c=1 rank-three Gram matrix."""
from fractions import Fraction as F
import json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent));import interval_undilated_septic_moments as im;import interval_c_one_prime_and_jets as cj
n=im.n;Z=n.Z;N=4;TV=F(5184);delta=F(1,4)
def tail(f0,jets):
 stop=N+16
 dprefix=sum(F(1,k+1)-F(1)/(F(k)+delta) for k in range(N,stop))
 x=F(stop);L=n.log_q((x+1)/(x+delta));g=F(1)/(x+delta)-F(1)/(x+1);gp=-(x+delta)**-2+(x+1)**-2;g3=-F(6)*(x+delta)**-4+F(6)*(x+1)**-4
 sup=n.add(L,(g/2-gp/12,g/2-gp/12));slo=(sup[0]+g3/F(720),sup[1]+g3/F(720));D=(dprefix-sup[1],dprefix-slo[0])
 out=n.mul(f0,D)
 for r in range(1,8):out=n.sub(out,n.mul(jets[r],n.sp_bounds(N,r+1,alpha=delta)))
 e=TV*n.sp_bounds(N,8,alpha=delta)[1]
 return n.add(out,(-e,e))
def iv(x):return (F(x[0]),F(x[1]))
def cell(name,moments,components):
 comp=components[name];f0=iv(comp['f0']);jets={r:iv(comp['jets'][str(r)]) for r in range(1,8)};finite=Z
 for k in range(N):finite=n.add(finite,n.sub(n.scale(F(1,k+1),f0),moments[(name,k)]))
 gp=n.add(n.gamma_interval(),(n.log_q(n.pi_interval()[0])[0],n.log_q(n.pi_interval()[1])[1]))
 arch=n.add(n.scale(F(-1),n.mul(f0,gp)),n.add(finite,tail(f0,jets)))
 return n.add(arch,iv(comp['prime'])),arch
def enc(x):return [str(x[0]),str(x[1])]
def main():
 root=pathlib.Path(__file__).parents[1]/'results'
 md=json.loads((root/'interval-undilated-septic-moments.json').read_text());cd=json.loads((root/'interval-c-one-prime-and-jets.json').read_text())
 moments={(('lag1' if r['profile']=='cross' else r['profile']),r['n']):iv(r['interval']) for r in md['rows']}
 components={(('lag1' if r['profile']=='cross' else r['profile'])):r for r in cd['rows']};vals=[]
 for name in ['baseline','lag1','lag2']:
  total,arch=cell(name,moments,components);vals.append(total)
 d,c1,c2=vals
 minor2=n.sub(n.mul(d,d),n.mul(c1,c1))
 det3=n.add(n.sub(n.sub(n.mul(n.mul(d,d),d),n.scale(F(2),n.mul(d,n.mul(c1,c1)))),n.mul(d,n.mul(c2,c2))),n.scale(F(2),n.mul(n.mul(c1,c1),c2)))
 assert d[0]>0 and minor2[0]>0 and det3[0]>0
 result={'schema':'marici.grothendieck.c-one-rank-three-gram-certificate.v1','split_N':N,'variation':str(TV),'cells':{'diagonal':enc(d),'lag1':enc(c1),'lag2':enc(c2)},'principal_minor_2':enc(minor2),'determinant_3':enc(det3),'passed':True,'claim_boundary':'Declared coherent c=1 executable form; external published-theorem authority remains pending.'}
 out=pathlib.Path(__file__).parents[1]/'results/c-one-rank-three-gram-certificate.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':True,'cells':{k:[float(F(x)) for x in v] for k,v in result['cells'].items()},'minor2_lower':float(minor2[0]),'det3_lower':float(det3[0])}))
if __name__=='__main__':main()
