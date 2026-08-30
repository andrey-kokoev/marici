"""Exact universal-R monodromy and reference partial trace for all D(S3) simples."""

import itertools
import json
import sympy as sp


def compose(p,q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out=[0,0,0]
    for i,image in enumerate(p): out[image]=i
    return tuple(out)
def conjugate(g,h): return compose(compose(g,h),inverse(g))
def parity(p): return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1
def cycle_type(p):
    fixed=sum(p[i]==i for i in range(3))
    return "e" if fixed==3 else ("t" if fixed==1 else "c")


def partial_trace_reference(matrix,da,db):
    return sp.Matrix(da,da,lambda i,j:sp.simplify(sum(matrix[i*db+k,j*db+k] for k in range(db))/db))


def main():
    group=list(itertools.permutations(range(3)))
    e,t,c=(0,1,2),(1,0,2),(1,2,0)
    reps={"e":e,"t":t,"c":c}
    classes={name:[g for g in group if cycle_type(g)==name] for name in reps}
    transporters={name:{target:next(q for q in group if conjugate(q,rep)==target) for target in classes[name]} for name,rep in reps.items()}
    sqrt3=sp.sqrt(3); omega=-sp.Rational(1,2)+sp.I*sqrt3/2
    rmat=sp.Matrix([[-sp.Rational(1,2),-sqrt3/2],[sqrt3/2,-sp.Rational(1,2)]])
    smat=sp.diag(1,-1); r=(1,2,0); s=(1,0,2)
    standard={}
    for k in range(3):
        pr,mr=e,sp.eye(2)
        for _ in range(k): pr,mr=compose(r,pr),rmat*mr
        for epsilon in range(2): standard[compose(pr,s if epsilon else e)]=sp.simplify(mr*(smat if epsilon else sp.eye(2)))

    labels=[("A","e","triv",1),("B","e","sign",1),("C","e","std",2),("D","t","plus",3),("E","t","minus",3),("F","c","triv",2),("G","c","omega",2),("H","c","omega2",2)]
    by_name={x[0]:x for x in labels}

    def internal_matrix(label,z):
        _,sector,irrep,_=label
        if sector=="e":
            if irrep=="triv": return sp.Matrix([[1]])
            if irrep=="sign": return sp.Matrix([[parity(z)]])
            return standard[z]
        if sector=="t": return sp.Matrix([[1 if irrep=="plus" or z==e else -1]])
        power={e:0,c:1,compose(c,c):2}[z]
        exponent=power*{"triv":0,"omega":1,"omega2":2}[irrep]%3
        return sp.Matrix([[sp.simplify(omega**exponent)]])

    def representation(label,g,x):
        _,sector,_,dimension=label
        fluxes=classes[sector]; internal_dim=dimension//len(fluxes)
        matrix=sp.zeros(dimension)
        for i,flux_in in enumerate(fluxes):
            flux_out=conjugate(x,flux_in)
            j=fluxes.index(flux_out)
            if g!=flux_out: continue
            qi=transporters[sector][flux_in]; qj=transporters[sector][flux_out]
            z=compose(compose(inverse(qj),x),qi)
            block=internal_matrix(label,z)
            matrix[j*internal_dim:(j+1)*internal_dim,i*internal_dim:(i+1)*internal_dim]=block
        return sp.simplify(matrix)

    def gauge(label,x):
        return sp.simplify(sum((representation(label,g,x) for g in group),sp.zeros(label[3])))

    # Representation sanity: identity and gauge group law.
    for label in labels:
        assert gauge(label,e)==sp.eye(label[3])
        assert all(sp.simplify(gauge(label,x)*gauge(label,y)-gauge(label,compose(x,y)))==sp.zeros(label[3]) for x in group for y in group)

    s_matrix=sp.Matrix([
        [sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)],
        [sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),-sp.Rational(1,2),-sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)],
        [sp.Rational(1,3),sp.Rational(1,3),sp.Rational(2,3),0,0,-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3)],
        [sp.Rational(1,2),-sp.Rational(1,2),0,sp.Rational(1,2),-sp.Rational(1,2),0,0,0],
        [sp.Rational(1,2),-sp.Rational(1,2),0,-sp.Rational(1,2),sp.Rational(1,2),0,0,0],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,sp.Rational(2,3),-sp.Rational(1,3),-sp.Rational(1,3)],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(2,3)],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,-sp.Rational(1,3),sp.Rational(2,3),-sp.Rational(1,3)],
    ])

    scalar_table={}
    all_scalar=True
    for ia,a in enumerate(labels):
        for ib,b in enumerate(labels):
            da,db=a[3],b[3]
            rab=sp.zeros(da*db); r21=sp.zeros(da*db)
            for g in group:
                rab+=sp.kronecker_product(representation(a,g,e),gauge(b,g))
                r21+=sp.kronecker_product(gauge(a,g),representation(b,g,e))
            monodromy=sp.simplify(r21*rab)
            assert sp.simplify(monodromy.H*monodromy)==sp.eye(da*db)
            reduced=partial_trace_reference(monodromy,da,db)
            expected=sp.simplify(6*s_matrix[ia,ib]/(da*db))
            scalar=sp.simplify(reduced-expected*sp.eye(da))==sp.zeros(da)
            all_scalar &= scalar
            scalar_table[a[0]+"|"+b[0]]=str(expected)
    assert all_scalar

    selected={label[0]:(scalar_table[label[0]+"|D"],scalar_table[label[0]+"|F"]) for label in labels}
    result={
        "schema":"marici.s3-universal-R-partial-trace.v1",
        "anyon_dimensions":{x[0]:x[3] for x in labels},
        "all_64_monodromies_unitary":True,
        "all_64_reference_partial_traces_are_scalar_on_target":all_scalar,
        "partial_trace_eigenvalue":"6*S_ab/(d_a*d_b)",
        "selected_D_F_normalized_monodromy_signatures":selected,
        "target_density_matrix_independence":"Tr[rho_a*Tr_b(M_ab)/d_b]=mu_ab_for_every_rho_a",
        "aggregate_gates":{
            "eight_induced_D_S3_representations_constructed":True,
            "gauge_actions_obey_S3_group_law":True,
            "universal_R_monodromies_are_unitary":True,
            "reference_partial_trace_is_scalar_for_every_simple_pair":all_scalar,
            "scalar_matches_normalized_modular_entry":True,
            "unknown_target_internal_state_drops_out":True,
            "reference_mixing_and_controlled_R_remain_apparatus_requirements":True,
        },
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__": main()
