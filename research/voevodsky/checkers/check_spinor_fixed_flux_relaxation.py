"""Joint charged-spinor/electric relaxation with exact relative face flux.

Exact symmetric-two-copy positive-operator certificate gives a global lower
bound over all pure spinors; an explicit source-derived one-axis state gives
an upper bound. No claim that this variational state is the exact minimizer.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import combinations_with_replacement
import json
from check_spinor_matter_link_adapter import decode
from check_electron_tetrahedral_spinor import D, G0, G1, gc, gm, ga, gs, gt, gmm, ident, sm, ma, pos

BASE=Path(__file__).resolve().parents[1]


def act(a,v): return tuple(gt(gm(x,y) for x,y in zip(row,v)) for row in a)
def inner(v,w,metric):return gt(gs(n,gm(gc(x),y)) for n,x,y in zip(metric,v,w))


def positive_definite(matrix):
    size=len(matrix)
    l=[[G0 for _ in range(size)] for _ in range(size)]
    pivots=[]
    for i in range(size):
        pivot=matrix[i][i]
        for k in range(i):pivot=ga(pivot,gs(-pivots[k],gm(l[i][k],gc(l[i][k]))))
        assert pivot[1]==0
        if not pos(pivot[0]):return False
        pivots.append(pivot[0])
        for j in range(i+1,size):
            residual=matrix[j][i]
            for k in range(i):residual=ga(residual,gs(-pivots[k],gm(l[j][k],gc(l[i][k]))))
            l[j][i]=gs(D(1)/pivot[0],residual)
    return True


def symmetric_operator(k,metric,c):
    pairs=list(combinations_with_replacement(range(4),2))
    def entry(i,j,p,q):
        value=G0
        if j==q:value=ga(value,gs(F(1,2),k[i][p]))
        if i==p:value=ga(value,gs(F(1,2),k[j][q]))
        if i==j==p==q:value=ga(value,(c,F(0)))
        return value
    operator=[]
    for i,j in pairs:
        row=[]
        for p,q in pairs:
            value=entry(i,j,p,q)
            if p!=q:value=ga(value,entry(i,j,q,p))
            row.append(value)
        operator.append(row)
    tensor_metric=[metric[i]*metric[j]*(1 if i==j else 2) for i,j in pairs]
    assert all(gs(tensor_metric[i],operator[i][j])==gc(gs(tensor_metric[j],operator[j][i]))
               for i in range(10) for j in range(10))
    def shifted(energy):
        return [[gs(tensor_metric[i],ga(operator[i][j],(-energy,F(0)) if i==j else G0))
                 for j in range(10)] for i in range(10)]
    return pairs,operator,tensor_metric,shifted


def main():
    path=BASE/'results/electron_tetrahedral_spinor_store.json'
    raw=path.read_bytes();store=json.loads(raw)
    face=[tuple(tuple(decode(z) for z in row) for row in p) for p in store['face_projectors']]
    local=[tuple(p[i][0] for i in range(2)) for p in face]
    metric=[gt(gm(gc(z),z) for z in v)[0] for v in local]
    v=tuple(tuple(local[j][i%2] if i//2==j else G0 for j in range(4)) for i in range(8))
    decoder=tuple(tuple(gs(D(1)/n,gc(v[i][j])) for i in range(8)) for j,n in enumerate(metric))
    n=tuple(tuple(gs(F(1,2),gmm(face[i//2],face[j//2])[i%2][j%2]) for j in range(8)) for i in range(8))
    reduced_n=gmm(decoder,gmm(n,v))
    k=sm(2,ma(ident(4),sm(-1,reduced_n)))
    assert gmm(k,k)==sm(2,k)
    beta,eta=F(3,5),F(1,5)
    c=beta/10
    # C*A=0 makes relative phases pure gauge. Minimize E exactly:
    # L=5I-ones, phi=-(rho+1)/5, energy=beta*(1+sum rho^2)/10.
    linv=[[F(i==j,5)+F(1,5) for j in range(4)] for i in range(4)]
    grounded=[[5*F(i==j)-1 for j in range(4)] for i in range(4)]
    assert [[sum(grounded[i][k]*linv[k][j] for k in range(4)) for j in range(4)] for i in range(4)]==[[F(i==j) for j in range(4)] for i in range(4)]
    # Build the explicit source two-direction subspace at each face.
    lo_r,hi_r=F(0),F(1)
    def polynomial(r):return 3*r**4+6*c*r**3-2*c*r-3
    for _ in range(90):
        mid=(lo_r+hi_r)/2
        if polynomial(mid)<0:lo_r=mid
        else:hi_r=mid
    r=(lo_r+hi_r)/2
    t=r*r/(1+r*r)
    assert F(1,4)<t<F(1,2)
    upper=(r-1)**2/(1+r*r)+c*(1+(r**4+F(1,3))/(1+r*r)**2)+eta/2
    coherent=2*beta/15+eta/2
    assert upper<coherent
    for address in range(4):
        e=tuple(G1 if i==address else G0 for i in range(4))
        w=act(ma(ident(4),sm(-1,k)),e)
        assert w[address]==G0
        assert inner(e,w,metric)==G0
        assert inner(w,w,metric)==(metric[address],F(0))
        assert act(k,e)==tuple(ga(x,gs(-1,y)) for x,y in zip(e,w))
        assert act(k,w)==tuple(ga(gs(-1,x),y) for x,y in zip(e,w))
        for i in range(4):
            if i!=address:assert metric[i]*gm(gc(w[i]),w[i])[0]==metric[address]/3
        # No radicals needed: use unnormalized r*e+w and its exact metric.
        trial=tuple(ga(gs(r,x),y) for x,y in zip(e,w))
        norm=inner(trial,trial,metric)[0]
        density=[m*gm(gc(z),z)[0]/norm for m,z in zip(metric,trial)]
        assert sum(density)==1 and density[address]==D(t)
        assert all(density[i]==D((1-t)/3) for i in range(4) if i!=address)
        kinetic=inner(trial,act(k,trial),metric)[0]/norm
        assert kinetic==D((r-1)**2/(1+r*r))
        phi=[-(x+1)/5 for x in density]
        edges=[(i,j) for i in range(4) for j in range(i+1,4)]+[(4,i) for i in range(4)]
        fields=[phi[j]-phi[i] for i,j in edges[:6]]+phi
        divergence=[D() for _ in range(5)]
        for (i,j),field in zip(edges,fields):
            divergence[i]-=field;divergence[j]+=field
        assert divergence==[-x for x in density]+[D(1)]
        assert sum(x*x for x in fields)==(1+sum(x*x for x in density))/5
        assert kinetic+beta*sum(x*x for x in fields)/2+eta/2==D(upper)
    # The quartic functional is the expectation of this symmetric operator
    # on a tensor-square pure state. Its unrestricted symmetric ground is a
    # rigorous lower bound, even if the eigenvector is not a product state.
    pairs,operator,tmetric,shifted=symmetric_operator(k,metric,c)
    lo,hi=F(0),c/3
    assert positive_definite(shifted(lo))
    assert not positive_definite(shifted(hi))
    for _ in range(40):
        mid=(lo+hi)/2
        if positive_definite(shifted(mid)):lo=mid
        else:hi=mid
    assert positive_definite(shifted(lo))
    lower=c+eta/2+lo
    assert beta/8+eta/2<lower<upper<coherent
    # Verify the symmetric expectation formula on independent exact states.
    samples=((G1,G0,G0,G0),(G1,G1,G1,G1),((F(1,3),F(1,5)),(F(-2,7),F(1,4)),(F(3,8),F(-1,6)),(F(1,2),F(2,9))))
    for a in samples:
        norm=inner(a,a,metric)[0]
        tensor=tuple(gm(a[i],a[j]) for i,j in pairs)
        actual=inner(tensor,act(operator,tensor),tmetric)[0]/(norm*norm)
        kinetic=inner(a,act(k,a),metric)[0]/norm
        density=[m*gm(gc(z),z)[0]/norm for m,z in zip(metric,a)]
        assert actual==kinetic+c*sum(x*x for x in density)
    report={
        'verification_passed':True,'source_sha256':sha256(raw).hexdigest(),
        'constraint':'C*A=0 mod 2*pi; source Wilson flux retained up to gauge',
        'eliminated_electric_energy':'beta*(1+sum_i rho_i^2)/10+eta/2',
        'full_relaxed_functional':'<psi,K_e psi>+beta*(1+sum_i |psi_i|^4)/10+eta/2, norm psi=1',
        'fixture':{'beta':str(beta),'eta':str(eta)},
        'global_energy_interval':[str(lower),str(upper)],
        'global_energy_interval_decimal':[float(lower),float(upper)],
        'lower_certificate':'Exact weighted complex LDL positivity on Sym^2(C^4); tensor-square expectation identity checked.',
        'upper_certificate':'Four source-equivalent one-axis trial states with full electric flux retained.',
        'coherent_source_energy':str(coherent),
        'coherent_source_energy_decimal':float(coherent),
        'variational_high_face_density':float(t),
        'variational_other_face_density':float((1-t)/3),
        'variational_dark_fraction':float((r-1)**2/(2*(1+r*r))),
        'pure_coherent_state_is_global_minimum':False,
        'exact_global_minimizer_identified':False,
        'elementary_with_one_unit_occupation_interval':[float(1+lower),float(1+upper)],
        'same_exterior_sector_corrections':{'proton':str(beta/24+eta/2),'neutral_belt':'0'},
        'scope':'Global energy bounds for classical pure spinor amplitudes with hard source flux, not a quantum mixed-state or nuclear binding calculation.',
        'next_gate':'Determine the global minimizing state and spin transport after density deformation; construct the flux-sector implementation before using this energy as a particle rest gap.',
    }
    out=BASE/'results/spinor_fixed_flux_relaxation.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
