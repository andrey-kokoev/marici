"""Joint carrier probes carrying actual matrix slot responses.

State responses and reversal-class arrow sums have an explicit decoder. Retained
within-class records recover individual slots. Identity evaluation reproduces
the original equal-slot assembly; uniform carrier averaging is a different map.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import runpy
from biclique_complex import add_scaled

root=Path(__file__).parent
p=runpy.run_path(str(root/'check_carrier_probe_adapter.py'))
a=runpy.run_path(str(root/'check_shared_leg_dg_realization.py'))
add,scale,mul,Z=a['add'],a['scale'],a['mul'],a['Z']
group,edges,selected=p['group'],p['edges'],p['selected']
columns=p['arrow_slots']+p['state_slots']
values=a['values']; d4=values['d']  # fixed reference value supplied by this fixture
x=[values[f'ax{i}'] for i in range(11)]; y=[values[f'ay{j}'] for j in range(11)]
s=[values[f'sx{i}'] for i in range(4)]; t=[values[f'sy{j}'] for j in range(4)]


def total(matrices):
    out=Z
    for matrix in matrices: out=add(out,matrix)
    return out


def responses(x,y,s,t):
    return [add(mul(y[j],x[i]),scale(-1,d4)) for i,j in product(range(11),repeat=2)]+[
            add(mul(t[j],s[i]),scale(-1,d4)) for i,j in product(range(4),repeat=2)]


def encode(residuals,probe_columns=columns):
    out={}
    for column,R in zip(probe_columns,residuals):
        for index,c in column.items(): out[index]=add(out.get(index,Z),scale(c/F(137),R))
    return {i:v for i,v in out.items() if v!=Z}


R=responses(x,y,s,t); field=encode(R)
identity_index=group.index(tuple(range(4)))
assert field.get(24*identity_index+identity_index,Z)==scale(F(1,137),total(R))
# Pointwise probe-factorized construction has the original typed multiplication
# order and keeps arrow and state intermediate spaces separate.
for gi,g in enumerate(group):
    X=total(scale(p['fixed'][j].get(gi,0),x[i]) for i,j in enumerate(selected))
    S=total(scale(p['points'][i].get(gi,0),s[i]) for i in range(4))
    for hj,h in enumerate(group):
        Y=total(scale(p['fixed'][j].get(hj,0),y[i]) for i,j in enumerate(selected))
        T=total(scale(p['points'][i].get(hj,0),t[i]) for i in range(4))
        count=sum(col.get(24*gi+hj,0) for col in columns)
        value=scale(F(1,137),add(add(mul(Y,X),mul(T,S)),scale(-count,d4)))
        assert field.get(24*gi+hj,Z)==value

# Decode states using3-cycles fixing exactly one label on each carrier.
state_readouts={}
for i,j in product(range(4),repeat=2):
    left=next(k for k,g in enumerate(group) if [n for n in range(4) if g[n]==n]==[i])
    right=next(k for k,g in enumerate(group) if [n for n in range(4) if g[n]==n]==[j])
    state_readouts[i,j]=scale(137,field.get(24*left+right,Z))
    assert state_readouts[i,j]==R[121+4*i+j]
# Decode arrow reversal-class sums using permutations fixing exactly each pair,
# subtracting the now-known four state contributions.
aliases=defaultdict(list)
for i,j in product(range(11),repeat=2):
    key=(tuple(sorted(edges[selected[i]])),tuple(sorted(edges[selected[j]])))
    aliases[key].append(11*i+j)
assert len(aliases)==36
hidden={}; decoded={}
for (left_pair,right_pair),members in aliases.items():
    left=next(k for k,g in enumerate(group) if tuple(i for i in range(4) if g[i]==i)==left_pair)
    right=next(k for k,g in enumerate(group) if tuple(i for i in range(4) if g[i]==i)==right_pair)
    state_part=total(state_readouts[i,j] for i in left_pair for j in right_pair)
    summed=add(scale(137,field.get(24*left+right,Z)),scale(-1,state_part))
    assert summed==total(R[i] for i in members)
    mean=scale(F(1,len(members)),summed)
    for i in members:
        hidden[i]=add(R[i],scale(-1,mean))
        decoded[i]=add(mean,hidden[i])
    assert total(hidden[i] for i in members)==Z
assert sum(len(v)-1 for v in aliases.values())==85
assert [decoded[i] for i in range(121)]+[state_readouts[i,j] for i,j in product(range(4),repeat=2)]==R

# A valid leg-map perturbation is invisible to the field but changes a named
# rectangle: interchange two reverse-arrow x maps with identical probes.
first=selected.index(edges.index((0,2))); reverse=selected.index(edges.index((2,0)))
x_swapped=list(x); x_swapped[first],x_swapped[reverse]=x_swapped[reverse],x_swapped[first]
changed=responses(x_swapped,y,s,t)
assert encode(changed)==field and changed!=R
rectangle=lambda data:add(add(data[12],data[0]),scale(-1,add(data[11],data[1])))
assert rectangle(changed)!=rectangle(R)
assert total(changed)==total(R)

# Uniform carrier averaging and identity evaluation have different block weights.
uniform=scale(F(1,576),total(field.values()))
expected=scale(F(1,137),add(scale(F(1,144),total(R[:121])),scale(F(1,16),total(R[121:]))))
assert uniform==expected and uniform!=scale(F(1,137),total(R))

# Minimal linear feature envelope under pointwise multiplication. A probe asks
# that a subset be fixed; products union the subsets. Fixing3 points fixes all4.
def canonical(mask): return 15 if mask.bit_count()>=3 else mask
def multiply(f,g): return canonical(f[0]|g[0]),canonical(f[1]|g[1])
singles={1<<i for i in range(4)}
pairs={sum(1<<i for i in pair) for pair in p['pairs']}
features=set(product(singles,singles))|set(product(pairs,pairs))
assert len(features)==52
levels=[features]
for _ in range(2):
    current=levels[-1]
    levels.append({multiply(f,g) for f,g in product(current,repeat=2)})
assert list(map(len,levels))==[52,113,121]
assert {multiply(f,g) for f,g in product(levels[-1],repeat=2)}==levels[-1]
# These are independent functions, rather than just distinct syntactic masks.
one_carrier=singles|pairs|{15}
single_columns=[{i:F(1) for i,g in enumerate(group) if all(g[j]==j for j in range(4) if mask&(1<<j))} for mask in one_carrier]
assert p['rank'](single_columns)==11
assert levels[-1]==set(product(one_carrier,one_carrier))
# An independent constant reference supplies the extra unital channel.
assert p['rank'](single_columns+[{i:F(1) for i in range(24)}])==12
assert len(levels[-1]|{(0,0)})==122
# A faithful alternative needs a retained marked context: reference edge(0,1)
# and a state basepoint outside it. Transporting this context preserves S4
# covariance; choosing one context is not derived by the probe construction.
root_edge=(0,1); state_base=2
root_arrows=[{k:F(1) for k,g in enumerate(group) if (g[root_edge[0]],g[root_edge[1]])==e}
             for e in edges]
root_states=[{k:F(1) for k,g in enumerate(group) if g[state_base]==i} for i in range(4)]
root_columns=[p['tensor'](root_arrows[i],root_arrows[j]) for i in selected for j in selected]
root_columns += [p['tensor'](u,v) for u in root_states for v in root_states]
assert p['rank']([root_arrows[i] for i in selected]+root_states)==15
assert p['rank'](root_columns)==137
for relabel in group:
    inv=tuple(relabel.index(i) for i in range(4))
    for g in group:
        conjugated=tuple(relabel[g[inv[i]]] for i in range(4))
        for e in edges:
            assert ((g[0],g[1])==e)==((conjugated[relabel[0]],conjugated[relabel[1]])==(relabel[e[0]],relabel[e[1]]))
        for i in range(4):
            assert (g[state_base]==i)==(conjugated[relabel[state_base]]==relabel[i])

class Decoder:
    def __init__(self,cols):
        self.pivots={}
        for j,col in enumerate(cols):
            vector=dict(col); expression={j:F(1)}
            while vector:
                pivot=min(vector); c=vector[pivot]
                if pivot in self.pivots:
                    row,expr=self.pivots[pivot]
                    add_scaled(vector,row,-c); add_scaled(expression,expr,-c)
                else:
                    self.pivots[pivot]=({k:v/c for k,v in vector.items()},{k:v/c for k,v in expression.items()})
                    break
            else: raise AssertionError('probe coefficients are not identifiable')
    def decode(self,vector):
        vector=dict(vector); out={}
        while vector:
            pivot=min(vector); c=vector[pivot]
            row,expression=self.pivots[pivot]
            add_scaled(vector,row,-c); add_scaled(out,expression,c)
        return out

root_field=encode(R,root_columns); decoder=Decoder(root_columns)
channels={(i,j):decoder.decode({k:137*M[i][j] for k,M in root_field.items() if M[i][j]}) for i,j in product(range(2),repeat=2)}
recovered=[tuple(tuple(channels[i,j].get(k,F(0)) for j in range(2)) for i in range(2)) for k in range(137)]
assert recovered==R and rectangle(recovered)==rectangle(R)
assert scale(F(1,137),total(recovered))==scale(F(1,137),total(R))
assert encode(changed,root_columns)!=root_field
# Faithful decoding is linear, but does not commute with pointwise composition.
# Two valid one-leg perturbations occupy disjoint rooted arrow contexts.
x1=[a['I']]*11; x2=list(x1)
x1[0]=add(a['I'],a['H']); x2[1]=add(a['I'],a['K'])
y0=[d4]*11; s0=[a['I']]*4; t0=[d4]*4
R1=responses(x1,y0,s0,t0); R2=responses(x2,y0,s0,t0)
field1=encode(R1,root_columns); field2=encode(R2,root_columns)
assert not field1.keys()&field2.keys()
mean1=scale(F(1,137),total(R1)); mean2=scale(F(1,137),total(R2))
reference_inverse=scale(F(1,2),a['I'])
composed_means=mul(mul(mean2,reference_inverse),mean1)
assert composed_means!=Z  # pointwise mixed field is identically zero
# Independently paired slot contexts restore the mean-composition square.
paired=scale(F(1,137**2),total(mul(mul(right,reference_inverse),left)
            for right in R2 if right!=Z for left in R1 if left!=Z))
assert paired==composed_means
# A basepoint on the reference edge fails the same faithful primitive test.
inside=[{k:F(1) for k,g in enumerate(group) if g[0]==i} for i in range(4)]
assert p['rank']([root_arrows[i] for i in selected]+inside)==12
print('The joint matrix-valued probe field exactly realizes the arrow/state factorization and the fixed-reference137-slot response.')
print('3-cycle samples recover16 state responses; transposition samples then recover36 arrow-class sums. Retaining85 within-class directions restores all named slots.')
print('A reverse-arrow leg swap preserves the entire field and mean but changes a named mixed rectangle: kernel retention is essential.')
print('Identity evaluation recovers equal-slot averaging; uniform carrier averaging weights arrow and state slots by1/144 and1/16.')
print('Recursive pointwise composition expands the residual feature envelope52->113->121, then stabilizes; a constant reference adds one channel.')
print('A marked edge plus an outside state basepoint instead gives a rank137 joint adapter; an exact decoder restores every matrix slot, its mean and named mixed defects.')
print('A valid disjoint-context perturbation shows that decoded averaging and pointwise composition do not commute; independent slot pairing restores the mixed term exactly.')
print('Marked-context relabelling is equivariant. An inside state basepoint loses rank; the context and physical sampling/readout law remain explicit choices.')
print('These are feature ranks under specified probe choices, not independent physical parameters or a derived coupling normalization.')
