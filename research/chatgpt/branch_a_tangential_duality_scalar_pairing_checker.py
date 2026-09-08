#!/usr/bin/env python3
"""Exact tangential-duality comparison and its scalar pairing on both excess traces.

Standalone: Python standard library only.  Coefficients are polynomials, not
floating point or values at sample points.  Builds the 50-state ambient
resolution of the full six-variable normalization ring, 100/500-state
resolutions of the occurrence/interval targets, and both 64-state-source
comparison maps.  The proof accompanying this checker establishes the
all-polynomial mapping-module classification by the dualizing truncation
triangle.  No flatness or freeness over the singular ring is imputed to its
ambient free resolution.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

VARIABLES=('X02','X04','X24','X13','X15','X35','beta','X03','X25')
SHORT=VARIABLES[:6]
ZERO=(0,)*len(VARIABLES)
NEG=(0,1,2)
POS=(3,4,5)
EMPTY=((),())
COUNTS=Counter()


def check(ok, family, detail=''):
    if not ok:
        raise AssertionError(f'{family}: {detail}')
    COUNTS[family]+=1


def put(v, key, c):
    if c:
        v[key]=v.get(key,0)+c
        if not v[key]:
            del v[key]


def add(v,w,scale=1):
    out=dict(v)
    for k,c in w.items():
        put(out,k,scale*c)
    return out


def mon(*indices):
    p=[0]*len(VARIABLES)
    for i in indices:
        p[i]+=1
    return tuple(p)


def plus(p,q):
    return tuple(a+b for a,b in zip(p,q))


def minus(p,q):
    return tuple(a-b for a,b in zip(p,q))


def multiply(v,p,c=1):
    out={}
    for (j,q),a in v.items():
        put(out,(j,plus(p,q)),c*a)
    return out


def apply(d,v):
    out={}
    for (j,p),c in v.items():
        for (i,q),a in d.get(j,{}).items():
            put(out,(i,plus(p,q)),c*a)
    return out


def normalize_R(v):
    return {(j,p):c for (j,p),c in v.items()
            if not(any(p[i] for i in NEG) and any(p[i] for i in POS))}


def scalar_apply(phi,v):
    out={}
    for (s,p),c in v.items():
        for (t,q),a in phi.items():
            if s==t:
                put(out,plus(p,q),c*a)
    return out


def ambient_resolution():
    states=[EMPTY]
    for n in range(1,6):
        for p in range(1,4):
            for q in range(1,4):
                if p+q==n+1:
                    states.extend((I,J) for I in combinations(NEG,p)
                                  for J in combinations(POS,q))
    degree={s:0 if s==EMPTY else len(s[0])+len(s[1])-1 for s in states}
    weight={s:mon(*(s[0]+s[1])) for s in states}
    d={s:{} for s in states}
    for I,J in states[1:]:
        s=(I,J)
        if degree[s]==1:
            d[s][(EMPTY,mon(*(I+J)))]=1
        else:
            if len(I)>1:
                for k,i in enumerate(I):
                    d[s][((I[:k]+I[k+1:],J),mon(i))]=(-1)**k
            if len(J)>1:
                for k,j in enumerate(J):
                    d[s][((I,J[:k]+J[k+1:]),mon(j))]=(-1)**(len(I)-1+k)
    check([sum(degree[s]==n for s in states) for n in range(6)]
          ==[1,9,18,15,6,1],'ambient_resolution_ranks')
    for s in states:
        check(not apply(d,d[s]),'ambient_resolution_square',s)
        check(all(degree[t]==degree[s]-1 for t,p in d[s]),'ambient_resolution_degree',s)
        check(all(plus(weight[t],p)==weight[s] for t,p in d[s]),'ambient_resolution_weight',s)
    return states,degree,weight,d


def tensor_resolution(pstates,pdegree,pweight,pd,interval=False):
    if interval:
        local=('p03','p25','g','h03','h25','p03k','p25k','gk','h03k','h25k')
        ld={'p03':2,'p25':2,'g':3,'h03':3,'h25':3,
            'p03k':3,'p25k':3,'gk':4,'h03k':4,'h25k':4}
        # Only short-coordinate weight is used here; long-coordinate degrees
        # and external orientation lines are recorded in the proof.
        lw={t:mon(5) if t.endswith('k') else ZERO for t in local}
        dt={t:{} for t in local}
        dt['g']={('p03',mon(7)):1,('p25',mon(8)):1}
        dt['h03']={('p03',mon(6,7)):1}
        dt['h25']={('p25',mon(6,8)):1}
        dt['p03k']={('p03',mon(5)):1}
        dt['p25k']={('p25',mon(5)):1}
        dt['gk']={('p03k',mon(7)):1,('p25k',mon(8)):1,('g',mon(5)):-1}
        dt['h03k']={('p03k',mon(6,7)):1,('h03',mon(5)):-1}
        dt['h25k']={('p25k',mon(6,8)):1,('h25',mon(5)):-1}
    else:
        local=('e0','e1');ld={'e0':3,'e1':4}
        lw={'e0':ZERO,'e1':mon(5)}
        dt={'e0':{},'e1':{('e0',mon(5)):-1}}
    for t in local:
        check(not apply(dt,dt[t]),'local_differential_square',t)
    states=[(s,t) for s in pstates for t in local]
    deg={(s,t):pdegree[s]+ld[t] for s,t in states}
    wt={(s,t):plus(pweight[s],lw[t]) for s,t in states}
    d={j:{} for j in states}
    for s,t in states:
        for (r,p),c in pd[s].items():
            put(d[s,t],((r,t),p),c)
        for (u,p),c in dt[t].items():
            put(d[s,t],((s,u),p),(-1)**pdegree[s]*c)
    for s in states:
        check(not apply(d,d[s]),'total_resolution_square',s)
        check(all(deg[t]==deg[s]-1 for t,p in d[s]),'total_resolution_degree',s)
    return states,deg,wt,d,local,ld,dt


def conductor_koszul():
    st=[J for n in range(7) for J in combinations(range(6),n)]
    dg={J:len(J)+2 for J in st}
    wt={J:mon(*J) for J in st}
    d={J:{(J[:k]+J[k+1:],mon(j)):(-1)**k for k,j in enumerate(J)} for J in st}
    for J in st:
        check(not apply(d,d[J]),'six_variable_source_square',J)
    return st,dg,wt,d


def raw_epsilon(which,J):
    out={}
    if len(J)==1 and J[0] in POS and (which=='E' or J[0]!=5):
        out[((EMPTY,'e0'),mon(*J))]=1
    if which=='R' and len(J)==2 and J[0] in POS and J[1]==5:
        out[((EMPTY,'e1'),mon(J[0]))]=1
    return out


def integer_solve(columns,rhs):
    """Rational row reduction, verified integral solution; free coordinates zero."""
    if not columns:
        check(not rhs,'empty_linear_system_consistent')
        return []
    keys=sorted(set(rhs)|{k for c in columns for k in c},key=repr)
    n=len(columns)
    rows=[[Fraction(c.get(k,0)) for c in columns]+[Fraction(rhs.get(k,0))] for k in keys]
    pivots=[];r=0
    for col in range(n):
        pivot=next((i for i in range(r,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        q=rows[r][col]
        rows[r]=[v/q for v in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][col]:
                a=rows[i][col]
                rows[i]=[u-a*v for u,v in zip(rows[i],rows[r])]
        pivots.append(col);r+=1
        if r==len(rows):
            break
    check(all(any(row[:n]) or not row[n] for row in rows),'comparison_lift_consistent')
    ans=[Fraction(0)]*n
    for i,col in enumerate(pivots):
        ans[col]=rows[i][-1]
    check(all(x.denominator==1 for x in ans),'comparison_lift_integral')
    ans=list(map(int,ans))
    got={}
    for c,a in zip(columns,ans):
        got=add(got,c,a)
    check(got==rhs,'comparison_lift_solution')
    return ans


def lift_epsilon(which,pdegree,ost,odg,owt,od,kst,kdg,kwt,kd):
    F={}
    for J in kst:
        raw=raw_epsilon(which,J)
        allowed=[]
        for t in ost:
            p=minus(kwt[J],owt[t])
            if odg[t]==kdg[J] and min(p)>=0 and pdegree[t[0]]>0:
                allowed.append((t,p))
        desired={}
        for (K,p),c in kd[J].items():
            desired=add(desired,multiply(F[K],p,c))
        check(not normalize_R(add(desired,apply(od,raw),-1))
              or bool(allowed),'raw_augmentation_lift_gate',(which,J))
        rhs=add(desired,apply(od,raw),-1)
        sol=integer_solve([apply(od,{k:1}) for k in allowed],rhs)
        F[J]=add(raw,{k:c for k,c in zip(allowed,sol) if c})
        check(apply(od,F[J])==desired,'resolved_excess_map_chain',(which,J))
        aug=normalize_R({(t,p):c for (t,p),c in F[J].items() if t[0]==EMPTY})
        check(aug==raw,'resolved_map_correct_augmentation',(which,J))
    return F


def serialize_vector(v):
    return [[s,list(p),c] for (s,p),c in sorted(v.items(),key=lambda kv:repr(kv[0]))]


def serialize_matrix(M):
    return [[s,serialize_vector(v)] for s,v in M.items() if v]


def total_map(local_map,pstates,states):
    return {(s,t):{((s,u),p):c for (u,p),c in local_map.get(t,{}).items()}
            for s,t in states}


def verify_map(F,source,ds,dt,label):
    for s in source:
        check(apply(dt,F.get(s,{}))==apply(F,ds.get(s,{})),label,s)


def run(output):
    ps,pdg,pwt,pd=ambient_resolution()
    os,odg,owt,od,_,_,_=tensor_resolution(ps,pdg,pwt,pd)
    ts,tdg,twt,td,tl,tld,tldiff=tensor_resolution(ps,pdg,pwt,pd,True)
    ks,kdg,kwt,kd=conductor_koszul()
    check((len(ps),len(os),len(ts),len(ks))==(50,100,500,64),'full_state_counts')
    FE=lift_epsilon('E',pdg,os,odg,owt,od,ks,kdg,kwt,kd)
    FR=lift_epsilon('R',pdg,os,odg,owt,od,ks,kdg,kwt,kd)
    check((sum(map(len,FE.values())),sum(map(len,FR.values())))==(52,46),'lift_nonzero_counts')

    top=(NEG,POS)
    omit=(NEG,POS[:-1])
    phiO={((top,'e0'),ZERO):1,((omit,'e1'),ZERO):-1}
    phi={t:{((top,t),ZERO):1,((omit,t+'k'),ZERO):-1} for t in ('g','h03','h25')}
    for s in os:
        check(not scalar_apply(phiO,od[s]),'occurrence_duality_cocycle',s)
    for name,f in phi.items():
        for s in ts:
            check(not scalar_apply(f,td[s]),'interval_duality_cocycle',(name,s))
    # Dropping either dualizing component violates the top chain equation.
    bad={((top,'e0'),ZERO):1}
    check(scalar_apply(bad,od[top,'e1'])=={mon(5):1},'essential_dualizing_correction')

    qlocal={'g':{('e0',ZERO):1},'gk':{('e1',ZERO):1}}
    q=total_map(qlocal,ps,ts)
    verify_map(q,ts,td,od,'full_endpoint_quotient_chain')
    endpoints={j for j in ts if j[1] not in ('g','gk')}
    for s in endpoints:
        check(all(t in endpoints for t,p in td[s]),'both_endpoint_packets_subcomplex',s)
        check(not q[s],'quotient_keeps_endpoint_kernel',s)
        check(not scalar_apply(phi['g'],{(s,ZERO):1}),'relative_duality_endpoint_zero',s)
    for s in ts:
        check(scalar_apply(phiO,q[s])==scalar_apply(phi['g'],{(s,ZERO):1}),
              'relative_duality_factorization',s)
    xi0={('g',mon(6)):-1,('h03',ZERO):1,('h25',ZERO):1}
    xi1={('gk',mon(6)):-1,('h03k',ZERO):1,('h25k',ZERO):1}
    jxi=total_map({'e0':xi0,'e1':xi1},ps,os)
    verify_map(jxi,os,od,td,'both_endpoints_xi_chain')
    full={name:{J:apply(jxi,F[J]) for J in ks} for name,F in [('E',FE),('R',FR)]}
    for name,F in full.items():
        verify_map(F,ks,kd,td,'full_trace_lift_chain_'+name)
        check(sum(map(len,F.values()))=={'E':156,'R':138}[name],'full_trace_lift_counts',name)

    results={}
    for name,F in [('E',FE),('R',FR)]:
        comp={J:scalar_apply(phiO,F[J]) for J in ks if scalar_apply(phiO,F[J])}
        check(comp=={tuple(range(6)):{ZERO:1}},'occurrence_trace_scalar_unit',name)
        results[name]=[[J,[[list(p),c] for p,c in v.items()]] for J,v in comp.items()]
    pairing={}
    for name,f in phi.items():
        expected={'g':{mon(6):-1},'h03':{ZERO:1},'h25':{ZERO:1}}[name]
        pairing[name]={}
        for trace,F in full.items():
            comp={J:scalar_apply(f,F[J]) for J in ks if scalar_apply(f,F[J])}
            check(comp=={tuple(range(6)):expected},'full_trace_duality_pairing',(name,trace))
            pairing[name][trace]=[[list(p),c] for p,c in expected.items()]
        for J in ks:
            check(not scalar_apply(f,add(full['E'][J],full['R'][J],-1)),
                  'relation_difference_scalar_zero',(name,J))

    # Complete polynomial relations among the three tangential classes.
    relation_homotopies={}
    for side,var in [('03',7),('25',8)]:
        H={((top,'p'+side),ZERO):-1,((omit,'p'+side+'k'),ZERO):-1}
        rel=add(multiply(phi['g'],mon(var)),multiply(phi['h'+side],mon(6,var)))
        for s in ts:
            check(scalar_apply(H,td[s])==scalar_apply(rel,{(s,ZERO):1}),
                  'all_polynomial_duality_relation',(side,s))
        relation_homotopies[side]=serialize_vector(H)
    # Explicit finite-adjunction currying.  Move T past P_R with the
    # Koszul sign, retaining the 50-state ambient dual rather than its
    # conductor cohomology alone.
    dual={s:{} for s in ps}
    for source,column in pd.items():
        for (target,power),coefficient in column.items():
            put(dual[target],(source,power),(-1)**(pdg[target]+1)*coefficient)
    for s0 in ps:
        check(not apply(dual,dual[s0]),'ambient_dual_square',s0)
    curried={}
    for name,f in phi.items():
        C={t:{} for t in tl}
        for ((s0,t),power),coefficient in f.items():
            put(C[t],(s0,power),(-1)**(pdg[s0]*tld[t])*coefficient)
        for t in tl:
            check(apply(dual,C[t])==apply(C,tldiff[t]),'explicit_curry_chain',(name,t))
        curried[name]=serialize_matrix(C)
    # The conductor quotient of the full target: closure and boundary matrices.
    # a,b,c,d,e correspond to g,h03,h25,p03k,p25k.
    # Closure forces d=e=0 over A, since beta*X03 and beta*X25 are nonzerodivisors.
    presentation=[['X03','X25'],['beta*X03','0'],['0','beta*X25']]
    readout={(0,mon(6)):-1,(1,ZERO):1,(2,ZERO):1}
    rel_x={(0,mon(7)):1,(1,mon(6,7)):1}
    rel_v={(0,mon(8)):1,(2,mon(6,8)):1}
    check(not scalar_apply(readout,rel_x),'scalar_relation_X03')
    check(not scalar_apply(readout,rel_v),'scalar_relation_X25')
    # Unimodular splitting by scalar coordinate, without beta localization.
    B={0:{(1,ZERO):1},1:{(0,ZERO):1,(1,mon(6)):1},
       2:{(1,ZERO):-1,(2,ZERO):1}}
    Bi={0:{(0,mon(6)):-1,(1,ZERO):1},
        1:{(0,ZERO):1},2:{(0,ZERO):1,(2,ZERO):1}}
    for i in range(3):
        check(apply(B,apply(Bi,{(i,ZERO):1}))=={(i,ZERO):1},'unimodular_scalar_split',i)
        check(apply(Bi,apply(B,{(i,ZERO):1}))=={(i,ZERO):1},'unimodular_scalar_split_inverse',i)
    check(apply(Bi,rel_x)=={(1,mon(7)):1},'split_relation_X03')
    check(apply(Bi,rel_v)=={(1,mon(8)):1,(2,mon(6,8)):1},'split_relation_X25')

    cert={
      'schema':'marici.branchA.tangential_duality_scalar_pairing.v1',
      'status':'constructed_relative_derived_tangential_comparison_and_universal_scalar_collapse',
      'variables':VARIABLES,
      'base_ring':'A=Z[beta,X03,X14,X25]; X14 is a spectator in every exported matrix',
      'ambient_ring':'S=A[X02,X04,X24,X13,X15,X35]',
      'normalization_ring':'R=S/(all nine negative-positive short products)',
      'ordered_volume':['dX02','dX04','dX24','dX13','dX15','dX35'],
      'external_lines':'All formulas use the inherited ordered native-pair and interval frames; restore their duals on tangential maps.',
      'ambient_resolution':{'ranks':[1,9,18,15,6,1],'differential':serialize_matrix(pd)},
      'source_koszul':{'ranks':[1,6,15,20,15,6,1],'shift':2,'differential':serialize_matrix(kd)},
      'occurrence_target_resolution':{'states':len(os),'differential':serialize_matrix(od)},
      'full_target_resolution':{'states':len(ts),'differential':serialize_matrix(td)},
      'duality_cocycle_on_occurrence':serialize_vector(phiO),
      'duality_cocycles_on_full_interval':{k:serialize_vector(v) for k,v in phi.items()},
      'explicit_curried_chain_maps':curried,
      'dualizing_differential_shifted_by_two':serialize_matrix(dual),
      'all_polynomial_relation_homotopies':relation_homotopies,
      'epsilon_lifts':{'E':serialize_matrix(FE),'R':serialize_matrix(FR)},
      'full_trace_lifts':{k:serialize_matrix(v) for k,v in full.items()},
      'endpoint_quotient':serialize_matrix(q),
      'xi_inclusion':serialize_matrix(jxi),
      'endpoint_connector':serialize_matrix({s:{(t,p):c for (t,p),c in td[s].items() if t in endpoints}
                                            for s in ts if s not in endpoints}),
      'occurrence_trace_compositions':results,
      'full_scalar_pairing':pairing,
      'mapping_module_presentation':presentation,
      'mapping_module_scalar_readout':['-beta','1','1'],
      'relative_scalar_readout':['-beta','-beta'],
      'unit_normalized_relative_readout':[1,1],
      'normalized_relative_scope':'beta invertible; raw map and both other generators remain polynomial at beta=0',
      'universal_kernel_on_recorded_trace_lattice':[1,-1],
      'all_polynomial_classification_proof':'Dualizing triangle has branch-volume terms in homological degrees 5 and 6. Perfect T has terms only in 2..4. Hence Hom(T,D[2])=Hom(T,A[3]); compute its three-coordinate cokernel. No finite-degree extrapolation.',
      'limitations':[
        'The ambient free models are S-free, not strict R-free models of the dualizing object.',
        'The relative map has zero restrictions to both interval endpoint packets; it is not an unproved positive endpoint-normalized PC trace.',
        'Scalar duality kills the nonzero conormal/source-relation difference; it is not a faithful substitute for the two-grade normalization readout.',
        'The physical Delta_J and the spatial reciprocal/tangential realization are not identified.'
      ],
      'counts':dict(sorted(COUNTS.items()))
    }
    canonical=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
    cert['certificate_content_sha256']=sha256(canonical).hexdigest()
    output.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':cert['status'],'exact_checks':sum(COUNTS.values()),
                      'relative_pairing':[-1,-1],'relative_pairing_factor':'beta',
                      'general_pairing':'(-beta*a+b+c)*(1,1)',
                      'certificate_content_sha256':cert['certificate_content_sha256']},sort_keys=True))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_tangential_duality_scalar_pairing_certificate.json'))
    args=parser.parse_args()
    run(args.output)
