"""Require a partial veto, not rejection of the entire candidate set."""
from ramsey38_cone_disagreement_trial import A as prior,old,previous,freeze,prev,json,sys,select,compare
P=prev.out/'ramsey38_partial_veto_predictions.json';A=prev.out/'ramsey38_partial_veto_screen.json';R=prev.out/'ramsey38_partial_veto_comparison.json'
protocol='Remaining catalogue records after 230000, stopping after two records with a partial veto. Exclude all eligible arrays in three earlier samples. Same root, pool and goal eligibility. Select before final search iff exterior-cone passed set is a proper NONEMPTY subset of edge/face candidates; no dependence on changed first choice. Verify all candidates including those neither rule selected.'
def contrast(d):return set()<set(d['passes'])<set(d['joint'])
def run():
    freeze(230000,477142,(old,previous,prior),select,A,protocol,lambda es:sum(any(contrast(d) for d in e['requests']) for e in es)>=2);data=json.loads(A.read_text());ds=[d for e in data['cases'] for d in e['requests']];cases=[dict(e,requests=[d for d in e['requests'] if contrast(d)]) for e in data['cases'] if any(contrast(d) for d in e['requests'])];counts=dict(screened=data['screened'],records=len(data['cases']),requests=len(ds),joint_nonempty=sum(bool(d['joint']) for d in ds),cone_nonempty=sum(bool(d['passes']) for d in ds),full_veto=sum(bool(d['joint']) and not d['passes'] for d in ds),partial_veto=sum(contrast(d) for d in ds));print(counts);prev.save(P,dict(protocol=protocol,screen_sha=prev.sha(A.read_bytes()),counts=counts,cases=cases))
if __name__=='__main__':
    if sys.argv[1]=='freeze':run()
    elif sys.argv[1]=='compare':
        assert json.loads(P.read_text())['cases'],'no qualifying requests';compare(P,R)
