#!/usr/bin/env python3
"""Conditional ordered-residue lifts at both added divisors and their common center."""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_boundary_berezin_current import s
ROOT=Path(__file__).resolve().parents[3]
DIVISORS='research/benincasa/results/history6_current_split_divisors.json'
CORNER='research/benincasa/results/history6_quotient_boundary.json'
LINK='research/benincasa/results/history6_current_normal_link.json'


def main():
    receipts={p:json.loads((ROOT/p).read_text()) for p in (DIVISORS,CORNER,LINK)}
    for p,receipt in receipts.items():
        assert receipt['passed']
        for source,h in receipt['source_sha256'].items():assert sha256((ROOT/source).read_bytes()).hexdigest()==h,source
    assert receipts[DIVISORS]['checker_sha256']==sha256((ROOT/'research/benincasa/checkers/check_history6_current_split_divisors.py').read_bytes()).hexdigest()
    corner=receipts[CORNER]['source_corner_extraction'];assert corner['deleted_order']==['b2','b4'] and corner['deletion_parity']==-1
    x,y,z,r,t,a,c,u,v=s.symbols('b2 b3 b4 rho T r s u v')
    variables=(x,y,z);g=y*(x+y+z)/((x+y)*(y+z));h=1-g
    assert s.factor(g-s.sympify(receipts[CORNER]['source_c6'],locals={'b2':x,'b3':y,'b4':z}))==0
    F=[s.factor(weight/(x*y*z)) for weight in (g,h)]
    def scalar_residue(coeff,word):
        for normal in word:coeff=s.factor(s.residue(coeff,normal,0))
        return coeff
    def deletion_parity(word):
        remaining=['b1','b2','b3','b4','b5','b6','b7','b8'];sign=1
        for normal in word:
            idx=remaining.index(str(normal));sign*=(-1)**idx;remaining.pop(idx)
        return sign
    # Existing two-deletion word is regular on y!=0 and does not choose
    # between the OTHER center's decorated lifts without a completion word.
    original=[scalar_residue(q,(x,z)) for q in F]
    assert original==[1/y,0]
    assert deletion_parity((x,z))==-1
    assert -y*original[0]==s.Rational(corner['K0_coefficient'])
    flags=[];periods={}
    for word in itertools.permutations(variables):
        p=s.Matrix([scalar_residue(q,word) for q in F]);periods[word]=p
        assert p==(s.Matrix([0,1]) if word[0]==y else s.Matrix([1,0]))
        parity=deletion_parity(word)
        flags.append({'deletion_word':[str(q) for q in word],
            'radius_hierarchy':' < '.join('epsilon_'+str(q) for q in word),
            'fixed_normal_order_db2_db3_db4_periods':[int(q) for q in p],
            'source_eight_form_deletion_parity':parity,
            'raw_source_iterated_residue_coefficients':[int(q) for q in parity*p],
            'physical_admission':'Conditional contour flag only; not an owning-source selection.'})
    assert deletion_parity((x,z,y))*periods[x,z,y]==s.Matrix([1,0])
    # Compare every adjacent flag exchange. Correct orientation first:
    # walls remain nonzero even though total periods stay equal.
    exchanges=[]
    for word in itertools.permutations(variables):
        for i in (0,1):
            target=list(word);target[i],target[i+1]=target[i+1],target[i];target=tuple(target)
            if tuple(map(str,word))>=tuple(map(str,target)):continue
            delta=periods[target]-periods[word]
            assert sum(delta)==0
            nonzero=delta!=s.zeros(2,1)
            swapped={word[i],word[i+1]}
            assert nonzero==(i==0 and y in swapped)
            divisor='p36:b2+b3' if swapped=={x,y} else 'p58:b3+b4' if swapped=={y,z} else 'none:b2_b4_commute_after_orientation'
            exchanges.append({'from':[str(q) for q in word],'to':[str(q) for q in target],
                'wall':divisor,'orientation_corrected_split_difference':[int(q) for q in delta],
                'nonzero':nonzero})
    assert len(exchanges)==6 and sum(q['nonzero'] for q in exchanges)==2
    # Second two-normal center y=z=0, x!=0. Apply exactly the same
    # radial-first normal-current construction used at x=y=0.
    second=[s.factor(s.residue(-t*q.subs({y:r*t,z:t},simultaneous=True),t,0)) for q in F]
    assert second==[-1/(x*(r+1)),-1/(x*r*(r+1))]
    second_normal=[s.factor(x*q) for q in second]
    inv=s.Symbol('inverse_rho')
    second_R=s.Matrix([[s.residue(q,r,p) if p!=s.oo else s.residue(q.subs(r,1/inv)*(-1/inv**2),inv,0) for p in (0,-1,s.oo)] for q in second_normal])
    assert second_R==s.Matrix([[0,-1,1],[-1,1,0]])
    # Common triple center: projective normal fiber is P2, not the P1
    # of iteration2. Source dimension7 minus8 equals fiber2 minus codim3.
    substitution={x:a*t,y:c*t,z:t}
    jac=s.Matrix([a*t,c*t,t]).jacobian([a,c,t]).det();assert jac==t**2
    projective=[s.factor(s.residue(jac*q.subs(substitution,simultaneous=True),t,0)) for q in F]
    assert projective==[(a+c+1)/(a*(a+c)*(c+1)),1/(c*(a+c)*(c+1))]
    assert s.factor(sum(projective)-1/(a*c))==0
    # Source orientation moves three normals across b1, with minus sign.
    assert deletion_parity((x,y,z))==-1
    # Added projective lines meet at [x:y:z]=[1:-1:1], away from all
    # canonical coordinate lines. u=r+s,v=s+1 is orientation preserving.
    inverse={a:u-v+1,c:v-1}
    assert s.Matrix([u-v+1,v-1]).jacobian([u,v]).det()==1
    double=s.Matrix([scalar_residue(q.subs(inverse,simultaneous=True),(u,v)) for q in projective])
    assert double==s.Matrix([1,-1])
    assert scalar_residue((1/(a*c)).subs(inverse,simultaneous=True),(u,v))==0
    # The formal exceptional E7 is minus shared A3 times these P2 forms
    # and ordered external delta(nu2)delta(nu3)delta(nu4), not a contour.
    paths=[DIVISORS,CORNER,LINK,'research/benincasa/checkers/check_history6_current_split_divisors.py']
    out={'schema':'marici.benincasa.history6-current-ordered-lifts.v1','history_index':6,
        'owning_corner_word':corner,
        'corner_word_scope':'b2 then b4 is on b3!=0; regular g1_h0. Completing it with b3 gives one conditional flag, not source authorization of every other decorated contour.',
        'ordered_flags':flags,'adjacent_flag_exchanges':exchanges,
        'nonzero_exchange_count':2,
        'second_center':{'equations':['b3=0','b4=0'],'remaining_normal_base':'b2!=0',
            'direction':'rho=b3/b4','radial_first_coefficients_over_shared_center_current':[str(q) for q in second_normal],
            'residue_matrix_at_zero_minus1_infinity':[[int(q) for q in row] for row in second_R.tolist()],
            'status':'Conditional local incidence-current extension with grade1-2=7-8; not physical contour admission.'},
        'triple_center':{'equations':['b2=0','b3=0','b4=0'],
            'projective_chart':'b2=r*T,b3=s*T,b4=T; fiber=P2 of normal directions',
            'source_radial_first_orientation':-1,
            'projective_two_form_coefficients':[str(q) for q in projective],
            'conditional_E7_formula':'-A3*delta(nu2)delta(nu3)delta(nu4) times the displayed dr wedge ds forms, A3=N/(b1*b5*b6*b7*b8*J)|triple_center. The same ordered holomorphic delta and full degree8 normalized fermionic numerator are retained.',
            'grading':'fiber2 minus external codim3=-1=source7 minus8 bosonic constraints; fermionic degree8',
            'extra_lines':['r+s=0','s+1=0'],'extra_line_intersection':'[b2:b3:b4]=[1:-1:1], not positive, no canonical coordinate zero',
            'orientation_preserving_extra_line_normals':['u=r+s','v=s+1'],
            'double_residue_of_projective_forms':[int(q) for q in double],
            'double_residue_of_conditional_E7_over_A3_delta3':[int(q) for q in -double],
            'canonical_sum_double_residue':0,
            'scope_warning':'The P1 contour-kernel theorem of iteration2 is not a theorem about this P2 complement; additional cycle data can appear.'},
        'passed':True,'claim_boundary':'Conditional ordered-residue lifts with retained source signs, second-divisor wall and common triple-center projective forms. No exchange-independent split prescription or physical cycle inferred.',
        'next_action':'Compute the resolved projective normal arrangement complement at the triple center, its integral two-cycle/period lattice and forgetful map to the canonical complement. Determine the extra cycle-lift data and relations needed to glue the two P1 centers before proposing an owning-source physical prescription.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_current_ordered_lifts.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'conditional_flags':len(flags),'nonzero_adjacent_exchanges':2,
        'second_center_residue_matrix':out['second_center']['residue_matrix_at_zero_minus1_infinity'],
        'triple_center_extra_intersection_double_residue':[1,-1],'physical_admission':False},indent=2))

if __name__=='__main__':main()
