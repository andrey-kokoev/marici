"""Fourth-order-remainder integration of the completed-theta windows.

Integrate f(mid)+f''(mid)*h^2/24, with error <= h^5 sup|f^(4)|/1920.
Arb series coefficients are derivatives divided by factorials. Evaluate the
fourth coefficient on the ENTIRE cell, not just at its midpoint.
"""
from flint import arb,arb_series,ctx

def upper(x):return arb(x.upper())
def positive(x):return arb(0).union(upper(x))
def symmetric(x):return (-upper(x)).union(upper(x))

def integrate_cell(function,left,right):
    """Tuple-valued analytic integrand; fourth derivatives enclosed on whole cell."""
    step=right-left;assert step>0
    cell=left.union(right);mid=(left+right)/2
    values=function(arb_series([mid,1],5));derivatives=function(arb_series([cell,1],5))
    assert len(values)==len(derivatives)>0
    integrals=[];errors=[]
    for value,derivative in zip(values,derivatives):
        assert value[0].is_finite() and derivative[4].is_finite()
        err=upper(abs(derivative[4]))*step**5/80
        integrals.append(step*value[0]+step**3*value[2]/12+symmetric(err))
        errors.append(err)
    return integrals,errors

def window(A,p,cells=1024,bits=192):
    assert type(cells) is int and cells>0
    assert type(A) is int and A>=2 and type(p) is int and p>=2
    ctx.prec=bits;ctx.cap=5
    pi=arb.pi();t0=pi*A*A;loga=arb(A).log();V=arb(32);step=V/cells
    D=t0*arb(A)**(arb(7)/2)
    assert t0*(p*p-1)>V
    def finite(v):
        t=t0+v;x=(t/pi).log()/2
        atoms=sum(((4*(n*n*t)**2-6*n*n*t)*(-((n*n-1)*t0+n*n*v)).exp() for n in (1,2)),0)
        ep=(3*x).exp();em=(-3*x).exp()
        density=((ep+em)/2)*(x/2).exp()*atoms/(2*t*D)
        return density,(x*(ep-em)/(ep+em)-loga)*density
    sums=[arb(0),arb(0)];errors=[arb(0),arb(0)];omitted=[arb(0),arb(0)]
    for j in range(cells):
        left=j*step;right=(j+1)*step;cell=left.union(right)
        values,errs=integrate_cell(finite,left,right)
        for k in (0,1):
            sums[k]+=values[k]
            errors[k]+=errs[k]
        # Same complete n>=3 geometric majorant as the owning cell integrator.
        t=t0+cell;x=(t/pi).log()/2;ratio=(arb(4)/3)**4*(-7*t).exp()
        assert ratio<1
        theta_tail=4*t*t*81*(-8*t0-9*cell).exp()/(1-ratio)
        tail_density=(3*x).cosh()*(x/2).exp()*theta_tail/(2*t*D)
        omitted[0]+=step*positive(tail_density)
        omitted[1]+=step*(x*(3*x).tanh()-loga)*positive(tail_density)
    den=1-16*(-3*t0).exp();assert den>0
    tail=2*(-V).exp()*(V**3+6*V**2+15*V+16)/den
    integral=sums[0]+omitted[0]+positive(tail)
    centered=sums[1]+omitted[1]+symmetric((loga+arb(A*p).log())*tail)
    assert integral>0
    return {'X':D*(-t0).exp()*integral,'mu':loga+centered/integral,
            'scaled_integral':integral,'centered_integral':centered,'tail_bound':tail,
            'quadrature_remainder_bounds':errors,'omitted_atom_integrals':omitted,
            'cells':cells,'bits':bits,'series_order':4}
