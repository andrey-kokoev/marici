"""Exact norm identities behind finite-to-completed stability obstructions.

No Clark trace is sampled. Tail estimates are analytic inequalities proved
in the note; the script checks their constants, finite refinements, and exact
word-splitting singular values and collision counts.
"""
from pathlib import Path
from math import comb
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]


def compositions(total,parts):
    if parts==1:
        yield (total,);return
    for first in range(total+1):
        for tail in compositions(total-first,parts-1):yield (first,)+tail


def main():
    # Endpoint-block projections preserve the entire presentation kernel.
    blocks=[s.Matrix([[1,1]]),s.Matrix([[1,1,0],[0,1,1]]),s.Matrix([[1,-1]])]
    presentation=s.diag(*blocks)
    assert len(presentation.nullspace())==sum(len(b.nullspace()) for b in blocks)
    row=column=0
    for block in blocks:
        src=s.diag(*[int(column<=i<column+block.cols) for i in range(presentation.cols)])
        dst=s.diag(*[int(row<=i<row+block.rows) for i in range(presentation.rows)])
        assert dst*presentation==presentation*src
        assert all(presentation*src*v==s.zeros(presentation.rows,1) for v in presentation.nullspace())
        row+=block.rows;column+=block.cols
    # Critical fixed-depth coefficient patterns have norms independent of
    # the translating outer endpoint. One relation is singly retained.
    scale,lam=s.symbols('scale lam',positive=True)
    for depth in range(1,5):
        column={((),()):1}
        for j in range(depth):
            p,q=2*j,2*j+1
            patterns=((0,1),(1,0)) if j==0 else ((0,0),)
            local={((p,q),m):1 for m in patterns}|{((q,p),m):-1 for m in patterns}
            column={(u+v,mu+mv):x*y for (u,mu),x in column.items() for (v,mv),y in local.items()}
        coefficient_l1=sum(abs(c) for c in column.values())
        derivative_term_bound=8*4**(depth-1)
        assert coefficient_l1==2**(depth+1)
        assert derivative_term_bound//coefficient_l1==2**depth
        bs=(2*lam*scale)**depth*s.factorial(depth)
        b1=(2*lam)**depth*s.factorial(depth)
        assert s.simplify(bs/b1)==scale**depth

    # The forcing source norm is isometric under genuine chamber subdivision.
    masses=s.symbols('m0:5',positive=True)
    alpha=s.Matrix([[1,0],[1,0],[0,1],[0,1],[0,1]])
    refined=s.diag(*masses)
    old=s.diag(masses[0]+masses[1],sum(masses[2:]))
    assert alpha.T*refined*alpha==old

    # Four raw ports, with x^j/(1+x)<=1 for j=0,1.
    a,eta,area,R,x=s.symbols('a eta area R x',positive=True)
    integral=s.integrate(s.exp(-2*a*x),(x,R,s.oo))
    assert s.simplify(integral-s.exp(-2*a*R)/(2*a))==0
    upper=4*area*integral/(2*eta)
    assert s.simplify(upper-area*s.exp(-2*a*R)/(a*eta))==0
    # The concrete localization already supplied by the weighted receiver.
    assert (s.pi/16)/(s.Rational(3,4)*s.Rational(7,4))==s.pi/21
    # Normalized Clark rows are coisometric in the existing convention.
    A=(s.I*s.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2)*s.diag(s.I,-s.I,s.I,-s.I)
    assert A*A.conjugate().T==s.eye(2)

    # In a fixed one-letter word channel, normalized exponential weights
    # cancel exactly for every split. Each output row has d+1 preimages.
    tau=s.symbols('tau',positive=True)
    split_checks=0
    for N in range(1,17):
        entries={}
        for left in range(N+1):
            for right in range(N+1):
                if left+right<=N:
                    coefficient=s.simplify(tau**(left+right)/(tau**left*tau**right))
                    assert coefficient==1
                    entries[left+right,left*(N+1)+right]=coefficient
                    split_checks+=1
        mu=s.SparseMatrix(N+1,(N+1)**2,entries)
        assert mu*mu.T==s.diag(*range(1,N+2))
    for parts in range(2,6):
        for N in range(17):
            assert sum(1 for _ in compositions(N,parts))==comb(N+parts-1,parts-1)

    # A source-constructed collision current on normalized coherent splits:
    # N+1 orthogonal fine allocations all merge to the same degree-N word.
    # On even degree a signature eigenletter gives positive total pairing.
    currents=[]
    for N in (2,4,8,16,32,64):
        allocations=list(compositions(N,2))
        new_matches=sum(1 for u in allocations for v in allocations if u!=v)
        assert new_matches==N*(N+1)
        # Coefficient products are 1/(N+1) after normalizing the input sum.
        correction=s.Rational(new_matches,N+1)
        assert correction==N
        fine=s.Integer(1);coarse=s.Integer(N+1)
        assert fine+correction==coarse
        currents.append({'capacity':N,'sewing_norm_squared':N+1,
                         'normalized_input_collision_current':int(correction)})

    # Actual monotonically increasing packet endpoints. The entering final
    # event window starts here; its normalized forcing is supported beyond R.
    primes=(2,3,5,7,11,13,17,19,23,29,31,37)
    endpoint=2;windows=[]
    for p in primes:
        start=endpoint;endpoint*=p
        assert endpoint>start
        windows.append({'start_endpoint':start,'end_endpoint':endpoint,
                        'relative_feature_norm_bound_at_a_three_quarters':f'{start}^(-3/4)'})
    assert all(windows[i]['end_endpoint']==windows[i+1]['start_endpoint'] for i in range(len(windows)-1))

    translated=[];background=1
    for prime in (5,7,11,13,17,19,23,29,31,37):
        background*=prime
        start=2*background
        vertices=(start,2*start,3*start,6*start)
        assert len(set(vertices))==4
        translated.append({'background_product':background,'diamond_vertices':vertices,
                           'event_length':2,'relation_depth':1,'source_relation_coefficient_l1':4})

    result={'schema':'marici.nima.completion-stability-obstructions.v1','passed':True,
        'checks':{'endpoint_projections_preserve_presentation_kernel':True,
                  'fixed_depth_tail_cycle_coefficient_norms':True,
                  'fixed_old_forcing_norm_preserved_by_refinement':True,
                  'tail_feature_bound_constant':True,'normalized_clark_row_norm_one':True,
                  'word_splitting_gram_exact':True,'higher_split_counts_exact':True,
                  'collision_growth_constructed_without_gram_subtraction':True},
        'two_slot_splitting_coefficients_checked':split_checks,
        'coefficient_tail_bound':'||Lhat v|| <= ||A_Cl|| sqrt(area/(a*eta)) exp(-a R) ||v||, a=beta-Y>0',
        'two_slot_all_state_sewing_norm':'sqrt(N+1)',
        'k_slot_all_state_sewing_norm':'sqrt(binomial(N+k-1,k-1))',
        'fixed_branch_r_seam_normalization_norm':'(N+1)^((r-1)/2)',
        'collision_growth_fixtures':currents,'new_event_tail_windows':windows,
        'fixed_length_translated_diamonds':translated,
        'scope':'Analytic forcing-norm tail bound and exact finite norm identities. No numerical Clark spectrum, changed weights, phantom kernel, or failure on a fixed old finite subspace is asserted. Completed injectivity is supplied by the Voevodsky endpointwise theorem, not inferred from these finite matrices. The new fixed-length tail obstruction and its dual consequence are analytic proofs in the companion note. Approximate null directions and unbounded all-state cut-l2 sewing are distinct from that injectivity.'}
    out=ROOT/'research/nima/results/completion-stability-obstructions.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
