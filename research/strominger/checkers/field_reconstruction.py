"""Projector/cycle readout and exact reconstruction on an explicitly gated domain.

Returns a representative y and positive scale rho: y/sqrt(rho) is the original
field up to one common phase. No floating-point phase or square root is chosen.
"""
from itertools import combinations
from fractions import Fraction
from math import isqrt

def positive_real(value):
    """Certified sign in the source's chosen real embedding, not a float test."""
    if value.roots!=(2,3,5,-1) or any(value.c[8:]):raise ValueError('Expected a real source-field scalar')
    if not any(value.c):return False
    for bits in (8,16,32,64,128,256,512,1024,2048,4096):
        scale=1<<bits;lo=hi=Fraction(0)
        for mask,c in enumerate(value.c[:8]):
            if not c:continue
            radicand=1
            for bit,r in enumerate((2,3,5)):
                if mask&(1<<bit):radicand*=r
            n=radicand*scale*scale;k=isqrt(n)
            a=Fraction(k,scale);b=a if k*k==n else Fraction(k+1,scale)
            lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
        if lo>0:return True
        if hi<0:return False
    raise ValueError('Sign isolation budget exhausted')
from field_refibration import EDGES
from field_metric_comparisons import comparison_vectors,project,pairing,rank

def operator_readout(field,metric,operator,reference,zero):
    selected,right_arrows,right_states=comparison_vectors(field,reference,zero)
    _,left_arrows,left_states=comparison_vectors(project(field,operator,zero),reference,zero)
    state_metric={(i,j):(metric[i%3,j%3] if i//3==j//3 else zero) for i in range(12) for j in range(12)}
    blocks={name:tuple(tuple(pairing(right,left,K,zero) for right in rights) for left in lefts)
            for name,lefts,rights,K in [('arrow',left_arrows,right_arrows,metric),('state',left_states,right_states,state_metric)]}
    return {'reference':reference,'selected_edges':selected,'blocks':blocks}

def readout(field,metric,operators,reference,zero):
    if set(operators)!=set(('P','Q','C')):raise ValueError('Expected named P,Q,C channels')
    return {name:operator_readout(field,metric,op,reference,zero) for name,op in operators.items()}

def rref(matrix,zero,columns=None):
    rows=[list(row) for row in matrix]
    if not rows or any(len(row)!=len(rows[0]) for row in rows):raise ValueError('Invalid linear system')
    columns=len(rows[0]) if columns is None else columns
    pivots=[]
    for col in range(columns):
        start=len(pivots)
        found=next((i for i in range(start,len(rows)) if rows[i][col]!=zero),None)
        if found is None:continue
        rows[start],rows[found]=rows[found],rows[start]
        value=rows[start][col];rows[start]=[x/value for x in rows[start]]
        for i in range(len(rows)):
            if i!=start and rows[i][col]!=zero:
                value=rows[i][col];rows[i]=[x-value*y for x,y in zip(rows[i],rows[start])]
        pivots.append(col)
        if len(pivots)==len(rows):break
    return rows,pivots

def solve(matrix,values,zero):
    n=len(matrix[0]);rows,pivots=rref([list(row)+[b] for row,b in zip(matrix,values)],zero,n)
    if len(matrix)!=len(values):raise ValueError('Wrong right-hand-side size')
    if any(all(x==zero for x in row[:n]) and row[n]!=zero for row in rows):raise ValueError('Inconsistent measurements')
    if len(pivots)!=n:raise ValueError('Reference probes do not span the missing field triple')
    result=[zero]*n
    for row,col in zip(rows,pivots):result[col]=row[n]
    return tuple(result)

def intertwiner(P,C,Pt,Ct,zero,one):
    equations=[]
    for left,right in ((P,Pt),(C,Ct)):
        for i in range(3):
            for j in range(3):
                row=[zero]*9
                for k in range(3):
                    row[3*k+j]+=left.get((i,k),zero)
                    row[3*i+k]-=right[k][j]
                equations.append(row)
    rows,pivots=rref(equations,zero)
    free=[i for i in range(9) if i not in pivots]
    if len(free)!=1:raise ValueError('Named-operation intertwiner is not a unique line')
    solution=[zero]*9;solution[free[0]]=one
    for row,col in zip(rows,pivots):solution[col]=-row[free[0]]
    matrix=tuple(tuple(solution[3*i+j] for j in range(3)) for i in range(3))
    if rank(matrix,zero)!=3:raise ValueError('Intertwiner is singular')
    return matrix

def reconstruct_selected(data,metric,operators,zero,one):
    if set(data)!=set(operators) or set(data)!=set(('P','Q','C')):raise ValueError('Missing named measurement channel')
    reference=data['P']['reference'];selected=tuple(edge for edge in EDGES if edge!=reference)
    if reference not in EDGES:raise ValueError('Invalid reference')
    for channel in data.values():
        if channel['reference']!=reference or channel['selected_edges']!=selected:raise ValueError('Measurement provenance mismatch')
        if set(channel['blocks'])!=set(('arrow','state')):raise ValueError('Missing branch')
        for branch,n in (('arrow',11),('state',4)):
            m=channel['blocks'][branch]
            if len(m)!=n or any(len(row)!=n for row in m):raise ValueError('Wrong measurement shape')
    gram=tuple(tuple(data['P']['blocks']['arrow'][i][j]+data['Q']['blocks']['arrow'][i][j] for j in range(11)) for i in range(11))
    anchor=next((ids for ids in combinations(range(11),3) if rank(tuple(tuple(gram[j][i] for j in ids) for i in ids),zero)==3),None)
    if anchor is None:raise ValueError('Selected arrow fields do not span three dimensions')
    # Usual column Gram convention: M_rs = <anchor_r,anchor_s>.
    M=tuple(tuple(gram[j][i] for j in anchor) for i in anchor)
    def operator_in_anchor(name):
        block=data[name]['blocks']['arrow']
        columns=[solve(M,tuple(block[j][i] for i in anchor),zero) for j in anchor]
        return tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))
    S=intertwiner(operators['P'],operators['C'],operator_in_anchor('P'),operator_in_anchor('C'),zero,one)
    columns=tuple(tuple(S[i][j] for i in range(3)) for j in range(3))
    metric_image=tuple(tuple(pairing(columns[i],columns[j],metric,zero) for j in range(3)) for i in range(3))
    if not positive_real(M[0][0]):raise ValueError('Nonpositive anchor norm')
    rho=metric_image[0][0]/M[0][0]
    if not positive_real(rho):raise ValueError('Nonpositive normalization')
    if rho==zero or rho.flip(8)!=rho or any(metric_image[i][j]!=rho*M[i][j] for i in range(3) for j in range(3)):
        raise ValueError('Metric does not intertwine up to one common positive scale')
    field={}
    for j,edge in enumerate(selected):
        coefficients=solve(M,tuple(gram[j][i] for i in anchor),zero)
        field[edge]=tuple(sum((S[i][k]*coefficients[k] for k in range(3)),zero) for i in range(3))
    temporary=dict(field);temporary[reference]=(zero,zero,zero)
    measured=readout(temporary,metric,operators,reference,zero)
    for name in data:
        if any(measured[name]['blocks']['arrow'][i][j]!=rho*data[name]['blocks']['arrow'][i][j] for i in range(11) for j in range(11)):
            raise ValueError('Selected-arrow measurements are inconsistent')
    return {'representative':field,'normalization_squared':rho,'anchor_edges':tuple(selected[i] for i in anchor)}

def reconstruct(data,metric,operators,zero,one):
    selected_result=reconstruct_selected(data,metric,operators,zero,one)
    field=selected_result['representative'];rho=selected_result['normalization_squared']
    reference=data['P']['reference']
    a,t=reference;equations=[];values=[];probe_ranks={}
    for name in ('P','Q'):
        op=operators[name];local=[]
        for b in range(4):
            if b in (a,t):continue
            probe=field[b,t]
            row=tuple(sum((probe[i].flip(8)*metric[i,k]*op.get((k,j),zero) for i in range(3) for k in range(3)),zero) for j in range(3))
            remainder=zero
            for destination in range(4):
                if destination in (a,b,t):continue
                left=tuple(sum((op.get((i,k),zero)*field[a,destination][k] for k in range(3)),zero) for i in range(3))
                remainder+=pairing(field[b,destination],left,metric,zero)
            equations.append(row);local.append(row)
            values.append(rho*data[name]['blocks']['state'][a][b]-remainder)
        probe_ranks[name]=rank(local,zero)
    field[reference]=solve(equations,values,zero)
    # All 411 values must agree, including unused state and cycle measurements.
    predicted=readout(field,metric,operators,reference,zero)
    for name in data:
        for branch in ('arrow','state'):
            actual=data[name]['blocks'][branch];test=predicted[name]['blocks'][branch]
            if any(test[i][j]!=rho*actual[i][j] for i in range(len(actual)) for j in range(len(actual))):raise ValueError('Measurements fail full regenerated consistency')
    # Positive rho is certified in the source real embedding. Full regeneration
    # validates all channels against an actual field, rather than assuming PSD.
    return {'representative':field,'normalization_squared':rho,'anchor_edges':selected_result['anchor_edges'],'reference_probe_ranks':probe_ranks}
