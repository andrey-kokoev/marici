"""Two-head fork packet preserves witnesses without inventing an issuer."""
from pathlib import Path
import json
A={'issuer':'toy-owner','source':'unit-square','event':'event-A','epoch':1,'sequence':2,'head':'head-A','row_digest':'rows-A'}
B={**A,'head':'head-B','row_digest':'rows-B'}
packet={'left':A,'right':B,'delivery':{'left_client':'client-1','right_client':'client-2'},
        'issuer_trust_anchor':None,'transport_attestation':None}
def validate(p):
 if 'left' not in p or 'right' not in p:return 'INCOMPLETE_TWO_HEAD_WITNESS'
 x,y=p['left'],p['right']
 fields=('issuer','source','event','epoch','sequence')
 if any(x.get(k)!=y.get(k) for k in fields):return 'DIFFERENT_AUTHORITY_SLOT'
 if x.get('head')==y.get('head') or x.get('row_digest')==y.get('row_digest'):return 'NO_CONFLICTING_HEADS'
 if not p.get('issuer_trust_anchor') or not p.get('transport_attestation'):return 'CONDITIONAL_FORK_PACKET_UNAUTHENTICATED'
 return 'EXTERNAL_AUTHENTICATION_NOT_IMPLEMENTED'
assert validate(packet)=='CONDITIONAL_FORK_PACKET_UNAUTHENTICATED'
assert validate({'left':A})=='INCOMPLETE_TWO_HEAD_WITNESS'
assert validate({**packet,'right':{**B,'issuer':'other-owner'}})=='DIFFERENT_AUTHORITY_SLOT'
assert validate({**packet,'right':A})=='NO_CONFLICTING_HEADS'
assert validate({**packet,'issuer_trust_anchor':'self-asserted','transport_attestation':'self-asserted'})=='EXTERNAL_AUTHENTICATION_NOT_IMPLEMENTED'
base=Path(__file__).resolve().parents[1]
(base/'results/fork-evidence-packet.json').write_text(json.dumps(packet,indent=2)+'\n')
report={'passed':True,'conditional_two_head_packet':True,'omitted_head_refused':True,'foreign_issuer_scope_refused':True,'same_head_refused':True,'self_declared_trust_and_transport_not_authenticated':True,'scope':'Toy bounded witness schema; no real issuer, signed checkpoints, authentic gossip, global anti-fork proof, execution authority or analytic correspondence.'}
(base/'results/fork-evidence-packet-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
