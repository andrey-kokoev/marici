"""Matched-budget removal of the endpoint gate. Keep ties visible. Score functions do not use repair labels."""
from ramsey_contact_overlap_transfer import profile,predict,D,CAT,find,decode
import gzip,json
from collections import defaultdict

def audit():
    refdata=json.loads((D.parent/'ramsey_contact_overlap_transfer.json').read_text());refs=refdata['training_profiles'];budget=refdata['predicted_links'];w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);possible=set(json.loads((D.parent/'ramsey_intact27_pack_layers.json').read_text())['87']['seven_candidates']);scores={};marked=set();percore=set();eligible=0
    for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        s=l.rstrip()
        if sum(s[1:].translate(w))!=87:continue
        a=decode(s.decode());
        if i in possible and find(a)['example']:continue
        eligible+=1;es,marks=predict(a);ends={v for e in marks for v in e};local=[]
        for e in es:
            h=profile(a,e);key=(i,e);scores[key]=min(sum(abs(x-y) for x,y in zip(h,r)) for r in refs);local.append(key)
            if ends.intersection(e):marked.add(key)
        if local:percore.update(key for key in local if scores[key]==min(scores[j] for j in local))
    truth={(i,tuple(e)) for i,e in refdata['actual']};old={(i,tuple(e)) for i,e in refdata['predictions']};assert len(scores)==15300 and eligible==1358 and len(marked)==1478 and len(truth-marked)==6
    def summary(keys):return dict(cost=len(keys),hits=len(keys&truth),hits_outside_gate=len((keys&truth)-marked),new_vs_old=len((keys&truth)-old),lost_vs_old=len((old&truth)-keys))
    def ranked(keys):
        ordered=sorted(keys,key=lambda k:(scores[k],k));cut=scores[ordered[budget-1]];sure={k for k in keys if scores[k]<cut};tied={k for k in keys if scores[k]==cut};n=budget-len(sure);return dict(lexicographic=summary(set(ordered[:budget])),cutoff=cut,below=summary(sure),ties=summary(tied),tie_slots=n,possible_hits=[len(sure&truth)+max(0,n-len(tied-truth)),len(sure&truth)+min(n,len(tied&truth))],all_ties=summary(sure|tied))
    out=dict(original=summary(old),ungated_per_core=summary(percore),gated_global=ranked(marked),ungated_global=ranked(set(scores)));print(out);(D.parent/'ramsey_contact_endpoint_ablation.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
