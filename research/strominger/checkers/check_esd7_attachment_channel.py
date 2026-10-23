"""Independent census comparison and hostile controls for source-rule assembly."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
from esd7_attachment_channel import produce, decode, Assembler

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/strominger/results/'
TARGET = 'research/voevodsky/results/esd7_explicit_analytical_census.json'
NATIVE = BASE+'channel-assembled-native-fixture.json'
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def rejected(records):
    try:
        decode(records)
    except ValueError:
        return True
    return False


def main():
    records = list(produce(7))
    assembled = decode(records)
    # The target enters only after assembly, and is never passed to the decoder.
    target = json.loads((ROOT/TARGET).read_text())
    kinds = ['vertices','edges','triangles','tetrahedra']
    check('full independently generated f-vector', [len(assembled[k]) for k in kinds] == [120,560,784,343])
    for kind in kinds:
        actual = assembled[kind]; expected = target[kind]
        check('exact labelled '+kind+' comparison', len(actual) == len(expected) and all(
            all(a[key] == b[key] for key in ['id'] + (['cumulative','barycentric'] if kind == 'vertices' else ['vertices'])
                + (['edges','incidence'] if kind == 'triangles' else ['edges','faces'] if kind == 'tetrahedra' else []))
            for a,b in zip(actual,expected)))
    all_cells = {c['id']:c for kind in kinds for c in assembled[kind]}
    for cell in all_cells.values():
        twice = Counter()
        for term in cell['boundary']:
            for sub in all_cells[term['cell']]['boundary']:
                twice[sub['cell']] += term['sign']*sub['sign']
        if any(twice.values()):
            raise AssertionError('nonzero boundary squared '+cell['id'])
    check('signed boundary squared vanishes on every cell', True)
    global_boundary = Counter()
    for t in assembled['tetrahedra']:
        for term in t['boundary']:
            global_boundary[term['cell']] += t['orientation']*term['sign']
    check('all588 interior faces cancel and196 boundary faces remain',
          sum(f['incidence'] == 2 for f in assembled['triangles']) == 588 and
          sum(n != 0 for n in global_boundary.values()) == 196 and
          all(global_boundary[f['id']] == 0 for f in assembled['triangles'] if f['incidence'] == 2))
    # 784 faces =588 shared +196 exterior; no target face table is needed for this law.
    check('shared face homotopies are referenced rather than copied per tetrahedron', all(
        set(t['coherenceObligation'][key] for key in ['H_ABC','H_ABD','H_ACD','H_BCD']) == set(t['faces'])
        for t in assembled['tetrahedra']))
    check('every formal face homotopy has matching composite and direct endpoints', all(
        [all_cells[e]['vertices'] for e in f['homotopyObligation']['composite']] ==
        [f['vertices'][:2],f['vertices'][1:]] and
        all_cells[f['homotopyObligation']['direct']]['vertices'] == [f['vertices'][0],f['vertices'][2]]
        for f in assembled['triangles']))
    check('analytical face and tetrahedral fillers remain explicit undischarged obligations',
          not assembled['analyticalCoherenceDischarged'] and
          all(not f['homotopyObligation']['discharged'] for f in assembled['triangles']) and
          all(not t['coherenceObligation']['discharged'] for t in assembled['tetrahedra']))
    reverse = decode([records[0], *reversed(records[1:-1]), records[-1]])
    check('attachment reordering preserves complete labelled incidence and distinct occurrence log',
          all(reverse[k] == assembled[k] for k in kinds) and reverse['records'] != assembled['records'] and
          reverse['occurrences'] == assembled['occurrences'])
    check('scale family is a construction rule rather than a fixed343-cell table', all(
        len(decode(produce(scale))['tetrahedra']) == scale**3 for scale in [1,2,3,4]))
    check('every attachment has an explicit incremental prefix', len(assembled['prefixes']) == len(records) and
          [p['cells'][3] for p in assembled['prefixes'][1:-1]] == list(range(1,344)))
    native = json.loads((ROOT/NATIVE).read_text())
    vertices = {v['id']:tuple(v['barycentric']) for v in assembled['vertices']}
    ids = {tuple(sorted(vertices[v] for v in c['vertices'])):c['id'] for k in kinds for c in assembled[k]}
    def embed(point):
        return tuple(2-int(x) for x in point.split(','))
    cells = [{'nativeCell':c['id'],'generatedCell':ids.get(tuple(sorted(embed(v) for v in c['vertices'])))} for c in native['cells']]
    faces = [{'nativeOperation':o['id'],'generatedFace':ids.get(tuple(sorted(embed(v) for v in o['face'])))}
             for o in native['operations'] if o.get('face')]
    check('all five native fixture bodies embed in generated cells', len(cells) == 5 and all(c['generatedCell'] for c in cells))
    check('every native physical interface embeds in a shared generated face', bool(faces) and
          all(c['generatedFace'] and all_cells[c['generatedFace']]['incidence'] == 2 for c in faces))
    tests = []
    bad = copy.deepcopy(records); bad[1]['order'] = [0,0,2]; tests.append(('invalid axis order',bad))
    bad = copy.deepcopy(records); bad[1]['base'] = [-1,0,0]; tests.append(('outside chamber',bad))
    bad = copy.deepcopy(records); bad[2]['occurrence'] = bad[1]['occurrence']; tests.append(('duplicate occurrence',bad))
    bad = copy.deepcopy(records); duplicate = copy.deepcopy(bad[1]); duplicate['occurrence'] = 'extra'; bad.insert(2,duplicate); tests.append(('duplicate geometric attachment',bad))
    bad = copy.deepcopy(records); bad.pop(100); tests.append(('missing attachment at closure',bad))
    bad = copy.deepcopy(records); bad[0]['tetrahedra'] = target['tetrahedra']; tests.append(('completed target injection',bad))
    tests.extend([('missing close',records[:-1]),('after close',records+[records[1]]),
                  ('truncation to114 records is not full assembly',records[:113]+[records[-1]])])
    for name,bad in tests:
        check('reject '+name, rejected(bad))
    a = Assembler(); a.feed(records[0])
    try:
        a.feed({'type':'bogus'})
    except ValueError:
        pass
    try:
        a.feed(records[1]); fail_closed = False
    except ValueError:
        fail_closed = True
    check('failed assembly cannot resume', fail_closed)
    stream_path = BASE+'esd7-geometric-attachment-channel.json'
    assembly_path = BASE+'esd7-channel-generated-assembly.json'
    for p,data in [(stream_path,{'records':records}),(assembly_path,assembled)]:
        (ROOT/p).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    inputs = [TARGET,NATIVE,stream_path,assembly_path,
              'research/strominger/checkers/esd7_attachment_channel.py',
              'research/strominger/checkers/check_esd7_attachment_channel.py',
              'research/voevodsky/checkers/check_esd7_explicit_analytical_census.py']
    report = {'status':'passed','check_count':len(checks),'checks':checks,'recordCount':len(records),
              'counts':{k:len(assembled[k]) for k in kinds},'nativeEmbedding':{'cells':cells,'interfaces':faces},
              'targetUsedByDecoder':False,'geometricReconstructionEstablished':True,
              'full114ChannelEstablished':False,'analyticalCoherenceDischarged':False,'globalFieldTransportEstablished':False,
              'pendingObligations':{'faceHomotopies':784,'tetrahedralCoherences':343},
              'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
              'scope':'Source-rule geometric reconstruction through345 records, not the conjectured114-record retained channel. Shared signed incidence is verified; analytical fillers and full-complex field transport are not supplied.'}
    out = ROOT/BASE/'esd7-attachment-channel-verification.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','recordCount','counts','pendingObligations']}))


if __name__ == '__main__':
    main()
