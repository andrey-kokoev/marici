"""Append-only gain refinement with local chart-dependent cache binding."""
from dataclasses import dataclass
import copy
from fractions import Fraction as Q
from balanced_gain_adapter import validate,chart,normalize,compile_gain
from modular_difference_interfaces import closure,block_edges,compose_blocks,digest,rational
from verify_balanced_gain_adapter import check

def dependency(raw,scales,normalized,index):
    block=raw['blocks'][index]
    return digest({'rule':'balanced-gain-block-v1','m':raw['m'],'source_binding':raw['binding'],
      'raw_block':block,'local_scales':[[v,str(scales[v])] for v in block['nodes']],
      'normalized_block':normalized['blocks'][index]})

def row(values,allowed):
    if not isinstance(values,(tuple,list)) or len(values)!=4:raise ValueError('GAIN_ROW_REQUIRED')
    u,v,g,b=values;g,b=rational(g),rational(b)
    if type(u) is not int or type(v) is not int or u==0 or v==0 or u not in allowed or v not in allowed or g<=0:
        raise ValueError('INVALID_RAW_GAIN_ROW')
    return [u,v,str(g),str(b)]

@dataclass(frozen=True)
class GainHistory:
    _state: object
    _proof: object
    @classmethod
    def create(cls,raw):
        state=validate(raw)
        if state['retention']!='archive-backed':raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        _,proof=compile_gain(state);check(state,proof)
        return cls(copy.deepcopy(state),copy.deepcopy(proof))
    def descriptor(self):return copy.deepcopy(self._state)
    def certificate(self):return copy.deepcopy(self._proof)
    def audit(self,node,threshold):
        if type(node) is not int or node==0 or node not in self._state['public']:raise ValueError('UNEXPOSED_RAW_ATOM')
        h=rational(threshold);check(self._state,self._proof)
        if self._proof['status']=='UNSUPPORTED':raise NotImplementedError('UNBALANCED_CHART')
        if self._proof['status']=='INCONSISTENT':return {'node':node,'threshold':str(h),'status':'INCONSISTENT'}
        scale=Q(self._proof['scales'][node]);bounds={(u,v):Q(w) for u,v,w in self._proof['normalized']['summary']}
        lo,hi=-scale*bounds[node,0],scale*bounds[0,node]
        return {'node':node,'threshold':str(h),'interval':[str(lo),str(hi)],
                'status':'FORCED_TRUE' if hi<=h else 'FORCED_FALSE' if lo>h else 'UNRESOLVED'}
    def refine_block(self,index,values):
        if type(index) is not int or not 0<=index<len(self._state['blocks']):raise ValueError('INVALID_BLOCK')
        return self._append({'kind':'block-gain','block':index,'row':row(values,self._state['blocks'][index]['nodes'])})
    def refine_public(self,values):
        return self._append({'kind':'public-gain','row':row(values,self._state['public'])})
    def _append(self,operation):
        if self._state['retention']!='archive-backed':raise PermissionError('FINE_EVIDENCE_NOT_RETAINED')
        before=self._state;check(before,self._proof);after=copy.deepcopy(before)
        if operation['kind']=='block-gain':after['blocks'][operation['block']]['evidence'].append(operation['row'])
        else:after['exterior'].append(operation['row'])
        after=validate(after);scales,cycle=chart(after)
        packet={'state':after,'state_digest':digest(after)}
        transition={'kind':'incremental-gain-v1','before_digest':digest(before),'previous_proof_digest':digest(self._proof),
                    'operation':copy.deepcopy(operation),'reused_blocks':[],'recomputed_blocks':[],
                    'dependencies':[],'changed_scale_nodes':[],'after':packet}
        if cycle is not None:
            packet.update(status='UNSUPPORTED',reason='UNBALANCED_CHART',gain_cycle=cycle)
        else:
            normalized=normalize(after,scales);proofs=[]
            if 'scales' not in self._proof:raise AssertionError('append cannot repair an unbalanced gain walk')
            old_scales=self._proof['scales'];old_normalized=self._proof['normalized']['state']
            transition['changed_scale_nodes']=[v for v,s in enumerate(scales) if str(s)!=old_scales[v]]
            for i,b in enumerate(normalized['blocks']):
                old=dependency(before,old_scales,old_normalized,i);new=dependency(after,scales,normalized,i)
                transition['dependencies'].append([old,new])
                if old==new:
                    proofs.append(copy.deepcopy(self._proof['normalized']['blocks'][i]));transition['reused_blocks'].append(i)
                else:
                    proofs.append(closure(b['nodes'],block_edges(b)));transition['recomputed_blocks'].append(i)
            _,composed=compose_blocks(normalized,proofs)
            packet.update(status=composed['status'],scales=list(map(str,scales)),normalized=composed)
        return GainHistory(copy.deepcopy(after),copy.deepcopy(packet)),transition
