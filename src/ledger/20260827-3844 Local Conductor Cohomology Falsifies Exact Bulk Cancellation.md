# 3844 — Local Conductor Cohomology Falsifies Exact Bulk Cancellation

## Conjecture tested

The relative-current finiteness conjecture proposed that a source-derived exact bulk or endpoint term cancels the two active conductor logarithms inside the frozen five-wall meromorphic complex, with no subtraction datum.

Its cheapest mandatory consequence is local: at each active conductor, the logarithmic wall residue must be removable by another incident source term or by an exact local primitive.

## Exact hostile point

Use the strict-triangle source point

\[
(x,y,z)=(2,3,4).
\]

At the selected (g_1) conductor,

\[
a=\frac{3\sqrt{46}}2,
\qquad b=7.
\]

All other marked equations are nonzero:

\[
q_{g_2}=-6+\frac{3\sqrt{46}}2,
\quad
q_{g_3}=11+\frac{3\sqrt{46}}2,
\quad
q_{g_{23}}=5,
\quad
q_{g_{31}}=-3+\frac{3\sqrt{46}}2.
\]

The unsplit numerator is

\[
q_{g_{23}}+q_{g_{31}}=2+\frac{3\sqrt{46}}2\ne0,
\]

and the iterated conductor residue is

\[
\frac{16}{99225}-\frac{\sqrt{46}}{101430}\ne0.
\]

At the selected (g_2) conductor,

\[
a=6,
\qquad b=\sqrt{94}.
\]

Again every other marked wall is absent, the unsplit numerator is

\[
1+\sqrt{94}\ne0,
\]

and the iterated residue is

\[
\frac1{2025}-\frac{\sqrt{94}}{28200}\ne0.
\]

## Local obstruction

Each selected point is therefore an isolated transverse intersection of one marked wall with the square-root conductor. A nonzero iterated logarithmic residue at such an intersection is a local de Rham cohomology invariant. Adding an exact bulk primitive that is regular on the remaining frozen supports cannot change it.

There is also no second incident marked-wall residue available for local Čech cancellation.

## Falsification

The proposed no-subtraction exact-bulk cancellation is false. The complete frozen five-wall meromorphic complex contains no exact homotopy capable of removing either active conductor class.

This does not forbid:

- the source-defined distributional boundary value;
- a relative-chain object retaining the conductor class;
- an independently authorized subtraction or renormalization map;
- additional support derived from an enlarged source.

It does forbid treating finiteness as an automatic consequence of five-wall Čech closure.

## Updated interpretation

The conductor logarithms are not artifacts of splitting one finite object into walls. They are genuine local coefficient classes. Whether they contribute to a physical observable is a later readout or renormalization question.

Thus the surviving architecture is:

\[
\text{closed five-wall coefficient cocycle}
+
\text{nontrivial conductor costalks}
+
\text{source-authorized physical readout still required}.
\]

No new Carrier stratum is indicated.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_conductor_local_cohomology_obstruction.py`
- `research/benincasa/results/rank26-conductor-local-cohomology-obstruction.json`

The checker passes six exact gates.

## Next falsifier

Classify the source-authorized boundary-value or renormalization maps on the two conductor costalks. Test whether the published prescription selects a unique functional, leaves finite scheme freedom, or annihilates the classes through physical-chain incidence. Do not search for another exact cancellation inside the already falsified frozen complex.
