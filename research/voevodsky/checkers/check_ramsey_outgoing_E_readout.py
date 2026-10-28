"""Correct the N-selector test: ordered E window on a typed outgoing reference."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/strominger/checkers'))
from exact_multiradical import Radical as R, mm, adj, identity, serialize

pins = {}
def load(path):
    raw = (ROOT/path).read_bytes()
    pins[path] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def restore(matrix):
    return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in matrix]

def select(indices):
    return [[R(int(j==i)) for j in range(5)] for i in indices]

def main():
    prior = load('research/voevodsky/results/ramsey-based-port-readout-v1.json')
    for path, digest in prior['source_sha256'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, path
        pins[path]=digest
    seed = load('research/strominger/results/full-five-channel-candidate/verification.json')
    native = load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    seam = load('research/strominger/results/T-seam-transition/verification.json')
    # Read current owning JS exports, not a transcription of E's window.
    module_paths = [
        'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
        'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
        'research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs',
        'research/strominger/demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs']
    js = """
import {windowProtocol} from './research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {activePhaseSlots,spectralReadout} from './research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const E=windowProtocol.find(x=>x.species==='electron');
const active=[[2,3],[5,7],[11,13]],value=[[17,19],[23,29],[0,0],[0,0],[0,0]];
activePhaseSlots.electron.forEach((slot,i)=>value[slot]=active[i]);
const readout=spectralReadout('electron',value);
console.log(JSON.stringify({window:[...E.window],context:E.continuation,slots:activePhaseSlots.electron,active,readout}));
"""
    run = subprocess.run(['node','--input-type=module','-e',js], cwd=ROOT, capture_output=True, text=True, check=True)
    owner = json.loads(run.stdout)
    for p in module_paths: pins[p]=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
    incoming,outgoing,Q=seam['incomingReference'],seam['outgoingReference'],seam['basisMap']
    assert owner['window']==['M1','C1','C2'] and owner['context']=='M2'
    assert [incoming[i] for i in owner['slots']]==owner['window']
    slots=[outgoing.index(name) for name in owner['window']]
    complement=[i for i in range(5) if i not in slots]
    assert slots==[2,1,3] and complement==[0,4]
    assert [outgoing[i] for i in complement]==['M0','M2']
    U,B=restore(prior['fullFieldMap']),restore(seed['neutronFiveEmbedding'])
    metric=list(map(F,native['source']['metric']))
    readout=[[B[j][i].conj()*metric[j] for j in range(36)] for i in range(5)]
    Pi=select(Q)
    assert mm(U,B)==mm(B,Pi) and mm(readout,U)==mm(Pi,readout)
    active=select(slots); rest=select(complement); packet=active+rest
    assert mm(adj(packet),packet)==identity(5)
    Ereadout=mm(active,readout); Creadout=mm(rest,readout)
    assert mm(Ereadout,U)==mm(mm(active,Pi),readout)
    assert mm(Creadout,U)==mm(mm(rest,Pi),readout)
    assert mm(adj(packet),mm(packet,mm(readout,U)))==mm(Pi,readout)
    # These are exact formal-coordinate witnesses, not one numerical sample.
    assert mm(active,Pi)==select([Q[i] for i in slots])
    dropped=mm(adj(active),active)
    assert dropped!=identity(5)
    for slot in complement:
        basis=[[R(int(i==slot))] for i in range(5)]
        assert mm(active,basis)==[[R()] for _ in range(3)]
        assert mm(packet,basis)!=[[R()] for _ in range(5)]
    # Catch both the earlier wrong-species selector and reuse of unrebased E indices.
    assert select([1,2,3])!=active
    assert select(owner['slots'])!=active
    assert mm(select([1,2,3]),mm(Pi,readout))!=mm(active,mm(Pi,readout))
    assert [outgoing[i] for i in owner['slots']]!=owner['window']
    # JS spectral reconstruction is floating-point API regression, separately
    # identified from the exact rational/radical selector equations above.
    error=max(abs(x-y) for row,want in zip(owner['readout']['reconstructed'],owner['active']) for x,y in zip(row,want))
    assert error<1e-12
    assert [r['slot'] for r in owner['readout']['complement']]==[0,1]
    pins[Path(__file__).relative_to(ROOT).as_posix()]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    exact_path='research/strominger/checkers/exact_multiradical.py'
    pins[exact_path]=hashlib.sha256((ROOT/exact_path).read_bytes()).hexdigest()
    result={
        'schema':'marici.ramsey-outgoing-E-readout.v1', 'checkerStatus':'passed',
        'node':'T-seam-based-port-readout-binding',
        'scientificStatus':'ordered_outgoing_E_readout_and_full_complement_pass',
        'corrects':'research/voevodsky/results/ramsey-based-port-readout-v1.json#namedReadout',
        'correction':'The previous unchanged-N-selector failure does not obstruct the intended outgoing E window.',
        'outgoingReference':outgoing,'orderedWindow':owner['window'],'outgoingWindowSlots':slots,
        'nativeIncomingEWindowSlots':owner['slots'], 'context':owner['context'],
        'complementSlots':complement,'complementMarks':[outgoing[i] for i in complement],
        'sourceSlotsReadAfterQ':[Q[i] for i in slots],
        'exactFull36ActiveReadoutSquare':True,'exactFull36ComplementReadoutSquare':True,
        'exactFiveCoefficientRecovery':True,
        'activeReadout':serialize(Ereadout),'complementReadout':serialize(Creadout),
        'negativeControls':['unchanged N selector rejected','unrebased incoming E selector rejected','either discarded complement direction destroys recovery'],
        'nativeSpectralAPIRegression':{'maxReconstructionError':error,'tolerance':1e-12,
            'note':'Scratch array tests spectral arithmetic only. Its complement slots are not claimed to have native incoming-reference provenance.'},
        'remainingObligations':[
            'Source selection of the sector assignment remains conditional on the prior five-column seed/Q ansatz.',
            'An ordered E observation on a36-coordinate retained field is not yet identification with the native8-coordinate E return or joint44 NE exchange.',
            'The outgoing complement M0,M2 is retained under those labels; M2 is not silently renamed incoming C0.',
            'Native transition admission, full occurrence/geometry witnesses and global coherence are not established by this selector test.'
        ],
        'netOutcomeChanged':False,'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-outgoing-E-readout-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['checkerStatus','scientificStatus','orderedWindow','outgoingWindowSlots','complementMarks','exactFiveCoefficientRecovery']}))

if __name__=='__main__': main()
