#!/usr/bin/env python3
"""Exact Morse-to-conductor-fibre comparison, at the specified coefficient level.

Standard library only.  Reconstructs all 1,169 loaded barycentric states,
tensors the separate occurrence Koszul factor (2,338 states), and checks the
endpoint connecting maps and the top-based fibre map.  No network, prior
artifact, symbolic-computation library, or placeholder assertion is required.

Usage:
    python morse_relative_source_comparison_checker.py
    python morse_relative_source_comparison_checker.py --output /some/directory

The polynomial ring and quotient, basis orders, sparse maps, provenance and
scope limitations are exported to the descriptively named certificate.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

N = 6
DIAGONALS = tuple((a, b) for a in range(N) for b in range(a + 1, N)
                  if b-a != 1 and (a,b) != (0,5))
DI = {d:i for i,d in enumerate(DIAGONALS)}
SHORT = tuple(i for i,d in enumerate(DIAGONALS) if (d[1]-d[0])%3 != 0)
LONG = tuple(i for i in range(9) if i not in SHORT)
PLUS = frozenset(DI[d] for d in ((1,3),(1,5),(3,5)))
MINUS = frozenset(DI[d] for d in ((0,2),(0,4),(2,4)))
AD = DI[(0,3)]; X1 = DI[(1,3)]; X3 = DI[(3,5)]; X5 = DI[(1,5)]; X0 = DI[(0,2)]
EXCEPTIONAL = 9
VARIABLES = (tuple('X%02d'% (10*a+b) for a,b in DIAGONALS)
             + tuple('t%02d'%(10*DIAGONALS[i][0]+DIAGONALS[i][1]) for i in SHORT)
             + tuple('u%02d'%(10*DIAGONALS[i][0]+DIAGONALS[i][1]) for i in LONG))
NV = len(VARIABLES)
ZERO_EXP = (0,)*NV
Poly = dict[tuple[int,...],int]
Vector = dict[int,Poly]
ONE: Poly = {ZERO_EXP:1}
TESTS = Counter()

def check(condition: bool, label: str) -> None:
    TESTS[label] += 1
    if not condition:
        raise AssertionError(label)

def p_add(p:Poly,q:Poly,sign:int=1)->Poly:
    ans=dict(p)
    for mon,c in q.items():
        ans[mon]=ans.get(mon,0)+sign*c
        if not ans[mon]: del ans[mon]
    return ans

def p_scale(p:Poly,c:int)->Poly:
    return {m:c*v for m,v in p.items() if c*v}

def p_mul(p:Poly,q:Poly,quotient:bool=True)->Poly:
    ans={}
    for m,c in p.items():
        for n,e in q.items():
            v=tuple(a+b for a,b in zip(m,n))
            if quotient and any(v[i] for i in PLUS) and any(v[i] for i in MINUS):
                continue
            ans[v]=ans.get(v,0)+c*e
            if not ans[v]:del ans[v]
    return ans

def p_reduce(p:Poly)->Poly:
    return {m:c for m,c in p.items()
            if not (any(m[i] for i in PLUS) and any(m[i] for i in MINUS))}

def p_eps(p:Poly)->Poly:
    return {m:c for m,c in p.items() if all(m[i]==0 for i in SHORT)}

def p_var(index:int)->Poly:
    exp=list(ZERO_EXP);exp[index]=1
    return {tuple(exp):1}

def occurrence(indices)->Poly:
    exp=list(ZERO_EXP)
    for i in indices:exp[i]+=1
    return {tuple(exp):1}

def normal(i:int)->Poly:
    if i in SHORT:
        return p_mul(p_var(i),p_var(9+SHORT.index(i)),quotient=False)
    return p_var(15+LONG.index(i))

def v_add(v:Vector,w:Vector,sign:int=1)->Vector:
    ans={i:dict(p) for i,p in v.items()}
    for i,p in w.items():
        ans[i]=p_add(ans.get(i,{}),p,sign)
        if not ans[i]:del ans[i]
    return ans

def v_scale(v:Vector,p:Poly,quotient:bool=True)->Vector:
    return {i:a for i,c in v.items() if (a:=p_mul(c,p,quotient))}

def apply(columns:list[Vector],v:Vector,quotient:bool=True)->Vector:
    ans={}
    for i,p in v.items():
        ans=v_add(ans,v_scale(columns[i],p,quotient))
    return ans

def crosses(d,e)->bool:
    if set(d)&set(e):return False
    def inside(v,a,b): return 0<(v-a)%N<(b-a)%N
    return (inside(e[0],*d)!=inside(e[1],*d)
            and inside(d[0],*e)!=inside(d[1],*e))

def old(face:frozenset[int])->frozenset[int]:
    return frozenset((face-{EXCEPTIONAL})|{AD,X1}) if EXCEPTIONAL in face else face

def reconstruct():
    faces=set()
    for k in range(4):
        for c in combinations(range(9),k):
            if all(not crosses(DIAGONALS[a],DIAGONALS[b]) for a,b in combinations(c,2)):
                faces.add(frozenset(c))
    expanded=set()
    for face in faces:
        if {AD,X1}<=face:
            for retained in (set(),{AD},{X1}):
                expanded.add(frozenset((face-{AD,X1})|{EXCEPTIONAL}|retained))
        else: expanded.add(face)
    expanded=tuple(sorted(expanded,key=lambda f:(len(f),tuple(sorted(f)))))
    flags=[]
    def extend(flag):
        flags.append(flag)
        for larger in expanded:
            if flag[-1]<larger:extend(flag+(larger,))
    for f in expanded:extend((f,))
    bare=[]
    for flag in flags:
        for k in range(len(old(flag[0]))+1):
            for H in combinations(sorted(old(flag[0])),k):bare.append((flag,H))
    states=[(flag,H,k) for flag,H in bare for k in (0,1)]
    def degree(state):return len(state[0])-1+len(state[1])+state[2]
    states.sort(key=lambda st:(degree(st),tuple(tuple(sorted(f)) for f in st[0]),st[1],st[2]))
    positions={st:i for i,st in enumerate(states)}
    ds=[]
    for flag,H,occ in states:
        col={}; base=len(flag)-1
        if len(flag)>=2:
            for j in range(len(flag)):
                ff=flag[:j]+flag[j+1:]
                poly=occurrence(old(flag[1])-old(flag[0])) if j==0 else ONE
                target=positions[(ff,H,occ)]
                col=v_add(col,{target:p_scale(poly,(-1)**j)})
        for j,h in enumerate(H):
            target=positions[(flag,H[:j]+H[j+1:],occ)]
            col=v_add(col,{target:p_scale(normal(h),(-1)**(base+j))})
        if occ:
            target=positions[(flag,H,0)]
            col=v_add(col,{target:p_scale(p_var(X3),(-1)**(base+len(H)))})
        ds.append(col)
    return expanded,flags,bare,states,positions,ds,degree

# One fibre F: degree zero (old J0, conductor C); degree one the five
# Entry-436 coordinates; degree two the four original coordinates; degree three one.
F_DEGREES=[0,0,1,1,1,1,1,2,2,2,2,3]
Z:Vector={2:ONE,4:ONE}
RROW={4:1,5:1,6:1}

def fibre_reduce(v:Vector)->Vector:
    return {i:a for i,p in v.items() if (a:=p_eps(p) if i==1 else p)}

def fibre_d(v:Vector)->Vector:
    ans={}
    d1=[1,-1,-1,-1,-1]
    d2=[[1,0,0,0],[1,0,0,0],[0,1,0,-1],[0,-1,1,0],[0,0,-1,1]]
    d3=[0,1,1,1]
    for i,p in v.items():
        if 2<=i<=6:
            ans=v_add(ans,{0:p_scale(p,d1[i-2])})
            if i in RROW:ans=v_add(ans,{1:p_eps(p)})
        elif 7<=i<=10:
            for j,row in enumerate(d2):
                if row[i-7]:ans=v_add(ans,{j+2:p_scale(p,row[i-7])})
        elif i==11:
            for j,c in enumerate(d3):
                if c:ans=v_add(ans,{j+7:p_scale(p,c)})
    return fibre_reduce(ans)

def fibre_h(v:Vector)->Vector:
    # Integral deformation retract onto [B --epsilon--> C].
    h0=[1,0,0,0,0]
    h1=[[0,1,0,0,0],[0,0,0,-1,-1],[0,0,0,0,-1],[0,0,0,0,0]]
    h2=[0,0,0,1]
    ans={}
    for i,p in v.items():
        if i==0:
            for j,c in enumerate(h0):
                if c:ans=v_add(ans,{j+2:p_scale(p,c)})
        elif 2<=i<=6:
            for j,row in enumerate(h1):
                if row[i-2]:ans=v_add(ans,{j+7:p_scale(p,row[i-2])})
        elif 7<=i<=10 and h2[i-7]:
            ans=v_add(ans,{11:p})
    return ans

def fibre_ip(v:Vector)->Vector:
    # Inclusion composed with projection, using r in degree one.
    ans={1:v.get(1,{})} if v.get(1) else {}
    return v_add(ans,v_scale(Z,road(v)))

def road(v:Vector)->Poly:
    ans={}
    for i,c in RROW.items():ans=p_add(ans,p_scale(v.get(i,{}),c))
    return ans

def poly_json(p):
    return [{'coefficient':c,'powers':{VARIABLES[i]:e for i,e in enumerate(m) if e}}
            for m,c in sorted(p.items())]

def face_name(f):
    return ['E' if i==9 else '%d%d'%DIAGONALS[i] for i in sorted(f)]

def state_name(st):
    flag,H,occ=st
    return {'flag':[face_name(f) for f in flag],
            'normal_circles':['%d%d'%DIAGONALS[i] for i in H],
            'occurrence_factor':'h_occ35' if occ else 'p_occ35'}

def internal_degree(st):
    f,H,occ=st;deg=[0]*18
    for i in old(f[0]):deg[i]-=1
    for i in H:deg[9+i]+=1
    if occ:deg[X3]+=1
    return tuple(deg)

def polynomial_degree(mon):
    deg=[0]*18
    for i in range(9):deg[i]+=mon[i]
    for j,i in enumerate(SHORT):
        deg[i]-=mon[9+j];deg[9+i]+=mon[9+j]
    for j,i in enumerate(LONG):deg[9+i]+=mon[15+j]
    return tuple(deg)

def kernel_rank_over_q(rows,ncols):
    mat=[[Fraction(x) for x in row] for row in rows if any(row)]
    pivots=[];r=0
    for c in range(ncols):
        p=next((j for j in range(r,len(mat)) if mat[j][c]),None)
        if p is None:continue
        mat[r],mat[p]=mat[p],mat[r]
        a=mat[r][c];mat[r]=[v/a for v in mat[r]]
        for j in range(len(mat)):
            if j!=r and mat[j][c]:
                a=mat[j][c];mat[j]=[v-a*w for v,w in zip(mat[j],mat[r])]
        pivots.append(c);r+=1
    return r,pivots

def main(output:Path):
    global TESTS
    TESTS=Counter()
    expanded,flags,bare,states,pos,d_free,degree=reconstruct()
    check(len(expanded)==51,'expanded_face_census')
    check(len(flags)==581,'flag_census')
    check(len(bare)==1169,'loaded_source_census')
    check(len(states)==2338,'corrected_source_census')
    for j,col in enumerate(d_free):
        check(not apply(d_free,col,quotient=False),'polynomial_d_squared')
        for i,p in col.items():
            check(degree(states[i])==degree(states[j])-1,'differential_chain_degree')
            for mon in p:
                gd=tuple(x+y for x,y in zip(internal_degree(states[i]),polynomial_degree(mon)))
                check(gd==internal_degree(states[j]),'differential_internal_degree')
    ds=[{i:p_reduce(p) for i,p in col.items() if p_reduce(p)} for col in d_free]
    for col in ds:check(not apply(ds,col),'normalization_quotient_d_squared')
    for i in range(12):check(not fibre_d(fibre_d({i:ONE})),'fibre_d_squared')
    check(fibre_d(Z)=={1:ONE},'fibre_unit_boundary')
    for i in range(12):
        vv={i:ONE}
        lhs=v_add(fibre_d(fibre_h(vv)),fibre_h(fibre_d(vv)))
        check(lhs==v_add(vv,fibre_ip(vv),-1),'fibre_deformation_retract')
    for i in range(12):check(not road(fibre_d({i:ONE})),'road_row_chain_identity')

    endpoints={'plus':PLUS,'minus':MINUS}
    indices={lab:pos[((face,),(),0)] for lab,face in endpoints.items()}
    rows={lab:[col.get(index,{}) for col in ds] for lab,index in indices.items()}
    maps={lab:[v_scale(Z,p) for p in row] for lab,row in rows.items()}
    # Independent endpoint basis lines must be retained for degree-zero homogeneity.
    line_weights={lab:tuple(-int(i in face) if i<9 else 0 for i in range(18))
                  for lab,face in endpoints.items()}
    for lab,m in maps.items():
        for j,col in enumerate(m):
            check(not p_eps(rows[lab][j]),'endpoint_connecting_coefficient_in_conductor_ideal')
            check(fibre_d(col)==apply(m,ds[j]),'endpoint_map_chain_equation')
            if col:
                check(degree(states[j])==1,'endpoint_map_chain_degree')
                for p in col.values():
                    for mon in p:
                        gd=tuple(a+b for a,b in zip(line_weights[lab],polynomial_degree(mon)))
                        check(gd==internal_degree(states[j]),'endpoint_map_framed_internal_degree')
        check(sum(bool(c) for c in m)==11,'endpoint_map_nonzero_source_columns')
        # Multiplication by every conductor coordinate has an explicit fibre primitive.
        for short in SHORT:
            hh=[{} for _ in states]
            hh[indices[lab]]=v_scale(Z,p_var(short))
            for j in range(len(states)):
                lhs=v_add(fibre_d(hh[j]),apply(hh,ds[j]))
                rhs=v_scale(m[j],p_var(short))
                check(lhs==rhs,'six_conductor_annihilating_homotopies')

    # The top-based fibre map is a distinct construction, with its canonical
    # nullhomotopy retained. It has a unit on [top,D03] but also on [top,v+].
    top=frozenset();itop=pos[((top,),(),0)]
    h_top=[{} for _ in states];h_top[itop]=v_scale(Z,p_scale(ONE,-1))
    m_top=[v_add(fibre_d(h_top[j]),apply(h_top,ds[j])) for j in range(len(states))]
    for j,col in enumerate(m_top):
        check(fibre_d(col)==fibre_reduce(apply(m_top,ds[j])),'top_map_chain_equation')
        if col:
            for p in col.values():
                for mon in p:check(polynomial_degree(mon)==internal_degree(states[j]),'top_map_internal_degree')
    generic_indices=[pos[((top,frozenset({l})),(),0)] for l in LONG]
    for j in generic_indices:check(m_top[j]==Z,'top_map_unit_long_flag')
    for lab,face in endpoints.items():
        j=pos[((top,face),(),0)]
        check(m_top[j]==Z,'top_map_lower_roof_collision')
    check(m_top[itop]=={1:p_scale(ONE,-1)},'top_map_conductor_component')

    # Rebuild all three named Morse chains from the supplied seven triangles.
    qd=frozenset({AD}); ec=frozenset({X1,X3}); er=frozenset({AD,X3})
    b1=frozenset({EXCEPTIONAL,X1,X3}); he=frozenset({EXCEPTIONAL,X3})
    bd=frozenset({EXCEPTIONAL,AD,X3}); c=frozenset({AD,X0,X3})
    def singleton(flag,scalar=ONE,sign=1,occ=0):
        return {pos[(tuple(flag),(),occ)]:p_scale(scalar,sign)}
    hm={}
    for apex,edge,left,right,scalar in [(top,ec,PLUS,b1,ONE),(top,he,b1,bd,ONE),(qd,er,bd,c,p_var(AD))]:
        hm=v_add(hm,singleton((apex,edge,right),scalar,-1))
        hm=v_add(hm,singleton((apex,edge,left),scalar,1))
    hm=v_add(hm,singleton((top,qd,bd)))
    xi={}
    for edge,left,right,scalar in [(ec,PLUS,b1,p_var(X1)),(he,b1,bd,occurrence((AD,X1))),(er,bd,c,p_var(AD))]:
        xi=v_add(xi,singleton((edge,right),scalar))
        xi=v_add(xi,singleton((edge,left),scalar,-1))
    qj=v_add(v_add(singleton((top,PLUS),ONE,-1),singleton((top,qd))),singleton((qd,c),p_var(AD)))
    dxi=apply(ds,xi)
    check(apply(ds,hm)==v_add(qj,v_scale(xi,p_var(X3)),-1),'full_loaded_morse_identity')
    def lift_occ(v):
        return {pos[(states[j][0],states[j][1],1)]:p for j,p in v.items()}
    hhat=v_add(hm,lift_occ(xi),-1)
    qhat=v_add(qj,lift_occ(dxi),-1)
    check(apply(ds,hhat)==qhat,'corrected_morse_identity')
    check(not apply(ds,qhat),'corrected_morse_boundary_closed')
    check(bool(qhat),'corrected_morse_boundary_not_deleted')
    raw_plus=p_scale(occurrence(PLUS),-1)
    check(apply(maps['plus'],qj)==v_scale(Z,raw_plus),'positive_roof_cubic_value')
    check(apply(maps['plus'],xi)==v_scale(Z,p_scale(occurrence((X1,X5)),-1)),'positive_gallery_quadratic_value')
    check(apply(maps['plus'],lift_occ(dxi))==v_scale(Z,raw_plus),'endpoint_correction_matches_cubic')
    for lab,m in [*maps.items(),('top',m_top)]:
        check(not apply(m,hhat),'corrected_thimble_image_zero')
        check(not apply(m,qhat),'corrected_boundary_image_zero')
    check(not apply(m_top,qj),'top_map_complete_roof_cancellation')
    check(not apply(maps['minus'],qj),'negative_endpoint_not_on_positive_roof')
    for m in maps.values():
        for j in generic_indices:check(not m[j],'endpoint_map_generic_flag_zero')

    # First conductor coefficients on all six endpoint normal circles and
    # all six one-occurrence incoming flags, plus both auxiliary occurrence states.
    jet_rows=[]
    for lab,face in endpoints.items():
        for k in sorted(face):
            j_normal=pos[((face,),(k,),0)]
            j_occ=pos[((face-{k},face),(),0)]
            check(rows[lab][j_normal]==normal(k),'endpoint_normal_circle_image')
            check(rows[lab][j_occ]==p_var(k),'endpoint_first_occurrence_flag_image')
            check(not {i:p_eps(p) for i,p in ds[j_normal].items() if p_eps(p)},
                  'derived_conductor_endpoint_circle_closed')
            for dd in ds:
                check(not p_eps(dd.get(j_normal,{})),
                      'derived_conductor_endpoint_circle_not_a_boundary_detector')
            jet_rows.append({'sheet':lab,'normal':'%d%d'%DIAGONALS[k],
                             'normal_circle_source_column':j_normal,
                             'normal_circle_coefficient':poly_json(normal(k)),
                             'incoming_flag_source_column':j_occ,
                             'incoming_flag_coefficient':poly_json(p_var(k))})
        j=pos[((face,),(),1)]
        check(rows[lab][j]==p_var(X3),'auxiliary_occurrence_generator_retained')
        check(not {i:p_eps(p) for i,p in ds[j].items() if p_eps(p)},
              'derived_conductor_auxiliary_occurrence_closed')
        for dd in ds:
            check(not p_eps(dd.get(j,{})),
                  'derived_conductor_auxiliary_occurrence_not_a_boundary_detector')

    # Independent all-coefficient proof in the accompanying note establishes
    # H^0 Hom(S,C)=C^2. This finite matrix is an additional exact control.
    zero_states=[j for j,s in enumerate(states) if degree(s)==0]
    zpos={j:k for k,j in enumerate(zero_states)}
    equations=[]
    for j,s in enumerate(states):
        if degree(s)!=1:continue
        row=[0]*len(zero_states)
        for i,p in ds[j].items():
            # Valid specialization of the conductor's spectator variables to 1.
            row[zpos[i]]=sum(p_eps(p).values())
        equations.append(row)
    rank,pivots=kernel_rank_over_q(equations,len(zero_states))
    check(rank==49,'conductor_h0_specialization_rank')
    free={zero_states[k] for k in range(51) if k not in pivots}
    check(free==set(indices.values()),'conductor_h0_specialization_free_endpoint_columns')

    # Homotopy-independence tests at the conductor: a nullhomotopy of m_sigma
    # would have endpoint scalar a in I and u_i(a-1)=0. The exact normal-form
    # argument is given in the note; verify the algebraic annihilator witnesses.
    for lab,face in endpoints.items():
        opposite=MINUS if lab=='plus' else PLUS
        for k in face:
            for j in opposite:
                check(not p_mul(normal(k),p_var(j)),'opposite_sheet_annihilator_control')
            check(bool(normal(k)),'normal_not_zero_in_glued_ring')
    check(not p_eps(p_var(X3)),'unit_road_condition_support_specialization')
    check(p_eps(ONE)==ONE,'unit_not_in_common_occurrence_ideal')

    basis_json=[state_name(s) for s in states]
    diff_json=[{'source':j,'target':i,'polynomial':poly_json(p)}
               for j,col in enumerate(ds) for i,p in sorted(col.items())]
    map_json={lab:[{'source_column':j,'source':state_name(states[j]),
                    'fibre_entries':{str(i):poly_json(p) for i,p in sorted(col.items())}}
                   for j,col in enumerate(m) if col] for lab,m in {**maps,'top':m_top}.items()}
    matrix_payload={'source_basis':basis_json,'source_differential':diff_json,'maps':map_json}
    digest=sha256(json.dumps(matrix_payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result={
        'schema':'marici.morse_relative_source_comparison.v1',
        'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'source_paths':['research/voevodsky/check_d03_pabs_morse_pullback.rs',
                        'research/voevodsky/check_d03_normalized_blowdown_counit.py',
                        'research/voevodsky/check_physical_derived_pullback_after_transform.py'],
        'coefficient_ring':{'variables':VARIABLES,'relations':'all X_i X_j with i positive and j negative',
                            'positive_shorts':['13','15','35'],'negative_shorts':['02','04','24'],
                            'short_graph':'u_i=t_i X_i','long_normals':'independent',
                            'additional_localizations':'none; identities extend to source monodromy units'},
        'counts':{'expanded_faces':len(expanded),'flags':len(flags),'loaded_states':len(bare),
                  'corrected_states':len(states),'source_ranks':dict(sorted(Counter(degree(s) for s in states).items())),
                  'source_nonzero_differential_entries':len(diff_json),
                  'plus_map_nonzero_columns':sum(bool(c) for c in maps['plus']),
                  'minus_map_nonzero_columns':sum(bool(c) for c in maps['minus']),
                  'top_map_nonzero_columns':sum(bool(c) for c in m_top)},
        'matrix_sha256':digest,
        'fibre':{'degrees':F_DEGREES,'z':{'2':1,'4':1},'road_row':[0,0,1,1,1],
                  'd_F_z':'conductor coordinate 1',
                  'homology':'I in homological degree one',
                  'endpoint_line_occurrence_weights':line_weights},
        'endpoint_maps':{'formula':'m_sigma(v)=z*lambda_sigma(d_S v) in degree one; zero otherwise',
                         'relative_boundary_homotopy':'zero',
                         'independent_detected_submodule':'C^2 with endpoint basis lines retained',
                         'annihilator_of_each_class':'I',
                         'ordinary_projection_to_J':'nullhomotopic by z*lambda_sigma',
                         'proof_not_exhaustive_computation':'nonvanishing uses exact Hom connecting sequence and annihilator argument in note'},
        'top_map':{'formula':'m_top=d_F h_top+h_top d_S, h_top(top)=-z',
                   'unit_on_each_pure_long_flag':True,'same_unit_on_lower_top_endpoint_flag':True,
                   'ordinary_fibre_class':'zero','support_Q_preservation':'fails if z is the fixed nonzero Q readout'},
        'morse_evaluation':{'positive_raw_roof':poly_json(raw_plus),
                            'positive_endpoint_correction':poly_json(raw_plus),
                            'corrected_roof_image':0,'corrected_thimble_image':0,
                            'raw_roof_first_nonzero_conductor_order':3},
        'first_symbol_rows':jet_rows,
        'derived_conductor_degree_one':{
            'target_H1':'I/I^2 with endpoint line copied as appropriate',
            'six_native_circle_images':'t_i [X_i] z_sheet; six independent source cycles',
            'auxiliary_occurrence_images':'[X35] z_sheet for each endpoint copy',
            'all_t_i_zero_control':'six native-circle images vanish; auxiliary occurrence directions are a separate factor'},
        'universal_unit_test':'For any coefficient chain map to F, r m(q_J p)=X35*r m(xi p); it cannot equal 1 in the unlocalized ring.',
        'physical_scope':{'relative_coefficient_maps_constructed':True,
                           'complete_corrected_morse_source_used':True,
                           'six_functor_spatial_correspondence_constructed':False,
                           'physical_endpoint_swap_identification':False,
                           'physical_Delta_J_value_determined':False,
                           'source_boundary_mapped_to_nonzero_homology_generator':False},
        'checks':dict(TESTS),'total_checks':sum(TESTS.values()),
        'source_basis_and_sparse_matrices':matrix_payload
    }
    output.mkdir(parents=True,exist_ok=True)
    path=output/'morse_relative_source_comparison_certificate.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['counts','matrix_sha256','total_checks','physical_scope']},indent=2))
    print('certificate:',path)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args()
    main(args.output)
