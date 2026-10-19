"""Retained native-electron return-image packet. No native producer is executed."""
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
NATIVE=ROOT/'research/voevodsky/checkers'
if str(NATIVE) not in sys.path: sys.path.insert(0,str(NATIVE))
from check_electron_configuration_dimension_trial import decode
from check_electron_tetrahedral_spinor import adj, act, ident, sm
from check_electron_charge_spin_frontier import ga, gs, gm, gc, gt, gmm, spin, G0, G1
from itertools import product
STORE=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json'
I=ident(2)
E=tuple(spin(tuple(F(int(k==j)) for k in range(4))) for j in (1,2,3))
def norm(z): return gt(gm(gc(x),x) for x in z)
def matrix_add(a,b): return tuple(tuple(ga(x,y) for x,y in zip(r,s)) for r,s in zip(a,b))
quaternions={tuple(F(s if k==j else 0) for k in range(4)) for j in range(4) for s in (-1,1)}
quaternions.update(tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=4))
ACTIONS=tuple(sorted((spin(q) for q in quaternions),key=repr))

@dataclass(frozen=True)
class Archive:
    source_sha256: str
    initial_spinor: tuple
    word: tuple=()

@dataclass(frozen=True)
class SourceState:
    archive: Archive
    raw: tuple

@dataclass(frozen=True)
class Packet:
    archive: Archive
    spinor: tuple
    directions: tuple

class Interface:
    def __init__(self):
        self.digest=sha256(STORE.read_bytes()).hexdigest()
        store=json.loads(STORE.read_text(encoding='utf-8'))
        self.K=tuple(row for p in store['face_projectors'] for row in tuple(tuple(decode(x) for x in row) for row in p))
        self.D=sm(F(1,2),adj(self.K))
        assert gmm(self.D,self.K)==I
        self.N=gmm(self.K,self.D)
        self.stages=[]
        for stage in 'LGN':
            rows=[[G0 for _ in range(8)] for _ in range(8)]
            for a in store['arrows']:
                if a['stage']==stage: rows[a['target']][a['source']]=decode(a['weight'])
            self.stages.append(tuple(map(tuple,rows)))
        assert self.N==self.stages[-1]
        self.raw_actions={u:gmm(gmm(self.K,u),self.D) for u in ACTIONS}
    def replay(self,archive):
        if archive.source_sha256!=self.digest: raise ValueError('source binding')
        z=archive.initial_spinor
        if len(z)!=2 or norm(z)!=G1: raise ValueError('normalized spinor')
        for u in archive.word:
            if u not in self.raw_actions: raise ValueError('operation unavailable')
            z=act(u,z)
        return z
    def seed(self,z):
        a=Archive(self.digest,tuple(z)); self.replay(a)
        return SourceState(a,act(self.K,z))
    def validate_source(self,s):
        if len(s.raw)!=8 or s.raw!=act(self.K,self.replay(s.archive)):
            raise ValueError('raw state/image/history mismatch')
    def validate_packet(self,p):
        if p.spinor!=self.replay(p.archive): raise ValueError('packet history mismatch')
        if p.directions!=tuple(act(e,p.spinor) for e in E): raise ValueError('frame mismatch')
    def extract(self,s):
        self.validate_source(s)
        z=act(self.D,s.raw)
        return Packet(s.archive,z,tuple(act(e,z) for e in E))
    def recover(self,p):
        self.validate_packet(p)
        return SourceState(p.archive,act(self.K,p.spinor))
    def source_step(self,s,u):
        self.validate_source(s)
        if u not in self.raw_actions: raise ValueError('operation unavailable')
        a=Archive(s.archive.source_sha256,s.archive.initial_spinor,s.archive.word+(u,))
        return SourceState(a,act(self.raw_actions[u],s.raw))
    def packet_step(self,p,u):
        self.validate_packet(p)
        if u not in self.raw_actions: raise ValueError('operation unavailable')
        a=Archive(p.archive.source_sha256,p.archive.initial_spinor,p.archive.word+(u,))
        z=act(u,p.spinor)
        return Packet(a,z,tuple(act(e,z) for e in E))
