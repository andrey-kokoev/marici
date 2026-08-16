---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Marked-Corner Triple-Normal Blowup and the Rank-Two Relative Gate

## Record

Status: canonical carrier-level third-Rees interval derived; the induced
nine-master Cut--nearby commutator remains uncomputed.

This entry continues entry 222. It changes no denominator, normalization,
marked section, support summand, projector, or carrier incidence.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the third-normal marked-corner class is not selected canonically by
the frozen source chain and existing flagged carrier.}
}
\]

The finite falsifier was a source-fixed oriented class on the minimal log
blowup. Such a class would show that no support-switch object is required at
carrier level.

## Frozen local family

Write

\[
x=X_1,\quad y=X_2,\quad E=E_T,
\quad a=y+A,\quad b=x+B
\]

at the positive real marked corner. The exact Cayley--Menger residue family
verified in entry 222 has central conductor

\[
K_0=R^2,
\qquad
R=xa^2+yb^2-xy(x+y),
\]

and cubic tangent cone

\[
-8xy(x+y)E
\left(
AB+\frac E2(A+B)+E^2
\right).
\]

The tangent equation of the conductor is \(A+B=0\). Restriction to it gives

\[
\boxed{
8xy(x+y)E(A-E)(A+E).
}
\]

Thus the frozen third-normal geometry is the triple line arrangement

\[
E=0,\qquad A=E,\qquad A=-E.
\]

## Minimal log blowup

Blow up only the already marked corner \((A,E)=(0,0)\). In the chart

\[
r=\frac AE
\]

the exceptional divisor is \(\mathbf P^1\), and the three strict transforms
meet it at

\[
p_0:r=\infty,\qquad p_-:r=-1,\qquad p_+:r=1.
\]

No fitted divisor has been inserted: these points are the projectivized
normal directions of the frozen conductor and its two moving branches.

The exceptional relative group is

\[
H_1\bigl(\mathbf P^1,\{p_0,p_-,p_+\};\mathbf Z\bigr)
\simeq
\widetilde H_0\{p_0,p_-,p_+\}
\simeq
\mathbf Z^2.
\]

Take the basis

\[
e_-=[p_-]-[p_0],
\qquad
e_+=[p_+]-[p_0].
\]

## Canonical source interval

Entry 180 freezes the continuation through the lower-half energy tube, the
positive Cayley--Menger square-root sheet, orientation \(da\wedge db\), unit
Jacobian, and unit multiplicity. Under \(r=A/E\), the two moving boundary
branches approach \(p_-\) and \(p_+\). Their oriented interval therefore has

\[
\partial[p_-,p_+]
=[p_+]-[p_-]
=e_+-e_-.
\]

Consequently the frozen source data select

\[
\boxed{
\partial\Gamma_{\rm exc}=(-1,1)
}
\]

in the ordered basis \((e_-,e_+)\). Reversing the already frozen orientation
would reverse the sign; it is not an independent admissible choice.

Only \((a,b)=(y,x)\) lies on the positive real loop-edge chamber for
\(x,y>0\). The other three sign corners are occurrence/deck companions, not
four independent physical-chain choices.

## Verdict

The carrier-level noncanonicity conjecture is falsified:

\[
\boxed{
\text{the existing marked flags and the source orientation canonically
generate a nonzero third-Rees relative interval.}
}
\]

This strengthens the unbounded-grade form of H2. The depth-two form remains
falsified.

The result does **not** yet prove that Cut and nearby cycles commute on the
full coefficient system. The rank-two exceptional Tate group must still be
mapped into the nine-master algebraic--elliptic extension, and the resulting
can--variation class compared with the source Cut residue. No such
coefficient-level map is fitted here.

## Classification

- existing carrier: total-energy normal, Cut divisor, conductor, two axial
  marked flags, and their minimal blowup;
- soft support: excluded by \(xy(x+y)\ne0\);
- graph homology: none;
- Tate/Kummer coefficient data: the exceptional relative group is rank-two
  Tate;
- elliptic Gauss--Manin data: unchanged;
- extension data: target of the next comparison;
- genuinely new carrier incidence: none.

## Exact evidence

- `research/benincasa/check_et_cut_nearby_normal_form.rs`;
- `research/benincasa/et-cut-nearby-normal-form.json`;
- 4,225 exact integer tests of the complete degree-six family;
- warnings-denied optimized Rust compilation and zero-result execution via
  the governed Scheduler MCP.

## Next finite falsifier

Construct the functorial map from the exceptional basis
\((e_-,e_+)\) into the specialized nine-master Gysin sequence and evaluate it
on \((-1,1)\). Compare the result with the two orders

\[
\psi_{E=0}\circ\operatorname{Res}_{q_{\mathcal G_{12}}=0},
\qquad
\operatorname{Res}_{q_{\mathcal G_{12}}=0}\circ\psi_{E=0}.
\]

If their difference is the image of the frozen third-Rees interval under the
predeclared Gysin/excess calculus, H2 survives this coefficient-level gate.
If no canonical map exists without a support-switch object or new incidence,
the shared-calculus form of H2 fails.

## Outcome contract

~~~json
{
  "claim": "The frozen physical Leray germ canonically selects the third-normal marked-corner relative class on the minimal log blowup.",
  "status": "survived",
  "triple_normal_arrangement": ["E=0", "A=E", "A=-E"],
  "exceptional_points": ["p0=infinity", "pminus=-1", "pplus=1"],
  "relative_rank": 2,
  "canonical_boundary_vector": [-1, 1],
  "physical_real_corner": "(a,b)=(y,x)",
  "new_carrier_incidence": false,
  "full_nine_master_cut_nearby_commutator_computed": false,
  "next_experiment": "Map (-1,1) functorially into the specialized nine-master Gysin extension and compute the Cut-nearby commutator."
}
~~~
