import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1021=json.loads((ROOT/"results"/"wp1021_normalized_pairing_cp_no_go.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1021["status"]=="PASS"

I=sp.I
z=sp.Rational(4,5)+I*sp.Rational(3,5)
t=sp.Rational(-10,381)
Y0=sp.diag(1,2,4)
Y0[0,1]=t
a=sp.Matrix([1,2,3])
b=sp.Matrix([[2,1,1]])
Hu=sp.diag(1,4,9)
c=Y0*b.T
Q=a*c.T-c*a.T
qcycle=[sp.factor(Q[0,1]),sp.factor(Q[1,2]),sp.factor(Q[2,0])]
assert qcycle==[sp.Rational(-742,381),sp.Integer(2),sp.Rational(244,127)]
assert all(q!=0 for q in qcycle)
assert (a.T*a)[0]==14 and (b*b.T)[0]==6

Yd=Y0+z*a*b
Hd=sp.simplify(Yd*Yd.H)
edges=[Hd[0,1],Hd[1,2],Hd[2,0]]
assert all(edge!=0 for edge in edges)
T=sp.factor(sp.im(edges[0]*edges[1]*edges[2]))
C=sp.simplify(Hu*Hd-Hd*Hu)
assert T==0 and C.det()==0
assert C.rank()==2
disc_u=sp.discriminant(Hu.charpoly().as_expr(),Hu.charpoly().gen)
disc_d=sp.factor(sp.discriminant(Hd.charpoly().as_expr(),Hd.charpoly().gen))
assert disc_u!=0 and disc_d!=0
assert Yd.det()!=0

# Deliberate contrasting obstruction: restoring the undeformed WP90
# background preserves the same a,b,z and produces nonzero physical CP.
Y00=sp.diag(1,2,4)
Yw=Y00+z*a*b
Hw=sp.simplify(Yw*Yw.H)
nonzero_obstruction=sp.factor((Hu*Hw-Hw*Hu).det())
assert nonzero_obstruction==1152*I

Js=[sp.Rational(str(row["J"])) for row in ensemble["records"]]
assert len(Js)==1210 and all(j!=0 for j in Js)

result={
 "schema":"marici.flavor.wp1022.v1","status":"PASS",
 "source_domain":"fixed-norm rank-one FDM-2 portal with all three bivector and Gram-cycle edges nonzero",
 "background_deformation":"Y0[0,1]=-10/381",
 "fixed_norms":{"a_norm_squared":"14","b_norm_squared":"6"},
 "oriented_bivector_cycle":[str(q) for q in qcycle],
 "gram_cycle_edges":[str(e) for e in edges],
 "transmission_discriminant":str(T),
 "commutator_rank":C.rank(),"commutator_determinant":"0",
 "up_discriminant":str(disc_u),"down_discriminant":str(disc_d),
 "contextual_partition":"fully cyclic portals still split into T=0 cancellation and T!=0 transmission classes",
 "classification":"cyclic-incidence rigidifier with fixed norms, but not a physical CP selector or positive-margin constructor",
 "smallest_exact_falsifier":"one rational real-background entry t=-10/381 cancels T while every q_ij and every Gram cycle edge remains nonzero",
 "deliberate_failure_nonzero_obstruction":str(nonzero_obstruction),
 "instrument":"signed Jarlskog/CKM readout detects cancellation but does not exclude it",
 "ensemble_sheets_tested":len(Js),
 "claim_boundary":"tests nonzero cyclic incidence and fixed norms; does not exclude a source law directly fixing oriented volume T",
 "remaining_gate":"derive a weak-basis-invariant nonzero oriented-volume equation or margin rather than support and norm constraints",
}
out=ROOT/"results"/"wp1022_cyclic_incidence_cancellation_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1022 PASS: all cycle edges nonzero but T =",T)
