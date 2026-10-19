"""Exact F2 Laurent matrices; imports only numerical matrices from paper TeX."""
import re
Z=frozenset();ONE=frozenset({(0,0,0)})
def poly(text):
    text=re.sub(r'\s+','',text).replace('*','')
    text=re.sub(r'\\frac\{([1xyz]+)\}\{([1xyz]+)\}',r'\1/\2',text).replace('(','').replace(')','')
    result=Z
    for term in text.split('+'):
        if term=='0':continue
        pieces=term.split('/');assert len(pieces)<=2 and all(re.fullmatch('[1xyz]+',p) for p in pieces),text
        numerator=pieces[0];denominator=pieces[1] if len(pieces)==2 else ''
        exponent=tuple(numerator.count(c)-denominator.count(c) for c in 'xyz')
        result=result^frozenset({exponent})
    return result
def mul(a,b):
    result=set()
    for x in a:
        for y in b:
            t=tuple(u+v for u,v in zip(x,y))
            if t in result:result.remove(t)
            else:result.add(t)
    return frozenset(result)
def bar(a):return frozenset(tuple(-v for v in t) for t in a)
def zero(n,m):return [[Z for _ in range(m)] for _ in range(n)]
def eye(n):return [[ONE if i==j else Z for j in range(n)] for i in range(n)]
def omega(n):return [[ONE if (i+n)%(2*n)==j else Z for j in range(2*n)] for i in range(2*n)]
def mm(A,B):
    C=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(B[k]):
                    if y:C[i][j]=C[i][j]^mul(x,y)
    return C
def dag(A):return [[bar(v) for v in col] for col in zip(*A)]
def inv(A):
    n=len(A);M=[r[:]+e for r,e in zip(A,eye(n))]
    for k in range(n):
        p=next(i for i in range(k,n) if len(M[i][k])==1);M[k],M[p]=M[p],M[k]
        unit=bar(M[k][k]);M[k]=[mul(unit,x) for x in M[k]]
        for i in range(n):
            if i!=k and M[i][k]:
                f=M[i][k];M[i]=[x^mul(f,y) for x,y in zip(M[i],M[k])]
    assert [r[:n] for r in M]==eye(n)
    return [r[n:] for r in M]
def matrices(text):
    result=[]
    for block in re.findall(r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',text,re.S):
        rows=[[x.strip() for x in r.strip().split('&')] for r in block.split(r'\\') if r.strip()]
        if rows and all(len(r)==len(rows[0]) for r in rows):result.append(rows)
    return result
def import_matrices(text):
    sectionA=text.split(r'\label{app:4XC}',1)[1].split(r'\section{Polynomial representation',1)[0]
    sectionB=text.split(r'\label{app:Polynomial}',1)[1].split(r'\section{Entanglement renormalization',1)[0]
    a=matrices(sectionA);b=matrices(sectionB)
    select=lambda ms,n,m:[[[poly(x) for x in r] for r in M] for M in ms if len(M)==n and len(M[0])==m]
    A,B=select(a,6,3);W,T=select(a,6,6)
    return A,B,W,T,select(b,16,8)[0],select(b,16,16)[0],select(b,8,8)[0]
def shear(W,T,ancilla_identity=False):
    w=eye(16);t=eye(16)
    for i in range(6):
        for j in range(6):w[8+i][j]=W[i][j];t[i][8+j]=T[i][j]
    if ancilla_identity:
        for i in (6,7):w[8+i][i]=ONE;t[i][8+i]=ONE
    return w,t

def notebook_gates(text):
    block=text.split('RowBox[{"Vtransformed", "="',1)[1].split('RowBox[{"Dagger",',1)[0]
    tokens=re.findall(r'"((?:\\.|[^"\\])*)"',block)
    expr=''.join(t for t in tokens if not t.startswith('\\'))
    gates=re.findall(r'~(cNot|hadamard|cPhase|swapRow|rowMul|cPhaseg)~\{([^{}]+)\}',expr)
    assert len(gates)==expr.count('~')//2,(len(gates),expr)
    return [(kind,args.split(',')) for kind,args in gates]
def gate_matrix(kind,args):
    E=eye(16)
    if kind=='hadamard':
        for v in args:
            i=int(v)-1;E[i],E[i+8]=E[i+8],E[i]
    elif kind=='swapRow':
        i,j=[int(v)-1 for v in args]
        E[i],E[j]=E[j],E[i];E[i+8],E[j+8]=E[j+8],E[i+8]
    elif kind=='rowMul':
        i=int(args[0])-1;f=poly(args[1]);assert len(f)==1;E[i][i]=E[i+8][i+8]=f
    elif kind=='cPhase':E[int(args[0])+7][int(args[0])-1]=poly(args[1])
    else:
        i,j=int(args[0])-1,int(args[1])-1;f=poly(args[2])
        if kind=='cNot':E[i][j]=f;E[j+8][i+8]=bar(f)
        else:assert kind=='cPhaseg';E[i+8][j]=f;E[j+8][i]=bar(f)
    return E
