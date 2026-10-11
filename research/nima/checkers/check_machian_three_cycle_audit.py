"""Exact audit of the old Machian scalar cycle; do not rerun old claim generators.

Recover the supplied coefficients from the original AST, reconstruct scalar
arrows, and distinguish type-loop closure, state return and gain calibration.
No dimensionful gravitational constant is derived here.
"""
import ast
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]


def evaluate(node,env):
    if isinstance(node,ast.Constant) and isinstance(node.value,(int,float)):
        return F(str(node.value))
    if isinstance(node,ast.Name):return env[node.id]
    if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return -evaluate(node.operand,env)
    if isinstance(node,ast.BinOp):
        a,b=evaluate(node.left,env),evaluate(node.right,env)
        if isinstance(node.op,ast.Add):return a+b
        if isinstance(node.op,ast.Sub):return a-b
        if isinstance(node.op,ast.Mult):return a*b
        if isinstance(node.op,ast.Div):return a/b
        if isinstance(node.op,ast.Pow):
            assert b.denominator==1
            return a**int(b)
    raise ValueError(ast.dump(node))


@dataclass(frozen=True)
class Arrow:
    source: str
    target: str
    gain: F

    def then(self,other):
        if self.target!=other.source:raise ValueError('unmatched boundary')
        return Arrow(self.source,other.target,self.gain*other.gain)

    def apply(self,x):return self.gain*x


def main():
    path=ROOT/'checkers/check_machian_3cycle.py'
    raw=path.read_bytes();tree=ast.parse(raw)
    assignments={t.id:n.value for n in tree.body if isinstance(n,ast.Assign)
                 for t in n.targets if isinstance(t,ast.Name)}
    declaration=next(n for n in tree.body if isinstance(n,ast.Assign)
                     and isinstance(n.targets[0],ast.Tuple)
                     and [v.id for v in n.targets[0].elts]==['r','l','s','c'])
    env={name:F(value.value) for name,value in zip(('r','l','s','c'),declaration.value.elts)}
    k1=evaluate(assignments['k1'],env);k2=evaluate(assignments['k2'],env)
    assert k1==F(1,90) and k2==F(1,5280)
    L=Arrow('identity','left',1+k1)
    R=Arrow('left','right',1-k2)
    unchanged=Arrow('right','identity',F(1))
    first_two=L.then(R)
    loop=first_two.then(unchanged)
    assert loop.source==loop.target and loop.gain!=1
    defect=loop.apply(F(1))-1
    assert defect==F(5189,475200)
    assert loop.apply(F(0))==0  # zero state would conceal nonidentity gain
    closing=Arrow('right','identity',1/first_two.gain)
    assert first_two.then(closing).gain==1
    epsilon_return=closing.gain-1
    assert epsilon_return==-F(5189,480389)
    # Old epsilon_id_theory compensates to a prescribed target total gain,
    # not to identity. Freeze both additive and old series-target choices.
    additive=1+k1-k2
    assert additive-first_two.gain==k1*k2==F(1,475200)
    additive_compensation=additive/first_two.gain-1
    assert additive_compensation==F(1,480389)
    infinite_tail=k1/F(11**2)*F(11,12)
    assert infinite_tail==F(1,11880)
    truncated_tail=sum(((-1)**(n+1)*k1/F(11**(n-1)) for n in range(3,20)),F(0))
    truncated_target=additive+truncated_tail
    old_compensation=truncated_target/first_two.gain-1
    assert first_two.gain*(1+old_compensation)==truncated_target!=1
    # Closure leaves the first two gains free: matched typed examples.
    alternatives=[]
    for left,right in ((L.gain,R.gain),(F(2),F(3)),(F(3,2),F(4,5))):
        a=Arrow('identity','left',left);b=Arrow('left','right',right)
        c=Arrow('right','identity',1/(left*right))
        assert a.then(b).then(c).gain==1
        alternatives.append(dict(left=str(left),right=str(right),return_gain=str(c.gain)))
    try:L.then(L)
    except ValueError:pass
    else:raise AssertionError('unmatched arrows accepted')
    # Recompute the old hierarchy comparisons without inheriting their
    # 'derived' classifications or overwriting their generated artifacts.
    base=F(12*11**15);weak_scale=F(246);observed=F('1.220890e19')
    variants=[]
    for name,Z in (('additive correction',1/additive),('two-leg product inverse',1/first_two.gain),
                   ('complete identity loop gain',F(1))):
        ratio=base*Z;mass=weak_scale*ratio
        variants.append(dict(name=name,Z=str(Z),Planck_to_weak_ratio=str(ratio),
                             Planck_mass_GeV_if_v_246=str(mass),mass_decimal_GeV=float(mass),
                             mass_relative_error_percent=float(100*(mass/observed-1)),
                             G_relative_error_percent=float(100*((observed/mass)**2-1))))
    result=dict(schema='marici.nima.machian-three-cycle-audit.v1',status='pass',
                source=str(path.relative_to(ROOT)),source_sha256=hashlib.sha256(raw).hexdigest(),
                obligation='typed scalar composition and distinction between prescribed holonomy and identity-return witness',
                supplied_gram_numbers={k:str(v) for k,v in env.items()},left_increment=str(k1),right_increment=str(-k2),
                two_leg_gain=str(first_two.gain),unchanged_return_identity_defect=str(defect),
                actual_identity_return_gain=str(closing.gain),actual_identity_return_increment=str(epsilon_return),
                additive_target_gain=str(additive),additive_vs_product_difference=str(k1*k2),
                return_increment_to_additive_target=str(additive_compensation),
                infinite_series_tail=str(infinite_tail),old_finite_series_compensation=str(old_compensation),
                alternative_closed_cycles=alternatives,hierarchy_comparisons=variants,
                disposition='The declared zero-correction third leg closes stage labels, not the scalar state. True identity return fixes only the compensating inverse; it does not select the first two coefficients, exponent or physical normalization.',
                residual='Scalar-arrow reconstruction of supplied old formulas, not an independently source-generated WG physical cycle. A nonidentity loop could represent holonomy, but then its physical readout needs a separate law. No derivation of G or alpha_G established.')
    (ROOT/'results/machian-three-cycle-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('old_finite_series_compensation','hierarchy_comparisons')},indent=2))


if __name__=='__main__':main()
