"""Exact finite graph/Fourier source packet; no theta or amplituhedron identification."""
import json
from pathlib import Path
import sympy as s


def eq(a,b):
    return all(s.simplify(x)==0 for x in a-b)


def main():
    n=4
    I=s.eye(n)
    S=s.zeros(n)
    for j in range(n):
        S[(j+1)%n,j]=1
    # Oriented edges e_j : j -> j+1; B is incidence, not a fitted kernel.
    B=S-I
    Z=s.Matrix([[1,0,0,0]])
    O=B.col_join(Z)
    select=s.zeros(n,n+1)
    for i,j in enumerate((0,1,2,4)):
        select[i,j]=1
    R=(select*O).inv()*select
    F=s.Matrix(n,n,lambda j,k:s.I**(-j*k)/2)
    P=s.Matrix(n,n,lambda i,j:int(i==(-j)%n))
    # Reflection sends the oriented edge j -> j+1 to -e_(-j-1).
    D=-S.inv()*P
    frames={}
    recovery={}
    for polarity in (1,-1):
        for phase in range(4):
            A=s.diag(F**(polarity*phase),s.ones(1))
            frames[polarity,phase]=A*O
            recovery[polarity,phase]=R*A.inv()
    checks={
        'incidence_cycle_kernel':B.rank()==3 and eq(B*s.ones(n,1),s.zeros(n,1)),
        'history_plus_cycle_recovers_source':eq(R*O,I),
        'fourier_fourth_power':eq(F**4,I),
        'fourier_square_is_reflection':eq(F**2,P),
        'source_reflection_involutive':eq(D*D,I),
        'source_polarity_reverses_successor':eq(D*S,S.inv()*D),
        'source_reflection_intertwines_incidence':eq(B*D,P*B),
        'all_eight_chart_recoveries':all(eq(recovery[key]*frames[key],I) for key in frames),
    }
    seam={}
    for polarity in (1,-1):
        U=s.diag(F**polarity,s.ones(1))
        seam[polarity]=O*S**polarity*recovery[polarity,3]
        checks['chart_steps_'+str(polarity)]=all(
            eq(U*frames[polarity,j],frames[polarity,j+1]) for j in range(3))
        checks['seam_source_naturality_'+str(polarity)]=eq(
            seam[polarity]*frames[polarity,3],O*S**polarity)
        checks['full_turn_is_successor_'+str(polarity)]=eq(
            seam[polarity]*U**3*O,O*S**polarity)
        checks['seam_not_identity_closure_'+str(polarity)]=not eq(O*S**polarity,O)
    # Anti-linear polarity map on each image: y -> L_j conjugate(y).
    real_maps={j:frames[-1,j]*D*s.conjugate(recovery[1,j]) for j in range(4)}
    checks['all_polarity_squares']=all(eq(
        real_maps[j]*s.conjugate(frames[1,j]),frames[-1,j]*D) for j in range(4))
    checks['mixed_polarity_seam']=eq(
        real_maps[0]*s.conjugate(seam[1]*frames[1,3]),
        seam[-1]*real_maps[3]*s.conjugate(frames[1,3]))
    # Drop only the cycle port. Every Fourier history still kills this source.
    h=s.ones(n,1)
    checks['all_history_charts_miss_cycle']=all(eq(
        frames[key][:4,:]*h,s.zeros(n,1)) for key in frames)
    checks['retained_cycle_detects_hostile']=all(frames[key][4,:].dot(h)==1 for key in frames)
    # The seam induces a determinant map on the four-dimensional image,
    # never the determinant of its rank-four five-dimensional extension.
    reduced=R*seam[1]*frames[1,3]
    K=reduced-I
    r=s.simplify(-s.trace(K)+s.trace(K*K)/2)
    checks['image_seam_is_source_translation']=eq(reduced,S)
    checks['ambient_seam_singular_but_image_seam_unit']=(seam[1].det()==0 and reduced.det()==-1)
    checks['seam_det3_exact']=(r==6 and reduced.det()==-1)
    # A single step of ordinary Fourier closure would instead return O.
    naive=s.diag(F,s.ones(1))
    checks['naive_wrap_has_nonzero_source_residual']=not eq(naive*frames[1,3],O*S)
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.two-polarity-four-chart-cycle-seam.v1',
        'strength':'finite_graph_source_realization',
        'source':'oriented cycle on four labelled vertices and edges',
        'checks':checks,
        'ranks':{'history':B.rank(),'joint':O.rank(),'ambient_seam':seam[1].rank()},
        'cycle_hostile':[str(x) for x in h],
        'image_seam_determinant':str(reduced.det()),
        'image_seam_det3':{'prefactor':'-1','exponent':str(r)},
        'unsupported':['theta source comparison','amplituhedron canonical-form comparison',
                       'Euler endpoint trace identities','archimedean sewing','completion',
                       'interpretation of the earlier -4/5 residual'],
    }
    out=Path(__file__).resolve().parents[1]/'results/two-polarity-four-chart-cycle-seam.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
