---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Exact-Lift Special-Fiber Relation Is the Algebraic Gysin Relation

## Record

Status: exact finite-field vector-level identification on both components of
the algebraic dlog divisor. This continues Entries 178 and 388--390, 400.

## Hard-to-vary claim

The common divisor found in Entry 400 could still support two unrelated
coefficient mechanisms. The finite falsifier is whether the additional
exact-lift gauge vector agrees with the source-defined algebraic Gysin
generator \(v_{\rm alg}\) in the common master basis.

## Frozen master map

The twelve marked masters are
\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9).
\]
Thus indices \(8,9,10,11\) are \((e_6,e_7,e_8,e_9)\).

At a generic fiber the projected exact-lift gauge plane pivots in \(e_1,e_2\).
On either component
\[
D_-=E^2-X_1X_2=0,qquad D_+=E^2+X_1X_2=0,
\]
the rank-three special-fiber gauge space acquires one RREF row pivoting at
\(e_6\). Its earlier coordinates vanish by construction. The invariant datum
to compare is its tail in \((e_7,e_8,e_9)\).

The source infinity-Gysin kernel generator is
\[
\begin{aligned}
v_{\rm alg}={}&
(X_1^2-X_2^2)(X_1^2X_2^2-E^4)e_7\\
&+2X_1^2(E^2+X_2^2)e_8
-2X_2^2(E^2+X_1^2)e_9.
\end{aligned}
\]
On either \(D_\pm\), the \(e_7\) coefficient vanishes.

## Exact test

At
\[
u=3,5,7,11,19,37
\]
on both \(D_-\) and \(D_+\), and at exact-form degrees 8 and 10:

- the new \(e_6\)-pivot row exists;
- its \((e_7,e_8,e_9)\) tail is nonzero;
- all three pairwise minors between that tail and \(v_{\rm alg}\) vanish;
- the degree-8 and degree-10 normalized tails are identical.

All 24 tested special-fiber relations therefore have the form
\[
\boxed{
e_6+\lambda_\pm v_{\rm alg}=0,
\qquad \lambda_\pm\ne0.
}
\]

## Verdict

The alternative-mechanism hypothesis is falsified in the tested fibers.
The exact-lift rank jump is the presentation shadow of the same algebraic
Gysin plane and quotient line that produced
\[
\alpha_{\rm alg}=d\log(E^4-X_1^2X_2^2).
\]

The chain of evidence is now vector-level:
\[
\text{infinity-Gysin kernel }\langle e_6,v_{\rm alg}\rangle
\longrightarrow
\text{rank-one quotient}
\longrightarrow
d\log D
\longrightarrow
e_6+\lambda v_{\rm alg}=0\text{ on }D.
\]

No new carrier stratum and no second coefficient mechanism are required.

## Epistemic boundary

This is a fiberwise finite-field identity in the frozen master projection.
It does not construct a global rational chain map, determine \(\lambda_\pm\)
symbolically, or fix integral lattice normalization. It does not establish
physical-chain monodromy.

It supplies no home for \(\mathcal Q\), which remains coprime to \(D\) and
regular in the frozen coefficient module at generic \(\mathcal Q=0\).

## Classification

- carrier: unchanged;
- coefficient object: algebraic Gysin plane
  \(\langle e_6,v_{\rm alg}\rangle\);
- special-fiber relation: \(e_6+\lambda_\pm v_{\rm alg}=0\);
- support: \(E^4-X_1^2X_2^2=0\);
- new primitive: none.

## Next falsifier

Reconstruct \(\lambda_-\) and \(\lambda_+\) as rational functions on the
two divisor components and compare their residues with the unit residues of
\(d\log D\). This tests whether the local presentation relation glues to the
known quotient connection without an unobserved unit or ramified
normalization.

## Evidence

- `research/benincasa/exact-lift-valg-special-fiber-identity.json`
- `research/benincasa/generic_algebraic_line_provenance.json`
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`
