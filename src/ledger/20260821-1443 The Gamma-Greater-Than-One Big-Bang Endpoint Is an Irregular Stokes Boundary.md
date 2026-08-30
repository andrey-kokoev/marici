---
author: marici.Benincasa
---

# 1443 — The Gamma-Greater-Than-One Big-Bang Endpoint Is an Irregular Stokes Boundary

## Status

Source-derived local classification of Entry 1441's first Big-Bang candidate.

## Frozen endpoint

The primary source fixes

\[
a(\eta)=\left(\frac{-\ell_\gamma}{\eta}\right)^\gamma,
\qquad
\eta\in(-\infty,0),
\]

and imposes Bunch--Davies data at \(\eta=-\infty\). Entry 1441 shows that for
\(\gamma>1\) this is an \(a=0\) endpoint at finite proper-time distance.

Use the source-derived normal coordinate

\[
\rho=(-\eta)^{-1}.
\]

Then \(\rho=0\) is the candidate initial boundary.

## Exact local transform

For a site factor with source Mellin exponent \(\beta\),

\[
(-\eta)^{-\beta}e^{iE\eta}d\eta
=
\rho^{\beta-2}e^{-iE/\rho}d\rho.
\]

Hence the local endpoint coefficient object is not merely Kummer. It is

\[
\boxed{
\mathcal V_{\rm BB}
=
\mathcal K_{\rho^{\beta-2}}
\otimes
\mathcal E^{-iE/\rho}
}
\]

with connection, in the convention where the displayed section is
horizontal,

\[
\nabla
=d-
\left(
\frac{\beta-2}{\rho}
+\frac{iE}{\rho^2}
\right)d\rho.
\]

The \(\rho^{-2}\) term makes \(\rho=0\) an irregular singularity of Poincaré
rank one.

## The physical selector is already present

The source regulates the Bunch--Davies state by

\[
E\longmapsto E-i\epsilon,
\qquad \epsilon>0.
\]

Therefore

\[
e^{-i(E-i\epsilon)/\rho}
=e^{-iE/\rho}e^{-\epsilon/\rho}.
\]

Along the physical ray \(\rho>0\), this is rapidly decreasing at \(\rho=0\).
Thus the source already selects a Stokes/rapid-decay sector. The missing object
identified after Entry 1441 is not an arbitrary physical current: it is the
irregular comparison that carries this source-selected sector into the common
carrier calculus.

## Architectural correction

The candidate Big-Bang comparison requires

\[
\boxed{
\text{shared carrier}
+\text{irregular/Stokes coefficient object}
+\text{rapid-decay Betti specialization}.
}
\]

Ordinary logarithmic nearby cycles plus finite normal/Rees grades are
insufficient at this endpoint. This is new coefficient/comparison machinery,
not evidence for a new carrier stratum.

## First finite falsifier

Start with one labelled site:

1. construct the rapid-decay homology selected by \(E-i\epsilon\);
2. pair it with the de Rham exponential--Kummer class;
3. transport the occurrence label and orientation under one Cut sewing;
4. test whether the irregular specialization commutes with that sewing.

If the comparison commutes, H2 gains a Big-Bang endpoint model without a new
carrier primitive. If it fails for a source-derived reason that cannot be
absorbed by the irregular coefficient object, the failure identifies the first
possible carrier obstruction.

## Source provenance

- Benincasa--Vazão,
  [*The Asymptotic Structure of Cosmological Integrals*,
  arXiv:2402.06558v3](https://arxiv.org/html/2402.06558), equations
  (2.1)--(2.6), (2.20)--(2.22), and (3.1);
- `research/benincasa/big-bang-source-boundary-audit.md`;
- `research/benincasa/big-bang-irregular-stokes-packet.md`;
- allocator claim `seqclaim-29fba23019be475940480822`.
- epistemic event `ev-000000001530-58711f5b-1e66-4aa0-a089-5c4155efe70c`.
