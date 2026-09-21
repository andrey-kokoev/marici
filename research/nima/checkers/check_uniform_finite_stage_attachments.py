"""Exact regressions for finite-horizon attachment/refinement formulas."""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
from math import comb,factorial
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('descent',HERE/'check_seven_event_factorization_descent.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def ordered(start,column,k):
    out=defaultdict(int)
    for (word,marks),coefficient in column.items():
        states=[start]
        for j in word:states.append(states[-1]|(1<<j))
        for cuts in combinations(range(len(word)),k):
            markers=tuple(('e',states[i],states[i+1],marks[i]) for i in cuts)
            bounds=(-1,)+cuts+(len(word),)
            buffers=[f.record(states[left+1],word[left+1:right],marks[left+1:right])
                     for left,right in zip(bounds,bounds[1:])]
            for entries in product(*(b.items() for b in buffers)):
                value=coefficient
                for _,v in entries:value*=v
                out[markers,tuple(w for w,_ in entries)]+=value
    return f.clean(out)


def joint(columns):
    out=defaultdict(int)
    for entries in product(*(c.items() for c in columns)):
        markers=[];buffers=[];value=1
        for i,((x,y,u,k,v),coefficient) in enumerate(entries):
            value*=coefficient;markers.append(('e',x,y,k))
            if i==0:buffers.append(u)
            else:buffers[-1]+=u
            buffers.append(v)
        out[tuple(markers),tuple(buffers)]+=value
    return f.clean(out)


def complex_d(a,b,m):
    out=s.zeros(m-a,m-b)
    for i in range(m-b):out[b-a+i,i]=1
    return out


def projection(rows,cols):return s.eye(cols)[:rows,:]


def main():
    products=0;vanishings=0;nonminimal=0
    for k in range(1,5):
        kinds_list=list(product((0,1),repeat=k)) if k<=3 else [(0,)*k]
        for kinds in kinds_list:
            factors=[f.relation((2*i,2*i+1),kind) for i,kind in enumerate(kinds)]
            for tail_length in (0,1):
                local=list(factors)
                if tail_length:
                    local[-1]=f.multiply(local[-1],{((2*k,),(1,)):1})
                source=f.chain_product(local);cycles=[];state=0
                for factor in local:
                    cycles.append(f.derivative(state,factor))
                    state|=sum(1<<j for j in next(iter(factor))[0])
                actual=ordered(0,source,k)
                assert actual==joint(cycles) and actual
                assert not f.balanced_boundary(actual)
                products+=1;nonminimal+=tail_length
            # An extra relation has zero kth ordered derivative.
            larger=f.chain_product(factors+[f.relation((2*k,2*k+1),0)])
            assert not ordered(0,larger,k)
            vanishings+=1
            assert -k-(1-k)==-1 and -k-(-k)==0
    refinements=0;compositions=0
    for a,b,l,m in combinations(range(1,10),4):
        dm=complex_d(a,b,m);dl=complex_d(a,b,l)
        qm=projection(l-b,m-b);q0=projection(l-a,m-a)
        assert q0*dm==dl*qm
        km=s.zeros(m-b,m-l);k0=s.zeros(m-a,m-l)
        for i in range(m-l):km[l-b+i,i]=1;k0[l-a+i,i]=1
        assert qm*km==s.zeros(l-b,m-l)
        assert q0*k0==s.zeros(l-a,m-l)
        assert dm*km==k0  # kernel differential is identity in these coordinates.
        kernel_d=dm[l-a:,l-b:]
        contraction=s.eye(m-l)
        assert kernel_d*contraction==s.eye(m-l)
        assert contraction*kernel_d==s.eye(m-l)
        assert max(sum(abs(contraction[i,j]) for i in range(m-l)) for j in range(m-l))==1
        # The bottom G_b and the ordinary G_a observations are first coordinates.
        assert projection(1,l-b)*qm==projection(1,m-b)
        assert projection(1,l-a)*q0==projection(1,m-a)
        refinements+=1
    for a,b,h,l,m in combinations(range(1,10),5):
        assert projection(h-b,l-b)*projection(l-b,m-b)==projection(h-b,m-b)
        assert projection(h-a,l-a)*projection(l-a,m-a)==projection(h-a,m-a)
        compositions+=1
    weights=0
    for horizon,n,lam,radius in product(range(1,11),range(26),(1,2),(1,2)):
        total=sum((2*lam*radius)**j*factorial(j)*comb(n,j)
                  for j in range(1,min(n,horizon)+1))
        bound=(4*lam*radius)**horizon*factorial(horizon)*(1+n)**horizon
        assert total<=bound
        weights+=1
    result={'passed':True,'ordered_product_identities':products,
            'nonminimal_product_identities':nonminimal,'next_power_vanishings':vanishings,
            'refinement_kernel_and_chain_checks':refinements,
            'nested_refinement_compositions':compositions,'uniform_horizon_weight_checks':weights,
            'scope':'Finite regressions for a proof uniform in finite horizons. No inverse-limit realization or completed projectivity is tested or asserted.'}
    out=HERE.parent/'results/uniform-finite-stage-attachments.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
