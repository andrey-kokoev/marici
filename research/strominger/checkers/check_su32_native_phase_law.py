"""Exact operation-derived phase constraints and invariant doublets.
No geometric route generation; source permutations are read, never rewritten.
"""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'research/strominger/results/su32-native-phase-law-v1'


def perm(p):
    return s.Matrix([[int(j == p[i]) for j in range(5)] for i in range(5)])


def simp(m):
    return m.applyfunc(s.simplify)


def group(generators):
    identity = tuple(range(5))
    found = {identity}
    queue = [identity]
    for p in queue:
        for g in generators:
            q = tuple(p[g[i]] for i in range(5))
            if q not in found:
                found.add(q)
                queue.append(q)
    return sorted(found)


def orbital_count(elements):
    unseen = {(i,j) for i in range(5) for j in range(5)}
    orbits = []
    while unseen:
        i,j = min(unseen)
        orbit = {(p[i],p[j]) for p in elements}
        unseen -= orbit
        orbits.append(sorted(orbit))
    return orbits


def rowperm(m):
    return tuple(next(j for j in range(5) if m[i,j] == 1) for i in range(5))


def record(m):
    return [[str(s.simplify(x)) for x in row] for row in m.tolist()]


def run():
    paths = [ROOT/'research/nima/generative-phase-assembly.mjs', ROOT/'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs']
    hashes = {str(p.relative_to(ROOT)).replace('\\','/'): sha256(p.read_bytes()).hexdigest() for p in paths}
    assembly, phase = [p.read_text() for p in paths]
    pn = json.loads(re.search(r'\bPN=(\[[^]]+\])', assembly)[1])
    ne = json.loads(re.search(r'\bNE=(\[[^]]+\])', assembly)[1])
    rp = json.loads(re.search(r'proton:Object.freeze\((\[[^]]+\])\)', phase)[1])
    rn = json.loads(re.search(r'neutron:Object.freeze\((\[[^]]+\])\)', phase)[1])
    ops = [('PN','P','N',pn), ('inverse-PN','N','P',pn), ('NE','N','E',ne), ('P-reader','P','P',rp), ('N-reader-or-NN','N','N',rn)]
    nodes = [(role,i) for role in 'PNE' for i in range(5)]
    constraints = []
    for name,source,target,p in ops:
        for i in range(5):
            constraints.append((name,(target,i),(source,p[i])))
    matrix = s.zeros(len(constraints),15)
    for row,(_,a,b) in enumerate(constraints):
        matrix[row,nodes.index(a)] += 1
        matrix[row,nodes.index(b)] -= 1
    assert matrix.rank() == 14
    assert matrix.nullspace() == [s.ones(15,1)]
    # All group-valued diagonal entries are equated, not just infinitesimal weights.
    parent = {n:n for n in nodes}
    def root(n):
        while parent[n] != n:
            n = parent[n]
        return n
    for _,a,b in constraints:
        parent[root(a)] = root(b)
    assert len({root(n) for n in nodes}) == 1
    # A noncommon phase survives PN/NE if transported by species, but fails a reader.
    Dp = s.diag(s.I,1,1,1,1)
    PN,NE,A = perm(pn),perm(ne),perm(rp)
    Dn,De = PN*Dp*PN.T, NE*PN*Dp*PN.T*NE.T
    assert Dn*PN == PN*Dp and De*NE == NE*Dn
    assert Dp*A != A*Dp
    # Linear NE cannot intertwine opposite uniform phase weights.
    assert (-s.I*s.eye(5))*NE != NE*(s.I*s.eye(5))

    # Pull N reader to the P coefficient reference, using the actual PN inverse.
    B = PN.T*perm(rn)*PN
    C = A*B
    I = s.eye(5)
    assert A*A == B*B == C**5 == I
    assert C != I and A*C*A == C.T
    dg = group([rp,rowperm(B)])
    assert len(dg) == 10
    orbitals = orbital_count(dg)
    assert len(orbitals) == 3
    Q0 = s.ones(5)/5
    S = C+C.T
    a,b = (s.sqrt(5)-1)/2, -(s.sqrt(5)+1)/2
    Q1 = simp((S-b*I-(2-b)*Q0)/(a-b))
    Q2 = simp(I-Q0-Q1)
    projectors = [Q0,Q1,Q2]
    assert [q.rank() for q in projectors] == [1,2,2]
    for i,q in enumerate(projectors):
        assert simp(q*q-q) == s.zeros(5) and q.T == q
        assert simp(A*q-q*A) == simp(B*q-q*B) == s.zeros(5)
        for j,r in enumerate(projectors):
            if i != j:
                assert simp(q*r) == s.zeros(5)
    transports = {'P':I,'N':PN,'E':NE*PN}
    sectors = {role:[simp(t*q*t.T) for q in projectors] for role,t in transports.items()}
    for _,source,target,p in ops:
        m = perm(p)
        for i in range(3):
            assert simp(sectors[target][i]*m-m*sectors[source][i]) == s.zeros(5)

    # Explicit logical coordinates with retained positive metric; no fitted basis.
    frames = []
    for q in projectors[1:]:
        columns = q.columnspace()
        frame = s.Matrix.hstack(*columns)
        gram = simp(frame.T*frame)
        assert len(columns) == 2 and s.simplify(gram.det()) > 0 and gram[0,0] > 0
        decoder = simp(gram.inv()*frame.T)
        assert simp(frame*decoder-q) == s.zeros(5)
        actions = {name:simp(decoder*m*frame) for name,m in [('A',A),('B',B),('C',C)]}
        for name,m in [('A',A),('B',B),('C',C)]:
            u = actions[name]
            assert simp(m*frame-frame*u) == s.zeros(5,2)
            assert simp(u.T*gram*u-gram) == s.zeros(2)
        assert s.simplify(actions['A'].det()) == s.simplify(actions['B'].det()) == -1
        assert s.simplify(actions['C'].det()) == 1
        frames.append({'frame':record(frame),'metric':record(gram),'decoder':record(decoder),'actions':{k:record(v) for k,v in actions.items()}})
    # Common slot phase is unique only within the diagonal-in-native-slots class.
    independent = simp(Q0+s.I*Q1-Q2)
    assert simp(independent.conjugate().T*independent-I) == s.zeros(5)
    assert simp(independent*A-A*independent) == simp(independent*B-B*independent) == s.zeros(5)
    assert any(independent[i,j] != 0 for i in range(5) for j in range(5) if i != j)

    # Additional four-vertex geometry hypothesis: proper permutations fix slot 4.
    even4 = [tuple(p)+(4,) for p in permutations(range(4)) if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 == 0]
    enlarged = group(even4+[rowperm(C)])
    assert len(enlarged) == 60 and len(orbital_count(enlarged)) == 2
    hostile = perm([1,2,0,3,4])
    defects = [simp(hostile*q-q*hostile) for q in projectors[1:]]
    assert all(d != s.zeros(5) for d in defects)
    # Do not remove the collective state when reporting the two doublets.
    collective = s.ones(5,1)
    assert Q0*collective == collective and simp((Q1+Q2)*collective) == s.zeros(5,1)
    assert all(sha256(p.read_bytes()).hexdigest() == hashes[str(p.relative_to(ROOT)).replace('\\','/')] for p in paths)
    for p in [Path(__file__),ROOT/'research/strominger/su32-native-phase-law-v1.md']:
        hashes[str(p.relative_to(ROOT)).replace('\\','/')] = sha256(p.read_bytes()).hexdigest()
    return {'schema':'su32.native-phase-law.v1','passed':True,
            'classification':'common_slot_phase_and_two_reader_invariant_doublets; geometric_extension_mixes_doublets',
            'admitted_scope':'Exact five-slot coefficient grammar, stationary species-indexed phase action; no signed-wire binding',
            'sourcePermutations':dict(PN=pn,NE=ne,Preader=rp,Nreader=rn),
            'phaseConstraints':{'nodes':nodes,'equations':constraints,'rank':14,'nullity':1,'commonDiagonalGroup':'U(1)','absoluteCharacterWeightSelected':False},
            'readerGroup':{'A':rp,'B':list(rowperm(B)),'C':list(rowperm(C)),'order':10,'commutantDimension':len(orbitals),'projectorRanks':[1,2,2]},
            'projectors':{role:[record(q) for q in qs] for role,qs in sectors.items()},'doubletFrames':frames,
            'nonDiagonalIndependentPhase':record(independent),
            'geometricExtension':{'additionalHypothesis':'prior four-vertex A4 action fixing context slot','groupOrder':len(enlarged),'commutantDimension':2,'doubletCommutatorDefects':[record(d) for d in defects]},
            'hostiles':['transported independent slot phase fails reader intertwiner','opposite P/E phase weights fail the linear NE intertwiner','independent sector phases survive outside slot-diagonal class','added geometric A4 mixes doublets','doublet-only decoding loses nonzero collective state'],
            'globalSignedRecordAssignment':None,'nativeHopfBinding':False,
            'residuals':['Signed records to coefficient states not specified','Doublet phase freedom larger than diagonal slot phase','Six-reading geometric transport may mix doublets; tested A4 extension does'],
            'next_falsifier':'Compare the actual Su-32 occurrence-transition maps with these projectors; require phase covariance and retained mean before claiming global Hopf sectors.',
            'sourceHashes':hashes}


if __name__ == '__main__':
    result = run()
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('sourceHashes','doubletFrames','projectors','nonDiagonalIndependentPhase','geometricExtension','phaseConstraints')},indent=2))
