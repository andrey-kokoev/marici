"""Algebraic reverse transport; no solver imports or optimizer calls.

Domain: the exact full-schema translation of a TwoFreeTail descriptor,
objectives +/- the first free atom, explicit nonnegative row weights.
"""
from fractions import Fraction as Q
from verify_two_free_schema_bridge import expected_translation,check
from verify_two_free_tail_queries import reconstruct,verify,digest

def reverse_objective(origin,sign,proof):
    if type(sign) is not int or sign not in (-1,1):raise ValueError('UNSUPPORTED_OBJECTIVE')
    target=expected_translation(origin);m=origin['m'];i,j=origin['free'];pins=dict((k,Q(h)) for k,h in origin['pins'])
    objective=['0']*(m+2);objective[i+2]=str(sign)
    check(target,{'kind':'maximize','objective':objective},proof)
    rows=reconstruct(origin);weights={};constant=Q(0);removed=0
    for index,raw in proof['weights']:
        w=Q(raw)
        if index<2*m:
            atom,orientation=divmod(index,2)
            if atom in pins:
                slack=100+2*atom-pins[atom] if orientation==0 else pins[atom]
                assert slack>=0;constant+=w*slack;removed+=1;continue
            position=0 if atom==i else 2
            index=position+(1 if orientation==0 else 0)
        elif index<2*m+2*len(pins):
            removed+=1;continue  # Exact pin equalities become 0<=0.
        else:index=4+index-2*m-2*len(pins)
        weights[index]=weights.get(index,Q(0))+w
    terms=[[k,str(v)] for k,v in sorted(weights.items()) if v]
    normal=tuple(sum(Q(v)*rows[k][0][n] for k,v in terms) for n in (0,1))
    bound=sum((Q(v)*rows[k][1] for k,v in terms),Q(0))
    if proof['status']=='EMPTY':
        assert normal==(0,0) and bound<0
        result={'status':'INCONSISTENT','farkas':terms}
    else:
        # Primal feasibility + dual equality force every discarded positive
        # constant's total contribution to vanish at an optimum.
        assert constant==0 and normal==(sign,0) and bound==Q(proof['value'])
        result={'point':[proof['x'][i],proof['x'][j]],'value':proof['value'],'dual':terms}
    return result,{'constant_removed':str(constant),'input_terms':len(proof['weights']),
                   'removed_terms':removed,'output_terms':len(terms)}

def reverse_pair(origin,query,proofs):
    if len(proofs)!=2:raise ValueError('TWO_OBJECTIVE_PROOFS_REQUIRED')
    low,l=reverse_objective(origin,-1,proofs[0]);high,h=reverse_objective(origin,1,proofs[1])
    empty='farkas' in low;assert empty==('farkas' in high)
    if empty:result=low
    else:
        lo=-Q(low['value']);hi=Q(high['value']);threshold=Q(query['threshold'])
        status='FORCED_TRUE' if hi<=threshold else 'FORCED_FALSE' if lo>threshold else 'UNRESOLVED'
        result={'status':status,'interval':[str(lo),str(hi)],'minimum':low,'maximum':high}
    sd=digest(origin)
    packet={'schema':'two-free-tail-certificate-v1','state':origin,'query':query,'state_digest':sd,
            'query_digest':digest({'state_digest':sd,'query':query}),'result':result}
    verify(origin,query,packet)
    return packet,[l,h]
