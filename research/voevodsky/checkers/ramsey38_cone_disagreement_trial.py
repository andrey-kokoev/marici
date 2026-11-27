"""Select disagreements without consulting any post-middle continuation outcome."""
from ramsey38_exposure_cone_holdout import P as previous,old,prev,freeze,select,compare,json,sys
P=prev.out/'ramsey38_cone_disagreement_predictions.json';A=prev.out/'ramsey38_cone_disagreement_screen.json';R=prev.out/'ramsey38_cone_disagreement_comparison.json';S=prev.out/'ramsey38_cone_disagreement_scores.json'
protocol='Records 165001..230000 inclusive, same first eligible novel root per record with competing reachable early-burial middle meshes, exclude previous two middle-pool samples. Freeze all candidates, select only requests where joint edge/face and exterior-cone predicted sets differ. Stop at three disagreement records or range cap. Verify rejected meshes and all alternatives in same pool with independent unrestricted final census. Distinguish rejecting false choice from improving first success.'
def done(es):return sum(any(d['passes']!=d['joint'] for d in e['requests']) for e in es)>=3
def run():
    freeze(165000,230000,(old,previous),select,A,protocol,done);data=json.loads(A.read_text());out=[];stats=dict(requests=0,joint_nonempty=0,disagreements=0,changed_first=0)
    for e in data['cases']:
        dif=[]
        for d in e['requests']:
            stats['requests']+=1;stats['joint_nonempty']+=bool(d['joint']);stats['changed_first']+=d['cone']!=d['edgeface']
            if d['passes']!=d['joint']:stats['disagreements']+=1;dif.append(d)
        if dif:out.append(dict(e,requests=dif))
    print(stats);prev.save(P,dict(protocol=protocol,screen_sha=prev.sha(A.read_bytes()),counts=stats,cases=out))
def score():
    data=json.loads(P.read_text());assert data['screen_sha']==prev.sha(A.read_bytes());compare(P,R);it=iter(json.loads(R.read_text())['results']);out=[]
    for e in data['cases']:
        for d in e['requests']:
            z=next(it);assert (e['record'],d['moves'],d['goal'])==(z['record'],z['moves'],z['goal']);rej=set(d['joint'])-set(d['passes']);ok=set(z['ok']);out.append(dict(record=e['record'],goal=d['goal'],moves=d['moves'],rejected=sorted(rej),rejected_valid=sorted(rej&ok),alternatives=sorted(ok-rej),old_hit=d['edgeface'] in ok,new_hit=d['cone'] in ok));print(out[-1])
    prev.save(S,dict(comparison_sha=prev.sha(R.read_bytes()),results=out))
if __name__=='__main__':{'freeze':run,'compare':score}[sys.argv[1]]()
