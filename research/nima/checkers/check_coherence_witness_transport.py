"""Witness changes can be certified, but their comparison routes must also agree."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import copy
import json
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


g=load('fixture_producer',ROOT/'checkers/check_tetrahedral_coherence.py')
v=load('witness_verifier',ROOT/'certificates/verify_coherence_witness_transport.py')
c=v.Checker(g.SV);s=c.s


def scaled(m,k):return [[k*x for x in row] for row in m]
def diagonal(values):return [[F(values[i]) if i==j else F(0) for j in range(5)] for i in range(5)]


def main():
    structural=s.load(g.STRUCT/'results/structural-gain-square.json')
    q=diagonal((2,3,5,7,11));r=diagonal((3,5,7,11,13))
    structures=[structural,g.reframe(structural,q)]
    structures.append(g.reframe(structures[1],r))
    frames=[s.eye(5),q,s.mul(r,q)];factors=[F(1),F(2),F(3)]
    stages=[g.stage(st) for st in structures]
    for st,factor in zip(stages,factors):
        for key in ('h0','h1'):st['faces']['023'][key]=g.pack(scaled(g.mat(st['faces']['023'][key]),factor))
        st['tetrahedron']['k0']=g.pack(scaled(g.mat(st['tetrahedron']['k0']),factor))
    comparisons={}
    for key in ('01','12','02'):
        i,j=map(int,key);u=s.mul(frames[j],g.invdiag(frames[i]))
        corrections={face:g.pack(s.zero(5,5)) for face in c.faces}
        corrections['023']=g.pack(scaled(s.mul(u,g.mat(stages[i]['edges']['03'])),factors[j]-factors[i]))
        comparisons[key]={'vertex_maps':{str(vertex):g.pack(u) for vertex in range(4)},'face_rehomotopies':corrections}
    bundle={'schema':'corrected-tetrahedral-witness-transport-v1',
        'scope':'finite-fixture-not-an-identification-of-the-four-physical-towers',
        'stages':stages,'comparisons':comparisons}
    result=c.verify(bundle)
    strict={'schema':'filtered-module-tetrahedral-tower-fixture-v1','scope':bundle['scope'],
            'stages':stages[:2],'transitions':[{'vertex_maps':comparisons['01']['vertex_maps']}]}
    try:g.c.verify(strict)
    except ValueError as exc:assert 'face-witness transport' in str(exc)
    else:raise AssertionError('Strict transport should reject the changed witnesses')
    corruptions=[]
    bad=copy.deepcopy(bundle);bad['comparisons']['01']['face_rehomotopies']['023']=g.pack(s.zero(5,5));corruptions.append(bad)
    # A nonzero closed degree-two perturbation leaves a stage valid, but requires its own comparison data.
    bad=copy.deepcopy(bundle)
    z=s.mul(g.mat(stages[1]['structural']['nodes']['11']['left']),g.mat(stages[1]['edges']['03']))
    bad['stages'][1]['tetrahedron']['k0']=g.pack(c.add(g.mat(stages[1]['tetrahedron']['k0']),z))
    c.stage(bad['stages'][1]);corruptions.append(bad)
    # All three comparisons are individually valid, yet the chosen corrections fail composition.
    bad=copy.deepcopy(bundle);direct=bad['comparisons']['02']['face_rehomotopies']
    u2=g.mat(comparisons['02']['vertex_maps']['2'])
    cycle=s.mul(g.mat(stages[2]['structural']['nodes']['01']['left']),s.mul(u2,g.mat(stages[0]['edges']['02'])))
    direct['012']=g.pack(c.add(g.mat(direct['012']),cycle))
    direct['013']=g.pack(c.add(g.mat(direct['013']),s.mul(g.mat(stages[2]['edges']['23']),cycle)))
    decoded=[c.stage(st) for st in stages]
    for key,raw in bad['comparisons'].items():
        i,j=map(int,key);c.comparison(decoded[i],decoded[j],raw)
    corruptions.append(bad)
    bad=copy.deepcopy(bundle);bad['scope']='actual-four-tower-identification';corruptions.append(bad)
    bad=copy.deepcopy(bundle);bad['comparisons']['01']['face_rehomotopies']['023'][0][0]='0';corruptions.append(bad)
    failures=[]
    for bad in corruptions:
        try:c.verify(bad)
        except ValueError as exc:failures.append(str(exc))
        else:raise AssertionError('Invalid witness transport accepted')
    assert any('rehomotopy routes disagree' in failure for failure in failures)
    # The previous obstructed face cannot be reached by a module-linear degree-two rehomotopy.
    ob=c.stage(g.stage(structures[1],True));old=decoded[0];u=q
    changes=[c.add(s.mul(ob['faces']['023'][degree],u),s.neg(s.mul(u,old['faces']['023'][degree]))) for degree in (0,1)]
    assert c.add(*changes)!=s.zero(5,5) # Every delta(J) has component sum zero.
    with tempfile.TemporaryDirectory(prefix='witness-transport-') as directory:
        d=Path(directory)
        for path in (ROOT/'certificates/verify_coherence_witness_transport.py',ROOT/'certificates/verify_tetrahedral_coherence.py',g.SV):
            (d/path.name).write_bytes(path.read_bytes())
        (d/'bundle.json').write_text(json.dumps(bundle),encoding='utf-8')
        run=subprocess.run([sys.executable,'-I',str(d/'verify_coherence_witness_transport.py'),
            str(d/'bundle.json'),str(d/g.SV.name)],cwd=d,capture_output=True,text=True,timeout=120)
        assert run.returncode==0,(run.stdout,run.stderr)
    (ROOT/'results/corrected-coherence-witness-transport.json').write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')
    report={'passed':True,'verification':result,'strictly_rejected_witness_change_is_now_certified':True,
        'individually_valid_but_noncomposing_comparisons_rejected':True,
        'original_obstruction_survives_admitted_face_rehomotopy':True,
        'corruptions_rejected':len(failures),'rejection_reasons':failures,'isolated_verification':True}
    (ROOT/'results/coherence-witness-transport-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
