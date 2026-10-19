"""Source-bound rank-one packet extraction; native metric normalization kept symbolic."""
from dataclasses import dataclass, replace
from hashlib import sha256
import json
from pathlib import Path
from fractions import Fraction as F
from assemble_metric_coefficient_protocol import (ROOT,A,ZERO,ONE,read_operator,product,sharp,integer_trace)

def digest(p): return sha256(p.read_bytes()).hexdigest()
def act(op,v):
    out=[ZERO]*len(v)
    for (i,j),a in op.items(): out[i]+=a*v[j]
    return tuple(out)
def dot(row,v): return sum((a*b for a,b in zip(row,v)),ZERO)
def norm(v,m): return sum((a.flip(8)*A(w)*a for a,w in zip(v,m)),ZERO)
def ci(): return A(tuple(F(i==8) for i in range(16)))
@dataclass(frozen=True)
class Archive:
    packet_digest:str
    seed:A
    word:tuple=()
@dataclass(frozen=True)
class State:
    archive:Archive
    numerator:tuple
    squared_normalizer:A
@dataclass(frozen=True)
class Packet:
    archive:Archive
    phase:A
    tangent:A

class LineInterface:
    """State denotes numerator/sqrt(rho), not numerator in a rescaled source metric."""
    def __init__(self,path):
        self.path=path;self.digest=digest(path)
        self.data=json.loads(path.read_text(encoding='utf-8'))
        self.metric=tuple(map(F,self.data['source']['metric']));n=len(self.metric)
        self.ops={s:read_operator(self.data['operators'][s],n) for s in 'LGN'}
        N=self.ops['N']
        assert integer_trace(N)==1 and product(N,N)==N and sharp(N,self.metric)==N
        j=min(i for (i,k),v in N.items() if i==k and v!=ZERO)
        self.column=tuple(N.get((i,j),ZERO) for i in range(n))
        self.row=tuple(N.get((j,k),ZERO)/N[j,j] for k in range(n))
        self.rho=norm(self.column,self.metric)
        assert self.rho==A(self.metric[j])*N[j,j] and self.rho!=ZERO
        assert dot(self.row,self.column)==ONE
        assert {(i,k):a*b for i,a in enumerate(self.column) for k,b in enumerate(self.row) if a*b!=ZERO}==N
        # D is precisely K^sharp/rho, with the ORIGINAL source metric.
        assert self.row==tuple(a.flip(8)*A(w)/self.rho for a,w in zip(self.column,self.metric))
        for s,M in self.ops.items():
            assert sharp(M,self.metric)==M and product(M,M)==M
            assert act(M,self.column)==self.column
            assert product(M,N)==N and product(N,M)==N
    def replay(self,a):
        if a.packet_digest!=self.digest: raise ValueError('source binding')
        if a.seed.flip(8)*a.seed!=ONE: raise ValueError('unit phase')
        if any(s not in self.ops for s in a.word): raise ValueError('unavailable operation')
        return a.seed
    def seed(self,z):
        a=Archive(self.digest,z);self.replay(a)
        return State(a,tuple(x*z for x in self.column),self.rho)
    def validate(self,s):
        z=self.replay(s.archive)
        if s.squared_normalizer!=self.rho: raise ValueError('normalization tag')
        if s.numerator!=tuple(x*z for x in self.column): raise ValueError('image/history mismatch')
    def extract(self,s):
        self.validate(s);z=dot(self.row,s.numerator)
        return Packet(s.archive,z,ci()*z)
    def recover(self,p):
        if p.phase!=self.replay(p.archive): raise ValueError('packet history')
        if p.tangent!=ci()*p.phase: raise ValueError('tangent')
        return State(p.archive,tuple(x*p.phase for x in self.column),self.rho)
    def source_step(self,s,command):
        self.validate(s)
        if command not in self.ops: raise ValueError('unavailable operation')
        return State(replace(s.archive,word=s.archive.word+(command,)),act(self.ops[command],s.numerator),self.rho)
    def packet_step(self,p,command):
        self.recover(p)
        if command not in self.ops: raise ValueError('unavailable operation')
        return replace(p,archive=replace(p.archive,word=p.archive.word+(command,)))

def reject(action,message):
    try: action()
    except ValueError as e: assert message in str(e)
    else: raise AssertionError('accepted '+message)

def main():
    receipt=ROOT/'research/strominger/results/common-three-carrier-protocol/verification.json'
    old=json.loads(receipt.read_text(encoding='utf-8'));assert old['status']=='passed'
    pins={**old['source_hashes'],**old['packet_hashes']}
    pins[receipt.relative_to(ROOT).as_posix()]=digest(receipt)
    pins[Path(__file__).resolve().relative_to(ROOT).as_posix()]=digest(Path(__file__))
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale prerequisite'
    output={};checks={};interfaces={}
    phases=[ONE,-ONE,ci(),A(F(3,5))+ci()*A(F(4,5))]
    for name in ('proton','neutron'):
        f=LineInterface(ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json');interfaces[name]=f
        for z in phases:
            s=f.seed(z);p=f.extract(s)
            assert f.recover(p)==s and f.extract(f.recover(p))==p
            assert norm(s.numerator,f.metric)==f.rho
            assert p.phase.flip(8)*p.tangent==ci() and p.tangent.flip(8)*p.tangent==ONE
            for a in 'LGN':
                assert f.extract(f.source_step(s,a))==f.packet_step(p,a)
                for b in 'LGN':
                    assert f.extract(f.source_step(f.source_step(s,a),b))==f.packet_step(f.packet_step(p,a),b)
            s1=f.source_step(s,'L');assert s1.numerator==s.numerator and s1!=s
        s=f.seed(ONE);p=f.extract(s)
        reject(lambda:f.extract(replace(s,squared_normalizer=ONE)),'normalization tag')
        reject(lambda:f.extract(replace(s,archive=replace(s.archive,seed=-ONE))),'image/history')
        reject(lambda:f.recover(replace(p,tangent=ZERO)),'tangent')
        reject(lambda:f.source_step(s,'spin-mix'),'unavailable operation')
        reject(lambda:f.packet_step(p,'spin-mix'),'unavailable operation')
        metric_counting=norm(f.column,(F(1),)*len(f.column))
        if name=='neutron': assert metric_counting!=f.rho
        checks[name+'_exact_rank_one_factor_and_original_metric_decoder']=True
        checks[name+'_normalized_phase_packet_and_archive_recovery']=True
        checks[name+'_three_stage_and_nine_composition_squares']=True
        checks[name+'_normalization_history_tangent_and_domain_hostiles']=True
        output[name]={'packet_sha256':f.digest,'raw_complex_coordinates':len(f.column),
          'return_rank':1,'normalized_return_real_dimension':1,'projective_return_real_dimension':0,
          'normalizer_squared':f.rho.record(),'counting_norm_squared':metric_counting.record(),
          'encoder_column':[x.record() for x in f.column],'decoder_row':[x.record() for x in f.row],
          'native_task':['L','G','N'],'native_return_action':'all three stages fix the line pointwise',
          'continuous_phase_preparation':'supplied initial-state family, not generated by the native stage task',
          'spin_doublet':'not supplied: independent second component requires rank enlargement'}
    p=interfaces['proton'].extract(interfaces['proton'].seed(ONE))
    reject(lambda:interfaces['neutron'].recover(p),'source binding')
    checks['proton_neutron_source_labels_not_interchangeable']=True
    checks['neutron_counting_norm_cannot_replace_native_metric']=True
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    checks['all_upstream_source_and_packet_pins_unchanged']=True
    report={'schema':'marici.rank-one-return-packets.v1','status':'pass','checks':checks,'carriers':output,
      'comparison':{'same_convention':'full normalized native return state, phase retained','proton_n':1,'neutron_n':1,'electron_n':3,
      'boundary':'Dimensions of different actual return fibers under one convention, not physical particle dimensions or a common spin interface.'},
      'normalization':'(numerator,rho) denotes numerator/sqrt(rho) in the unmodified source metric; no new algebraic field approximation.',
      'scope':'Return-image and L/G/N task only; does not reconstruct arbitrary raw states or supply spin/coupling maps.',
      'source_sha256':pins,'native_producers_executed':False,'formal_proof_recompiled':False,'mass_claim':False}
    (ROOT/'research/strominger/results/rank-one-return-packets-v1.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('carriers','source_sha256')},indent=2))
if __name__=='__main__':main()
