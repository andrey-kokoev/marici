"""Paired frozen largest-domain and smallest-label one-pin plans."""
from ramsey38_one_pin_holdout import P as previous,prior,old,select,apply_pin,compare,freeze,prev,json,sys
P=prev.out/'ramsey38_large_pivot_predictions.json';R=prev.out/'ramsey38_large_pivot_comparison.json';B=prev.out/'ramsey38_label_pivot_control_predictions.json';C=prev.out/'ramsey38_label_pivot_control_comparison.json'
protocol='First novel eligible arrays after 824; stop after three records with different pivot labels or 24 records (not based on filling outcomes). Compare largest-domain, smallest-label tie vs smallest ambiguous label, same first lexical star, same committed collar and single propagation. No retries. Every ordered edge target; independent exhaustive seven-label extension census.'
def both(e,L,rs,candidates):
    base=select(e,L,rs,candidates);a=apply_pin(e,base);b=apply_pin(e,base,True);return dict(b,control=a,different=bool(a['pin'] and b['pin']['vertex']!=a['pin']['vertex']))
def done(es):return len(es)>=24 or sum(any(d['different'] for d in e['requests']) for e in es)>=3
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        freeze(824,(old,prior,previous),both,P,protocol,done);data=json.loads(P.read_text());data['paired_sha']=prev.sha(P.read_bytes());
        for e in data['cases']:e['requests']=[dict(j=d['j'],l=d['l'],**d['control']) for d in e['requests']]
        prev.save(B,data)
    elif sys.argv[1]=='compare':compare(P,R);compare(B,C)
