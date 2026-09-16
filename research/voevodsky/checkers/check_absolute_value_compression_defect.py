"""Exact packet-compression audit for polarized minimalization."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tp(a):return [list(x) for x in zip(*a)]
def comp(v,a):return mm(mm(tp(v),a),v)
def add(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
# D has eigenvalues +/-1; |D|=I and its Jordan Grams are rank-one.
D=[[F(0),F(1)],[F(1),F(0)]];I=[[F(1),F(0)],[F(0),F(1)]];Dp=scale(F(1,2),add(I,D));Dm=scale(F(1,2),sub(I,D))
# Coordinate packet is not reducing: compressed signed form vanishes while both polarities retain 1/2.
V=[[F(1)],[F(0)]];Dv=comp(V,D);Tv=comp(V,add(Dp,Dm));defect=sub(comp(V,I),[[abs(Dv[0][0])]]);Kv=scale(F(1,2),sub(Tv,[[abs(Dv[0][0])]]))
# Positive eigenspace packet is reducing; rational normalization is represented with weighted compression.
# For v=(1,1)/sqrt(2), v* A v = (1/2)(1,1) A (1,1)^T.
def eigcomp(a):return [[F(1,2)*sum(a[i][j] for i in range(2) for j in range(2))]]
De=eigcomp(D);defect_e=sub(eigcomp(I),[[abs(De[0][0])]])
checks={'full_pair_is_minimal':add(Dp,Dm)==I,'coordinate_packet_signed_part_zero':Dv==[[F(0)]],'coordinate_packet_balanced_mass':comp(V,Dp)==[[F(1,2)]] and comp(V,Dm)==[[F(1,2)]],'compression_identity':Kv==scale(F(1,2),defect),'nonreducing_defect_nonzero':defect==[[F(1)]],'reducing_packet_defect_zero':defect_e==[[F(0)]]}
out={'schema':'marici.voevodsky.absolute-value-compression-defect.v1','matrices':{'D':[[str(x) for x in r] for r in D],'D_plus':[[str(x) for x in r] for r in Dp],'D_minus':[[str(x) for x in r] for r in Dm]},'coordinate_packet':{'compressed_D':str(Dv[0][0]),'forced_common_remainder':str(Kv[0][0]),'absolute_value_compression_defect':str(defect[0][0])},'reducing_packet':{'absolute_value_compression_defect':str(defect_e[0][0])},'checks':checks,'passed':all(checks.values()),'physical_gate':'For a cofinal target-adapted packet filtration P_n, prove a regulator-tail bound sup_{alpha>=alpha_n} ||P_n |D_alpha| P_n - |P_n D_alpha P_n||| -> 0, or the equivalent physical residual commutator estimate.'}
if __name__=='__main__':
 p=ROOT/'results'/'absolute-value-compression-defect.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
