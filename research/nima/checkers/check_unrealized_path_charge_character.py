"""Sharp conditional phase-character test of unrealized-path charge.
The endpoint-phase adapter is declared, not derived electromagnetism.
Integer Laurent exponents cover U(1); C3 values are exact controls only.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
from check_natural_tower_return import PACKETS,LABELS
from check_triangle_half_phase import zadd,zmul,zconj
ROOT=Path(__file__).resolve().parents[1]
REG={label:(a,b) for label,a,b in PACKETS}
EDGES=tuple(REG)
ONE=(F(1),F(0));OMEGA=(F(-1,2),F(1,2))

@dataclass(frozen=True)
class PathRecord:
    word:tuple
    realized:bool
    description:str

def exponents(record):
    word=record.word
    assert word and all(w in REG for w in word)
    assert all(REG[a][1]==REG[b][0] for a,b in zip(word,word[1:]))
    return tuple(word.count(e) for e in EDGES)

def character(counts):
    out=[0]*4
    for n,e in zip(counts,EDGES):
        a,b=REG[e];out[LABELS.index(a)]-=n;out[LABELS.index(b)]+=n
    return tuple(out)

def powz(z,n):
    if n<0:return powz(zconj(z),-n)
    out=ONE
    for _ in range(n):out=zmul(out,z)
    return out

def value(counts,links):
    out=ONE
    for n,z in zip(counts,links):out=zmul(out,powz(z,n))
    return out

def main():
    p=PathRecord(('AB',),True,'executed')
    r=PathRecord(('AD','DB'),False,'available')
    pc,rc=exponents(p),exponents(r)
    chi=character(pc)
    assert chi==character(rc)==(-1,1,0,0)
    realized=PathRecord(r.word,True,'freshly executed alternative')
    duplicate=PathRecord(r.word,False,'second description of the same alternative')
    assert exponents(realized)==exponents(duplicate)==rc
    loop=tuple(a-b for a,b in zip(rc,pc))
    assert character(loop)==(0,0,0,0) and any(loop)
    inverse=tuple(-a for a in pc)
    ba=exponents(PathRecord(('BA',),True,'independent supplied return'))
    assert character(ba)==character(inverse)==(1,-1,0,0)
    assert ba!=inverse # Same boundary character is not the same path/connection.
    links=tuple(OMEGA if e=='AD' else ONE for e in EDGES)
    phases=(ONE,OMEGA,powz(OMEGA,2));tests=0
    for gauges in product(phases,repeat=4):
        moved=tuple(zmul(zmul(gauges[LABELS.index(b)],z),zconj(gauges[LABELS.index(a)])) for z,(_,a,b) in zip(links,PACKETS))
        z=zmul(gauges[1],zconj(gauges[0]))
        for counts in (pc,rc):assert value(counts,moved)==zmul(z,value(counts,links))
        assert value(loop,moved)==value(loop,links)==OMEGA
        # Sum of alternative amplitudes remains weight +1, not number-of-paths.
        total=zadd(value(pc,links),value(rc,links))
        changed=zadd(value(pc,moved),value(rc,moved))
        assert changed==zmul(z,total)
        tests+=1
    # A nonzero complex-linear realization from weight -1 to +1 would require
    # z^-1 * t = z * t for every z. The formal characters differ; a C3 probe
    # already rejects the identity map (unlike the ambiguous probe z=-1).
    assert OMEGA!=zconj(OMEGA)
    assert zmul(zconj(OMEGA),ONE)!=zmul(OMEGA,ONE)
    # Conjugation intertwines those weights but is an extra ANTILINEAR action.
    for a in (ONE,OMEGA,zadd(ONE,OMEGA)):
        assert zconj(zmul(zconj(OMEGA),a))==zmul(OMEGA,zconj(a))
    # The natural dual evaluation is neutral; a dual is not a new particle.
    assert tuple(a+b for a,b in zip(chi,tuple(-c for c in chi)))==(0,0,0,0)
    result=dict(schema='marici.nima.unrealized-path-charge-character.v1',status='pass',
        paths={'executed':list(p.word),'available':list(r.word)},
        endpoint_character=list(chi),formal_status_character_difference=[0]*4,
        exact_phase_assignments=tests,
        relative_loop={'edge_exponents':dict(zip(EDGES,loop)),'endpoint_character':[0]*4,'nontrivial_phase_control':'exp(2*pi*i/3)'},
        realization='Changing the execution-status tag does not change path endpoints, orientation or character.',
        dual_control='Opposite character is produced by inverse/dual/conjugate structure, not by unexecuted status. Nonzero complex-linear realization between opposite U(1) weights is impossible without further structure.',
        conservation_condition='If weights are identified with physical charges, converting -q into +q requires a compensating -2q change elsewhere; no such mechanism is supplied here.',
        native_boundary='Inspected native rules distinguish inversion and composition but do not supply an unrealized-path-to-dual constructor or electromagnetic coupling.',
        disposition='The proposed status-only mechanism does not produce negative charge in the existing conditional phase adapter. Available paths can retain neutral relative holonomy/interference information.',
        scope='A U(1) probe is an explicit representation hypothesis. This is neither a derivation of electromagnetism nor a no-go for every possible realization of the intuition.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ('agda/NativeTableRules.agda','checkers/check_seed_typed_execution.py','checkers/check_natural_tower_return.py','137-local-endpoint-phase-adapter.md','checkers/check_unrealized_path_charge_character.py')})
    (ROOT/'results/unrealized-path-charge-character.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
