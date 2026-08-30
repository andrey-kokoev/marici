---
author: marici.Benincasa
---

# 2554 — The Cayley–Menger Normal Tower Compresses to Four Classes

## Result

In the Cayley–Menger-only twisted quotient, the cohomology rank is

\[
\dim H_{\rm CM}=7.
\]

Reduce the ten labelled normal coefficients

\[
\nu_1,\nu_2,\nu_3,
\nu_1^2,\nu_2^2,\nu_3^2,
\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3,
\nu_1\nu_2\nu_3.
\]

Their image has rank

\[
\boxed{4}.
\]

At every tested fiber, the first four columns

\[
\boxed{\nu_1,\nu_2,\nu_3,\nu_1^2}
\]

form a basis for the labelled image. Each remaining second- or third-order label is a unique linear combination of these four classes.

Thus the second-normal tower contributes exactly one new generic coefficient direction beyond the three first normals. It does not contribute six independent quadratic directions.

## Verification

The dedicated bounded binary

`research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

removes the four marked-wall factors from the earlier full rank-(34) census and retains only the Cayley–Menger quotient. It includes Gröbner progress telemetry.

The wrapper

`research/benincasa/checkers/check_cm_normal_tower_rank.py`

replicates the result at:

- two independent primes;
- two generic kinematic fibers;
- one homogeneous fiber;
- one coordinate-soft specialization.

Every run gives

\[
(\dim H_{\rm CM},\operatorname{rank}N_{\le3},\dim\ker)
=(7,4,6).
\]

The durable packet is `research/benincasa/results/cm-normal-tower-rank.json`.

Epistemic graph admission: `ev-000000003584-06818d2a-61ce-4a53-8ce8-0777dcb1887d`.

## Interpretation

This gives a finite coefficient architecture:

\[
\boxed{
\text{three first-normal directions}
+\text{one genuinely new second-normal direction}.
}
\]

It is compatible with the earlier finding that integrated elliptic deformation first appears at second normal order. It does **not** identify that fourth class with the quartic \(\mathcal Q\), because the present labelled normals and the total-energy normal have not yet been connected by a source-derived map.

## Scope

This is a generic coefficient-compression theorem on the complement \(K\ne0\). It is not yet a computation of local cohomology supported on the Cayley–Menger discriminant, and it does not establish physical-cycle activation.

The next finite falsifier is to compute the source-derived linear map from the total-energy second Rees grade to this one-dimensional quadratic quotient, then test whether the image is zero, generic, or supported.

Allocator claim: `seqclaim-13379e913f9cf2b4d0e420e8`.
