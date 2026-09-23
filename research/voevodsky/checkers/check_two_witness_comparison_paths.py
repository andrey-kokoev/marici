"""Two row-witness paths yield same signed delta, different replay records."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
A=(((-Q(1),Q(0)),Q(0)),((Q(1),Q(0)),Q(1)),((Q(0),-Q(1)),Q(0)),((Q(0),Q(1)),Q(1)))
P=((Q(0),Q(1),Q(0),Q(1)),Q(1));R=((Q(0),Q(1),Q(1),Q(2)),Q(0))
f=((3,0,2,1),(Q(2),Q(3),Q(1,2),Q(4)))
g=((2,0,3,1),(Q(1,2),Q(5),Q(2),Q(3)))
def apply_rows(rows,w):
 p,s=w;return tuple((tuple(s[j]*x for x in rows[p[j]][0]),s[j]*rows[p[j]][1]) for j in range(4))
def apply_packet(packet,w):
 p,s=w;return tuple(packet[0][p[j]]/s[j] for j in range(4)),packet[1]
def compose(f,g):
 p,s=f;q,t=g
 return tuple(p[q[j]] for j in range(4)),tuple(s[q[j]]*t[j] for j in range(4))
def digest(rows):return sha256(repr(rows).encode()).hexdigest()
def delta(u,v):return tuple(v[0][i]-u[0][i] for i in range(4)),v[1]-u[1]
B=apply_rows(A,f);C=apply_rows(B,g);h=compose(f,g)
assert C==apply_rows(A,h)
sequential=(apply_packet(apply_packet(P,f),g),apply_packet(apply_packet(R,f),g))
direct=(apply_packet(P,h),apply_packet(R,h))
assert sequential==direct
assert delta(*sequential)==apply_packet(delta(P,R),h)
path_two=(digest(A),digest(B),digest(C));path_one=(digest(A),digest(C))
assert path_two!=path_one and path_two[1]!=path_two[0] and path_two[1]!=path_two[2]
def replay(first,second,expected_middle):
 if digest(apply_rows(A,first))!=expected_middle:raise ValueError('MIDDLE_MANIFEST_MISMATCH')
 return apply_rows(apply_rows(A,first),second)
assert replay(f,g,digest(B))==C
try:replay(f,g,digest(C))
except ValueError as err:assert str(err)=='MIDDLE_MANIFEST_MISMATCH'
else:raise AssertionError('stale middle accepted')
report={'passed':True,'sequential_direct_packet_and_delta_equal':True,'two_distinct_manifest_paths':True,'middle_manifest_required_for_two_step_replay':True,'stale_middle_refused':True,'source_digest':path_two[0],'middle_digest':path_two[1],'destination_digest':path_two[2],'scope':'Positive row witnesses and signed square packet delta; mathematical composite equality does not identify witness execution histories, grant issuer authority or map analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/two-witness-comparison-paths.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
