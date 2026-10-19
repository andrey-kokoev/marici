"""Explicit coframed metric comparisons. No physical calibration or fixed d.

State vectors use destination-labelled slots (zero at the source vertex), so
fiber comparison never depends on an arbitrary ordering of three neighbors.
"""
from field_refibration import EDGES

def pairing(left,right,metric,zero):
    return sum((left[i].flip(8)*metric[i,j]*right[j] for i in range(len(left)) for j in range(len(right))),zero)

def comparison_vectors(field,reference,zero):
    if set(field)!=set(EDGES) or any(len(v)!=3 for v in field.values()):raise ValueError('Expected twelve triples')
    if reference not in EDGES:raise ValueError('Invalid reference')
    selected=tuple(edge for edge in EDGES if edge!=reference)
    arrows=tuple(tuple(field[edge]) for edge in selected)
    states=tuple(tuple(zero if destination==source else field[source,destination][axis]
                      for destination in range(4) for axis in range(3)) for source in range(4))
    return selected,arrows,states

def readout(field,metric,reference,zero):
    selected,arrows,states=comparison_vectors(field,reference,zero)
    state_metric={(i,j):(metric[i%3,j%3] if i//3==j//3 else zero) for i in range(12) for j in range(12)}
    # Slot (i,j) is Y_j X_i, matching the owner's chronological parent convention.
    blocks={name:tuple(tuple(pairing(right,left,K,zero) for right in vectors) for left in vectors)
            for name,vectors,K in [('arrow',arrows,metric),('state',states,state_metric)]}
    return {'reference':reference,'selected_edges':selected,'blocks':blocks}

def project(field,operator,zero):
    return {edge:tuple(sum((operator.get((i,j),zero)*v[j] for j in range(3)),zero) for i in range(3)) for edge,v in field.items()}

def rectangular_legs(field,metric,reference,zero):
    selected,arrows,states=comparison_vectors(field,reference,zero)
    state_metric={(i,j):(metric[i%3,j%3] if i//3==j//3 else zero) for i in range(12) for j in range(12)}
    assigned={}
    for tag,vectors,K in [('a',arrows,metric),('s',states,state_metric)]:
        for i,v in enumerate(vectors):
            assigned[f'{tag}x{i}']=tuple((entry,) for entry in v)
            assigned[f'{tag}y{i}']=(tuple(sum((v[k].flip(8)*K[k,j] for k in range(len(v))),zero) for j in range(len(v))),)
    return assigned

def matmul(a,b,zero):
    if not a or not b or any(len(row)!=len(a[0]) for row in a) or any(len(row)!=len(b[0]) for row in b) or len(a[0])!=len(b):
        raise ValueError('Matrix shape mismatch')
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),zero) for j in range(len(b[0]))) for i in range(len(a)))

def rank(matrix,zero):
    rows=[list(row) for row in matrix];pivot=0
    for col in range(len(rows[0])):
        found=next((i for i in range(pivot,len(rows)) if rows[i][col]!=zero),None)
        if found is None:continue
        rows[pivot],rows[found]=rows[found],rows[pivot]
        value=rows[pivot][col];rows[pivot]=[x/value for x in rows[pivot]]
        for i in range(pivot+1,len(rows)):
            if rows[i][col]!=zero:
                value=rows[i][col];rows[i]=[x-value*y for x,y in zip(rows[i],rows[pivot])]
        pivot+=1
        if pivot==len(rows):break
    return pivot
