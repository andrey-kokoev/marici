"""Uniform readout bounds and a finite robust attachment witness margin."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reconstruction',HERE/'certify_joint_cubic_reconstruction.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
ctx.prec=192
pi=arb.pi();L=c.L


def moments(a):
    q0=pi*a*a;T=arb(32);N=2048;step=T/N
    assert 3*q0>T
    X=arb(0);J=arb(0)
    for j in range(N):
        v=(j*step).union((j+1)*step);q=q0+v;x=(q/pi).log()/2
        density=(2*q-3)*(-v).exp()+(32*q-12)*(-3*q0-4*v).exp()
        ratio=(arb(4)/3)**4*(-7*q).exp()
        density+=c.base.pos(2*q*81*(-8*q0-9*v).exp()/(1-ratio))
        density*=(x/2).exp()
        X+=step*(3*x).cosh()*density
        J+=step*x*(3*x).sinh()*density
    H=1+16*(-3*q0).exp()/(1-(arb(3)/2)**4*(-5*q0).exp())
    factor=2*pi**(-arb(7)/4)*H*(-T).exp();q=q0+T
    X+=c.base.pos(factor*(q**3+3*q**2+6*q+6))
    J+=c.base.pos(factor*(q**4+4*q**3+12*q**2+24*q+24))
    assert X>0
    return J/X


def main():
    assert L>0
    D=(1+arb(6).log())*(1+arb(210).log())/18
    assert D<1
    x=arb(2).log()
    assert x*(3*x).tanh()-L>(1+x)/4
    k0=pi*(1-(-arb(1)).exp())/8
    assert k0**2*arb(6)**(arb(11)/2)*2**11>5
    mus={a:moments(a) for a in (2,4,12,60)}
    d=(mus[4]-mus[2])*(mus[60]-mus[12])/18
    assert d>arb(1)/25
    d_infinity=arb(2).log()*arb(5).log()/18
    assert d_infinity>0
    margin=(1-Q(1,100))*(Q(1,25)-Q(1,100))-Q(1,100)**2
    assert margin==Q(37,1250) and margin>0
    result={'passed':True,'arithmetic':'Arb 192 bits; exact rational determinant bound',
        'uniform_normalized_residual_coefficient_bound':'|sigma_0|,|sigma_x| <= (1+log A)^2',
        'bound_constant_before_rounding':str(D),
        'residual_readout_inverse_upper_bound':'exp(101*pi*A^2)',
        'normalized_positive_attachment_at_background_2':str(d),
        'limiting_positive_attachment':str(d_infinity),
        'example_true_interval_matrix_determinant_lower_bound':str(margin),
        'scope':'Rigorous finite margins and constants. Infinite instability and conditional rates use the accompanying source-sequence and theta-asymptotic arguments. No physical acquisition or norm on Ext is asserted.'}
    out=HERE.parent/'results/attachment-readout-stability.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
