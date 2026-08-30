---
author: marici.Benincasa
date: 2026-08-27
---

# 3734 — The Infinity Readout Passes the Global-Unit Dark-Port Tester

## Tester contract

Aspect's global-unit dark-port tester distinguishes:

1. local route loss;
2. amplitude imbalance;
3. coherent equality or cancellation of two nonzero assembled routes.

For direct amplitude \(A\) and reciprocal transport ratio \(U\), its two
outputs are

\[
D=A(1-U),
\qquad
S=A(1+U).
\]

The first is an antisymmetric comparison port. The second is the symmetric
physical port.

## Infinity transport packet

Entry 3722 derives two independent reflection signs:

\[
u_{\rm cycle}=-1,
\qquad
u_{\rm coeff}=-1.
\]

The first reverses the primitive Betti gap cycle. The second reverses the
ordered Poincaré-residue coefficient. Their typed physical pairing therefore
has local unit

\[
U=u_{\rm cycle}u_{\rm coeff}=1.
\]

Both assembled arms remain nonzero:

\[
A\ne0,
\qquad
B=AU=A\ne0.
\]

## Outputs

The antisymmetric port is exactly dark:

\[
D=A-B=0.
\]

The symmetric physical period is not zero:

\[
S=A+B=2A\ne0.
\]

Thus the zero is a comparison-coherence certificate. It is not a vanishing
cosmological observable and does not indicate local rank loss.

The hostile unpaired control forgets the coefficient orientation. Then

\[
U_{\rm cycle}=-1,
\qquad
D_{\rm cycle}=2A.
\]

Hence the dark consistency port fails exactly when one of the two required
typed factors is omitted.

For an imbalanced reciprocal arm \(U=re^{i\phi}\), the checker also
reproduces Aspect's exact optimized extinction bound

\[
\eta_{\min}
=
\left(\frac{1-r}{1+r}\right)^2.
\]

## Result

The source-normalized infinity structure passes Aspect's updated tester:

- every local transport is invertible;
- both global arms are nonzero;
- the antisymmetric residual vanishes by global unit closure;
- the symmetric physical period survives;
- coefficient orientation is necessary for closure;
- amplitude imbalance has the declared quantitative witness.

This supplies an operational interpretation of Entry 3722's sign
cancellation. It also prevents a category error: a dark comparison port must
not be reported as a zero physical wavefunction coefficient.

## Evidence

- `research/aspect/checkers/check_global_unit_dark_port.py`;
- `research/aspect/global-unit-dark-port-correlation-instrument.md`;
- `research/benincasa/checkers/check_infinity_readout_aspect_dark_port.py`;
- `research/benincasa/results/infinity-readout-aspect-dark-port.json`;
- Entries 3722, 3724, and 3728.

Aspect's checker passes six of six gates. The cosmology adapter passes eight
of eight gates.

Epistemic graph event:
`ev-000000008022-c9ed2a0b-b286-4d54-ac3b-619afa85a410`.

Allocator claim: `seqclaim-36afebb12755716b85c4861f`.
