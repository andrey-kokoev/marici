"""Certified two-translate Gram minor in Nima's declared spline convention."""
from fractions import Fraction as F
from math import comb
import json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parents[2] / "nima" / "checkers"))
import preconditioned_spline_weil as n

Z=n.Z
BASE=[F(1),F(-5),F(33,4),F(-5),F(1)]; BASE_M=[2,1,0,-1,-2]
CROSS=[F(1,2),F(-5,2),F(37,8),F(-5),F(37,8),F(-5,2),F(1,2)]; CROSS_M=[3,2,1,0,-1,-2,-3]

def profile(u,a,coeff,ms):
    out=Z
    for c,m in zip(coeff,ms): out=n.add(out,n.scale(c,n.k7_iv(n.add(u,n.scale(F(m),a)))))
    return out

def zero_jet(r,a,coeff,ms):
    if r%2 and r<7 and coeff==list(reversed(coeff)): return Z
    out=Z
    for c,m in zip(coeff,ms): out=n.add(out,n.scale(c,n.k7_deriv_iv(n.scale(F(m),a),r,right=(r==7))))
    return n.scale(F(1,2)**r,out)

def prime(a,coeff,ms,wrong=False):
    out=Z
    for p in n.primes(1024):
        q=p
        while q<=1024:
            w=n.mul(n.log_q(F(p)),n.inv(n.sqrt_q(F(q))))
            out=n.add(out,n.scale(F(2) if wrong else F(-2),n.mul(w,profile(n.log_q(F(q)),a,coeff,ms))))
            q*=p
    return out

def exact_In(a,j,coeff,ms):
    out=Z
    for c,m in zip(coeff,ms): out=n.add(out,n.scale(c,n.integral_shift(m,a,j)))
    return out

def arch_tail(a,coeff,ms,N=3):
    f0=profile(Z,a,coeff,ms); delta=F(1,4); stop=N+16
    dprefix=sum(F(1,j+1)-F(1)/(F(j)+delta) for j in range(N,stop))
    x=F(stop); L=n.log_q((x+1)/(x+delta)); g=F(1)/(x+delta)-F(1)/(x+1)
    gp=-(x+delta)**-2+(x+1)**-2; g3=-F(6)*(x+delta)**-4+F(6)*(x+1)**-4
    sup=n.add(L,(g/2-gp/12,g/2-gp/12)); slo=(sup[0]+g3/F(720),sup[1]+g3/F(720))
    D=(dprefix-sup[1],dprefix-slo[0]); out=n.mul(f0,D)
    for r in range(1,8): out=n.sub(out,n.mul(zero_jet(r,a,coeff,ms),n.sp_bounds(N,r+1,alpha=delta)))
    # Signed atomic eighth-derivative tail, generalized from Nima's baseline checker.
    atom=Z
    for c0,m in zip(coeff,ms):
        for j in range(9):
            x=n.sub((F(2*(j-4)),F(2*(j-4))),n.scale(F(2*m),a))
            if x[1]<=0: continue
            assert x[0]>0
            q=4*N+1
            first=n.scale((F(2,q)**8)*(F(2)**(q*m)),n.exp_half(-q*(j-4)))
            ratio_hi=F(1)/(F(1)+x[0])
            kernel=(first[0],first[1]/(1-ratio_hi))
            weight=c0*F(((-1)**j)*comb(8,j),128)
            atom=n.add(atom,n.scale(weight,kernel))
    return n.sub(out,atom)

def arch(a,coeff,ms):
    f0=profile(Z,a,coeff,ms); finite=Z
    for j in range(3): finite=n.add(finite,n.sub(n.scale(F(1,j+1),f0),exact_In(a,j,coeff,ms)))
    gp=n.add(n.gamma_interval(),(n.log_q(n.pi_interval()[0])[0],n.log_q(n.pi_interval()[1])[1]))
    return n.add(n.scale(F(-1),n.mul(f0,gp)),n.add(finite,arch_tail(a,coeff,ms)))

def energy(a,coeff,ms,wrong=False): return n.add(arch(a,coeff,ms),prime(a,coeff,ms,wrong))
def enc(x): return [str(x[0]),str(x[1])]

def main():
    a=n.scale(F(2),n.log_q(F(2)))
    # Reuse the already certified baseline interval; compute only the new cross cell.
    diagonal=(F(11790450740162717,10**21),F(11906013635010338,10**21)); cross=energy(a,CROSS,CROSS_M)
    determinant=n.sub(n.mul(diagonal,diagonal),n.mul(cross,cross))
    coherent_eigenvalue=n.add(diagonal,cross)
    disagreement_eigenvalue=n.sub(diagonal,cross)
    coherent_packet_energy=n.scale(F(2),coherent_eigenvalue)
    disagreement_packet_energy=n.scale(F(2),disagreement_eigenvalue)
    assert determinant[1] < 0 and disagreement_packet_energy[1] < 0 < coherent_packet_energy[0]
    data={"schema":"marici.grothendieck.two-translate-spline-gram.v1","translation":"4 log 2","diagonal":enc(diagonal),"cross":enc(cross),"determinant":enc(determinant),"coherent_eigenvalue":enc(coherent_eigenvalue),"disagreement_eigenvalue":enc(disagreement_eigenvalue),"coherent_packet_energy":enc(coherent_packet_energy),"disagreement_packet_energy":enc(disagreement_packet_energy),"baseline_regression_execution":"structured_command_execution:e_2648_1788310649689691500_15","claim_boundary":"Declared executable convention; generalized signed atomic archimedean tail; no external source authority."}
    out=pathlib.Path(__file__).parents[1]/"results/two-translate-spline-gram.json";out.write_text(json.dumps(data,indent=2)+"\n")
    print(json.dumps({"diagonal":[float(x) for x in diagonal],"cross":[float(x) for x in cross],"determinant":[float(x) for x in determinant],"coherent_eigenvalue":[float(x) for x in coherent_eigenvalue],"coherent_packet_energy":[float(x) for x in coherent_packet_energy],"disagreement_packet_energy":[float(x) for x in disagreement_packet_energy]}))
if __name__=="__main__": main()
