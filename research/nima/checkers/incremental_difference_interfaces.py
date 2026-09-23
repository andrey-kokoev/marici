"""Persistent difference refinements; no gain-chart reuse is admitted."""
from dataclasses import dataclass
import copy
from modular_difference_interfaces import canonical,compile_state,compose_blocks,closure,block_edges,summary,digest,rational
from verify_modular_difference_interfaces import check

def edge(raw,allowed):
    if not isinstance(raw,(tuple,list)) or len(raw)!=3:raise ValueError('DIFFERENCE_EDGE_REQUIRED')
    u,v,w=raw
    if type(u) is not int or type(v) is not int or u not in allowed or v not in allowed:raise ValueError('UNEXPOSED_ENDPOINT')
    return [u,v,str(rational(w))]
def dependency(state,index):
    return digest({'source_rule':'raw-tail-caps-v1','m':state['m'],'binding':state['binding'],'block':state['blocks'][index]})

@dataclass(frozen=True)
class ArchivedHistory:
    _state: object
    _proof: object
    @classmethod
    def create(cls,raw):
        state=canonical(raw)
        if state['retention']!='archive-backed':raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        _,proof=compile_state(state);check(state,proof)
        return cls(copy.deepcopy(state),copy.deepcopy(proof))
    def descriptor(self):return copy.deepcopy(self._state)
    def certificate(self):return copy.deepcopy(self._proof)
    def refine_block(self,index,row):
        if type(index) is not int or not 0<=index<len(self._state['blocks']):raise ValueError('INVALID_BLOCK')
        operation={'kind':'block-edge','block':index,'edge':edge(row,self._state['blocks'][index]['nodes'])}
        return self._append(operation)
    def refine_public(self,row):
        return self._append({'kind':'public-edge','edge':edge(row,self._state['public'])})
    def _append(self,operation):
        before=self._state;check(before,self._proof);after=copy.deepcopy(before)
        changed=[]
        if operation['kind']=='block-edge':
            index=operation['block'];after['blocks'][index]['evidence'].append(operation['edge']);changed=[index]
        else:after['exterior'].append(operation['edge'])
        after=canonical(after);proofs=copy.deepcopy(self._proof['blocks']);reused=[]
        for index,b in enumerate(after['blocks']):
            if index in changed:proofs[index]=closure(b['nodes'],block_edges(b))
            else:
                assert dependency(before,index)==dependency(after,index);reused.append(index)
        _,proof=compose_blocks(after,proofs)
        transition={'kind':'archived-difference-refinement-v1','before_digest':digest(before),
          'previous_proof_digest':digest(self._proof),'operation':copy.deepcopy(operation),
          'dependencies':[[dependency(before,i),dependency(after,i)] for i in range(len(proofs))],
          'reused_blocks':reused,'recomputed_blocks':changed,'after':proof}
        return ArchivedHistory(copy.deepcopy(after),copy.deepcopy(proof)),transition

@dataclass(frozen=True)
class PublicHistory:
    _state: object
    @classmethod
    def from_live(cls,descriptor):
        if descriptor['retention']!='public-only':raise ValueError('EXPLICIT_PUBLIC_ONLY_STATE_REQUIRED')
        state={'schema':'public-difference-history-v1','m':descriptor['m'],'binding':descriptor['binding'],
               'public':copy.deepcopy(descriptor['public']),'retention':'public-only','origin_digest':descriptor['origin_digest'],
               'base_summary':copy.deepcopy(descriptor['summary']),'frames':[]}
        return cls(state)
    def descriptor(self):return copy.deepcopy(self._state)
    def refine_public(self,row):
        before=self._state;row=edge(row,before['public']);after=copy.deepcopy(before);after['frames'].append(row)
        proof=closure(after['public'],after['base_summary']+after['frames'])
        transition={'kind':'public-difference-refinement-v1','before_digest':digest(before),
          'operation':{'kind':'public-edge','edge':row},'after':after,'closure':proof}
        if proof['status']=='CONSISTENT':transition['summary']=summary(after['public'],proof,after['public'])
        return PublicHistory(after),transition
    def refine_block(self,*args):raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
    def expose(self,requested):
        if not set(requested)<=set(self._state['public']):raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        return self
