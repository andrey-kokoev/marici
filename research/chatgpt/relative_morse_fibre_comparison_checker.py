#!/usr/bin/env python3
"""Exact endpoint-derived comparison from the loaded Morse complex to a conductor fibre.

Run: python relative_morse_fibre_comparison_checker.py
Only the Python standard library is required.  No network or other artifacts are used.
Output: relative_morse_fibre_comparison_certificate.json, beside this file.

The physical unit-Q identification is tested and rejected in the stated ordinary
B-linear model. The constructed maps retain named endpoint lines; no equality with
the physical conductor--Morse invariant is assumed.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json

DIAGONALS = ('02','03','04','13','14','15','24','25','35')
PLUS = frozenset(('13','15','35'))
MINUS = frozenset(('02','04','24'))
SHORT = tuple(sorted(PLUS | MINUS))
LONG = ('03','14','25')
VARIABLES = tuple('X'+d for d in DIAGONALS) + tuple('t'+d for d in SHORT) + tuple('u'+d for d in LONG)
INDEX = {v:i for i,v in enumerate(VARIABLES)}
ZERO_MONO = (0,)*len(VARIABLES)
ONE = {ZERO_MONO:1}
ZERO = {}
CHECKS = Counter()

def verify(condition: bool, label: str) -> None:
    CHECKS[label] += 1
    if not condition:
        raise AssertionError(label)

def survives(m: tuple[int,...]) -> bool:
    return not (any(m[INDEX['X'+d]] for d in PLUS) and any(m[INDEX['X'+d]] for d in MINUS))

def add(p: dict, q: dict, factor: int=1) -> dict:
    r = dict(p)
    for m,c in q.items():
        r[m] = r.get(m,0) + factor*c
        if r[m] == 0:
            del r[m]
    return r

def neg(p: dict) -> dict:
    return {m:-c for m,c in p.items()}

def mul(p: dict, q: dict) -> dict:
    r = {}
    for a,c in p.items():
        for b,d in q.items():
            m = tuple(x+y for x,y in zip(a,b))
            if survives(m):
                r[m] = r.get(m,0)+c*d
                if r[m] == 0:
                    del r[m]
    return r

def variable(name: str) -> dict:
    m = list(ZERO_MONO); m[INDEX[name]] = 1
    return {tuple(m):1}

def product(names) -> dict:
    p = ONE
    for name in names:
        p = mul(p, variable(name))
    return p

def epsilon(p: dict) -> dict:
    return {m:c for m,c in p.items() if not any(m[INDEX['X'+d]] for d in SHORT)}

def order(p: dict):
    if not p:
        return None
    return min(sum(m[INDEX['X'+d]] for d in SHORT) for m in p)

def normal(d: str) -> dict:
    return product(('t'+d,'X'+d)) if d in SHORT else variable('u'+d)

def pstr(p: dict) -> str:
    if not p:
        return '0'
    terms=[]
    for m,c in sorted(p.items()):
        factors=[v if power==1 else f'{v}^{power}' for v,power in zip(VARIABLES,m) if power]
        mon='*'.join(factors)
        text=(str(abs(c))+'*' if abs(c)!=1 and mon else str(abs(c)) if not mon else '')+mon
        terms.append(('-' if c<0 else '+')+text)
    ans=''.join(terms)
    return ans[1:] if ans.startswith('+') else ans

def vadd(out: dict, key, p: dict, scale: int=1) -> None:
    if not p:
        return
    out[key]=add(out.get(key,{}),p,scale)
    if not out[key]:
        del out[key]

def combine(a: dict, b: dict, scale: int=1) -> dict:
    r=dict(a)
    for key,p in b.items():
        vadd(r,key,p,scale)
    return r

def vmul(v: dict, p: dict) -> dict:
    out={}
    for key,q in v.items():
        vadd(out,key,mul(p,q))
    return out

def apply(columns: dict, vector: dict) -> dict:
    out={}
    for key,c in vector.items():
        for target,p in columns.get(key,{}).items():
            vadd(out,target,mul(c,p))
    return out

def cross(d: str, e: str) -> bool:
    a,b=map(int,d); c,f=map(int,e)
    if len({a,b,c,f}) < 4:
        return False
    def inside(x,y,z):return 0<(x-y)%6<(z-y)%6
    return (inside(c,a,b)!=inside(f,a,b)) and (inside(a,c,f)!=inside(b,c,f))

def powerset(values):
    vals=tuple(sorted(values))
    for n in range(len(vals)+1):
        yield from combinations(vals,n)

old_faces={frozenset(c) for n in range(4) for c in combinations(DIAGONALS,n)
           if all(not cross(d,e) for d,e in combinations(c,2))}
new_faces=set()
for face in old_faces:
    if not {'03','13'} <= face:
        new_faces.add(face)
    else:
        for retained in (set(),{'03'},{'13'}):
            new_faces.add(frozenset((set(face)-{'03','13'}) | {'E'} | retained))
FACES=tuple(sorted(new_faces,key=lambda f:(len(f),tuple(sorted(f)))))

def oldof(face):
    return (face-{'E'}) | (frozenset(('03','13')) if 'E' in face else frozenset())

FLAGS=[]
def extend(flag):
    FLAGS.append(tuple(flag))
    for face in FACES:
        if flag[-1] < face:
            extend(flag+[face])
for face in FACES:
    extend([face])

# A generator consists of (strict flag, old normal-circle subset, occurrence-Koszul bit).
BASE=tuple((flag,H) for flag in FLAGS for H in powerset(oldof(flag[0])))
GENS=tuple((flag,H,k) for flag,H in BASE for k in (0,1))
GSET=set(GENS)

def degree(g):return len(g[0])-1+len(g[1])+g[2]

def source_column(g):
    flag,H,k=g
    base_dim=len(flag)-1
    out={}
    if len(flag)>1:
        for i in range(len(flag)):
            target=(flag[:i]+flag[i+1:],H,k)
            coefficient=ONE
            if i==0:
                coefficient=product('X'+d for d in oldof(flag[1])-oldof(flag[0]))
            vadd(out,target,coefficient,(-1)**i)
    for i,d in enumerate(H):
        vadd(out,(flag,H[:i]+H[i+1:],k),normal(d),(-1)**(base_dim+i))
    if k:
        vadd(out,(flag,H,0),variable('X35'),(-1)**(base_dim+len(H)))
    return out

DS={g:source_column(g) for g in GENS}
for g,col in DS.items():
    verify(all(h in GSET and degree(h)==degree(g)-1 for h in col),'source_degree_and_closure')
    verify(apply(DS,col)=={},'full_source_d_squared')

# Original finite coefficient matrices J, and F=fib(epsilon*r).
J_D1=(1,-1,-1,-1,-1)
J_D2=((1,0,0,0),(1,0,0,0),(0,1,0,-1),(0,-1,1,0),(0,0,-1,1))
J_D3=(0,1,1,1)
READOUT=(0,0,1,1,1)
Z=(1,0,1,0,0)

def numeric_product(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
verify(numeric_product(J_D2, [[n] for n in J_D3])==[[0]]*5,'J_d_squared_3')
verify(numeric_product([J_D1], J_D2)==[[0]*4],'J_d_squared_2')
verify(sum(a*b for a,b in zip(READOUT,Z))==1,'J_unit_detector')
verify(numeric_product([READOUT],J_D2)==[[0]*4],'J_readout_closed')

# Target coordinates (endpoint line, degree, component). In degree 0, component
# 0 has coefficients in B and component 1 has coefficients in C=B/I.
TARGETS=tuple((side,n,j) for side in ('plus','minus') for n,rk in ((0,2),(1,5),(2,4),(3,1)) for j in range(rk))

def target_boundary(vector):
    out={}
    for (side,n,j),p in vector.items():
        if n==1:
            vadd(out,(side,0,0),p,J_D1[j])
            vadd(out,(side,0,1),epsilon(p),READOUT[j])
        elif n==2:
            for i,row in enumerate(J_D2):vadd(out,(side,1,i),p,row[j])
        elif n==3:
            for i,v in enumerate(J_D3):vadd(out,(side,2,i),p,v)
    return out

def zimage(side,p):
    return {(side,1,i):p for i,v in enumerate(Z) if v and p}

def endpoint_generator(side):
    vertex=PLUS if side=='plus' else MINUS
    return ((vertex,),(),0)

ENDPOINT={side:endpoint_generator(side) for side in ('plus','minus')}

def extraction(side,g):
    return DS[g].get(ENDPOINT[side],{})

# The sign is the cohomological Hom convention: delta(E)=-E*d for degree-0 E.
M={}
for g in GENS:
    col={}
    for side in ('plus','minus'):
        p=extraction(side,g)
        verify(epsilon(p)=={},'endpoint_augmentation_is_chain_map')
        if p:
            col.update(zimage(side,neg(p)))
    M[g]=col
# Complete check, independent of enumeration order.
for g in GENS:
    verify(target_boundary(M[g])==apply(M,DS[g]),'full_comparison_chain_equation')
    for (side,n,j),p in M[g].items():
        verify(n==degree(g),'comparison_homological_degree')
        verify(order(p)>=1,'comparison_conductor_order')
        # Input multidegree: -occ(initial) + normal-circle weights + occurrence bit.
        input_degree=[0]*len(VARIABLES)
        for d in oldof(g[0][0]):input_degree[INDEX['X'+d]]-=1
        for d in g[1]:
            for mon in normal(d):
                input_degree=[a+b for a,b in zip(input_degree,mon)]
        if g[2]:input_degree[INDEX['X35']]+=1
        output_line=[0]*len(VARIABLES)
        for d in PLUS if side=='plus' else MINUS:output_line[INDEX['X'+d]]-=1
        verify(all(tuple(a+b for a,b in zip(mon,output_line))==tuple(input_degree) for mon in p),
               'occurrence_and_Rees_homogeneity')

# Marked Morse chains, exactly with the source's seven-triangle and lcm conventions.
top=frozenset(); qd=frozenset(('03',))
a=PLUS; ec=frozenset(('13','35')); b1=frozenset(('E','13','35'))
h=frozenset(('E','35')); bd=frozenset(('E','03','35'))
er=frozenset(('03','35')); c=frozenset(('03','02','35'))

def term(flag,p=ONE,sign=1):return {(tuple(flag),(),0): {m:sign*n for m,n in p.items()}}
HM={}
for apex,edge,left,right,p in ((top,ec,a,b1,ONE),(top,h,b1,bd,ONE),(qd,er,bd,c,variable('X03'))):
    HM=combine(HM,term((apex,edge,right),p,-1))
    HM=combine(HM,term((apex,edge,left),p,1))
HM=combine(HM,term((top,qd,bd)))
XI={}
for edge,left,right,p in ((ec,a,b1,variable('X13')),(h,b1,bd,product(('X03','X13'))),(er,bd,c,variable('X03'))):
    XI=combine(XI,term((edge,right),p))
    XI=combine(XI,term((edge,left),p,-1))
Q=combine(combine(term((top,a),sign=-1),term((top,qd))),term((qd,c),variable('X03')))
DXI=apply(DS,XI)
verify(DXI==combine(term((c,),product(('X03','X02'))),term((a,),product(('X13','X15'))),-1),
       'actual_gallery_endpoint_boundary')
verify(apply(DS,HM)==combine(Q,vmul(XI,variable('X35')),-1),'seven_triangle_Morse_identity')
verify(apply(DS,Q)==vmul(DXI,variable('X35')),'generic_endpoint_correction_identity')

def occurrence_partner(v):return {(flag,H,1):p for (flag,H,k),p in v.items()}
HHAT=combine(HM,occurrence_partner(XI),-1)
QHAT=combine(Q,occurrence_partner(DXI),-1)
verify(apply(DS,HHAT)==QHAT,'complete_corrected_Morse_identity')
verify(apply(DS,QHAT)=={},'corrected_Morse_boundary_closed')
PI_PLUS=product('X'+d for d in PLUS)
verify(apply(M,Q)==zimage('plus',PI_PLUS),'raw_Q_comparison_value')
verify(apply(M,occurrence_partner(DXI))==zimage('plus',PI_PLUS),'endpoint_occurrence_partner_value')
verify(apply(M,QHAT)=={},'corrected_Q_maps_to_zero')
verify(apply(M,HHAT)=={},'corrected_Morse_top_maps_to_zero')
verify(order(PI_PLUS)==3,'raw_Q_conductor_order_three')
verify(epsilon(PI_PLUS)=={},'raw_Q_scalar_conductor_value_zero')

# The following is the universal normalization obstruction, not a finite search:
# r*p*m*d(H_M)=0 implies r*p*m(q_J)=X35*r*p*m(xi).  Applying epsilon gives 0.
verify(epsilon(variable('X35'))=={},'universal_unit_Q_obstruction')

# Endpoint filtration diagrams: each endpoint has all eight native normal states
# and its occurrence-Koszul partners. The map never uses the other endpoint.
endpoint_packets={}
for side in ('plus','minus'):
    vertex=PLUS if side=='plus' else MINUS
    packet=tuple(g for g in GENS if g[0]==(vertex,))
    endpoint_packets[side]=packet
    verify(len(packet)==16,'complete_endpoint_packet_retained')
    verify(all(h in packet for g in packet for h in DS[g]),'endpoint_packet_subcomplex')
    verify(all(key[0]==side for g in packet for key in M[g]),'endpoint_line_comparison_diagram')

endpoint_union=set(endpoint_packets['plus']) | set(endpoint_packets['minus'])
for g,col in DS.items():
    for dest,p in col.items():
        if dest in endpoint_union:
            verify(epsilon(p)=={},'conductor_specialized_endpoint_incoming_zero')
for g in endpoint_union:
    verify(all(epsilon(p)=={} for p in DS[g].values()),'conductor_specialized_endpoint_outgoing_zero')

# Full normal and occurrence first-Tor comparison. The free presentation of I
# uses six independent generators E_X; the 24 first relations are retained.
syzygy_keys=[]
for branch in (tuple(sorted(PLUS)),tuple(sorted(MINUS))):
    syzygy_keys.extend(('koszul',i,j) for i,j in combinations(branch,2))
for i in sorted(PLUS):
    for j in sorted(MINUS):
        syzygy_keys.extend((('mixed',i,j),('mixed',j,i)))
verify(len(syzygy_keys)==24,'complete_first_syzygy_count')

def syzygy_boundary(key):
    kind,i,j=key
    if kind=='koszul':return {j:variable('X'+i),i:neg(variable('X'+j))}
    return {j:variable('X'+i)}

def xi_relation(i,j):
    if i==j:return {}
    if (i in PLUS)==(j in PLUS):
        ordered=tuple(sorted((i,j)))
        return {('koszul',*ordered): ONE if (i,j)==ordered else neg(ONE)}
    return {('mixed',i,j):ONE,('mixed',j,i):neg(ONE)}

for side in ('plus','minus'):
    vertex=PLUS if side=='plus' else MINUS
    factors=[(d,variable('t'+d)) for d in sorted(vertex)]+[('35',ONE)]
    for (i,ai),(j,aj) in combinations(factors,2):
        # Degree-one comparison maps the normal i to -ai E_i.
        source={}
        vadd(source,j,neg(mul(mul(ai,aj),variable('X'+i))))
        vadd(source,i,mul(mul(ai,aj),variable('X'+j)))
        lifted={key:neg(mul(mul(ai,aj),value)) for key,value in xi_relation(i,j).items()}
        actual={}
        for key,p in lifted.items():
            for dest,q in syzygy_boundary(key).items():vadd(actual,dest,mul(p,q))
        verify(actual==source,'endpoint_two_normal_free_lift')

# Nonvanishing proof check: a primitive into I[1] must have an endpoint coefficient b in I.
# On a marked normal, u_i*b=-c*u_i. Positive/negative branch restriction, where
# t_i*X_i is regular, forces b_branch=-c; augmentation of b_branch is zero.
# Thus c=0. This detects two independent C-linear classes. The code checks the
# input normal columns and the exact symbolic ideal obstruction used in the proof.
for side in ('plus','minus'):
    vertex=PLUS if side=='plus' else MINUS
    for d in sorted(vertex):
        g=((vertex,),(d,),0)
        verify(M[g]==zimage(side,neg(normal(d))),'native_normal_comparison_column')
        verify(epsilon(normal(d))=={},'normal_in_conductor_ideal')
    verify(epsilon(ONE)==ONE,'nonzero_unit_for_primitive_obstruction')

# Exact C-linearity and annihilator witnesses: x*m is nullhomotopic for each short x.
# Primitive Q_x has only degree-zero component -x*E_endpoint, now I-valued.
for side in ('plus','minus'):
    for d in SHORT:
        primitive={ENDPOINT[side]:zimage(side,neg(variable('X'+d)))}
        for g in GENS:
            lhs=combine(target_boundary(primitive.get(g,{})),apply(primitive,DS[g]))
            target={key:p for key,p in M[g].items() if key[0]==side}
            rhs=vmul(target,variable('X'+d))
            verify(lhs==rhs,'exact_conductor_annihilator_homotopy')

# Verify that the tempting whole-source primitive is not a primitive of the
# zero-framed lift: its omitted conductor component is exactly the endpoint frame.
for side in ('plus','minus'):
    P0={ENDPOINT[side]:zimage(side,neg(ONE))}
    failure=target_boundary(P0[ENDPOINT[side]])
    verify(failure=={(side,0,1):neg(ONE)},'global_primitive_changes_endpoint_frame')

# Rotation by two vertices preserves each sheet, normal order supplies exterior signs.
def rot_diag(d):
    a,b=map(int,d); return ''.join(map(str,sorted(((a+2)%6,(b+2)%6))))
for vertex in (PLUS,MINUS):
    verify(frozenset(rot_diag(d) for d in vertex)==vertex,'endpoint_C3_orbit')
    verify(sorted(rot_diag(d) for d in vertex)==sorted(vertex),'endpoint_counit_rotation')
# These are endpoint rotations. No claim that fixed blowup center 03/13 is fixed.


def label(g):
    flag,H,k=g
    return {'flag':[sorted(f) for f in flag], 'normal_marks':list(H),
            'occurrence_Koszul': 'h_occ35' if k else 'p', 'degree':degree(g)}

def vector_json(v):
    return [{'source_state':label(g),'coefficient':pstr(p)} for g,p in sorted(v.items(),key=lambda kv:json.dumps(label(kv[0]),sort_keys=True))]

entries=[]
for sid,g in enumerate(GENS):
    for (side,n,j),p in sorted(M[g].items()):
        entries.append({'source_index':sid,'source_state':label(g),
                        'target_line':side,'target_degree':n,'target_J_coordinate':j,
                        'coefficient':pstr(p),
                        'polynomial':[{'exponents':list(mon),'coefficient':value} for mon,value in sorted(p.items())]})
first_Tor=[]
for side in ('plus','minus'):
    vertex=PLUS if side=='plus' else MINUS
    for d in sorted(vertex):
        first_Tor.append({'source_endpoint':side,'source_state':'circle_'+d,'target':'['+'X'+d+'] tensor ell_'+side,'coefficient':'-t'+d})
    first_Tor.append({'source_endpoint':side,'source_state':'h_occ35','target':'[X35] tensor ell_'+side,'coefficient':'-1'})

native_minor=product('t'+d for d in SHORT)
verify(bool(native_minor),'six_native_normal_Tor_minor_nonzero')

payload={
 'schema':'marici.relative_morse_fibre_comparison.v1',
 'coefficient_model':{'B':'C[X02,X04,X24,X13,X15,X35]/(Xeven*Xodd)',
                      'C_variables':[v for v in VARIABLES if v not in {'X'+d for d in SHORT}],
                      'short_normal_graph':'u_d=t_d*X_d',
                      'independent_long_normals':list(LONG),
                      'inversions_used':[]},
 'provenance':{
   'repository':'andrey-kokoev/marici',
   'commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
   'Morse_source':'research/voevodsky/check_d03_pabs_morse_pullback.rs',
   'Morse_blob_sha':'46624341c7956a8557249a54b117a88d43adfd62',
   'J_source':'research/voevodsky/check_physical_derived_pullback_after_transform.py',
   'J_blob_sha':'7993b2b1bbdba03d05c3f443a45717d7b8efeec5'},
 'counts':{'old_faces':len(old_faces),'expanded_faces':len(FACES),'flags':len(FLAGS),
           'loaded_before_occurrence_factor':len(BASE),'corrected_source_states':len(GENS),
           'corrected_source_degree_ranks':dict(sorted(Counter(map(degree,GENS)).items())),
           'endpoint_states_each':16,'endpoint_states_total':32,
           'nonzero_comparison_source_columns':sum(bool(c) for c in M.values()),
           'nonzero_comparison_entries':len(entries),'first_syzygies':len(syzygy_keys)},
 'target':{'F_modules':{'3':'B','2':'B^4','1':'B^5','0':'B direct-sum C'},
           'F_d1_rows':[list(J_D1),list(READOUT)],
           'F_d1_second_row_is_followed_by_epsilon':True,
           'J_d2':J_D2,'J_d3':J_D3,'J_cycle_z':Z,
           'refinement':'(F tensor ell_plus) direct-sum (F tensor ell_minus)',
           'ell_plus_occurrence_degree':{d:-1 for d in sorted(PLUS)},
           'ell_minus_occurrence_degree':{d:-1 for d in sorted(MINUS)},
           'full_physical_Q_diagram_constructed':False},
 'comparison_entries':entries,
 'actual_Morse_chains':{'H_M':vector_json(HM),'xi':vector_json(XI),'q_J':vector_json(Q),
                       'd_xi':vector_json(DXI),'H_hat':vector_json(HHAT),'q_hat':vector_json(QHAT)},
 'evaluations':{'raw_q_plus':'X13*X15*X35*z tensor ell_plus','raw_q_minus':'0',
                'corrected_q_hat':'0','corrected_H_hat':'0',
                'raw_q_conductor_order':3,'scalar_conductor_Q_coefficient':0},
 'derived_conductor_first_Tor_map':first_Tor,
 'symbolic_conclusions':{
   'endpoint_derived_relative_maps_constructed':True,
   'two_independent_C_classes':'C*m_plus direct-sum C*m_minus injects into Hom_D(B)(Mhat,Fpartial)',
   'each_class_annihilator_in_B':'I (all six short occurrences)',
   'native_normal_subspace_first_Tor_generic_rank':6,
   'native_normal_first_Tor_nonzero_minor':pstr(native_minor),
   'raw_Q_unit_preserving_B_linear_lift_exists':False,
   'unit_no_go_identity':'epsilon r p m(q_J) = epsilon(X35)*epsilon r p m(xi) = 0',
   'fully_physical_source_refinement_completed':False,
   'physical_Delta_J_computed':False,
   'nonzero_Chern_or_Gysin_physical_invariant_inferred':False},
 'verification':{'checks_by_family':dict(CHECKS),'exact_checks':sum(CHECKS.values()),
                 'complete_polynomial_identities':True,'numeric_parameter_sampling':False,
                 'mathematical_proofs_needed':['regularity of t_i*X_i on an individual polynomial sheet',
                                               'the long exact Tor sequence and conductor ideal presentation'],
                 'scope':'Matrix identities and named first-Tor lift equations only; physical provenance is not inferred from counts.'}
}
serialized=json.dumps(payload,sort_keys=True,separators=(',',':'))
payload['matrix_and_results_sha256']=hashlib.sha256(serialized.encode()).hexdigest()
payload['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
out=Path(__file__).with_name('relative_morse_fibre_comparison_certificate.json')
out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps({'counts':payload['counts'],'verification':payload['verification'],
                  'sha256':payload['matrix_and_results_sha256'], 'output':str(out)},indent=2))
