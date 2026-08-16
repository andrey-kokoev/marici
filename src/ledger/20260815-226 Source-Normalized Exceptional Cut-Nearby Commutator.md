---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Source-Normalized Exceptional Cut-Nearby Commutator

## Record

Status: the universal exceptional Leray scalar and the resulting nine-master
Cut--nearby commutator are computed in the frozen equation-(58) de Rham
master normalization. The result is nonzero, lies wholly in the rank-seven
algebraic Tate/Kummer kernel, and introduces no carrier incidence.

This entry continues entries 224--225. It adds no denominator, carrier cell,
support summand, projector, or normalization.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the frozen physical Leray germ does not canonically normalize the
marked-corner coefficient functional.}
}
\]

The finite falsifier was a source-oriented meromorphic continuation of the
exceptional disk period, including the published lower-half energy boundary
value and the already frozen \(2\pi i\) Cut discontinuity.

## Frozen local data

Put

\[
\alpha=4x^2y^2,
\qquad
\beta=8xy(x+y),
\]

and on the exceptional disk set

\[
Q=\beta(1-r^2)-\alpha n^2>0.
\]

The weighted Cayley--Menger tangent is \(L=-Q\). The oriented boundary is
the interval from \(r=-1\) to \(r=+1\), inherited from the positive
Cayley--Menger chain and entry 180's Leray germ.

No compact disk was fitted after seeing the target: this disk is the
vanishing relative chain bounded by the two frozen moving branches.

## Meromorphic disk integral

For \(\Re\lambda>-1\), scaling
\(n=\sqrt{\beta/\alpha}\,v\) gives

\[
\int_D Q^\lambda\,dr\,dn
=
\sqrt{\frac\beta\alpha}\,
\beta^\lambda
\frac{\pi}{\lambda+1}.
\]

Meromorphic continuation to \(\lambda=-3/2\) therefore gives

\[
\operatorname{AC}\int_D Q^{-3/2}\,dr\,dn
=
-\frac{\pi}{8x^2y^2(x+y)}.
\]

## Source branch and Leray factor

The published prescription is \(E\to E-i0\). Since

\[
K=E^3L=E^3(-Q),
\]

one has on the exceptional disk

\[
K\longrightarrow -Q+i0,
\qquad
K^{-3/2}=+iQ^{-3/2}.
\]

Thus, in the frozen de Rham master normalization,

\[
\boxed{
I_{\rm loc}
=
-\frac{i\pi}{8x^2y^2(x+y)}.
}
\]

The common source double-pole numerator from entry 225 is
\(-8xy(x+y)\), so

\[
-8xy(x+y)I_{\rm loc}
=
\frac{i\pi}{xy}.
\]

Entry 180 fixes

\[
\operatorname{Disc}\frac1{q-i0}
=
2\pi i\,\delta(q).
\]

After this Leray discontinuity the common coefficient is therefore

\[
\boxed{
-\frac{2\pi^2}{xy}.
}
\]

## Nine-master commutator

In the literal equation-(58) order,

\[
\boxed{
[\psi_{E=0},\operatorname{Res}_{q_{\mathcal G_{12}}=0}]
=
\left(
0,0,-\frac{2\pi^2}{x},0,-\frac{2\pi^2}{y},
-\frac{2\pi^2}{xy},0,0,0
\right).
}
\]

Equivalently the nonzero entries retain the source-derived ratio

\[
e_3:e_5:e_6=y:x:1.
\]

The sign follows from the lower-half boundary value, the positive
Cayley--Menger sheet, orientation \(da\wedge db\), and the \(2\pi i\)
discontinuity. Reversing any of these frozen data is not admissible.

## Normalization boundary

The paper's general cosmological integral is written with a proportionality
sign and explicitly omits coupling- and \(\alpha\)-dependent overall
factors. The result above therefore claims the exact coefficient in the
source's equation-(58) de Rham master normalization, not an absolute
normalization for a fully coupled wavefunction observable. No omitted common
wavefunction prefactor can alter the carrier/coefficient classification or
the master ratios.

## Exceptional nearby monodromy

A loop around (E=0) sends (	au=E^{1/2}) to (-	au). In the weighted
chart this sends (n) to (-n). The signs of the Jacobian
(	au^5dr\wedge dn) and the chosen (K^{3/2}\sim	au^9L^{3/2}) cancel,
while (K_1\sim	au^4) is invariant. Therefore the normalized exceptional
double-pole class returns to itself:

\[
T_{\rm exc}=1,
\qquad
N_{\rm exc}=0.
\]

Its nearby-cycle graded factor is consequently rank-one Tate/Kummer with
trivial local character. The nontrivial rank-one nilpotent remains confined
to the independent elliptic nodal quotient.

## Gysin, nearby, and Rees comparison

The commutator has finite marked-corner support and

\[
R_\infty([\psi,\operatorname{Res}])=0.
\]

Hence it has:

- zero elliptic Gysin quotient;
- zero new elliptic monodromy;
- zero graph-homology contribution;
- support in the pre-existing rank-seven algebraic Tate/Kummer kernel;
- no new carrier incidence.

This is the source-normalized realization of the third-Rees interval found
in entries 222--225. It does not repair the falsified depth-two bound:
the marked physical Cut comparison first appears at third normal order.

The independent algebraic-letter identity remains

\[
\operatorname{gr}^{(2)}_E\mathcal Q=-8xy.
\]

It is coefficient data and is not identified with the third-order
Cayley--Menger smoothing coefficient.

## Verdict

The normalization-obstruction conjecture is falsified:

\[
\boxed{
\text{the frozen source data canonically produce a nonzero algebraic
Cut--nearby commutator without new carrier structure.}
}
\]

This strengthens H2 in unbounded filtered form:

\[
\text{shared carrier and comparison calculus}
+
\text{sector-specific filtered coefficient objects}.
\]

It does not restore a first-jet or depth-two formulation.

## Classification

- existing carrier: total-energy normal, Cut divisor, conductor, axial marked
  flags, and their minimal weighted log blowup;
- soft support: excluded by \(xy(x+y)\ne0\);
- graph homology: none;
- Tate/Kummer coefficient data: the entire nonzero commutator;
- elliptic Gauss--Manin data: zero image;
- extension data: no algebraic-to-elliptic component in this exceptional
  grade;
- genuinely new carrier incidence: none.

## Exact evidence

- `research/benincasa/check_et_cut_nearby_normal_form.rs`;
- `research/benincasa/et-cut-nearby-normal-form.json`;
- warnings-denied optimized Rust compilation;
- exact execution and JSON assertion through the governed Scheduler MCP;
- Scheduler result \(0\), followed by task disablement.

## Next finite falsifier

Compute the same source-normalized comparison at a second independent marked
Cut sector, obtained by cyclically rotating
\(q_{\mathcal G_{12}}\), while freezing occurrence labels before the
rotation. Test whether the three local algebraic commutators sew with the
source cyclic symmetry and Cut incidence signs.

Failure of cyclic sewing without a new incidence would falsify canonical
global assembly while leaving the local coefficient result intact. A need
for a genuinely new stratum would fire the shared-carrier falsifier.
