#!/usr/bin/env python3
"""Integral OS degree-two lattice and actual projective arrangement torus periods."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s
ROOT=Path(__file__).resolve().parents[3]
FLAGS='research/benincasa/results/history6_current_ordered_lifts.json'


def main():
    prior=json.loads((ROOT/FLAGS).read_text());assert prior['passed']
    for p,h in prior['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    assert prior['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_ordered_lifts.py').read_bytes()).hexdigest()
    r,z,u,v=s.symbols('r s u v')
    linear=[r,z,r+z,z+1];names=['R:r=0','S:s=0','L:r+s=0','D:s+1=0']
    pairs=list(itertools.combinations(range(4),2))
    wedge=[s.factor(s.Matrix([[s.diff(linear[i],r),s.diff(linear[i],z)],
        [s.diff(linear[j],r),s.diff(linear[j],z)]]).det()/(linear[i]*linear[j])) for i,j in pairs]
    # Affine chart of P2 minus its canonical infinity line. Degree-two
    # integral Orlik-Solomon relations: the origin triple and S,D parallel.
    relation=s.Matrix([[1,-1,0,1,0,0],[0,0,0,0,1,0]])
    assert (relation*s.Matrix(wedge)).applyfunc(s.factor)==s.zeros(2,1)
    # Basis eRS,eRL,eRD,eLD. Primitive unit relations eliminate eSL,eSD.
    reduction=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-1,1,0,0],[0,0,0,0],[0,0,0,1]])
    assert relation*reduction==s.zeros(2,4)
    basis=[wedge[i] for i in (0,1,2,5)]
    assert (s.Matrix(wedge)-reduction*s.Matrix(basis)).applyfunc(s.factor)==s.zeros(6,1)
    affine_intersections=[]
    for i,j in pairs:
        solutions=s.solve([linear[i],linear[j]],(r,z),dict=True)
        if not solutions:
            assert (i,j)==(1,3);continue
        point=solutions[0];members=[k for k,F in enumerate(linear) if F.subs(point)==0]
        key=tuple(str(point[q]) for q in (r,z))
        if not any(item['point']==list(key) for item in affine_intersections):
            affine_intersections.append({'point':list(key),'lines':[names[k] for k in members],'multiplicity':len(members)})
    assert sorted(item['multiplicity'] for item in affine_intersections)==[2,2,3]
    # Standard integral OS theorem: logarithmic forms divided by 2pi*i
    # generate torsion-free H* of this complex arrangement complement.
    b2=sum(item['multiplicity']-1 for item in affine_intersections);assert b2==4
    def res(coeff,word):
        for q in word:coeff=s.factor(s.residue(coeff,q,0))
        return coeff
    cycles=[]
    for label,sub,word in [('O_s_inner',{r:u,z:v},(v,u)),
                          ('O_r_inner',{r:u,z:v},(u,v)),
                          ('RD_double',{r:u,z:v-1},(u,v)),
                          ('LD_double',{r:u-v+1,z:v-1},(u,v))]:
        jac=s.Matrix([sub[r],sub[z]]).jacobian([u,v]).det()
        periods=[res(F.subs(sub,simultaneous=True)*jac,word) for F in basis]
        cycles.append({'cycle':label,'normals':{str(q):str(value) for q,value in sub.items()},
            'inner_outer_order':[str(q) for q in word],'basis_periods':[int(q) for q in periods]})
    pairing=s.Matrix([item['basis_periods'] for item in cycles]);assert pairing==s.Matrix([[1,0,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]])
    assert pairing.det()==1
    # Thus these ACTUAL small tori form a full integral two-cycle basis,
    # not merely a rational period screen or a guessed rank count.
    K,B=[s.sympify(q,locals={'r':r,'s':z}) for q in prior['triple_center']['projective_two_form_coefficients']]
    assert s.factor(K-basis[1]-basis[3])==0
    assert s.factor(B-basis[0]+basis[1]+basis[3])==0
    coefficients=s.Matrix([[0,1,0,1],[1,-1,0,-1]])
    periods=coefficients*pairing.T
    assert periods==s.Matrix([[0,1,0,1],[1,0,0,-1]])
    forget=s.Matrix([[1,1,0,0]])
    assert s.ones(1,2)*periods==forget
    kernel_forget=s.Matrix.hstack(s.Matrix([-1,1,0,0]),s.Matrix([0,0,1,0]),s.Matrix([0,0,0,1]))
    kernel_period=s.Matrix.hstack(s.Matrix([0,0,1,0]),s.Matrix([-1,1,0,-1]))
    assert forget*kernel_forget==s.zeros(1,3) and periods*kernel_period==s.zeros(2,2)
    assert periods.rank()==2 and kernel_period.rank()==2
    assert kernel_forget.rank()==3
    # Lifts of canonical class1 form Z3 torsor; split periods see only one
    # combination, leaving TWO additional invisible but nonzero classes.
    n,m,ell=s.symbols('n m ell',integer=True);lift=s.Matrix([1-n,n,m,ell])
    assert forget*lift==s.ones(1,1)
    assert periods*lift==s.Matrix([n+ell,1-n-ell])
    # Independently transport all six source normal flags into appropriate
    # affine projective charts. Record cycle classes, not only split periods.
    flag_classes=[]
    for flag in prior['ordered_flags']:
        word=flag['deletion_word'];outer=word[-1]
        if outer=='b4':
            sub={r:u,z:v};normal={'b2':u,'b3':v};orientation=1
        elif outer=='b2':
            sub={r:1/v,z:u/v};normal={'b3':u,'b4':v};orientation=1
        else:
            sub={r:u/v,z:1/v};normal={'b2':u,'b4':v};orientation=-1
        jac=s.factor(s.Matrix([sub[r],sub[z]]).jacobian([u,v]).det())
        order=tuple(normal[q] for q in word[:-1])
        row=s.Matrix([res(orientation*jac*F.subs(sub,simultaneous=True),order) for F in basis])
        coordinates=pairing.T.inv()*row
        assert all(q.is_Integer for q in coordinates)
        observed=periods*coordinates
        assert observed==s.Matrix(flag['fixed_normal_order_db2_db3_db4_periods'])
        flag_classes.append({'word':word,'outer_projective_chart':outer,'projective_orientation':orientation,
            'cycle_basis_coordinates':[int(q) for q in coordinates],'split_periods':[int(q) for q in observed]})
    flag_matrix=s.Matrix.hstack(*(s.Matrix(item['cycle_basis_coordinates']) for item in flag_classes))
    assert flag_matrix.rank()==4
    assert any(abs(flag_matrix[:,list(cols)].det())==1 for cols in itertools.combinations(range(6),4))
    # The two local center wall lifts can have equal split periods while
    # remaining distinct two-cycle classes. This is new gluing data.
    wall36=s.Matrix([-1,1,0,0]);wall58=s.Matrix([0,0,1,1])
    assert periods*wall36==periods*wall58==s.Matrix([1,-1])
    invisible_difference=wall58-wall36
    assert invisible_difference!=s.zeros(4,1) and periods*invisible_difference==s.zeros(2,1)
    paths=[FLAGS,'research/benincasa/checkers/check_history6_current_ordered_lifts.py']
    out={'schema':'marici.benincasa.history6-current-projective-lattice.v1','history_index':6,
        'space':'P2 minus canonical lines x=0,y=0,z=0 and added lines x+y=0,y+z=0; affine z1 chart is C2 minus r0,s0,r+s0,s+1=0.',
        'integral_topology_input':'Integral Orlik-Solomon theorem for complex hyperplane arrangements: torsion-free cohomology generated by normalized logarithmic forms. Complete affine degree2 relations are the origin triple and the parallel S,D pair.',
        'affine_intersections':affine_intersections,'betti_numbers':[1,4,4],
        'wedge_pair_order':[[names[i],names[j]] for i,j in pairs],
        'integral_degree2_relations':[[int(q) for q in row] for row in relation.tolist()],
        'integral_form_basis':['dlog(r) wedge dlog(s)','dlog(r) wedge dlog(r+s)',
            'dlog(r) wedge dlog(s+1)','dlog(r+s) wedge dlog(s+1)'],
        'cycles':cycles,'integral_pairing_determinant':1,
        'split_period_matrix':[[int(q) for q in row] for row in periods.tolist()],
        'E7_period_sign':'Multiply both projective period rows by -A3*delta(nu2)delta(nu3)delta(nu4); source orientation and normal convention unchanged.',
        'canonical_forgetful_map':[int(q) for q in forget],
        'forgetful_kernel_basis_columns':[[int(q) for q in row] for row in kernel_forget.tolist()],
        'simultaneous_split_period_kernel_basis_columns':[[int(q) for q in row] for row in kernel_period.tolist()],
        'canonical_class1_lift':{'cycle_coordinates':[str(q) for q in lift],
            'free_integral_parameters':['n','m','ell'],'split_periods':[str(q) for q in periods*lift],
            'meaning':'Canonical contour lifts form Z3 torsor. Splits see n+ell, not m or an independent n-versus-ell redistribution; two nonzero cycle directions are invisible.'},
        'all_six_source_flags':flag_classes,'source_flags_generate_full_integral_H2':True,
        'two_local_center_wall_lifts':{'p36':[int(q) for q in wall36],'p58':[int(q) for q in wall58],
            'equal_split_periods':[1,-1],'nonzero_invisible_difference':[int(q) for q in invisible_difference]},
        'scope_correction':'Unlike the single P1 center, this P2 complement DOES have nonzero classes annihilating both split periods. The prior P1 theorem remains valid in its stated scope.',
        'passed':True,'claim_boundary':'Integral local projective two-cycle lattice, actual unimodular torus pairing, conditional flag classes and missing gluing/lift data; not a physical cycle, global weighted-chain certificate or ordinary blowdown form.',
        'next_action':'Test full triple-center current covariance under GL3 normal-frame changes, transporting the complete five-line arrangement and cycle classes rather than just split periods. Compare overlap boundary maps to both P1 centers before proposing a physical source lift.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_projective_lattice.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'H2_rank':4,'actual_torus_pairing_det':1,'split_period_matrix':out['split_period_matrix'],
        'canonical_lift_rank':3,'invisible_split_kernel_rank':2,'six_source_flags_integrally_generate':True,
        'physical_admission':False},indent=2))

if __name__=='__main__':main()
