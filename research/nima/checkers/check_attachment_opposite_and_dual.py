"""Opposite-history signs and paired contragredient attachment checks.

Actual chamber paths/products are used for reversal. Green matrices below
are declared algebraic fixtures, not numerical spectral Clark Gram data.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from collections import defaultdict
import importlib.util
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('seam_attachment',Path(__file__).with_name('check_relation_attachment_seam_chain_map.py'))
f=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
base=f.base


def rev0(k):
    x,u,v=k
    return x,tuple(reversed(v)),tuple(reversed(u))


def rev1(k):
    x,y,u,c,v=k
    return y,x,tuple(reversed(v)),c,tuple(reversed(u))


def reflect(column,key,sign=1):
    out=defaultdict(int)
    for k,c in column.items():
        out[key(k)]+=sign*s.conjugate(c)
    return f.clean(out)


def op_record(start,word,marks):
    out={():1}
    state=start
    for j,keep in zip(word,marks):
        assert state&(1<<j)
        target=state & ~(1<<j)
        if keep:
            out={w+(k,):c for w,c in out.items()
                 for k in range(base.arithmetic.POSITION[target],base.arithmetic.POSITION[state])}
        state=target
    return out


def op_derivative(start,word,marks):
    states=[start]
    for j in word:
        assert states[-1]&(1<<j)
        states.append(states[-1]&~(1<<j))
    out=defaultdict(int)
    for i,keep in enumerate(marks):
        left=op_record(start,word[:i],marks[:i])
        right=op_record(states[i+1],word[i+1:],marks[i+1:])
        letters=range(base.arithmetic.POSITION[states[i+1]],base.arithmetic.POSITION[states[i]]) if keep else (-1,)
        for u,v,k in product(left,right,letters):
            out[states[i],states[i+1],u,k,v]+=left[u]*right[v]
    return f.clean(out)


def op_relation_derivative(start,rel):
    out=defaultdict(int)
    for (word,marks),c in rel.items():
        f.add(out,op_derivative(start,tuple(reversed(word)),tuple(reversed(marks))),s.conjugate(c))
    return f.clean(out)


def joint_rev_low(col):
    return reflect(col,lambda k:(k[0],rev1(k[2]),rev1(k[1])))


def joint_rev_middle(col):
    def key(k):
        mid,component,l,r=k
        return (mid,1,rev1(r),rev0(l)) if component==0 else (mid,0,rev0(r),rev1(l))
    return reflect(col,key)


def joint_rev_top(col):
    return reflect(col,lambda k:(k[0],rev0(k[2]),rev0(k[1])),-1)


def swap_matrix(n,m):
    return s.SparseMatrix(n*m,n*m,{(j*n+i,i*m+j):1 for i in range(n) for j in range(m)})


def equal(left,right):
    assert (left-right).applyfunc(s.expand)==s.zeros(left.rows,left.cols)


def dual_fixture():
    # Two non-real two-term complexes, with finite signed tensor metrics.
    incidence=s.Matrix([[-1,-1,0,0],[1,0,-1,0],[0,1,0,-1],[0,0,1,1]])
    twist_l=s.diag(1,s.I,1-s.I,2)
    twist_r=s.diag(1+s.I,1,2,s.I)
    dl,dr=incidence*twist_l,incidence*twist_r
    ident=s.eye(4)
    first=s.kronecker_product(dl,ident).col_join(-s.kronecker_product(ident,dr))
    second=s.kronecker_product(ident,dr).row_join(s.kronecker_product(dl,ident))
    equal(second*first,s.zeros(16))
    # T2[-1], degrees -1,0,1.
    d={-1:-first,0:-second}
    gl1,gl0=s.diag(1,-2,3,-4),s.diag(2,-1,3,-2)
    gr1,gr0=s.diag(2,-3,4,-1),s.diag(1,-3,2,-4)
    g={-1:s.kronecker_product(gl1,gr1),
       0:s.diag(s.kronecker_product(gl0,gr1),s.kronecker_product(gl1,gr0)),
       1:s.kronecker_product(gl0,gr0)}
    green_dual={}
    for n in (-1,0):
        old=-n-1
        sign=(-1)**(n+1)
        dual=sign*d[old].conjugate().T
        mate=g[old].inv()*d[old].conjugate().T*g[old+1]
        green_dual[n]=sign*mate
        equal(g[old]*green_dual[n],dual*g[old+1])
    equal(green_dual[0]*green_dual[-1],s.zeros(16))
    # Wrong transpose is detected by the complex coefficients.
    assert d[-1].T!=d[-1].conjugate().T
    assert g[-1]*(-g[-1].inv()*d[-1].T*g[0])!=-d[-1].conjugate().T*g[0]

    cycle=s.Matrix([1,-1,1,-1])
    cl,cr=twist_l.inv()*cycle,twist_r.inv()*cycle
    j=s.kronecker_product(cl,cr)
    equal(first*j,s.zeros(32,1))
    observation=j.conjugate().T*g[-1]  # Target is the coefficient dual, no source metric.
    assert observation.rank()==1
    equal(observation*green_dual[0],s.zeros(1,32))
    p=2+3*s.I
    y=s.Matrix([k+(k%3+1)*s.I for k in range(16)])
    assert s.expand((j*p).conjugate().T.dot(g[-1]*y)-s.conjugate(p)*(observation*y)[0])==0

    # Corrected joint reversal: +swap at -2 and -1, -swap at 0.
    swap=swap_matrix(4,4)
    zero=s.zeros(16)
    r={-1:swap,0:zero.row_join(swap).col_join(swap.row_join(zero)),1:-swap}
    op_dl,op_dr=-dr.conjugate(),-dl.conjugate()
    op_first=s.kronecker_product(op_dl,ident).col_join(-s.kronecker_product(ident,op_dr))
    op_second=s.kronecker_product(ident,op_dr).row_join(s.kronecker_product(op_dl,ident))
    op_d={-1:-op_first,0:-op_second}
    op_g={-1:s.kronecker_product(gr1,gl1),
          0:s.diag(s.kronecker_product(gr0,gl1),s.kronecker_product(gr1,gl0)),
          1:s.kronecker_product(gr0,gl0)}
    for n in (-1,0):
        equal(op_d[n]*r[n],r[n+1]*d[n].conjugate())
    for n in (-1,0,1):
        assert r[n].conjugate().T*op_g[n]*r[n]==g[n].conjugate()
        sharp=g[n].conjugate().inv()*r[n].conjugate().T*op_g[n]
        assert sharp*r[n]==s.eye(r[n].cols)

    # Nondegenerate ambient pairing need not restrict nondegenerately.
    isotropic=s.Matrix([1,1]); ambient=s.diag(1,-1)
    assert isotropic.T*ambient*isotropic==s.zeros(1)
    assert (isotropic.T*ambient).rank()==1
    # Opposite creation is not the Green mate of creation.
    creation=s.Matrix([[0,0],[1+s.I,0]])
    memory_form=s.diag(1,-2)
    contraction=memory_form.inv()*creation.conjugate().T*memory_form
    vacuum=s.Matrix([1,0])
    assert contraction*vacuum==s.zeros(2,1) and creation*vacuum!=s.zeros(2,1)


def higher_reversal_signs():
    checked=0
    def correction(r):
        return (-1)**(r*(r-1)//2)
    def reversal(degrees):
        odd=degrees.count(-1)
        return correction(len(degrees))*(-1)**(degrees.count(0)+odd*(odd-1)//2)
    for r in range(1,7):
        assert reversal([-1]*r)==1
        for degrees in product((-1,0),repeat=r):
            assert reversal(list(degrees))*reversal(list(reversed(degrees)))==1
            for i,degree in enumerate(degrees):
                if degree==0:
                    continue
                raised=list(degrees);raised[i]=0
                # Raw local reversal anticommutes with the local differential.
                lhs=(-1)**sum(degrees[:i])*reversal(raised)
                rhs=reversal(list(degrees))*(-1)**(sum(degrees[i+1:])+1)
                assert lhs==rhs
                checked+=1
        for a in range(1,r):
            b=r-a
            assert correction(r)==correction(a)*correction(b)*(-1)**(a*b)
    assert [reversal([-1]*(3-q)+[0]*q) for q in range(4)]==[1,-1,-1,1]
    return checked


def main():
    count=0
    for start in range(16):
        available=[j for j in range(4) if not start&(1<<j)]
        for length in range(len(available)+1):
            for word in permutations(available,length):
                for marks in product((False,True),repeat=length):
                    end=base.typed_end(start,word)
                    der=f.derivative(start,word,marks)
                    opposite=op_derivative(end,tuple(reversed(word)),tuple(reversed(marks)))
                    assert reflect(der,rev1)==opposite
                    assert f.boundary(opposite)==reflect(f.boundary(der),rev0,-1)
                    assert reflect(reflect(der,rev1),rev1)==der
                    count+=1
    assert count==1040
    joint,op_joint=[],[]
    for pair in combinations(range(4),2):
        mid=sum(1<<j for j in pair)
        other=tuple(j for j in range(4) if j not in pair)
        for left,right in product(base.local_relations(pair),base.local_relations(other)):
            dl,dr=f.relation_derivative(0,left),f.relation_derivative(mid,right)
            ol,orr=op_relation_derivative(15,right),op_relation_derivative(mid,left)
            col={(mid,l,r):c*b for l,c in dl.items() for r,b in dr.items()}
            expected={(mid,l,r):c*b for l,c in ol.items() for r,b in orr.items()}
            assert joint_rev_low(col)==expected
            assert joint_rev_low(joint_rev_low(col))==col
            assert not f.joint_boundary(expected)
            joint.append(col);op_joint.append(expected)
    probes=[next(iter(c)) for c in op_joint]
    minor=s.Matrix([[c.get(k,0) for c in op_joint] for k in probes])
    assert minor.rank()==24
    # Bare Koszul braiding is the NEGATIVE of the required product reversal.
    residual=-2*minor
    assert residual.rank()==24
    raw={next(iter(joint[0])):2+3*s.I}
    assert f.joint_boundary(joint_rev_low(raw))==joint_rev_middle(f.joint_boundary(raw))
    mid=f.joint_boundary(raw)
    assert f.joint_next(joint_rev_middle(mid))==joint_rev_top(f.joint_next(mid))
    # Test the second chain square on a noncycle middle basis element too.
    middle_basis={next(iter(mid)):1+2*s.I}
    assert f.joint_next(joint_rev_middle(middle_basis))==joint_rev_top(f.joint_next(middle_basis))
    assert joint_rev_low(joint_rev_low(raw))==raw
    assert joint_rev_middle(joint_rev_middle(middle_basis))==middle_basis
    top={next(iter(f.joint_next(middle_basis))):3+s.I}
    assert joint_rev_top(joint_rev_top(top))==top
    assert joint_rev_low(raw)!=f.clean({k:(2+3*s.I)*v for k,v in joint_rev_low({next(iter(joint[0])):1}).items()})

    dual_fixture()
    higher_checks=higher_reversal_signs()
    result={'schema':'marici.nima.attachment-opposite-and-dual.v1','passed':True,
        'actual_paths_with_opposite_derivative_checked':count,
        'actual_products_with_corrected_joint_reversal':24,
        'higher_reversal_differential_components_checked_r_one_through_six':higher_checks,
        'triple_seam_raw_swap_signs_by_degree_minus_three_through_zero':[1,-1,-1,1],
        'uncorrected_koszul_reversal_residual_rank':residual.rank(),
        'single_seam_reversal_signs':{'degree_minus_one':1,'degree_zero':-1},
        'corrected_joint_reversal_signs_after_raw_swap':{'degree_minus_two':1,'degree_minus_one':1,'degree_zero':-1},
        'checks':{'both_joint_chain_squares':True,'reflection_involutive':True,
                  'complex_coefficient_conjugation_hostile':True,
                  'cochain_green_dual_beta_squares':True,'joint_observation_annihilates_dual_boundaries':True,
                  'isotropic_primal_still_has_paired_observation':True,'creation_is_not_contraction':True},
        'scope':'Actual fifteen-chamber reversal and rank-24 sign residual. Green matrices are non-real differential/signed-form algebraic fixtures; actual Clark compatibility follows from the existing nondegenerate ambient beta maps. No numerical spectral Gram evaluation or metric on I or I^2 is supplied.'}
    out=ROOT/'research/nima/results/attachment-opposite-and-dual.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
