"""First closure experiment for PP, SP, PS using indexed finite containers.
Fixed binary binders are declared experimental semantics, not inferred from
source regrouping. Full expression words and reversible value codecs survive
normalization. Cardinal signatures alone are not used as comparison witnesses.
"""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json, random

OPS={'PP':('P','P'),'SP':('P','S'),'PS':('S','P')} # innermost first

def signature(word,initial=(0,0)):
    # Container normal form: bitstring choices of length a, 2^b Q-positions.
    a,b=initial
    for op in word:
        if op=='PP':a,b=4*a,b+2
        elif op=='SP':a,b=2*a+1,b+1
        elif op=='PS':a,b=2*a+2,b+1
        else:raise ValueError(op)
    return a,b

def expr(word):
    tree=('Q',)
    for op in word:
        for tag in OPS[op]:tree=(tag,tree)
    return tree

def dimensions(tree):
    if tree[0]=='Q':return 0,1
    a,d=dimensions(tree[1])
    return (a+1,d) if tree[0]=='S' else (2*a,2*d)

def encode(tree,value):
    """Explicit dependent-distributivity witness as retained choices and leaves."""
    tag=tree[0]
    if tag=='Q':return (), (value,)
    if tag=='S':
        choice,body=value
        assert choice in (0,1)
        bits,leaves=encode(tree[1],body)
        return (choice,)+bits,leaves
    a,x=encode(tree[1],value[0]);b,y=encode(tree[1],value[1])
    return a+b,x+y

def decode(tree,bits,leaves):
    a,d=dimensions(tree)
    if len(bits)!=a or len(leaves)!=d:raise ValueError('wrong dependent container dimensions')
    if any(x not in (0,1) for x in bits):raise ValueError('invalid choice')
    if tree[0]=='Q':return leaves[0]
    if tree[0]=='S':return bits[0],decode(tree[1],bits[1:],leaves)
    child_a,child_d=dimensions(tree[1])
    return (decode(tree[1],bits[:child_a],leaves[:child_d]),
            decode(tree[1],bits[child_a:],leaves[child_d:]))

# Preserve words while grouping by a canonical typed container signature.
levels=[];first_collision=None
for depth in range(9):
    groups=defaultdict(list)
    for word in product(OPS,repeat=depth):groups[signature(word)].append(word)
    collisions=[words for words in groups.values() if len(words)>1]
    if first_collision is None and collisions:first_collision=collisions[0][:2]
    levels.append({'depth':depth,'chains':3**depth,'container_types':len(groups),
                   'largest_equivalent_chain_family':max(map(len,groups.values()))})
assert first_collision is not None
for a,b in product(range(5),repeat=2):
    assert signature(first_collision[0],(a,b))==signature(first_collision[1],(a,b))==(32*a+36,b+5)
# Fully reversible comparison maps, including a diamond with three equivalent words.
rng=random.Random(17);roundtrips=0;triangles=0
for depth in range(7):
    groups=defaultdict(list)
    for word in product(OPS,repeat=depth):groups[signature(word)].append(word)
    for (a,b),words in groups.items():
        bits=tuple(rng.randrange(2) for _ in range(a))
        leaves=tuple(('source',i) for i in range(2**b))
        for word in words:
            tree=expr(word)
            assert dimensions(tree)==(a,2**b)
            value=decode(tree,bits,leaves)
            assert encode(tree,value)==(bits,leaves)
            assert decode(tree,*encode(tree,value))==value
            roundtrips+=1
        if len(words)>=3:
            x,y,z=map(expr,words[:3])
            vx=decode(x,bits,leaves)
            vy=decode(y,*encode(x,vx))
            vz=decode(z,*encode(y,vy))
            assert vz==decode(z,*encode(x,vx))
            triangles+=1
assert triangles>0
# Branch recurrence cannot occur at the formal-container level: b strictly grows.
for word in product(OPS,repeat=5):
    sigs=[signature(word[:k]) for k in range(6)]
    assert all(sigs[k+1][1]>sigs[k][1] for k in range(5))
    assert len(sigs)==len(set(sigs))
report={'passed':True,'semantics':'P(X)=Pi(i:Bool).X; S(X)=Sigma(i:Bool).X',
 'normal_form':'Sigma(bits:Bool^a).Pi(position:Fin(2^b)).Q; full word and reversible codec retained',
 'transition_rules':{'PP':'(a,b)->(4a,b+2)','SP':'(a,b)->(2a+1,b+1)','PS':'(a,b)->(2a+2,b+1)'},
 'levels':levels,'first_distinct_equivalent_words_innermost_first':first_collision,
 'first_equivalent_container_signature':signature(first_collision[0]),
 'first_relation_on_arbitrary_container_signature':'(a,b) -> (32a+36,b+5) for both chains',
 'codec_roundtrips':roundtrips,'comparison_triangle_checks':triangles,
 'finite_closed_rule_description':True,'strict_formal_period_along_branch':False,
 'scope':'Finite-set container interpretation with binary indices and explicitly constructed bijections. Repeated equivalence patterns across branches; no automatic higher-HoTT witness tower or proof this semantics is the intended closure-preserving source productization.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/three-operation-coherence-grammar.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
