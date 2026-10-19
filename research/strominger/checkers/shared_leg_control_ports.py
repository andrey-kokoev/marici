"""Differentiate actual shared-leg products; do not invent response actuators.

These columns describe mathematical preparation variations. Installation of
independent ports or conversion to forces is a separate authority boundary.
"""
import sympy as S


def primitive_legs(values):
    roles=(('ax',11),('ay',11),('sx',4),('sy',4))
    return tuple((role,i,S.Matrix(values[f'{role}{i}'])) for role,n in roles for i in range(n))


def response_field(legs):
    lookup={(role,i):matrix for role,i,matrix in legs}
    matrices=[]
    for tag,n in (('a',11),('s',4)):
        matrices += [lookup[(tag+'y',j)]*lookup[(tag+'x',i)] for i in range(n) for j in range(n)]
    return S.Matrix([[value for value in matrix] for matrix in matrices])


def product_jacobian(legs):
    """delta(Y_j X_i)=Y_j deltaX_i+deltaY_j X_i, in548 response coordinates."""
    lookup={(role,i):matrix for role,i,matrix in legs}
    columns=[]
    labels=[]
    for role,index,_ in legs:
        tag=role[0]
        n=11 if tag=='a' else 4
        offset=0 if tag=='a' else 121
        for a in range(2):
            for b in range(2):
                unit=S.zeros(2)
                unit[a,b]=1
                column=S.zeros(548,1)
                for other in range(n):
                    if role[1]=='x':
                        slot=offset+n*index+other
                        derivative=lookup[(tag+'y',other)]*unit
                    else:
                        slot=offset+n*other+index
                        derivative=unit*lookup[(tag+'x',other)]
                    column[4*slot:4*slot+4,0]=S.Matrix(4,1,list(derivative))
                columns.append(column)
                labels.append((role,index,a,b))
    return S.SparseMatrix.hstack(*(S.SparseMatrix(column) for column in columns)),tuple(labels)


def incoming_leg_projector(selected):
    """Original arrow target families; state legs have singleton families."""
    P=S.zeros(11)
    for i,edge in enumerate(selected):
        members=[j for j,e in enumerate(selected) if e[1]==edge[1]]
        for j in members: P[i,j]=S.Rational(1,len(members))
    return P


def gain_for_energy(energy, quadratic, quartic):
    """Conditional scalar energy task: H(q)=a q^2+b q^4, q in[0,1].

    Returns eta=1-q for the prior family-relaxation law, not actuator authority.
    """
    energy,quadratic,quartic=map(S.sympify,(energy,quadratic,quartic))
    if quadratic.is_positive is not True or quartic.is_positive is not True:
        raise ValueError('positive energy coefficients required')
    if (energy.is_nonnegative is not True
            or (quadratic+quartic-energy).is_nonnegative is not True):
        raise ValueError('target energy outside contraction range')
    q2=2*energy/(quadratic+S.sqrt(quadratic**2+4*quartic*energy))
    return S.simplify(1-S.sqrt(q2))


def leg_vector(legs):
    return S.Matrix([value for _,_,matrix in legs for value in matrix])


def vector_legs(vector,template):
    return tuple((role,index,S.Matrix(2,2,list(vector[4*i:4*i+4,0])))
                 for i,(role,index,_) in enumerate(template))
