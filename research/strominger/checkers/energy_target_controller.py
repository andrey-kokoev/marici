"""Conditional exact energy targeting; no free reset or new actuator.

Input energies and gains must already have an admitted mathematical meaning.
This module does not implement a physical measurement or actuator.
"""
import sympy as S
from energy_task_reduction import EnergyTaskState, gain_step, infer_components


def target_gain(state, target):
    target=S.sympify(target)
    # Reuse validation, including nonnegative components and provenance.
    gain_step(state,S.Integer(1))
    a,b=map(S.sympify,(state.one_leg,state.two_leg))
    total=a+b
    if target.is_nonnegative is not True or (total-target).is_nonnegative is not True:
        raise ValueError('target outside current contraction range')
    if target==total:
        return S.Integer(1)
    if target==0:
        return S.Integer(0)
    if b==0:
        return S.sqrt(target/a)
    if a==0:
        return (target/b)**S.Rational(1,4)
    return S.sqrt(2*target/(a+S.sqrt(a*a+4*b*target)))


def safe_probe(total,target):
    """Choose a nontrivial probe that cannot undershoot a positive target.

    For0<h<H, q²=(1+h/H)/2 and H_after>=q⁴ H>=h.
    Bounds concern the declared exact contraction law, not measurement noise.
    """
    total,target=map(S.sympify,(total,target))
    if total.is_positive is not True or target.is_positive is not True or (total-target).is_positive is not True:
        raise ValueError('probe requires0<target<initial energy')
    return S.sqrt((1+target/total)/2)


def finish_after_probe(total,after,probe,target,provenance):
    if not provenance:
        raise ValueError('measurement/protocol provenance required')
    a,b=infer_components(total,after,probe)
    initial=EnergyTaskState(a,b,provenance)
    probed=gain_step(initial,probe)
    # Crucial: target from the UPDATED state; never reset to initial silently.
    q=target_gain(probed.result,target)
    return probed,gain_step(probed.result,q)
