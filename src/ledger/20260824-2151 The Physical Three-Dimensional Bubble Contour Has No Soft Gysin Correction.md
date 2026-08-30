---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2151 — The Physical Three-Dimensional Bubble Contour Has No Soft Gysin Correction

> **Scope correction from Entry 2153.** The radial integrability calculation
> remains valid. It does not establish physical-chain compatibility for a
> coefficient morphism, because no such inter-sector morphism has been
> source-derived.

## Hard-to-vary claim

For the literal positive-energy bubble contour in three spatial dimensions,
Entry 2150's deletion morphism produces no boundary current at either of its
two exceptional divisors.

## Removed total-energy wall

The first exceptional divisor is

\[
q=x_1+x_2+2y_a=0.
\]

On the literal physical chamber

\[
x_1>0,
\qquad
x_2>0,
\qquad
y_a\ge0,
\]

one has \(q>0\). Hence the physical contour and its closure do not meet this
wall.

## Erased-edge soft endpoint

Near \(y_b=0\), use the loop momentum centered at the corresponding focus:

\[
y_b=r=|\ell-\ell_b|.
\]

At nonsoft external separation, the remaining factors are smooth and the
\(d\)-dimensional loop measure has radial form

\[
d^d\ell
\sim
r^{d-1}dr\,d\Omega.
\]

The deletion insertion contributes \(r^{-1}\), leaving

\[
r^{d-2}dr\,d\Omega.
\]

For \(d=3\), this is \(r,dr\,d\Omega\). Its radial primitive is proportional
to \(r^2\), which vanishes at the soft endpoint. Therefore no residue or
Gysin boundary current survives:

\[
\boxed{
\partial_{m soft}\Gamma_{m phys}(f\Omega)=0
\qquad(d=3).
}
\]

## Dimension dependence

The result is dimension-sensitive. The first marginal case is \(d=1\), where
the post-deletion measure is \(dr/r\) and a logarithmic endpoint class can
appear. Thus the vanishing is a physical three-dimensional statement, not a
pure Carrier theorem.

## Consequence

Combining Entries 2149--2151 gives the complete lower-arity pilot:

\[
\boxed{
\text{the bubble last-edge deletion is coefficient-horizontal and
physical-chain compatible on the generic }d=3\text{ chamber.}
}
\]

No supported correction is needed there. Soft external coincidences, other
dimensions, and analytically continued contours remain outside this claim.

## Evidence

- Benincasa--Dian, arXiv:2401.05207, equations (2.24), (2.26), and (2.30);
- Entries 2149--2150;
- `research/benincasa/checkers/bubble_soft_chain_boundary.rs`;
- allocator claim `seqclaim-23f30a90bc2c0630b4c10e0f`.

## Next falsifier

Transport the exact rational/logarithmic construction to one last-edge
deletion of the three-site triangle. Derive the component-energy numerator,
erased-edge denominator, and physical soft-boundary exponent before invoking
cyclic symmetry.
