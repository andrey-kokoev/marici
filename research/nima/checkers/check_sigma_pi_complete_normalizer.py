"""One complete rewrite schema for binary-indexed Sigma/Pi container chains.
Words run innermost first. S P -> P S S is dependent distributivity with
both binary choices retained. Intermediate chains need not be paired words.
"""
from itertools import product
from pathlib import Path
import json
EXPAND={'PP':'PP','SP':'PS','PS':'SP'}

def signature(word):
    a=b=0
    for c in word:
        if c=='S':a+=1
        elif c=='P':a*=2;b+=1
        else:raise ValueError('unknown constructor')
    return a,b

def reductions(word):
    return tuple(i for i in range(len(word)-1) if word[i:i+2]=='SP')

def rewrite(word,i):
    if i not in reductions(word):raise ValueError('not a redex')
    return word[:i]+'PSS'+word[i+2:]

def measure(word):
    s_count=0;counts=[]
    for c in word:
        if c=='S':s_count+=1
        else:counts.append(s_count)
    return tuple(counts)

def normalize(word):
    route=[word]
    while reductions(word):
        next_word=rewrite(word,reductions(word)[0])
        assert measure(next_word)<measure(word)
        assert signature(next_word)==signature(word)
        route.append(next_word);word=next_word
    a,b=signature(word)
    assert word=='P'*b+'S'*a
    return tuple(route)

# Exhaust arbitrary primitive words, including all expanded paired chains of
# length <=4. Check every local critical square without enumerating schedules.
words=edges=diamonds=0
for length in range(9):
    for letters in product('PS',repeat=length):
        word=''.join(letters);words+=1
        a,b=signature(word)
        assert normalize(word)[-1]=='P'*b+'S'*a
        sites=reductions(word)
        for i in sites:
            nxt=rewrite(word,i);edges+=1
            assert signature(nxt)==(a,b) and measure(nxt)<measure(word)
        for ii,i in enumerate(sites):
            for j in sites[ii+1:]:
                # Distinct SP redexes cannot overlap. Earlier rewrite adds one slot.
                assert j>=i+2
                left=rewrite(rewrite(word,i),j+1)
                right=rewrite(rewrite(word,j),i)
                assert left==right
                diamonds+=1
# Actual local equivalence and its inverse for tagged arbitrary leaf values.
leaf=('x','y')
def forward(value):
    (a,x),(b,y)=value
    return a,(b,(x,y))
def backward(value):
    a,(b,(x,y))=value
    return (a,x),(b,y)
for a,b,x,y in product((0,1),(0,1),leaf,leaf):
    value=((a,x),(b,y))
    assert backward(forward(value))==value
    assert forward(backward(forward(value)))==forward(value)
# Equality of terminal words yields an explicit zigzag by reversing one route.
first=('SP','PS','SP','PP');second=('PS','PP','SP','PS')
w1=''.join(EXPAND[c] for c in first);w2=''.join(EXPAND[c] for c in second)
r1=normalize(w1);r2=normalize(w2)
assert r1[-1]==r2[-1]=='P'*5+'S'*36
# Reversible records retain every intermediate expression.
report={'passed':True,'semantics':'fixed Bool-indexed dependent sums/products, inner-to-outer words',
 'single_rule':'SP -> PSS',
 'typed_rule':'Pi(i:Bool).Sigma(j:Bool).X ~= Sigma(j0:Bool).Sigma(j1:Bool).Pi(i:Bool).X',
 'normal_form':'P^b S^a; equivalently Sigma(bits:Bool^a).Pi(position:Fin(2^b)).Q',
 'termination_measure':'lexicographic tuple: number of S before each successive P; fixed tuple length',
 'primitive_words_checked':words,'one_step_checks':edges,'disjoint_local_diamonds':diamonds,
 'known_collision_routes':[list(r1),list(r2)],
 'complete_for_binary_container_signatures':True,
 'scope':'Written arbitrary-depth normalization proof accompanies finite tests. Complete presentation uses individual P,S intermediate chains; a finite presentation restricted to the three paired generators is not supplied. Higher-type automorphisms and arbitrary dependent-index grammar remain separate.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/sigma-pi-complete-normalizer.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='known_collision_routes'},indent=2))
