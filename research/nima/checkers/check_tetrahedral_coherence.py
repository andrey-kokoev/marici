"""Two-stage higher-coherence fixture; valid faces need not have a filler."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import copy
import json
import tempfile
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
STRUCT=ROOT.parent/'voevodsky'
SV=STRUCT/'certificates/verify_structural_gain_square.py'
spec=importlib.util.spec_from_file_location('tetra',ROOT/'certificates/verify_tetrahedral_coherence.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
c=v.Checker(SV);s=c.s


def mat(a):return [[F(x) for x in row] for row in a]
def pack(a):return [[str(x) for x in row] for row in a]
def invdiag(a):return [[1/a[i][i] if i==j else F(0) for j in range(len(a))] for i in range(len(a))]


def reframe(structural,q):
    result=copy.deepcopy(structural);qi=invdiag(q);ambient=s.block(q,s.eye(3));ai=s.block(qi,s.eye(3))
    for node in result['nodes'].values():
        for key in ('D','K','M','N','L','f','H'):node[key]=pack(s.mul(q,mat(node[key])))
        for key in ('left','right'):node[key]=pack(s.mul(s.mul(q,mat(node[key])),qi))
        for key in ('pi','private'):node[key]=pack(s.mul(mat(node[key]),qi))
        node['graph']=pack(s.mul(ambient,mat(node['graph'])))
    for edge in result['edges'].values():
        edge['upper']=pack(s.mul(s.mul(q,mat(edge['upper'])),qi))
        edge['pushout']=pack(s.mul(s.mul(ambient,mat(edge['pushout'])),ai))
    s.verify(result)
    return result


def stage(structural,obstructed=False):
    nodes=[structural['nodes'][key] for key in c.names]
    d=[mat(n['D']) for n in nodes]
    edges={key:s.mul(d[int(key[1])],invdiag(d[int(key[0])])) for key in c.edges}
    filler=edges['03']
    h0=s.mul(mat(nodes[3]['left']),filler)
    h1=s.mul(filler,mat(nodes[0]['left']))
    faces={key:{'h0':pack(s.zero(5,5)),'h1':pack(s.zero(5,5))} for key in c.faces}
    faces['023']={'h0':pack(h0),'h1':pack(h1 if obstructed else s.neg(h1))}
    return {'structural':structural,'edges':{k:pack(m) for k,m in edges.items()},'faces':faces,
            'tetrahedron':{'status':'OBSTRUCTED','entry':[1,0]} if obstructed else {'status':'FILLED','k0':pack(filler)}}


def bundle(structures,q,obstructed=False):
    return {'schema':'filtered-module-tetrahedral-tower-fixture-v1',
        'scope':'finite-fixture-not-an-identification-of-the-four-physical-towers',
        'stages':[stage(st,obstructed) for st in structures],
        'transitions':[{'vertex_maps':{str(i):pack(q) for i in range(4)}}]}


def main():
    structural=s.load(STRUCT/'results/structural-gain-square.json')
    q=[[F((2,3,5,7,11)[i]) if i==j else F(0) for j in range(5)] for i in range(5)]
    structures=[structural,reframe(structural,q)]
    good=bundle(structures,q);obstructed=bundle(structures,q,True)
    positive=c.verify(good);negative=c.verify(obstructed)
    assert positive['tetrahedral_statuses']==['FILLED','FILLED']
    assert negative['tetrahedral_statuses']==['OBSTRUCTED','OBSTRUCTED']
    corruptions=[]
    bad=copy.deepcopy(good);bad['stages'][0]['tetrahedron']['k0']=pack(s.zero(5,5));corruptions.append(bad)
    bad=copy.deepcopy(obstructed)
    for i in range(2):bad['stages'][i]['tetrahedron']=copy.deepcopy(good['stages'][i]['tetrahedron'])
    corruptions.append(bad) # All four faces pass; no module-linear K can fill them.
    bad=copy.deepcopy(good)
    for key in ('h0','h1'):
        bad['stages'][1]['faces']['023'][key]=pack([[2*x for x in row] for row in mat(bad['stages'][1]['faces']['023'][key])])
    bad['stages'][1]['tetrahedron']['k0']=pack([[2*x for x in row] for row in mat(bad['stages'][1]['tetrahedron']['k0'])])
    # Each tetrahedron still fills, but the chosen witnesses do not transport.
    for st in bad['stages']:c.stage(st)
    corruptions.append(bad)
    bad=copy.deepcopy(good);bad['stages'][0]['faces']['012']['h0'][0][0]='1';corruptions.append(bad)
    bad=copy.deepcopy(good);bad['stages'][0]['edges']['12'][0][0]='1';corruptions.append(bad)
    bad=copy.deepcopy(obstructed);bad['stages'][0]['tetrahedron']['entry']=[0,0];corruptions.append(bad)
    bad=copy.deepcopy(good);bad['scope']='four-physical-towers-identified';corruptions.append(bad)
    bad=copy.deepcopy(good);bad['stages'][0]['structural']['nodes']['10']['left']=copy.deepcopy(structural['nodes']['00']['left']);corruptions.append(bad)
    rejected=0
    for bad in corruptions:
        try:c.verify(bad)
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid higher coherence accepted')
    with tempfile.TemporaryDirectory(prefix='tetrahedral-coherence-') as directory:
        d=Path(directory)
        for source in (ROOT/'certificates/verify_tetrahedral_coherence.py',SV):
            (d/source.name).write_bytes(source.read_bytes())
        for name,obj in [('filled',good),('obstructed',obstructed)]:
            (d/(name+'.json')).write_text(json.dumps(obj),encoding='utf-8')
            run=subprocess.run([sys.executable,'-I',str(d/'verify_tetrahedral_coherence.py'),
                str(d/(name+'.json')),str(d/SV.name)],cwd=d,capture_output=True,text=True,timeout=120)
            assert run.returncode==0,(run.stdout,run.stderr)
    for name,obj in [('tetrahedral-coherence-filled',good),('tetrahedral-coherence-obstructed',obstructed)]:
        (ROOT/'results'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    report={'passed':True,'filled_tower':positive,'obstructed_tower':negative,
        'corruptions_rejected':rejected,'valid_faces_without_module_linear_filler':True,
        'individually_filled_stages_without_witness_transport_rejected':True,
        'isolated_verification':True,
        'limitation':'A finite typed higher-coherence mechanism, not an identification of the four actual productization towers or arbitrary higher cells.'}
    (ROOT/'results/tetrahedral-coherence-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
