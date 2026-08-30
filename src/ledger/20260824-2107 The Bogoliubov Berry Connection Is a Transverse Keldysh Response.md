# 2107 — The Bogoliubov Berry Connection Is a Transverse Keldysh Response

## Question

Entry 2104 found that the closed equal-source in-in value cancels common
Bogoliubov holonomy.  Entry 2105 showed that an asymmetric insertion can
recover it.  Test whether the native Keldysh source calculus already contains
the required asymmetry, without appending a laboratory control.

## Frozen Keldysh coordinates

Let \(\theta_+\) and \(\theta_-\) be the squeezed-phase protocol sources on
the two contour occurrences, and define

\[
\theta_c=\frac{\theta_++\theta_-}{2},
\qquad
\theta_q=\theta_+-\theta_-.
\]

For the source-normalized squeezed state of Entry 2101, the local Berry
connection is

\[
A_\theta=i\langle\zeta|\partial_\theta\zeta\rangle=-\frac89.
\]

The geometric influence factor is therefore

\[
Z_{\rm geom}
=\exp(iA_\theta\theta_q).
\]

## Diagonal value and transverse response

On the physical equal-source diagonal,

\[
Z_{\rm geom}|_{\theta_q=0}=1,
\]

in agreement with Schwinger–Keldysh unitarity.

Writing \(W=-i\log Z\), the two source derivatives are

\[
\frac{\partial W_{\rm geom}}{\partial\theta_c}=0,
\qquad
\boxed{
\frac{\partial W_{\rm geom}}{\partial\theta_q}\bigg|_{\theta_q=0}
=A_\theta=-\frac89.
}
\]

The quantum-source derivative is precisely the native in-in generator for the
response conjugate to the protocol.

## Narrow result

Closed-contour cancellation and physical phase response are compatible:

\[
\boxed{
\text{the Berry datum vanishes as an equal-source scalar value but survives
as the first transverse Keldysh jet.}
}
\]

Thus the native occurrence-resolved source calculus supplies the
branch-asymmetric port required by Entries 2104–2105.  The physical object is
a response covector, not the scalar value \(Z[J,J]\).

This is structurally parallel to the cosmological normal-jet lessons:

\[
\text{ordinary pullback or diagonal value}
\not\Rightarrow
\text{vanishing of a resolved transverse coefficient}.
\]

No new Carrier incidence and no external interferometer are required in this
finite Gaussian in-in model.

## Limitation and next falsifier

This derives the response typing and coefficient exactly, but not a specific
three-site loop observable.  The next test is to identify the corresponding
Keldysh quantum-source derivative in the frozen Bunch–Davies loop integrand
and determine whether its period pairing is nonzero or annihilated by the
physical contour.

## Durable evidence

- `research/benincasa/checkers/bogoliubov_keldysh_source_response.py`
- `research/benincasa/checkers/results/bogoliubov-keldysh-source-response.json`
- `research/benincasa/cubic-statistical-self-energy-variance.md`
- Ledger allocation: `seqclaim-24a79afa656209889dcb6c1f`

