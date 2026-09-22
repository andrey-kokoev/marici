"""Independent certificate replay: congruence, minimality and live lift."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    cp=OUT/'compressed-observer-live-lift-contract.json';c=load(cp)
    path=OUT/'compressed-observer-live-lift.json';r=load(path)
    source=OUT/'actual-source-evidence-coupling.json';data=load(source);states=data['states']
    assert sha(cp)==r['contract_sha256'] and sha(source)==r['source_sha256']==c['source_sha256']
    assert sha(OUT/'source-evidence-coupling-contract.json')==c['source_contract_sha256']
    oldlabels=list(map(tuple,c['current_labels']));newlabels=list(map(tuple,c['extended_labels']))
    assert len(oldlabels)==16 and newlabels==oldlabels+[('audit-origin',0),('audit-origin',1)]
    bits=[int(s['word'][:2]==[0,1]) for s in states]
    tables=[]
    for i,s in enumerate(states):
        edges={tuple(e):j for e,j in s['transitions']}
        old=[(e in edges,edges.get(e,i)) for e in oldlabels]
        tables.append((old,old+[(b==bits[i],i) for b in (0,1)]))
    for which,name in enumerate(('old','new')):
        classes=r[name+'_partition'];q=r[name+'_quotient']
        assert len(classes)==638 and set(classes)==set(range(len(q)))
        for i,s in enumerate(states):
            group=q[classes[i]];assert i in group['members']
            expected=[0,sum(1<<e for e in s['word']),s['received'],s['issued']]
            assert group['output']==expected
            assert group['transitions']==[[a,classes[j]] for a,j in tables[i][which]]
        for cid,group in enumerate(q):assert sorted(group['members'])==[i for i,k in enumerate(classes) if k==cid]
        witnesses=r[name+'_distinguishing_words'];pairs=set()
        for witness in witnesses:
            a,b=witness['classes'];assert 0<=a<b<len(q) and (a,b) not in pairs;pairs.add((a,b))
            different=q[a]['output']!=q[b]['output']
            for label in witness['word']:
                assert 0<=label<len(q[a]['transitions'])
                aa,an=q[a]['transitions'][label];ba,bn=q[b]['transitions'][label]
                different |= aa!=ba
                a,b=an,bn;different |= q[a]['output']!=q[b]['output']
            assert different,'invalid distinguishing continuation'
        assert len(pairs)==len(q)*(len(q)-1)//2
    old,new=r['old_partition'],r['new_partition'];oq,nq=r['old_quotient'],r['new_quotient']
    projection=r['refined_to_old_projection'];assert len(projection)==len(nq)
    for i in range(638):assert projection[new[i]]==old[i]
    for i,q in enumerate(nq):
        assert q['output']==oq[projection[i]]['output']
        for label,(a,j) in enumerate(q['transitions'][:16]):assert [a,projection[j]]==oq[projection[i]]['transitions'][label]
    lift={(a,b):n for a,b,n in r['lift_table']};assert len(lift)==len(r['lift_table'])==70
    assert set(lift)=={(old[i],bits[i]) for i in range(638)}
    assert set(lift.values())==set(range(len(nq)))
    count=0
    for i in range(638):
        assert lift[old[i],bits[i]]==new[i]
        for label,(admitted,j) in enumerate(tables[i][1]):
            assert bits[j]==bits[i]
            assert [admitted,lift[old[j],bits[j]]]==nq[lift[old[i],bits[i]]]['transitions'][label]
            count+=1
    for i in data['initial_state_ids']:assert lift[old[i],bits[i]]==new[i]
    split={cid for cid in range(len(oq)) if len({new[i] for i in oq[cid]['members']})>1}
    assert split=={w['old_class'] for w in r['old_class_split_obstructions']} and len(split)==8
    for witness in r['old_class_split_obstructions']:
        i,j=witness['source_states'];assert old[i]==old[j] and new[i]!=new[j] and bits[i]!=bits[j]
        assert tables[i][1][-1][0]!=tables[j][1][-1][0]
        assert lift[old[i],1-bits[i]]!=new[i]
    assert len(oq)==62<638 and len(nq)==70<638 and count==r['all_label_lift_checks']==11484
    report={'passed':True,'current_minimal_states':62,'extended_minimal_states':70,
      'split_old_classes':8,'compatible_class_bit_pairs':70,'all_label_lift_checks':count,
      'minimality':'All 1891 old and 2415 refined class pairs have verified distinguishing continuations.',
      'live_lift':'Checked initialization and one-step invariant imply correctness for arbitrary finite executions.',
      'retention_scope':'Known initial state and faithful origin-bit retention required; fabricated or lost provenance is not repaired by minimization.',
      'certificate_sha256':sha(path)}
    (OUT/'compressed-observer-live-lift-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
