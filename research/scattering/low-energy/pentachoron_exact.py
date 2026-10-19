"""Small exact Q(sqrt(2),sqrt(3),sqrt(5),i) toolkit for archived matrices.

No source-code execution or general expression evaluation is used by parse().
"""
import ast
from fractions import Fraction as Q
from functools import cache
from math import isqrt


class F:
    __slots__=('v',)

    def __init__(self,value=0):
        self.v=value.v if isinstance(value,F) else tuple(map(Q,value)) if isinstance(value,tuple) else (Q(value),)
        self.v=self.v+(Q(0),)*(16-len(self.v))
        assert len(self.v)==16

    def __bool__(self):return any(self.v)
    def __hash__(self):return hash(self.v)
    def __eq__(self,other):return isinstance(other,(F,int,Q)) and self.v==F(other).v
    def __neg__(self):return F(tuple(-v for v in self.v))
    def __add__(self,other):
        other=F(other)
        if not self:return other
        if not other:return self
        return F(tuple(a+b for a,b in zip(self.v,other.v)))
    __radd__=__add__
    def __sub__(self,other):return self+-F(other)
    def __rsub__(self,other):return F(other)+-self
    def __mul__(self,other):
        other=F(other)
        if not self or not other:return F()
        out=[Q(0)]*16
        for a,x in enumerate(self.v):
            if not x:continue
            for b,y in enumerate(other.v):
                if y:
                    common=a&b;factor=1
                    for bit,square in enumerate((2,3,5,-1)):
                        if common&(1<<bit):factor*=square
                    out[a^b]+=factor*x*y
        return F(tuple(out))
    __rmul__=__mul__
    def __truediv__(self,other):return self*inverse(F(other))
    def conjugate(self):return F(tuple(-v if i&8 else v for i,v in enumerate(self.v)))
    def encoded(self):return [str(v) for v in self.v]


@cache
def inverse(x):
    if not x:raise ZeroDivisionError('zero exact field element')
    top=max(i for i,v in enumerate(x.v) if v)
    if top==0:return F(1/x.v[0])
    bit=1<<(top.bit_length()-1)
    conjugate=F(tuple(-v if i&bit else v for i,v in enumerate(x.v)))
    norm=x*conjugate
    assert all(not v for i,v in enumerate(norm.v) if i&bit)
    return conjugate*inverse(norm)


def radical(n):
    assert type(n) is int and n>0
    coefficient=1;index=0
    for bit,prime in enumerate((2,3,5)):
        exponent=0
        while n%prime==0:exponent+=1;n//=prime
        coefficient*=prime**(exponent//2)
        if exponent%2:index|=1<<bit
    assert n==1,'radical outside declared field'
    return F(tuple(coefficient if i==index else 0 for i in range(16)))


@cache
def parse(text):
    def walk(n):
        if isinstance(n,ast.Constant) and type(n.value) is int:return F(n.value)
        if isinstance(n,ast.Name) and n.id=='I':return F(tuple(int(i==8) for i in range(16)))
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -walk(n.operand)
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='sqrt' and len(n.args)==1 and not n.keywords:
            arg=n.args[0]
            assert isinstance(arg,ast.Constant) and type(arg.value) is int
            return radical(arg.value)
        if isinstance(n,ast.BinOp):
            a,b=walk(n.left),walk(n.right)
            if isinstance(n.op,ast.Add):return a+b
            if isinstance(n.op,ast.Sub):return a-b
            if isinstance(n.op,ast.Mult):return a*b
            if isinstance(n.op,ast.Div):return a/b
        raise ValueError('unlicensed exact expression: '+ast.dump(n))
    return walk(ast.parse(text,mode='eval').body)


def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def adjoint(A):return [[v.conjugate() for v in row] for row in zip(*A)]
def mm(A,B):
    out=[[F() for _ in B[0]] for _ in A]
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(B[k]):
                    if b:out[i][j]=out[i][j]+a*b
    return out

def zero(A):return not any(v for row in A for v in row)
def encoded(A):return [[v.encoded() for v in row] for row in A]


def rref(A):
    A=[row[:] for row in A];pivots=[];r=0
    for j in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][j]),None)
        if p is None:continue
        A[p],A[r]=A[r],A[p];scale=inverse(A[r][j]);A[r]=[v*scale for v in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                factor=A[i][j];A[i]=[a-factor*b for a,b in zip(A[i],A[r])]
        pivots.append(j);r+=1
        if r==len(A):break
    return A,pivots


def kernel(A):
    R,pivots=rref(A);free=[j for j in range(len(A[0])) if j not in pivots];columns=[]
    for j in free:
        v=[F() for _ in A[0]];v[j]=F(1)
        for i,p in enumerate(pivots):v[p]=-R[i][j]
        columns.append(v)
    return [list(row) for row in zip(*columns)] if columns else [[] for _ in A[0]]


def positive(x):
    assert not any(x.v[8:]),'nonreal Hermitian pivot'
    for digits in (8,16,32,64,128):
        scale=10**digits;lo=Q(0);hi=Q(0)
        for i,c in enumerate(x.v[:8]):
            if not c:continue
            n=(2 if i&1 else 1)*(3 if i&2 else 1)*(5 if i&4 else 1)
            floor=isqrt(n*scale*scale);a=Q(floor,scale);b=a if floor*floor==n*scale*scale else a+Q(1,scale)
            lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
        if lo>0:return True
        if hi<0:return False
    raise AssertionError('unresolved pivot sign')


def psd_rank(A):
    """Exact Hermitian Schur congruence; pivot signs use rational enclosures."""
    assert A==adjoint(A)
    A=[row[:] for row in A];rank=0
    while A:
        p=next((i for i in range(len(A)) if A[i][i]),None)
        if p is None:
            assert zero(A),'zero diagonal with nonzero off-diagonal is not PSD'
            break
        assert positive(A[p][p]),'negative Schur pivot'
        ids=[i for i in range(len(A)) if i!=p];inv=inverse(A[p][p])
        A=[[A[i][j]-A[i][p]*inv*A[p][j] for j in ids] for i in ids];rank+=1
    return rank
