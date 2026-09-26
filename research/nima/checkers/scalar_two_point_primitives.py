"""Scoped two-point primitive library: real scalar, 3+1 dimensions, (+---).
Fourier kernels use exp(-ip.x); propagators carry i, stripped edges do not.
Distributions are formal symbolic outputs, not pointwise-evaluable amplitudes.
Primitive arithmetic is attributed SymPy evaluation, not finite-agent arithmetic.
"""
from dataclasses import dataclass
from fractions import Fraction
import sympy as s
from amplitude_identity_net import IdentityNet, Scalar, PORTS

CONVENTION = 'real scalar; D=4; metric +---; Fourier exp(-ip.x); hbar=1'

@dataclass(frozen=True)
class Block:
    kind: str
    expression: s.Expr
    representation: str
    prescription: str
    convention: str = CONVENTION

@dataclass(frozen=True)
class Request:
    operation: str
    arguments: tuple


def exact(x):
    x=s.sympify(x)
    if not isinstance(x,s.Expr) or x.has(s.Float,s.nan,s.zoo,s.oo,-s.oo):
        raise ValueError('finite exact scalar expression required')
    if x.is_commutative is not True:raise ValueError('commuting scalar required')
    return x


def momentum(p):
    if not isinstance(p,tuple) or len(p)!=4:raise ValueError('four-momentum tuple required')
    p=tuple(exact(v) for v in p)
    if any(v.is_real is not True for v in p):raise ValueError('real momentum components required')
    return p


def mass_value(m):
    m=exact(m)
    if m.is_nonnegative is not True:raise ValueError('nonnegative real mass required')
    return m


def kinetic(p,m):
    p=momentum(p);m=mass_value(m)
    return p[0]**2-sum(v**2 for v in p[1:])-m**2


def evaluate(request):
    if not isinstance(request,Request):raise TypeError('typed Request required')
    op=request.operation;args=request.arguments
    if op=='identity':
        if len(args)!=1 or not isinstance(args[0],Block):raise TypeError('identity transports a typed Block')
        return args[0]
    if op=='unit_current':
        if len(args)!=1 or not isinstance(args[0],str) or not args[0]:raise ValueError('leg label required')
        return Block('unit_current',s.S.One,'amputated rooted current','leg='+args[0]+'; no external propagator')
    if op=='stripped_edge':
        X,=args;X=exact(X)
        if X.is_zero is True:raise ValueError('channel pole')
        return Block('stripped_edge',1/X,'rational channel function','domain X != 0; coupling and phase stripped')
    if op in ('kinetic','inverse_propagator','feynman','time_ordered','wightman','dressed_feynman'):
        if len(args)!=(4 if op=='dressed_feynman' else 2):raise ValueError('wrong argument count')
        p,m=args[:2];p=momentum(p);K=kinetic(p,m)
        if op=='kinetic':return Block(op,K,'momentum kernel','free quadratic action kernel K=p^2-m^2')
        if op=='wightman':
            return Block(op,2*s.pi*s.Heaviside(p[0])*s.DiracDelta(K),'distribution',
                         'vacuum positive-frequency W+(p); formal distribution')
        if op=='dressed_feynman':
            sigma,provenance=args[2:];sigma=exact(sigma)
            if not isinstance(provenance,str) or not provenance:raise ValueError('self-energy provenance required')
            K=K-sigma
            note='D=i/(K-Sigma+i0); supplied Sigma, not computed; '+provenance
        else:note='D_F=i/(K+i0); free vacuum time ordering'
        # Positive regulator is retained as a symbol. No distributional limit is evaluated.
        epsilon=s.Symbol('epsilon',positive=True)
        if op=='inverse_propagator':
            return Block(op,(K+s.I*epsilon)/s.I,'regulated momentum kernel',
                         'algebraic inverse of i/(K+i epsilon), NOT the kinetic kernel')
        return Block(op,s.I/(K+s.I*epsilon),'regulated momentum kernel',note+'; epsilon -> 0+ unevaluated')
    if op=='one_particle_identity':
        p,q,m=args
        if not isinstance(p,tuple) or not isinstance(q,tuple) or len(p)!=3 or len(q)!=3:
            raise ValueError('two spatial momentum triples required')
        p=tuple(exact(v) for v in p);q=tuple(exact(v) for v in q);m=mass_value(m)
        if any(v.is_real is not True for v in p+q):raise ValueError('real momenta required')
        energy=s.sqrt(sum(v**2 for v in p)+m**2)
        expr=2*energy*(2*s.pi)**3*s.prod(s.DiracDelta(a-b) for a,b in zip(p,q))
        return Block(op,expr,'distribution','free stable one-particle S=I; covariant normalization; connected T=0')
    raise ValueError('unsupported primitive')


def regular_product(a,b):
    """Only a regular-expression helper, not a graph composition or LSZ rule."""
    if not isinstance(a,Block) or not isinstance(b,Block):raise TypeError('typed blocks required')
    if a.convention!=b.convention:raise ValueError('convention mismatch')
    if a.representation=='distribution' or b.representation=='distribution':
        raise ValueError('distribution multiplication requires an explicit justified operation')
    return Block('product',s.cancel(a.expression*b.expression),'regular expression',
                 'explicit algebraic product, not automatic physical sewing')

PORTS['N2_REQUEST']=('p',)

class TwoPointNet(IdentityNet):
    def __init__(self,request):
        # Validate before allocation; leave derived output unmaterialized until rewrite.
        evaluate(request)
        super().__init__(Scalar(Fraction(1)))
        n=next(n for n,(kind,_) in self.nodes.items() if kind=='INPUT')
        self.nodes[n]=('N2_REQUEST',request)

    def enabled(self):
        pairs=super().enabled()
        for n,(kind,_) in self.nodes.items():
            if kind!='N2_REQUEST':continue
            peer,port=self.wires[n,'p']
            if port=='p' and self.nodes[peer][0]=='ID':pairs.append((n,peer))
        return pairs

    def step(self,pair):
        if pair not in self.enabled():raise ValueError('inactive or consumed pair')
        n,_=pair;kind,payload=self.nodes[n]
        if kind=='N2_REQUEST':self.nodes[n]=('INPUT',evaluate(payload))
        super().step(pair)

    def meaning(self):
        requests=[p for k,p in self.nodes.values() if k=='N2_REQUEST']
        if requests:
            if len(requests)!=1:raise ValueError('duplicated request')
            return evaluate(requests[0])
        return super().meaning()
