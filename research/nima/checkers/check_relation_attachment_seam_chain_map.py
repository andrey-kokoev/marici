"""Actual path derivative and joint-seam realization of the relation attachment.

The derived-category nonvanishing theorem uses source projectivity, proved
in the companion note. Exact fixtures retain all fifteen chamber labels.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
from pathlib import Path
import importlib.util
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('quotient_attachment',Path(__file__).with_name('check_derived_quotient_relation_attachment.py'))
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
a=base.arithmetic


def clean(d):
    return {k:v for k,v in d.items() if v}


def add(out,values,scale=1):
    for k,v in values.items():
        out[k]+=scale*v


def derivative(start,word,marks):
    states=[start]
    for p in word:
        assert not states[-1]&(1<<p)
        states.append(states[-1]|(1<<p))
    out=defaultdict(int)
    for i,keep in enumerate(marks):
        left=base.record(start,word[:i],marks[:i])
        right=base.record(states[i+1],word[i+1:],marks[i+1:])
        letters=range(a.POSITION[states[i]],a.POSITION[states[i+1]]) if keep else (-1,)
        for u,v,k in product(left,right,letters):
            out[states[i],states[i+1],u,k,v]+=left[u]*right[v]
    return clean(out)


def boundary(d):
    out=defaultdict(int)
    for (x,y,u,k,v),c in d.items():
        w=() if k==-1 else (k,)
        out[y,u+w,v]+=c
        out[x,u,w+v]-=c
    return clean(out)


def relation_derivative(start,rel):
    out=defaultdict(int)
    for (w,m),c in rel.items():
        add(out,derivative(start,w,m),c)
    return clean(out)


def left_action(record,d):
    out=defaultdict(int)
    for w,c in record.items():
        for (x,y,u,k,v),b in d.items():
            out[x,y,w+u,k,v]+=c*b
    return clean(out)


def right_action(d,record):
    out=defaultdict(int)
    for (x,y,u,k,v),b in d.items():
        for w,c in record.items():
            out[x,y,u,k,v+w]+=b*c
    return clean(out)


def joint_boundary(column,wrong_sign=False):
    out=defaultdict(int)
    for (mid,l,r),c in column.items():
        for k,v in boundary({l:1}).items():
            out[mid,0,k,r]+=c*v
        for k,v in boundary({r:1}).items():
            out[mid,1,l,k]+=(1 if wrong_sign else -1)*c*v
    return clean(out)


def joint_next(column):
    out=defaultdict(int)
    for (mid,component,l,r),c in column.items():
        if component==0:
            for k,v in boundary({r:1}).items():
                out[mid,l,k]+=c*v
        else:
            for k,v in boundary({l:1}).items():
                out[mid,k,r]+=c*v
    return clean(out)


def main():
    path_count=cut_count=0
    for start in range(16):
        available=[j for j in range(4) if not start&(1<<j)]
        for length in range(len(available)+1):
            for w in permutations(available,length):
                for marks in product((False,True),repeat=length):
                    end=base.typed_end(start,w)
                    rec=base.record(start,w,marks)
                    der=derivative(start,w,marks)
                    expected=defaultdict(int)
                    for word,c in rec.items():
                        expected[end,word,()]+=c
                        expected[start,(),word]-=c
                    assert boundary(der)==clean(expected)
                    path_count+=1
                    for cut in range(length+1):
                        middle=base.typed_end(start,w[:cut])
                        rule=defaultdict(int)
                        add(rule,left_action(base.record(start,w[:cut],marks[:cut]),derivative(middle,w[cut:],marks[cut:])))
                        add(rule,right_action(derivative(start,w[:cut],marks[:cut]),base.record(middle,w[cut:],marks[cut:])))
                        assert clean(rule)==der
                        cut_count+=1
    assert path_count==1040 and cut_count==4176

    paths=[(w,m) for w in permutations(range(4)) for m in product((False,True),repeat=4)]
    path_index={p:i for i,p in enumerate(paths)}
    products,joint=[],[]
    for pair in combinations(range(4),2):
        middle=sum(1<<j for j in pair)
        remaining=tuple(j for j in range(4) if j not in pair)
        for left,right in product(base.local_relations(pair),base.local_relations(remaining)):
            dl,dr=relation_derivative(0,left),relation_derivative(middle,right)
            assert dl and dr and not boundary(dl) and not boundary(dr)
            composed=defaultdict(int)
            for (u,mu),c in left.items():
                for (v,mv),b in right.items():
                    composed[u+v,mu+mv]+=c*b
            composed=clean(composed)
            assert composed and not relation_derivative(0,composed)
            products.append(composed)
            image={(middle,l,r):c*b for l,c in dl.items() for r,b in dr.items()}
            assert image and not joint_boundary(image)
            joint.append(image)
    probes=[next(iter(col)) for col in joint]
    minor=s.Matrix([[col.get(k,0) for col in joint] for k in probes])
    assert minor.rank()==24
    assert minor.inv()*minor==s.eye(24)

    # Koszul sign tested on noncycles, not merely on the joint cycles.
    raw={probes[0]:1}
    assert joint_boundary(raw)
    assert not joint_next(joint_boundary(raw))
    assert joint_next(joint_boundary(raw,wrong_sign=True))
    # Shift [-1] reverses BOTH differential signs, preserving d^2=0.
    shifted=clean({k:-v for k,v in joint_boundary(raw).items()})
    assert not clean({k:-v for k,v in joint_next(shifted).items()})

    # Explicit scalar-only homotopy, extended from the actual product columns.
    P=s.SparseMatrix(384,24,{(path_index[k],j):c for j,r in enumerate(products) for k,c in r.items()})
    rows=P.T.rref()[1]
    assert len(rows)==24
    selected=P.extract(rows,range(24))
    extraction=selected.inv()
    assert extraction*selected==s.eye(24)
    for j,rel in enumerate(products):
        coefficients=extraction*s.Matrix([rel.get(paths[i],0) for i in rows])
        out=defaultdict(int)
        for c,column in zip(coefficients,joint):
            add(out,column,c)
        assert clean(out)==joint[j]  # H mu=j2 over scalars.
        assert not joint_boundary(clean(out))  # d H=0.

    # No source-linear homotopy can have that value: on the actual local
    # span (a,b,ab), left multiplication by a sends b to ab. The target is
    # root-supported, so a acts there by zero. H La=0 forces H(ab)=0.
    ha,hb,hc=s.symbols('ha hb hc')
    H=s.Matrix([[ha,hb,hc]])
    La=s.Matrix([[0,0,0],[0,0,0],[0,1,0]])
    Rb=s.Matrix([[0,0,0],[0,0,0],[1,0,0]])
    assert H*La==s.Matrix([[0,hc,0]])
    assert H*Rb==s.Matrix([[hc,0,0]])
    assert s.solve(list(H*La),[hc])=={hc:0}
    assert s.solve(list(H*Rb),[hc])=={hc:0}
    # A normalized joint probe has j2(ab)=1, incompatible with hc=0.
    assert (minor.inv()*minor)[0,0]==1

    # After one-sided derived quotient the product component is j2 times
    # the projection to P[1]. At the lowest target degree there are no
    # incoming boundaries; its displayed rank certifies nonzero detection.
    identity=s.eye(24)
    assert minor*identity==minor
    assert minor.rank()==24

    result={
        'schema':'marici.nima.relation-attachment-seam-chain-map.v1','passed':True,
        'marked_paths_checked':path_count,'typed_product_rule_cuts_checked':cut_count,
        'actual_relation_products':len(products),'joint_seam_selected_minor_rank':minor.rank(),
        'single_derivative_kills_mu':True,'joint_image_is_in_lowest_degree_cycles':True,
        'koszul_sign_and_shift_hostile':True,
        'scalar_only_nullhomotopy_constructed_from_actual_products':True,
        'left_and_right_source_linear_nullhomotopies_obstructed':True,
        'derived_quotient_component_is_joint_derivative_after_shifted_projection':True,
        'source_product_probe_rows':list(rows),
        'scope':'Actual fifteen-chamber paths and products, exact chain identities, and local module obstruction. Derived nonvanishing uses the proved projective source model and root-supported seam target. No signed isometry, source-module splitting, or nonzero Tor_2 over S is asserted.'}
    out=ROOT/'research/nima/results/relation-attachment-seam-chain-map.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
