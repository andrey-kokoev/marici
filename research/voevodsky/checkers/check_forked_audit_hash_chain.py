"""Linked hashes detect mutation, not which valid fork is authoritative."""
from hashlib import sha256
from pathlib import Path
import json
enc=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def block(seq,parent,payload):
 body={'sequence':seq,'parent':parent,'payload':payload}
 return {'body':body,'digest':sha256(enc(body)).hexdigest()}
def verify(chain):
 for i,node in enumerate(chain):
  body=node['body']
  if node['digest']!=sha256(enc(body)).hexdigest():return 'MUTATED_BLOCK'
  if body['sequence']!=i or (i and body['parent']!=chain[i-1]['digest']):return 'BROKEN_LINK'
 return 'INTERNALLY_VALID'
gen=block(0,'genesis',{'source':'unit-square'});common=block(1,gen['digest'],{'event':'prepared'})
a=block(2,common['digest'],{'event':'event-A','row_digest':'row-one'})
b=block(2,common['digest'],{'event':'event-A','row_digest':'row-two'})
A=[gen,common,a];B=[gen,common,b]
assert verify(A)==verify(B)=='INTERNALLY_VALID' and a['digest']!=b['digest']
mutated=[gen,common,{'body':{**a['body'],'payload':{'event':'event-A','row_digest':'mutated'}},'digest':a['digest']}]
assert verify(mutated)=='MUTATED_BLOCK'
def checkpoint_verdict(chain,trusted_checkpoint):
 if verify(chain)!='INTERNALLY_VALID':return 'BAD_CHAIN'
 if trusted_checkpoint is None:return 'FORK_UNRESOLVED_NO_TRUSTED_HEAD'
 if trusted_checkpoint['sequence']!=len(chain)-1 or trusted_checkpoint['digest']!=chain[-1]['digest']:return 'CHECKPOINT_MISMATCH'
 return 'CONDITIONAL_CHAIN_MATCH'
assert checkpoint_verdict(A,None)==checkpoint_verdict(B,None)=='FORK_UNRESOLVED_NO_TRUSTED_HEAD'
pinned={'sequence':2,'digest':a['digest']}
assert checkpoint_verdict(A,pinned)=='CONDITIONAL_CHAIN_MATCH'
assert checkpoint_verdict(B,pinned)=='CHECKPOINT_MISMATCH'
assert checkpoint_verdict(A,{'sequence':1,'digest':common['digest']})=='CHECKPOINT_MISMATCH'
report={'passed':True,'common_parent':True,'two_internally_valid_conflicting_heads':True,'single_branch_mutation_detected':True,'without_trusted_head':'FORK_UNRESOLVED_NO_TRUSTED_HEAD','conditional_pinned_head_rejects_other_branch':True,'noncertification':'Pinned head is a trusted input; no independent external checkpoint, issuer identity, globally consistent gossip or real Farkas event authenticated.'}
out=Path(__file__).resolve().parents[1]/'results/forked-audit-hash-chain.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
