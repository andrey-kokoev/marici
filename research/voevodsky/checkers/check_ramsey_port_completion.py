"""Exhaustive finite completion fibers under the existing independent-port policy."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def key(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def main():
    path=BASE/'results/ramsey-native-PN-overlap-span-v1.json';d=json.loads(path.read_text())
    for p,h in d['source_sha256'].items():assert sha(ROOT/p)==h,'stale admitted port '+p
    ports=d['witness']['ports'];assert len(ports)==48
    pairs=[(a,b) for a in ports for b in ports if a['face']==b['face']]
    assert len(pairs)==576
    for a,b in pairs:
        assert set(a['faceVertices'])==set(b['faceVertices'])  # keep each ordered record; compare support only
        assert a['permitMCount']==b['permitMCount']==2
    selectors={
      'source_only':lambda a,b:key(a),
      'source_and_target_roles':lambda a,b:key([a,b['role']]),
      'source_and_target_named_references':lambda a,b:key([a,b['source']['chart']['aliases']]),
      'source_and_target_references_and_reader':lambda a,b:key([a,b['source']['chart']['aliases'],b['sourceFrame']['window'],b['sourceFrame']['context']]),
      'source_and_requested_target_chart':lambda a,b:key([a,b['chart']])}
    audits={};witnesses={}
    for name,select in selectors.items():
        groups={}
        for a,b in pairs:groups.setdefault(select(a,b),[]).append((a,b))
        counts=[len(set(key(b) for a,b in group)) for group in groups.values()]
        audits[name]={'fibers':len(groups),'minimumDistinctTargets':min(counts),
          'maximumDistinctTargets':max(counts),'factorsOnDeclaredFiniteFamily':max(counts)==1}
        bad=next((g for g in groups.values() if len(set(key(b) for a,b in g))>1),None)
        if bad:
            a,b=bad[0];a2,c=next((x,y) for x,y in bad if y!=b)
            assert a==a2 and select(a,b)==select(a2,c) and b!=c
            witnesses[name]={'source':a,'target0':b,'target1':c}
    assert not audits['source_only']['factorsOnDeclaredFiniteFamily']
    assert not audits['source_and_target_roles']['factorsOnDeclaredFiniteFamily']
    assert audits['source_and_requested_target_chart']['factorsOnDeclaredFiniteFamily']
    assert audits['source_and_target_references_and_reader']['factorsOnDeclaredFiniteFamily']
    # Unique target selection is partial: arbitrary requested charts need not permit this face.
    lookup={(p['chart'],p['face']):p for p in ports};assert len(lookup)==48
    accepted=refused=0
    for a in ports:
        for chart in range(24):
            target=lookup.get((chart,a['face']))
            if target is None:refused+=1
            else:
                accepted+=1;assert (a,target) in pairs
    assert (accepted,refused)==(576,576)
    files=[path,Path(__file__),BASE/'contracts/ramsey-port-completion-attempt.v1.json',
      BASE/'results/ramsey-comparison-forgetting-v1.json']
    out={'schema':'marici.ramsey-port-completion.verification.v1','status':'passed',
      'scope_id':'existing-independent-port-completion-fibers-v1',
      'verification_level':'exhaustive exact finite runtime audit of previously validated port records; no new kernel replay',
      'admissionPolicyUnchanged':True,'ports':48,'admissiblePairs':576,'selectors':audits,
      'ambiguityWitnesses':witnesses,'requestedChartAccepted':accepted,'requestedChartRefused':refused,
      'requestedChartSelectorUsesAdmittedTargetTable':True,'sourceOnlyRoleTransportProved':False,
      'arbitraryRequestedChartTotalTransport':False,'parentDescentResolved':False,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in files}}
    (BASE/'results/ramsey-port-completion-v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','ambiguityWitnesses']},indent=2))
if __name__=='__main__':main()
