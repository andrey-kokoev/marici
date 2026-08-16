---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Complete Unsplit Master Restoration and Two-Grade Residue Vanishing

## Record

Status: the nonconstant Cayley--Menger branch and source double-pole master
factor omitted from the primitive argument of entries 232--233 have been
restored. Their leading logarithmic wall residue still vanishes, and the
next full coefficient also has zero logarithmic residue by an exact
coefficient identity.

This entry explicitly corrects the complete-primitive claim in entries
232--233. It preserves their denominator algebra but replaces the inference
about the complete integrand.

No denominator, carrier incidence, support summand, regulator hierarchy,
projector, or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{restoring the nonconstant }K_1/K^{3/2}\text{ factor produces a
nonzero wall residue at weight }-3\text{ or }-2.
}
\]

The finite falsifier was exact vanishing of both logarithmic residue
coefficients in the complete unsplit local form.

## Correction to entries 232--233

Those entries correctly derived the restored lower-denominator factor, but
then used

\[
d\left(\frac{n}{4xy,r}dn\right)
\]

as though it were a primitive of the complete integrand. The complete
exceptional master contains

\[
-\frac12\frac{K_1,da\wedge db}{K^{3/2}},
\]

whose leading coefficient depends nontrivially on \((r,n)\). The displayed
primitive is therefore not a complete-integrand primitive.

The correct invariant test is the logarithmic coefficient after reducing
higher normal poles modulo exact forms.

## Complete weighted expansion

Write

\[
K=\tau^6(k_0+\tau k_1+O(\tau^2)),
\]

\[
K_1^{\rm src}
=\tau^4(\ell_0+\tau\ell_1+O(\tau^2)).
\]

Exact substitution into the frozen source family gives

\[
k_0
=
4xy\left[n^2xy+2(x+y)(r^2-1)\right],
\]

\[
k_1
=
4nxy(x+y)(r^2-2r-1),
\]

\[
\ell_0=16xy(x+y),
\qquad
\ell_1=8nxy(x+y).
\]

The Jacobian remains

\[
da\wedge db=\tau^5dr\wedge dn.
\]

Together with the unsplit lower factor of entry 232, these determine the
complete coefficients at weights \(-3\) and \(-2\).

## Leading residue

Up to the common source branch and normalization, the weight \(-3\)
coefficient has the form

\[
F_{-3}
=
\frac{2(x+y)n}{r^2k_0^{3/2}},dr\wedge dn.
\]

Since \(k_0\) is even in \(r\), the Laurent expansion of
\(n/k_0^{3/2}\) has no linear \(r\) term. Therefore reduction of the
double pole produces no logarithmic coefficient:

\[
\boxed{\operatorname{Res}_{r=0}F_{-3}=0.}
\]

This is the complete-integrand reason the leading verdict of entry 233
survives.

## Next-grade residue

The lower-denominator expansion is

\[
\tau^3D_{\rm low}
=
-\frac{n}{4xy,r^2}
+
\tau\frac{n^2(r-1)}{4xy,r^3}
+
O(\tau^2).
\]

Expanding \(K_1K^{-3/2}\) to first order and reducing the resulting triple
and double poles, the only possible logarithmic coefficient is proportional
to

\[
[r]k_1+n[r^2]k_0.
\]

But

\[
[r]k_1=-8nxy(x+y),
\]

and

\[
n[r^2]k_0=8nxy(x+y).
\]

Hence

\[
\boxed{
[r]k_1+n[r^2]k_0=0,
}
\]

and therefore

\[
\boxed{\operatorname{Res}_{r=0}F_{-2}=0.}
\]

The cancellation uses the complete Cayley--Menger deformation; it is not
visible in the lower-denominator factor alone.

## Verdict

The nonzero-residue conjecture is falsified through two complete grades:

\[
\boxed{
\operatorname{Res}_{r=0}F_{-3}
=
\operatorname{Res}_{r=0}F_{-2}
=0.
}
\]

Thus the literal unsplit source still has no wall-supported logarithmic
class at the first two restored weights. The projected nine-master
commutator remains nonconservative under the literal occurrence lift.

This does not prove complete vanishing. Weight \(-1\) is the next possible
grade.

## Classification

- existing carrier: unchanged exceptional disk and marked collision wall;
- corrected complete coefficient object: lower factors times
  \(K_1K^{-3/2}\);
- logarithmic wall support at weights \(-3,-2\): zero;
- elliptic Gauss--Manin data: no new image;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_complete_unsplit_next_grade.rs`;
- `research/benincasa/complete-unsplit-next-grade.json`;
- exact weighted expansions at 20,655 integer specializations;
- exact residue identity \([r]k_1+n[r^2]k_0=0\);
- warnings-denied optimized Rust compilation and execution.

## Next finite falsifier

Compute the complete weight \(-1\) coefficient. This requires

- \(K\) through \(\tau^8\);
- \(K_1^{\rm src}\) through \(\tau^6\);
- the unsplit lower factor through relative order \(\tau^2\);
- reduction of poles through order \(r^{-4}\).

Test its logarithmic residue before any chain pairing or occurrence
forgetting. A nonzero residue is the first canonical full-source wall class.
Another zero moves the frontier one grade higher.

## Outcome contract

~~~json
{
  "claim": "Restoring the complete master factor produces a nonzero wall residue at weight -3 or -2.",
  "status": "falsified",
  "correction": "The primitive in entries 232-233 omitted the nonconstant K1/K^(3/2) factor.",
  "complete_residues": {
    "-3": 0,
    "-2": 0
  },
  "next_possible_grade": -1,
  "new_carrier_incidence": false,
  "next_experiment": "Compute and reduce the complete weight -1 coefficient."
}
~~~
