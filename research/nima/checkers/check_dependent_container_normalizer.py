"""Dependent container closure and retained reconstruction at two normalizations."""
from itertools import product
from pathlib import Path
import contextlib,io,json,random
from dependent_container_normalizer import Atom,Binder,normalize,encode,decode,as_expression
with contextlib.redirect_stdout(io.StringIO()):
    import check_dependent_sigma_pi_full_chains as prior

# Build exactly the earlier dependent grammar, including all leaf type labels.
domains={}
def leaf(i,j,k,l):
    name=f'B({i},{j},{k},{l})';domains[name]=prior.B(i,j,k,l)
    return Atom(name)
tree=Binder('Pi',tuple((i,Binder('Sigma',tuple((j,Binder('Pi',tuple((k,
    Binder('Sigma',tuple((l,leaf(i,j,k,l)) for l in prior.L(i,j,k))))
    for k in prior.K(i,j)))) for j in prior.J(i)))) for i in prior.I))
n=normalize(tree);assert n==normalize(tree,True)
source=prior.sources();normal_values=[]
for case in n.cases:
    for values in product(*(domains[typ] for _,typ in case.positions)):
        normal_values.append((case.shape,values))
assert {encode(n,x) for x in source}==set(normal_values)
assert all(decode(n,*encode(n,x))==x for x in source)
assert all(encode(n,decode(n,*v))==v for v in normal_values)
# Re-expressing a normal form supplies a legitimate next-level source.
second=normalize(as_expression(n))
for shape,values in normal_values:
    represented=(shape,values)
    assert decode(second,*encode(second,represented))==represented
# Broad finite structural regression, including empty sums/products.
rng=random.Random(81)
def generated(depth):
    if depth==0 or rng.randrange(4)==0:return Atom('opaque')
    return Binder(rng.choice(('Sigma','Pi')),tuple((i,generated(depth-1)) for i in range(rng.randrange(3))))
examples=[Atom('opaque'),Binder('Sigma',()),Binder('Pi',()),tree]
examples.extend(generated(4) for _ in range(60))
shape_checks=0
class Payload:
    def __deepcopy__(self,memo):raise AssertionError('payload copied')
for example in examples:
    normal=normalize(example);assert normal==normalize(example,True)
    assert normal.source is example
    next_normal=normalize(as_expression(normal))
    for case in normal.cases:
        values=tuple(Payload() for _ in case.positions)
        value=decode(normal,case.shape,values)
        shape2,values2=encode(normal,value)
        assert shape2==case.shape
        assert len(values)==len(values2) and all(a is b for a,b in zip(values,values2))
        represented=(case.shape,values)
        recovered=decode(next_normal,*encode(next_normal,represented))
        assert recovered[0]==case.shape
        assert all(a is b for a,b in zip(values,recovered[1]))
        shape_checks+=1
assert len(normalize(Binder('Sigma',())).cases)==0
empty_product=normalize(Binder('Pi',())).cases
assert len(empty_product)==1 and empty_product[0].positions==()
# Reject a witness list that drops a position from a dependent case.
case=next(c for c in n.cases if c.positions)
try:decode(n,case.shape,tuple(None for _ in case.positions[:-1]))
except ValueError:pass
else:raise AssertionError('missing witness accepted')
report={'passed':True,'dependent_source_values':len(source),
 'independently_enumerated_normal_values':len(normal_values),
 'dependent_choice_shapes':len(n.cases),
 'source_grammar_closes_under_normal_form_reexpression':True,
 'full_source_and_recursive_rule_records_retained':True,
 'finite_structural_examples':len(examples),'opaque_shape_roundtrips':shape_checks,
 'empty_sum_and_empty_product_distinguished':True,
 'scope':'Finite dependent binders with opaque leaf witnesses. General HoTT normal-form theorem given as a written induction; arbitrary higher comparison data not modeled by set-valued checks.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/dependent-container-normalizer.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
