"""Finite countermodel: equal cycle readings/action need not erase order.

Dimensionless exact toy model, not Planck-scale physics. A and B append
source labels, leave the chosen scalar presentation invariant, and carry
equal positive action charges. A common phase counts event number only.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]

def evaluate(word):
    # Phase is measured in turns. Two events constitute one stipulated cycle.
    phase=Q(0);action=Q(0);a=b=ab=ba=0;trace=[]
    for event in word:
        if event=='A':
            ba+=b;a+=1
        elif event=='B':
            ab+=a;b+=1
        else:raise ValueError('unknown event')
        phase+=Q(1,2);action+=Q(1,2)
        trace.append({'presentation':0,'phase_mod_one':str(phase%1),'action':str(action)})
    return {'presentation':0,'phase_mod_one':str(phase%1),
            'cycle_winding':int(phase),'action':str(action),
            'counts':[a,b],'ordered_pairs':[ab,ba],
            'oriented_order_residual':ab-ba,'visible_trace':trace}

def concat_signature(left,right):
    # Ordered pair information is compositional, but not additive alone.
    a,b=left['counts'];c,d=right['counts']
    ab,ba=left['ordered_pairs'];cd,dc=right['ordered_pairs']
    return [a+c,b+d],[ab+cd+a*d,ba+dc+b*c]

ab=evaluate('AB');ba=evaluate('BA')
for key in ('presentation','phase_mod_one','cycle_winding','action','counts','visible_trace'):
    assert ab[key]==ba[key]
assert ab['action']=='1' and ab['cycle_winding']==1
assert ab['oriented_order_residual']==1 and ba['oriented_order_residual']==-1
# The repeated presentation, the phase modulo a turn, AND winding fail to
# determine the source order. An order-sensitive residual distinguishes it.
assert ab['ordered_pairs']==[1,0] and ba['ordered_pairs']==[0,1]
checks=0
words=[''.join(w) for n in range(5) for w in product('AB',repeat=n)]
for u in words:
    for w in words:
        counts,pairs=concat_signature(evaluate(u),evaluate(w))
        full=evaluate(u+w)
        assert counts==full['counts'] and pairs==full['ordered_pairs']
        checks+=1
# A degree-two order residual is not a complete history encoding.
# Both histories have identical counts and ordered pair counts.
x=evaluate('ABBA');y=evaluate('BAAB')
for key in ('presentation','phase_mod_one','cycle_winding','action','counts','ordered_pairs','oriented_order_residual','visible_trace'):
    assert x[key]==y[key]
# A third-order subsequence coordinate resolves THIS collision.
def subsequences(word,pattern):
    state=[1]+[0]*len(pattern)
    for event in word:
        for j in range(len(pattern)-1,-1,-1):
            if pattern[j]==event:state[j+1]+=state[j]
    return state[-1]
assert subsequences('ABBA','ABB')==1 and subsequences('BAAB','ABB')==0
# Full ordered subsequence data through the admitted maximum word length
# separates this bounded alphabet source; the top-degree word is retained.
signatures={}
for word in words:
    signature=tuple(subsequences(word,p) for p in words)
    assert signature not in signatures
    signatures[signature]=word

report={'passed':True,'units':'dimensionless; cycle period and action unit are stipulated',
 'one_cycle_AB':ab,'one_cycle_BA':ba,
 'equal_readings_equal_positive_action_different_order':True,
 'composition_checks':checks,
 'second_order_collision':{'words':['ABBA','BAAB'],'shared_signature':x,
   'third_order_ABB_coordinate':[1,0]},
 'complete_bounded_history_test':{'maximum_length':4,'distinct_histories':len(words),
   'separated_by_full_ordered_signature':True},
 'interpretation':'A positive action budget and recurrent phase do not determine order. Ordered residuals can distinguish specific histories; a bounded-order residual need not preserve an unrestricted history.',
 'not_established':['Planck time as a universal recurrence period','a physical lower action bound',
   'pressure produced by Planck constant','physical measurement resolution or realizability']}
(ROOT/'research/voevodsky/results/equal-action-order-cycles.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
