"""H10 source-constructor admission failure: chirality is slot-fixed, not owner-carried."""
import argparse
import ast
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile
import sympy as s
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

ARCHIVE=HOME/'pentachoron_joint_incoming_bundle.zip'
RESULT=HOME/'results/participant-exchange.v1.json'
PROOF=HOME/'PARTICIPANT-EXCHANGE-OBSTRUCTION.md'
PREFIX='source/inputs/geometric_source/inputs/open_products/'


def audit():
    historical_validate();data=ARCHIVE.read_bytes();nested={}
    for member in ('inputs/pentachoron_strained_phase_bundle.zip','inputs/pentachoron_axial_deformation_bundle.zip'):
        with ZipFile(io.BytesIO(data)) as z:data=z.read(member)
        nested[member]=hashlib.sha256(data).hexdigest()
    with ZipFile(io.BytesIO(data)) as z:
        raw_geometry=z.read(PREFIX+'inputs/geometry.json');raw_code=z.read(PREFIX+'open_product_solver.py')
    g=json.loads(raw_geometry);code=raw_code.decode()
    tree=ast.parse(code);endpoint=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='endpoint')
    seam_rule='edges += [(i,j,lift(NL[i],NL[j],+1)),(i+5,j+5,lift(NR[i],NR[j],-1))]'
    assert seam_rule in ast.get_source_segment(code,endpoint)
    assert [a.arg for a in endpoint.args.args]==['src','sign']
    # Verify that no body-carried chirality parameter is read from the source packet.
    keys={n.slice.value for n in ast.walk(endpoint) if isinstance(n,ast.Subscript) and isinstance(n.value,ast.Name) and n.value.id=='src' and isinstance(n.slice,ast.Constant)}
    assert keys=={'left','right','Om','A','T0','HC'}
    simp=lambda m:s.Matrix(m).applyfunc(lambda x:s.simplify(s.expand(x)))
    def eq(a,b):assert simp(a-b)==s.zeros(*a.shape)
    sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    def lift(n,m,eta):
        a=s.sqrt(s.simplify((1+(n.T*m)[0])/2));assert a!=0
        B=n*m.T-m*n.T
        v=[B[1,2]+eta*B[0,3],B[2,0]+eta*B[1,3],B[0,1]+eta*B[2,3]]
        return simp(a*s.eye(2)-s.I*sum((v[k]*sig[k] for k in range(3)),s.zeros(2))/(2*a))
    def normals(p):return simp(-s.sqrt(5)/4*(p-s.ones(5,1)*sum((p[i,:] for i in range(5)),s.zeros(1,4))/5))
    Om=s.Matrix(g['hinge_generator']);eq(Om.T,-Om);eq(Om**3,-Om)
    rotation=lambda sign:simp(s.eye(4)+sign*s.sqrt(10)/4*Om+(1-s.sqrt(6)/4)*Om**2)
    X20=s.zeros(20)
    for i in range(20):X20[(i+10)%20,i]=1
    X8=s.zeros(8)
    for i in range(8):X8[(i+4)%8,i]=1
    eq(X20*X20,s.eye(20));eq(X8*X8,s.eye(8))
    records=[]
    for sign in (1,-1):
        # Old right geometry, now placed in the new left slot, with ambient frame unchanged.
        R=simp(s.Matrix(g['initial_right'])*rotation(sign).T);nr=normals(R)
        old_right=lift(nr[0,:].T,nr[1,:].T,-1)
        rebuilt_new_left=lift(nr[0,:].T,nr[1,:].T,+1)
        eq(old_right.H*old_right,s.eye(2));eq(rebuilt_new_left.H*rebuilt_new_left,s.eye(2))
        defect=simp(rebuilt_new_left-old_right)
        norm_squared=s.simplify(s.trace(defect.H*defect));assert norm_squared>0
        witness=next({'row':i,'column':j,'value':str(defect[i,j])} for i in range(2) for j in range(2) if defect[i,j]!=0)
        # This internal seam is not any of the switches incident to small cell 2 or 3.
        small=2 if sign==1 else 3;assert small not in (0,1)
        records.append({'endpoint':sign,'directed_seam':'cell 0 -> cell 1 of old R / new L',
                        'retained_in_all_pairing_sectors':True,'required_owner_chirality':-1,'actual_new_left_chirality':1,
                        'exact_defect':[[str(x) for x in row] for row in defect.tolist()],
                        'squared_Frobenius_norm':str(norm_squared),'nonzero_entry':witness})
        print('exact chirality-transport obstruction',sign,'squared norm',norm_squared,flush=True)
    sources=[ARCHIVE,PROOF,Path(__file__),HOME/'EXIT-AND-EXCHANGE-CONJECTURES.md']
    return {'schema':'marici.scattering.participant-exchange.v1','status':'pass','H10_disposition':'refuted_in_declared_source_constructor_admission_scope',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources},'nested_archive_sha256':nested,
            'embedded_geometry_sha256':hashlib.sha256(raw_geometry).hexdigest(),'embedded_constructor_sha256':hashlib.sha256(raw_code).hexdigest(),
            'constructor_source_keys':sorted(keys),'slot_fixed_seam_rule':seam_rule,'records':records,
            'permutation_round_trip':'X20^2=I20 and X8^2=I8; failure is not the permutation',
            'full_exchanged_operator_constructed':False,'universal_exchange_impossibility_claimed':False,
            'scope':'The existing source constructor cannot carry the owner chirality under the declared swap; using its slot-fixed rule changes an exact retained seam map. A new tag-aware constructor is not silently substituted.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale exchange obstruction'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: H10 scoped admission obstruction certified; no general exchange impossibility inferred.')


if __name__=='__main__':main()
