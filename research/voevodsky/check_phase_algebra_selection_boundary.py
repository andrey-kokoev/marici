"""Independent exact source/algebra audit; never writes owner research files.
Finite basis identities extend to the whole rational algebra by multilinearity.
This is not a formal model of every native higher-source policy.
"""
from pathlib import Path
from itertools import product
import contextlib, hashlib, importlib.util, io, json, re, shutil, sys
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
OWN=ROOT/'research/voevodsky'
OWNER=ROOT/'research/nima'
SANDBOX=ROOT/'temp/phase-selection-independent'
RECEIPT=OWN/'phase-algebra-selection-boundary.json'
RECEIPT.unlink(missing_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks={}
def check(name, condition):
    assert condition,name
    checks[name]=True

# The COMPLETE original checker runs on byte-identical sandbox copies.
paths=list((OWNER/'agda').rglob('*.agda'))+[OWNER/'checkers/check_phase_selection.py']
paths += [OWNER/'results'/n for n in ('phase-selection.json','agda-PhaseLiftCocycle.json','agda-ComparisonKineticReadout.json')]
before={str(p.relative_to(OWNER)):sha(p) for p in paths}
for p in paths:
    dest=SANDBOX/p.relative_to(OWNER)
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,dest)
spec=importlib.util.spec_from_file_location('independent_owner_phase_selection',SANDBOX/'checkers/check_phase_selection.py')
m=importlib.util.module_from_spec(spec)
saved=sys.dont_write_bytecode
sys.dont_write_bytecode=True
try:spec.loader.exec_module(m)
finally:sys.dont_write_bytecode=saved
with contextlib.redirect_stdout(io.StringIO()):m.main()
check('owner_research_inputs_and_receipts_unchanged',before=={str(p.relative_to(OWNER)):sha(p) for p in paths})
owner_result=json.loads((SANDBOX/'results/phase-selection.json').read_text())
check('complete_owner_classification_reproduced',owner_result['normalized_sign_cocycles']==16 and owner_result['classes_under_complex_rephasing']==2)

text=(OWNER/'agda/RetainedComparisonSeries.agda').read_text(encoding='utf-8')
match=re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$',text,re.M)
p=tuple(map(int,match.groups()))
actions=[tuple(4*(p[x] if g&1 else x)+(p[y] if g&2 else y) for x in range(4) for y in range(4)) for g in range(4)]
check('faithful_actual_source_action',len(set(actions))==4 and all(tuple(actions[g][actions[h][i]] for i in range(16))==actions[g^h] for g,h in product(range(4),repeat=2)))
P=[s.zeros(16) for _ in range(4)]
for g in range(4):
    for i in range(16):P[g][i,actions[g][i]]=1
check('source_permutation_implementers_compose_without_phase',all(P[g]*P[h]==P[g^h] for g,h in product(range(4),repeat=2)))

anchor=s.Matrix([1,0,0,0]); odd=s.Matrix([0,1,-1,0])
B=s.Matrix.hstack(*[s.kronecker_product(x,y) for x,y in ((anchor,anchor),(anchor,odd),(odd,anchor),(odd,odd))])
D=[s.diag(*[(-1)**(((g&1)*((h>>1)&1))^(((g>>1)&1)*(h&1))) for h in range(4)]) for g in range(4)]
check('same_active_intertwiner_for_both_products',all(P[g]*B==B*D[g] for g in range(4)))
cochains={'trivial':lambda g,h:0,'clifford':lambda g,h:((g>>1)&1)*(h&1)}
basis=[s.eye(4)[:,i] for i in range(4)]
def twisted(c,x,y):
    z=s.zeros(4,1)
    for g,h in product(range(4),repeat=2):z[g^h]+=(-1)**c(g,h)*x[g]*y[h]
    return z
alpha,beta=s.symbols('alpha beta')
for name,c in cochains.items():
    check(name+'_four_dimensional_associativity',all(twisted(c,twisted(c,x,y),z)==twisted(c,x,twisted(c,y,z)) for x,y,z in product(basis,repeat=3)))
    check(name+'_unit_and_positive_elementary_squares',all(twisted(c,basis[0],x)==twisted(c,x,basis[0])==x for x in basis) and all(twisted(c,basis[i],basis[i])==basis[0] for i in (1,2)))
    check(name+'_source_acts_by_algebra_automorphisms',all(D[g]*twisted(c,x,y)==twisted(c,D[g]*x,D[g]*y) for g in range(4) for x,y in product(basis,repeat=2)))
    check(name+'_coefficient_arithmetic_embeds_centrally',twisted(c,alpha*basis[0],beta*basis[0])==alpha*beta*basis[0] and all(twisted(c,alpha*basis[0],x)==twisted(c,x,alpha*basis[0])==alpha*x for x in basis))
check('products_are_genuinely_distinct',twisted(cochains['trivial'],basis[2],basis[1]) != twisted(cochains['clifford'],basis[2],basis[1]))
# Unlike the rank-one component classifier, evaluation at the proposed unit
# does not classify additive endomorphisms of this four-dimensional object.
check('source_itself_breaks_unique_endomorphism_classification',D[1]*basis[0]==basis[0] and D[1]!=s.eye(4) and D[1]*basis[2]==-basis[2])
for name,c in cochains.items():
    left=lambda x:s.Matrix.hstack(*(twisted(c,x,y) for y in basis))
    check(name+'_evaluation_section',all(left(x)*basis[0]==x for x in basis) and left(basis[0])==s.eye(4))
    check(name+'_section_image_closed_under_composition',all(left(x)*left(y)==left(twisted(c,x,y)) for x,y in product(basis,repeat=2)))
    check(name+'_section_is_source_equivariant',all(D[g]*left(x)*D[g]==left(D[g]*x) for g in range(4) for x in basis))

# The active four-space does NOT inherit pointwise source multiplication.
pointwise=lambda x,y:x.multiply_elementwise(y)
vectors=[B[:,i] for i in range(4)]
check('active_space_not_pointwise_closed',B.rank()==4 and s.Matrix.hstack(B,pointwise(vectors[1],vectors[1])).rank()==5)
check('declared_active_unit_cannot_preserve_pointwise_product',pointwise(vectors[0],vectors[1])==s.zeros(16,1) and all(twisted(c,basis[0],basis[1])==basis[1]!=s.zeros(4,1) for c in cochains.values()))
# Exact minimal unital pointwise envelope. Every projector is polynomial in
# the active readings, and conversely they span every active reading and 1.
projectors=[vectors[0]]
for v in vectors[1:]:projectors.extend([(pointwise(v,v)+v)/2,(pointwise(v,v)-v)/2])
projectors.append(s.ones(16,1)-sum(projectors,s.zeros(16,1)))
Q=s.Matrix.hstack(*projectors)
check('pointwise_envelope_has_eight_independent_idempotents',Q.rank()==8 and all(pointwise(x,y)==(x if i==j else s.zeros(16,1)) for i,x in enumerate(projectors) for j,y in enumerate(projectors)))
check('envelope_contains_unit_and_all_active_readings',sum(projectors,s.zeros(16,1))==s.ones(16,1) and s.Matrix.hstack(Q,B).rank()==8)
check('source_preserves_pointwise_envelope',all(P[g]*q in projectors for g in range(4) for q in projectors))
cells=[[i for i in range(16) if q[i]==1] for q in projectors]
check('all_source_states_retained_in_envelope_fibers',sorted(i for cell in cells for i in cell)==list(range(16)) and sorted(map(len,cells))==[1,1,1,1,1,2,2,7])

# Stronger test: both phases have inner actions on the full-source crossed
# product algebra, with ALL 64 arrow labels retained. No four-dimensional
# algebra-selection assumption is imposed here.
arrows=list(product(range(16),range(4)))
def term_mul(c,a,b):
    if a is None or b is None:return None
    sign,(x,g)=a; other,(y,h)=b
    if y!=actions[g][x]:return None
    return sign*other*((-1)**c(g,h)),(x,g^h)
def algebra_mul(c,a,b):
    result={}
    for i,v in a.items():
        for j,w in b.items():
            t=term_mul(c,(v,i),(w,j))
            if t is not None:
                value,k=t;result[k]=result.get(k,0)+value
    return {k:v for k,v in result.items() if v}
def scale(k,a):return {i:k*v for i,v in a.items() if k*v}
unit={(x,0):1 for x in range(16)}
U=[{(x,g):1 for x in range(16)} for g in range(4)]
center_dimensions={}
for name,c in cochains.items():
    check(name+'_retained_64_arrow_associativity',all(term_mul(c,term_mul(c,(1,a),(1,b)),(1,d))==term_mul(c,(1,a),term_mul(c,(1,b),(1,d))) for a,b,d in product(arrows,repeat=3)))
    check(name+'_retained_algebra_unit',all(algebra_mul(c,unit,{a:1})==algebra_mul(c,{a:1},unit)=={a:1} for a in arrows))
    check(name+'_inner_implementers_have_declared_phase',all(algebra_mul(c,U[g],U[h])==scale((-1)**c(g,h),U[g^h]) for g,h in product(range(4),repeat=2)))
    check(name+'_inner_implementation_on_full_source_observables',all(algebra_mul(c,algebra_mul(c,U[g],{(x,0):1}),scale((-1)**c(g,g),U[g]))=={(actions[g][x],0):1} for g in range(4) for x in range(16)))
    check(name+'_diagonal_pointwise_source_algebra_embeds',all(algebra_mul(c,{(x,0):1},{(y,0):1})==({(x,0):1} if x==y else {}) for x,y in product(range(16),repeat=2)))
    # Complete linear centralizer equations, not a gauge/basis convention.
    equations={}; index={a:i for i,a in enumerate(arrows)}
    for i,a in enumerate(arrows):
        for j,b in enumerate(arrows):
            for factor,t in ((1,term_mul(c,(1,a),(1,b))),(-1,term_mul(c,(1,b),(1,a)))):
                if t is not None:
                    value,k=t;key=(64*j+index[k],i)
                    equations[key]=equations.get(key,0)+factor*value
    center_dimensions[name]=64-s.SparseMatrix(4096,64,equations).rank()
    check(name+'_exact_center_dimension',center_dimensions[name]==({'trivial':25,'clifford':13}[name]))
check('retained_algebras_not_isomorphic_even_after_basis_change',center_dimensions['trivial']!=center_dimensions['clifford'])

# Trivial-phase operator realization: faithful on source observables, NOT on
# all retained arrow labels. Do not replace the 64-dimensional source algebra
# by its 36-dimensional operator image.
image=lambda a:(a[0],actions[a[1]][a[0]])
image_units={image(a) for a in arrows}
check('operator_image_dimension_36_not_64',len(image_units)==36)
check('operator_readout_has_nonzero_stabilizer_kernel',image((0,0))==image((0,1)) and (0,0)!=(0,1))
check('operator_readout_preserves_trivial_product',all((None if image(a)[1]!=image(b)[0] else (image(a)[0],image(b)[1]))==(None if (t:=term_mul(cochains['trivial'],(1,a),(1,b))) is None else image(t[1])) for a,b in product(arrows,repeat=2)))
check('innerness_on_ambient_matrix_algebra_covers_full_source',all(P[g]*s.diag(*s.eye(16)[:,x])*P[g].T==s.diag(*(P[g]*s.eye(16)[:,x])) for g in range(4) for x in range(16)))

formal_path=OWN/'phase-algebra-selection-boundary-formal.json'
formal=json.loads(formal_path.read_text())
check('fresh_formal_boundary_and_direct_rejection_controls',formal['passed'] and formal['fresh'] and formal['phase_boundary_mode'])
check('formal_runner_is_current',formal['checker_sha256']==sha(OWN/'check_native_radar_formal.py'))
# Bind fresh formal inventory to current files, without refreshing old receipts.
check('formal_source_closure_current',formal['original_sources_unchanged'] and all(sha(Path(name))==digest for name,digest in formal['source_snapshot_hashes'].items()))
result={'schema':'marici.voevodsky.phase-algebra-selection-boundary.v1','passed':all(checks.values()),'checks':checks,
 'owner_checker':'complete independent sandbox rerun; prior receipt bindings checked, not silently reissued',
 'owner_input_sha256':before,'pointwise_envelope_dimension':8,'retained_source_fibers':cells,
 'crossed_product_dimensions':{'trivial':64,'clifford':64},'crossed_product_center_dimensions':center_dimensions,'trivial_operator_image_dimension':36,'trivial_operator_kernel_dimension':28,
 'conclusion':'Both phase models admit associative full-source crossed-product algebras with inner source actions. Innerness selects Clifford only after the restricted algebra profile is fixed. The active four-space is not closed under source pointwise multiplication.',
 'scope':'Finite basis proofs plus rational multilinear extension; native formal history/action and nonuniqueness results. Not a model of all native higher-source axioms, a geometric free-component derivation, or physical phase selection.',
 'current_artifact_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [Path(__file__),formal_path,OWN/'agda/PhaseAlgebraSelectionBoundary.agda']}}
RECEIPT.write_text(json.dumps(result,indent=2)+'\n')
print('passed=',result['passed'],'checks=',len(checks),'pointwise_envelope=8 retained_algebras=64 operator_image=36 kernel=28')
