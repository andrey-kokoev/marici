"""Exact local gauge-hopping and transverse-vacuum reduction test.
Rational graph/Hodge arithmetic, certified exponential intervals, and explicit
finite-plaquette Schur bounds. No truncated canonical commutator is used.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(a):return [list(c) for c in zip(*a)]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[c*x for x in row] for row in a]
def norm(v):return sum(x*x for x in v)


def inverse(a):
    n=len(a);rows=[list(r)+i for r,i in zip(a,eye(n))]
    for k in range(n):
        pivot=next(i for i in range(k,n) if rows[i][k])
        rows[k],rows[pivot]=rows[pivot],rows[k]
        denominator=rows[k][k];rows[k]=[x/denominator for x in rows[k]]
        for i in range(n):
            if i!=k:
                c=rows[i][k];rows[i]=[x-c*y for x,y in zip(rows[i],rows[k])]
    out=[row[n:] for row in rows]
    assert mm(a,out)==eye(n)
    return out


def graph(edges):
    b=[[F((v==head)-(v==tail)) for tail,head in edges] for v in range(4)]
    l=mm(b,transpose(b));constant=[[F(1,4)]*4 for _ in range(4)]
    green=add(inverse(add(l,constant)),scale(-1,constant))
    longitudinal=mm(mm(transpose(b),green),b)
    transverse=add(eye(len(edges)),scale(-1,longitudinal))
    assert mm(longitudinal,longitudinal)==longitudinal
    assert mm(transverse,transverse)==transverse
    assert mm(b,transverse)==[[F(0)]*len(edges) for _ in range(4)]
    return b,green,longitudinal,transverse


def exp_negative(x):
    assert 0<=x<=1
    total=F(1);term=F(1)
    for k in range(1,41):
        term*=x/k
        total+=term if k%2==0 else -term
    lower,upper=total-term,total
    assert 0<lower<=upper<=1
    return lower,upper


def interval(v):return dict(exact=[str(x) for x in v],decimal=[float(x) for x in v])


def hopping_word_checks(edges):
    # Laurent polynomials in z=exp(i q a/2), with z^*=z^-1.
    def plus(a,b):
        out=dict(a)
        for k,v in b.items():out[k]=out.get(k,F(0))+v
        return {k:v for k,v in out.items() if v}
    def times(a,b):
        out={}
        for k,v in a.items():
            for l,w in b.items():out=plus(out,{k+l:v*w})
        return out
    def multiply(a,b):
        out=[[{} for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):out[i][j]=plus(out[i][j],times(a[i][k],b[k][j]))
        return out
    ident=[[{0:F(1)} if i==j else {} for j in range(4)] for i in range(4)]
    total=[[{} for _ in range(4)] for _ in range(4)]
    word=ident
    for tail,head in edges:
        r=[[dict(x) for x in row] for row in ident]
        r[tail][tail]={};r[head][head]={}
        r[head][tail]={1:F(1)};r[tail][head]={-1:F(1)}
        sharp=[[{-k:v for k,v in r[j][i].items()} for j in range(4)] for i in range(4)]
        assert sharp==r and multiply(r,r)==ident
        d=[{} for _ in range(4)];d[tail]={1:F(-1)};d[head]={0:F(1)}
        for i in range(4):
            for j in range(4):
                defect=times({-k:v for k,v in d[i].items()},d[j])
                expected=plus(ident[i][j],{k:-v for k,v in r[i][j].items()})
                assert defect==expected
                total[i][j]=plus(total[i][j],defect)
        word=multiply(r,word)
    assert word[0][0]=={4:F(1)} and all(not word[i][0] for i in (1,2,3))
    assert all(total[i][i]=={0:F(2)} for i in range(4))
    return dict(local_dressed_swaps_are_self_adjoint_involutions=True,
                kinetic_is_sum_of_positive_defects=True,closed_path_retains_weyl_power=4,
                diagonal_kinetic_term=2)


def main():
    edges=[(0,1),(1,2),(2,3),(3,0)]
    word_checks=hopping_word_checks(edges)
    b,green,pg,pt=graph(edges)
    u=[F(1,2)]*4
    assert pt==[[F(1,4)]*4 for _ in range(4)] and norm(u)==1
    curl=[[F(1)]*4]
    assert mv(curl,u)==[F(2)]
    assert mm(b,transpose(curl))==[[F(0)] for _ in range(4)]
    charges=[[F(v==x)-F(v==0) for v in range(4)] for x in range(4)]
    fields=[mv(transpose(b),mv(green,rho)) for rho in charges]
    electric=[norm(e)/2 for e in fields]
    assert electric==[F(0),F(3,8),F(1,2),F(3,8)]
    for k,(tail,head) in enumerate(edges):
        j=[F(i==k) for i in range(4)]
        change=[x-y for x,y in zip(charges[head],charges[tail])]
        assert mv(b,j)==change
        assert mv(pg,j)==[x-y for x,y in zip(fields[head],fields[tail])]
        assert mv(pt,j)==[F(1,4)]*4
        assert norm(mv(pt,j))==F(1,4)
        assert sum(u[i]*j[i] for i in range(4))==F(1,2)
        # The gradient-only repair changes all four links, not just the traversed link.
        assert sum(x!=0 for x in mv(pg,j))==4
    _,_,tree_pg,tree_pt=graph(edges[:3])
    assert tree_pg==eye(3) and tree_pt==[[F(0)]*3 for _ in range(3)]
    # Same endpoint, different retained circulation. A reverse edge cancels;
    # a forward loop returns the charge but not the field record.
    route_a=[F(1),F(1),F(0),F(0)]
    route_b=[F(0),F(0),F(-1),F(-1)]
    loop=[x-y for x,y in zip(route_a,route_b)]
    assert mv(b,route_a)==mv(b,route_b)==charges[2]
    assert loop==[F(1)]*4 and mv(b,loop)==[F(0)]*4
    assert mv(pg,loop)==[F(0)]*4 and mv(pt,loop)==loop
    assert norm(loop)/2==2
    assert mv(pt,[F(0)]*4)==[F(0)]*4

    cases=[]
    for root_kappa in (1,4,16):
        kappa=F(root_kappa**2);omega=F(2*root_kappa)
        variance=F(1,4*root_kappa)  # <a^2>, beta=1
        single_kick=F(1,2);loop_kick=F(2)
        single_mean=single_kick**2*variance
        loop_mean=loop_kick**2*variance
        assert single_mean==F(1,16*root_kappa) and loop_mean==F(1,root_kappa)
        assert omega*single_mean==F(1,8) and omega*loop_mean==2
        z=exp_negative(single_mean/2)
        probability=exp_negative(single_mean)
        leakage=(1-probability[1],1-probability[0])
        assert leakage[0]>0
        loop_probability=exp_negative(loop_mean)
        loop_leakage=(1-loop_probability[1],1-loop_probability[0])
        path_overlap=exp_negative(loop_mean/2)
        # Full H=H_T+U+K is positive; Q H Q>=omega on excited photons.
        # Uniform position trial: E<=5/16+2(1-Z)<=5/16+single_mean.
        energy_ceiling=F(5,16)+single_mean
        assert energy_ceiling<omega
        # ||QHP||^2 <= 4(1-Z^2) <= 4*single_mean at t=1.
        schur=4*single_mean/(omega-energy_ceiling)
        compression_error=single_mean  # ||H_PP-(L+U)|| <= 2(1-Z)
        cases.append(dict(kappa=str(kappa),omega=str(omega),vacuum_link_amplitude=interval(z),
            single_hop_excitation_probability=interval(leakage),
            single_hop_field_energy_increase='1/8',
            loop_excitation_probability=interval(loop_leakage),
            loop_field_energy_increase='2',two_path_field_overlap=interval(path_overlap),
            ground_energy_ceiling=str(energy_ceiling),
            full_vs_vacuum_compressed_ground_error_upper=str(schur),
            full_vs_electrostatic_ground_error_upper=str(schur+compression_error),
            full_vs_electrostatic_ground_error_decimal=float(schur+compression_error)))
    previous=BASE/'results/gauss_spatial_binding.json'
    prior=json.loads(previous.read_text(encoding='utf-8'))
    assert prior['verification_passed'] and prior['negative_level_certified']
    for name,digest in prior['source_hashes'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    paths=[Path(__file__),previous,ROOT/'research/nima/record-gauge-feedback-loop.md',
           BASE/'spinor-face-magnetic-action.md',BASE/'spinor-endpoint-constructor.md']
    result=dict(verification_passed=True,hopping_word_checks=word_checks,
        model='neutral pair on one square; Gauss-reduced noncompact harmonic link field; beta=q=t=1',
        independent_cycle_coordinate_retained=True,
        local_hopping_preserves_gauss=True,local_hopping_preserves_transverse_vacuum=False,
        gradient_only_repair_is_nonlocal_on_plaquette=True,tree_control_has_no_transverse_kick=True,
        same_endpoint_paths_leave_different_field_states=True,
        electrostatic_energies=[str(x) for x in electric],stiffness_cases=cases,
        exact_vacuum_invariance_no_go_scope='Nontrivial phase multiplication on any normalizable continuous cycle wavefunction; not just the harmonic ground state.',
        bare_hop_work_account_required=True,
        finite_graph_error_bound_only=True,infinite_volume_binding_transferred=False,
        physical_charge_translation_or_units_derived=False,
        source_hashes={str(p.relative_to(ROOT)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in paths})
    output=BASE/'results/gauss_dressed_hopping.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
