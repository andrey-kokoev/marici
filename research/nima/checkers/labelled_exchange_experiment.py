"""Conditional source-labelled experiment compiler; NOT native path descent.

The caller supplies a trusted native boundary evaluator, prepared means,
covariance and physical instrument assumptions. NumPy is required.
"""
from dataclasses import dataclass, replace
from itertools import product
import numpy as np


def frozen(a):
    a=np.array(a,dtype=float,copy=True)
    if not np.all(np.isfinite(a)): raise ValueError('nonfinite state')
    a.setflags(write=False)
    return a


@dataclass(frozen=True)
class Event:
    source_id: str
    source_label: tuple
    source_reference: tuple
    witness: tuple
    instrument_label: tuple
    instrument_reference: tuple


@dataclass(frozen=True)
class Packet:
    anchor: np.ndarray
    mismatch: np.ndarray
    covariance: np.ndarray
    history: tuple
    reference: tuple
    preparation_id: str


class Experiment:
    def __init__(self, reference=((0,1),(0,1))):
        self.reference=tuple(tuple(r) for r in reference)
        if len(self.reference)!=2 or any(len(r)!=2 or r[0]==r[1] or any(x not in range(4) for x in r) for r in self.reference):
            raise ValueError('invalid directed references')
        ea,eb=([e for e in product(range(4),repeat=2) if e[0]!=e[1] and e!=ref] for ref in self.reference)
        self.labels=tuple([('a',a,b) for a,b in product(ea,eb)]+[('s',a,b) for a,b in product(range(4),repeat=2)])
        self.index={label:i for i,label in enumerate(self.labels)}
        self.legs={'a':(ea,eb),'s':(list(range(4)),list(range(4)))}
        G=10*np.eye(4)+np.ones((4,4)); self.C=np.linalg.cholesky(np.kron(G,G)).T
        e=np.eye(4); features=[]
        for tag,a,b in self.labels:
            va=e[a] if tag=='s' else e[a[1]]-e[a[0]]
            vb=e[b] if tag=='s' else e[b[1]]-e[b[0]]
            v=self.C@np.kron(va,vb); features.append(v/np.linalg.norm(v))
        self.U=np.array(features)

    def compile(self,label,witness,boundary_of,source_id,composition='events'):
        if composition!='events': raise ValueError('native path composition is not admitted')
        if not source_id: raise ValueError('source provenance required')
        if label not in self.index: raise ValueError('unknown or excluded slot')
        tag,a,b=label; left,right=self.legs[tag]
        expected={(f'{tag}x{left.index(a)}',f'{tag}y{right.index(b)}'):1,('d',):-1}
        if boundary_of(witness)!=expected: raise ValueError('witness boundary does not match slot')
        retained=tuple(sorted((tuple(path),coefficient) for path,coefficient in witness.items()))
        return Event(source_id,label,self.reference,retained,label,self.reference)

    def _packet(self,x,cov,history,preparation_id):
        q,w=x[:16],x[16:]
        return Packet(frozen(q+self.U.T@w),frozen(w-self.U@q),frozen(cov),tuple(history),self.reference,preparation_id)

    def prepare(self,q,w,covariance,preparation_id):
        q=frozen(q); w=frozen(w); cov=frozen(covariance)
        if q.shape!=(16,) or w.shape!=(137,) or cov.shape!=(153,153): raise ValueError('state dimensions')
        if not preparation_id: raise ValueError('preparation provenance required')
        if np.max(np.abs(cov-cov.T))>1e-10 or np.linalg.eigvalsh(cov).min() < -1e-10:
            raise ValueError('covariance must be symmetric positive semidefinite')
        return self._packet(np.r_[q,w],cov,(),preparation_id)

    def state(self,packet):
        if packet.reference!=self.reference: raise ValueError('packet reference mismatch')
        q=np.linalg.solve(np.eye(16)+self.U.T@self.U,packet.anchor-self.U.T@packet.mismatch)
        return np.r_[q,packet.mismatch+self.U@q]

    def run(self,packet,events):
        x=self.state(packet); cov=np.array(packet.covariance); history=list(packet.history)
        for event in events:
            if event.instrument_reference!=self.reference: raise ValueError('event reference mismatch')
            i=self.index[event.instrument_label]
            d=np.r_[self.U[i],-np.eye(137)[i]]/np.sqrt(2)
            H=np.eye(153)-2*np.outer(d,d)
            x=H@x; cov=H@cov@H.T; history.append(event)
        return self._packet(x,cov,history,packet.preparation_id)

    def relabel(self,packet,pa,pb):
        if sorted(pa)!=list(range(4)) or sorted(pb)!=list(range(4)): raise ValueError('not permutations')
        def move(label):
            tag,a,b=label
            return (tag,pa[a],pb[b]) if tag=='s' else (tag,tuple(pa[t] for t in a),tuple(pb[t] for t in b))
        target=Experiment((tuple(pa[t] for t in self.reference[0]),tuple(pb[t] for t in self.reference[1])))
        perm=[target.index[move(label)] for label in self.labels]
        T=self.C@np.kron(np.eye(4)[:,pa],np.eye(4)[:,pb])@np.linalg.inv(self.C)
        O=np.zeros((153,153)); O[:16,:16]=T
        O[16+np.array(perm),16+np.arange(137)]=1
        history=tuple(replace(event,instrument_label=move(event.instrument_label),instrument_reference=target.reference) for event in packet.history)
        transported=target._packet(O@self.state(packet),O@packet.covariance@O.T,history,packet.preparation_id)
        return target,transported,O
