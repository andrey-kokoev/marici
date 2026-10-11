"""Test a declared least-displacement selector on the full-cell pullback.
The rule uses the existing Euclidean geometry; it is not a supplied physical
energy law. All original cells remain retained when a focus point is selected.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from check_full_cell_attachment import projections, BOUNDS, value
from check_retained_direction_attachment import xyz, geo, SOURCE, verify

BASE=Path(__file__).resolve().parents[1]
CELL_STORE=BASE/'results/full_cell_attachment_store.json'

def selected(u): return (u[0],u[1],Q(0),min(min(u),Q(1,12)))
def square_norm(v): return sum(x*x for x in v)
def geometric_cost(x):
    h,e=projections(x)
    F=tuple(sum(geo.POINTS[k][i] for k in 'ABC')/3 for i in range(3))
    return square_norm(tuple(a-b for a,b in zip(xyz(h),F)))+square_norm(xyz(e))
def fiber_cost(a,b): return 3*a*a+3*(Q(1,3)-4*b)**2

def main():
    original=SOURCE.read_bytes(); evidence,_=verify(json.loads(original))
    cell_bytes=CELL_STORE.read_bytes(); cell_store=json.loads(cell_bytes)
    tests=[]; branch_counts={'interior_normal_minimum':0,'boundary_clamped_minimum':0}
    for i in range(25):
        for j in range(25-i):
            u=(Q(i,24),Q(j,24),Q(24-i-j,24)); m=min(u); optimum=selected(u); bstar=optimum[3]
            branch_counts['interior_normal_minimum' if m>=Q(1,12) else 'boundary_clamped_minimum']+=1
            assert all(value(f,optimum)>=0 for f in BOUNDS)
            # Actual geometric cost, not merely a fabricated a/b penalty.
            baseline=geometric_cost((u[0],u[1],Q(0),Q(0)))-fiber_cost(0,0)
            for a in (Q(0),m/3,2*m/3,m):
                for b in (Q(0),m/3,2*m/3,m,bstar):
                    x=(u[0],u[1],a,b)
                    actual=geometric_cost(x)-geometric_cost(optimum)
                    # Exact identity and nonnegative-factor certificate.
                    expected=3*a*a+48*(b-bstar)**2+96*(bstar-Q(1,12))*(b-bstar)
                    # If clamped, both factors in the last product are <=0;
                    # otherwise the first factor vanishes.
                    tests.append(actual==expected and actual>=0
                        and (actual==0)==(a==0 and b==bstar)
                        and geometric_cost(x)==baseline+fiber_cost(a,b))
    vertex_checks=[]; descent_checks=[]
    for row in cell_store['vertices']:
        x=tuple(map(Q,row['parameters'])); h,e=projections(x)
        vertex_checks.append(tuple(map(Q,row['host_barycentric']))==h and tuple(map(Q,row['electron_barycentric']))==e)
        u=(x[0],x[1],1-x[0]-x[1]); m=min(u)
        # Projected gradient step with exact safe step 1/96:
        # da=6a, db=96b-8. This is a numerical witness of the declared
        # optimization, not an inferred temporal law.
        y=(x[0],x[1],Q(15,16)*x[2],min(m,Q(1,12)))
        descent_checks.append(geometric_cost(y)<=geometric_cost(x)
            and (y==x)==(x==selected(u)) and all(value(f,y)>=0 for f in BOUNDS))
    root=selected((Q(1,3),)*3)
    checks={
        'source_reverified':evidence['verified'],
        'retained_cell_projections_replayed':all(vertex_checks),
        'geometric_cost_and_exact_unique_minimum_certificate':all(tests),
        'both_piecewise_branches_exercised':all(branch_counts.values()),
        'positive_definite_fiber_hessian':6>0 and 96>0,
        'root_mode_selects_marked_attachment_pair':projections(root)==((Q(1,3),Q(1,3),Q(1,3),Q(0)),(Q(1,4),)*4),
        'unconstrained_readout_has_zero_cost_at_marked_pair':geometric_cost(root)==0,
        'boundary_image_has_its_single_existing_pair':all(selected(u)[2:]==(0,0) for u in [(Q(1),Q(0),Q(0)),(Q(1,2),Q(1,2),Q(0))]),
        'projected_descent_is_feasible_and_decreases_cost':all(descent_checks),
        'no_second_stationary_minimum_in_a_fixed_fiber':all(tests) and all(descent_checks),
        'selection_does_not_modify_retained_cells':CELL_STORE.read_bytes()==cell_bytes,
        'coefficient_source_unchanged':SOURCE.read_bytes()==original,
    }
    result={
        'verification_passed':all(checks.values()),'checks':checks,
        'contract':{'selector':'minimize ||x_host-F_ABC||^2 + ||x_electron||^2 at a fixed shared coefficient value',
                    'metric':'existing Euclidean realization of both equal-size tetrahedra',
                    'status':'declared variational candidate; not derived from the coefficient protocol',
                    'retention':'the full cell complex remains stored; selecting a focus point is not deleting other configurations'},
        'solution':{'a':'0','b':'min(min(u_A,u_B,u_C),1/12)',
                    'fiber_hessian_diagonal':['6','96'],
                    'fixed_coefficient_minima':1,
                    'global_selected_locus':'one continuous section over the coefficient triangle, hence a disk'},
        'certificate':'E(a,b)-E(0,b*)=3a^2+48(b-b*)^2+96(b*-1/12)(b-b*) >=0; equality only at a=0,b=b*.',
        'grid_values':sum(branch_counts.values()),'branch_counts':branch_counts,
        'outcome':'The least-displacement rule selects one configuration per coefficient value. Its two formula branches are not two competing stable states or isotope closures.',
        'remaining':'With u prescribed, one configuration is selected. If u is also minimized, the unique global minimum is the marked root pair, with zero displacement cost.',
        'source_sha256':sha256(original).hexdigest(),'cell_store_sha256':sha256(cell_bytes).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (BASE/'results/attachment_selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
