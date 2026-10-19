"""Exact H1 audit of both source endpoint poses. Requires sympy (uv --with sympy)."""
import argparse
import hashlib
import io
import json
from fractions import Fraction
from pathlib import Path
from zipfile import ZipFile
import sympy as s
from high_energy_scattering_net import ROOT, HOME, validate as validate_historical

ARCHIVE=HOME/'pentachoron_joint_incoming_bundle.zip'
RESULT=HOME/'results/local-full-spinor-switches.v1.json'
PREFIX='source/inputs/geometric_source/inputs/open_products/'


def audit(gate_sink=None):
    validate_historical()  # Verify frozen source archive hashes before reading nested inputs.
    evidence={ARCHIVE.relative_to(ROOT).as_posix():hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()}
    data=ARCHIVE.read_bytes()
    for member in ('inputs/pentachoron_strained_phase_bundle.zip','inputs/pentachoron_axial_deformation_bundle.zip'):
        with ZipFile(io.BytesIO(data)) as z:data=z.read(member)
        evidence[member]=hashlib.sha256(data).hexdigest()
    with ZipFile(io.BytesIO(data)) as z:
        geometry=z.read(PREFIX+'inputs/geometry.json')
        code=z.read(PREFIX+'open_product_solver.py')
    evidence[PREFIX+'inputs/geometry.json']=hashlib.sha256(geometry).hexdigest()
    evidence[PREFIX+'open_product_solver.py']=hashlib.sha256(code).hexdigest()
    g=json.loads(geometry)
    simp=lambda m:s.Matrix(m).applyfunc(lambda x:s.simplify(s.expand(x)))
    def eq(a,b):assert simp(a-b)==s.zeros(*a.shape)
    I=s.eye(2);sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    def pa(v):return simp(sum((v[i]*sig[i] for i in range(3)),s.zeros(2)))
    def wedge(a,b):return a*b.T-b*a.T
    def ch(b,eta=1):return s.Matrix([b[1,2]+eta*b[0,3],b[2,0]+eta*b[1,3],b[0,1]+eta*b[2,3]])
    def normals(p):return simp(-s.sqrt(5)/4*(p-s.ones(5,1)*sum((p[i,:] for i in range(5)),s.zeros(1,4))/5))
    def orientation(c,face):
        body,om=divmod(c,5);v=[k for k in range(5) if k!=om];rm=next(k for k in v if k not in face)
        return (-1)**(body+om+v.index(rm))
    Om=s.Matrix(g['hinge_generator']);eq(Om.T,-Om);eq(Om**3,-Om)
    records=[]
    for sign in (1,-1):
        # exp(+/- theta*Om/2); cos(theta/2)=sqrt(6)/4, sin(theta/2)=sqrt(10)/4.
        rot=lambda t:simp(s.eye(4)+t*s.sqrt(10)/4*Om+(1-s.sqrt(6)/4)*Om**2)
        L=simp(s.Matrix(g['initial_left'])*rot(-sign).T)
        R=simp(s.Matrix(g['initial_right'])*rot(sign).T)
        nl,nr=normals(L),normals(R);small=2 if sign==1 else 3
        eq(nr[small,:],-nl[small,:])
        for j in range(5):
            if j==small:continue
            face=tuple(k for k in range(5) if k not in (small,j));name=''.join('ABCDE'[k] for k in face)
            b=wedge((L[face[1],:]-L[face[0],:]).T,(L[face[2],:]-L[face[0],:]).T)
            expected=s.Integer(1) if set((small,j))=={2,3} else s.Rational(1,9) if j==4 else s.Rational(7,9)
            full_gate=s.zeros(20)
            for c in (small,j):
                pl=simp((I-pa(orientation(c,face)*ch(b,1)/(4*s.sqrt(3))))/2)
                pr=simp((I-pa(orientation(c+5,face)*ch(b,-1)/(4*s.sqrt(3))))/2)
                for p in (pl,pr):eq(p.H,p);eq(p*p,p);assert s.trace(p)==1
                if c==small:
                    tangent=simp((nl[j,:].T+nl[small,:].T/4)/s.sqrt(s.Rational(15,16)))
                    u=simp(s.I*pa(ch(wedge(nl[small,:].T,tangent))))
                else:
                    a=s.sqrt(s.simplify((1+(nl[c,:]*nr[c,:].T)[0])/2))
                    assert a!=0
                    u=simp(a*I-s.I*pa(ch(wedge(nl[c,:].T,nr[c,:].T)))/(2*a))
                eq(u.H*u,I)
                m=simp(pr*u*pl)
                eq(m.H*m,expected*pl)
                eq(pl*u.H*(I-pr)*u*pl,(1-expected)*pl)
                Q=simp(s.BlockMatrix([[I,u.H],[u,I]]).as_explicit()/2)
                eq(Q.H,Q);eq(Q*Q,Q)
                slots=[2*c,2*c+1,2*(c+5),2*(c+5)+1]
                for a,row in enumerate(slots):
                    for bcol,col in enumerate(slots):full_gate[row,col]=Q[a,bcol]
                J=s.BlockMatrix([[s.eye(4)-Q,Q],[Q,s.eye(4)-Q]]).as_explicit()
                eq(J.H,J);eq(J*J,s.eye(8))
                defect=s.BlockMatrix([[Q,-Q],[-Q,Q]]).as_explicit()
                eq((J-s.eye(8)).H*(J-s.eye(8)),2*defect)
                records.append({'endpoint':sign,'face':name,'cell':c,'selected_weight':str(expected),'complement_weight':str(1-expected),'exact_identities':'pass'})
                print('exact',sign,name,c,flush=True)
            if gate_sink is not None and name!='ABE':
                gate_sink.setdefault(sign,[]).append((name,full_gate))
            # The two four-coordinate blocks have disjoint supports inside C20.
            assert len({2*c+k for c in (small,small+5,j,j+5) for k in (0,1)})==8
    evidence[Path(__file__).relative_to(ROOT).as_posix()]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert len(records)==16
    return {'schema':'marici.scattering.local-full-spinor-switches.v1','status':'pass','source_sha256':evidence,
            'arithmetic':'exact sympy algebraic expressions, no floating tolerance','sympy_version':s.__version__,
            'endpoint_count':2,'additional_faces_per_endpoint':3,'local_blocks_checked':16,'includes_initial_ABE':True,
            'records':records,'full_C20_extension':'Two disjoint four-coordinate Q blocks and zero elsewhere; complementary cell coordinates retained. Thus Q20 is Hermitian idempotent. The same block polynomial gives the C40 sector-pair J involution and Gram defect identity.',
            'positivity':'The defect is a Gram operator (J-I)*(J-I); hence its quadratic form is nonnegative for every retained input.',
            'scope':'H1 only; no ordered-path equality, encoder transport, source-law derivation, continuum claim or physical outcome.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale H1 receipt'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: exact H1 identities at both endpoint poses, with complements retained.')


if __name__=='__main__':main()
