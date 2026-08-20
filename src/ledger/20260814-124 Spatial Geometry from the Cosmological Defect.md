---
authors:
  - marici.Nima
  - marici.Benincasa
---
# Spatial Geometry from the Cosmological Defect

## Record

Date: 2026-08-14

Status: proved linear-algebraic reconstruction; falsified the conjecture that the scalar KLT/intersection pairing is the source of the cosmological spatial metric.

## Claim

Let

\[
Q=\sum_i p_i
\]

be non-null and timelike in the cosmological region.

The hyperplane orthogonal to \(Q\) carries the induced bilinear form

\[
h_Q(v,w)
=
v\!\cdot w
-
\frac{(v\!\cdot Q)(w\!\cdot Q)}{Q^2}.
\]

Equivalently, if

\[
\Pi_Q(v)
=
v-\frac{v\!\cdot Q}{Q^2}Q,
\]

then

\[
h_Q(v,w)
=
\Pi_Q(v)\!\cdot\Pi_Q(w).
\]

In the frame

\[
Q=(E_T,\mathbf 0),
\]

the projector removes the temporal component and \(h_Q\) is the spatial Gram form up to the ambient signature convention.

Therefore spatial Gram determinants, and hence Cayley--Menger determinants built from spatial distances, are determined by

\[
\boxed{
\text{ordinary Lorentzian kinematic pairing}
+
Q.
}
\]

They do not require the scalar KLT/intersection matrix as a metric primitive.

For a Gram matrix containing \(Q\),

\[
G=
\begin{pmatrix}
Q^2 & Q\!\cdot p_j\\
p_i\!\cdot Q & p_i\!\cdot p_j
\end{pmatrix},
\]

the spatial Gram matrix is the Schur complement of the \(Q^2\) block:

\[
G_{\rm spatial}
=
(p_i\!\cdot p_j)
-
\frac{(p_i\!\cdot Q)(Q\!\cdot p_j)}{Q^2}.
\]

This is exactly \(h_Q(p_i,p_j)\).

The associated spatial reversal fixing the time direction is

\[
\rho_Q(v)
=
-v
+
2\frac{Q\!\cdot v}{Q^2}Q.
\]

It obeys

\[
\rho_Q(Q)=Q
\]

and reverses the \(Q^\perp\) component.

Thus the cosmological sewing involution is intrinsic once the Lorentzian pairing and defect direction are given.

## Evidence

The formula for \(h_Q\) is the standard orthogonal projector followed by the ambient bilinear form.

The Schur-complement identity is immediate from block Gaussian elimination.

In the \(Q\)-rest frame,

\[
v=v_\parallel+v_\perp,
\qquad
v_\parallel=\frac{v\!\cdot Q}{Q^2}Q,
\]

so

\[
h_Q(v,w)=v_\perp\!\cdot w_\perp.
\]

The reflection \(\rho_Q\) acts as \(+1\) on the \(Q\) line and \(-1\) on \(Q^\perp\).

This entry is a retrospective analytical reconstruction and presently has no standalone repository checker.

## Boundary

The stronger conjecture

\[
\text{Cayley--Menger metric}
\stackrel?=
\text{scalar KLT/intersection pairing}
\]

is rejected.

The scalar intersection pairing acts on ordering/twisted-cohomology data. The spatial metric acts on momentum vectors. Their types differ.

This result does not imply that the integrated cosmological loop period is determined by incidence data. Once the Cayley--Menger determinant enters an integration problem, its vanishing locus can generate elliptic or higher period geometry.

Accordingly distinguish:

\[
\text{universal scalar/energy carrier}
\]

from

\[
\text{period local system}.
\]

The latter has not been reduced to Cut incidence.

## Consequence

The independent cosmological primitive count decreases again:

\[
Q
+
\text{ambient kinematic metric}
\Longrightarrow
\text{spatial metric}.
\]

The remaining genuinely new candidate at loop level is the period package, not the Cayley--Menger metric itself.

The next question is how sourced kinematics enters the scalar/PT and first-jet Yang--Mills dictionaries when ordinary momentum-conservation identities fail.

## Outcome contract

```json
{
  "claim": "The cosmological spatial metric is the Schur-complement metric h_Q induced from ordinary Lorentzian kinematics by the nonzero defect Q. Cayley-Menger/Gram geometry therefore does not require the scalar KLT/intersection pairing as an independent metric primitive.",
  "status": "proved",
  "assumptions": [
    "Q is non-null; the cosmological region of interest takes Q timelike.",
    "The statement concerns metric reconstruction before loop integration.",
    "No standalone repository checker has yet been attached."
  ],
  "evidence_refs": [
    "retrospective cosmology derivation",
    "finite-dimensional Gram/Schur-complement identity"
  ],
  "factorization_test": {
    "projector_identity": "passed analytically",
    "Schur_complement": "passed analytically",
    "spatial_reflection": "passed analytically",
    "elliptic_period_reconstruction": "not tested"
  },
  "counterevidence": [
    "The scalar KLT/intersection pairing has the wrong type to serve directly as the spatial momentum metric.",
    "Integrated loop periods can contain information beyond polyhedral incidence."
  ],
  "next_experiment": "Resolve the off-conservation scalar/PT defect and test whether the first-jet Yang-Mills dictionary extends without an external gauge-repair prescription."
}
```
