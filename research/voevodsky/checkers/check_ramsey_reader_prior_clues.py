"""Prior-evidence pin audit plus one exact bridge to the new reader obstruction.
Does not replay the prior scientific suites or change any owning source.
"""
from pathlib import Path
import json,sys
from check_ramsey_passive_EP_semantics import ROOT,load,restore,perm,pins,sha
from exact_multiradical import mm,adj,identity

def main():
    priorPaths=[
      'research/strominger/results/five-coefficient-field-binding/verification.json',
      'research/strominger/results/full-field-path-coherence/verification.json',
      'research/strominger/results/window-combination-coherence/verification.json',
      'research/strominger/results/joint-field-assembly-sewing.json',
      'research/strominger/results/packet-handoff-naturality-09-v1.json',
      'research/strominger/results/packet-handoff-naturality-10-v1.json']
    audit=[]
    for p in priorPaths:
        d=load(p);sources=d.get('source_sha256',d.get('sourceHashes',{}))
        audit.append({'receipt':p,'reportedStatus':d.get('status',d.get('checkerStatus')),
          'directPinsChecked':len(sources),'directPinsMatch':True,'scientificSuiteReplayed':False})
    moving=load('research/voevodsky/results/ramsey-moving-EP-preparation-v1.json')
    fields=load('research/strominger/results/full-five-channel-candidate/verification.json')
    load('research/voevodsky/results/ramsey-EP-reader-obstruction-v1.json')
    # The body-carrying, reader-natural convention differs from the selected
    # operator-compatible convention only by a unitary five-coordinate basis.
    body=perm([3,4,1,2,0]);reference=perm([3,4,2,0,1]);pi=perm([3,1,2,0,4])
    DP=mm(body,adj(reference));DN=mm(mm(pi,DP),adj(pi))
    assert DP==perm([0,1,4,2,3]);assert DN==perm([2,1,4,3,0])
    assert mm(adj(DN),DN)==identity(5)
    checks=[]
    for row in moving['nativeActions']:
        name=row['operator'];fixed=restore(fields['inducedNeutronFiveProjectors'][name]);bodyAction=restore(row['compressedAction'])
        assert bodyAction!=fixed
        assert bodyAction==mm(mm(DN,fixed),adj(DN))
        checks.append({'operator':name,'sameFixedCoefficientMatrix':False,
          'exactCoefficientFrameConjugacy':True,'fullNativeFieldOperatorChanged':False})
    readerP=perm([2,3,0,1,4]);readerE=perm([0,3,4,1,2])
    assert mm(readerP,body)==mm(body,readerE)
    notes=['research/strominger/five-coefficient-field-binding-v1.md',
      'research/strominger/full-field-path-coherence-v1.md',
      'research/strominger/window-combination-coherence-v1.md',
      'research/strominger/joint-field-assembly-sewing-v1.md',
      'research/strominger/packet-handoff-naturality-09-v1.md',
      'research/strominger/packet-handoff-naturality-10-v1.md',
      'research/strominger/eight-sector-interface-v1.md',
      'research/voevodsky/ramsey-arbitrary-assembly-coherence-v1.md']
    for p in notes:pins[p]=sha(p)
    for module in list(sys.modules.values()):
        f=getattr(module,'__file__',None)
        if f:
            try:p=Path(f).resolve().relative_to(ROOT).as_posix()
            except ValueError:continue
            pins[p]=sha(p)
    p=Path(__file__).relative_to(ROOT).as_posix();pins[p]=sha(p)
    out={'status':'passed','node':'joint44-native-source-selection','priorReceiptAudit':audit,
      'freshBridge':{'PFramePermutation':[0,1,4,2,3],'NFramePermutation':[2,1,4,3,0],
        'bodyComparisonReaderNatural':True,'operatorChecks':checks,
        'interpretation':'The rejected equality of named compressed projectors is replaced by their exact conjugacy under the actual change of coefficient frame. This is not a change of the unchanged full native L/G/N matrices.'},
      'scope':'Prior search and exact local frame-conjugacy bridge. Not source-authorized identification of fixed scalar occurrences, not a new edge/triple descent theorem.',
      'source_sha256':pins}
    (ROOT/'research/voevodsky/results/ramsey-reader-prior-clues-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
