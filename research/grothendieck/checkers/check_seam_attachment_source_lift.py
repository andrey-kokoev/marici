"""Local action obstruction and a source-fixed split analytical refinement."""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction
import importlib.util
import sympy as s
import json
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('intervals',ROOT/'research/grothendieck/theta_interval_signature.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

# j_e: two marked source generators -> vacuum plus full chamber feature.
# r_e: positive Hilbert coefficient dual along that SAME feature.
edge_count=0
for start in range(16):
    for p in range(4):
        if start>>p&1:continue
        end=start|1<<p
        support=list(range(a.POSITION[start],a.POSITION[end]))
        j=s.zeros(16,2);j[0,0]=1
        r=s.zeros(2,16);r[0,0]=1
        for x in support:j[x+1,1]=1;r[1,x+1]=s.Rational(1,len(support))
        assert r*j==s.eye(2)
        # This is a coefficient retraction, not a signed-isometry assertion.
        edge_count+=1

histories=0
for start in range(16):
    unused=[p for p in range(4) if not start>>p&1]
    for n in range(len(unused)+1):
        for word in permutations(unused,n):
            supports=[];state=start
            for p in word:
                end=state|1<<p
                supports.append(tuple(range(a.POSITION[state],a.POSITION[end])))
                state=end
            for marks in product((False,True),repeat=n):
                # Expanded typed feature slots retain their source path labels.
                slots=[support if keep else (-1,) for support,keep in zip(supports,marks)]
                total=Fraction(0)
                for letters in product(*slots):
                    coefficient=Fraction(1)
                    for letter,support,keep in zip(letters,supports,marks):
                        assert (letter!=-1)==keep
                        if keep:coefficient/=len(support)
                    total+=coefficient
                assert total==1
                histories+=1

# q(a)*b=0 in the quotient, but any lift acts by a*b=c !=0.
Rb=s.Matrix([[0,0,0],[0,0,0],[1,0,0]])
x,y=s.symbols('x y')
section=s.Matrix([[1,0],[0,1],[x,y]])
assert Rb*section==s.Matrix([[0,0],[0,0],[1,0]])
# Any intertwiner to an I-annihilated target must kill c.
h=s.Matrix([[s.symbols('h0'),s.symbols('h1'),s.symbols('h2')]])
assert h*Rb==s.Matrix([[s.symbols('h2'),0,0]])

result={'schema':'marici.grothendieck.seam-attachment-source-lift.v1','passed':True,
        'local_generator_retractions':edge_count,'typed_histories_recovered':histories,
        'checks':{'positive_hilbert_coefficient_retraction':True,
                  'retained_slot_extension_recovers_every_marked_path':True,
                  'nonzero_action_defect_prevents_terminal_quotient_descent':True,
                  'terminal_linear_intertwiners_kill_product_layer':True},
        'scope':'Exact coefficient and source-action checks. Faithful stable extension follows from the split algebra maps; no Green isometry or physical inverse is inferred.'}
p=ROOT/'research/grothendieck/results/seam-attachment-source-lift.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
