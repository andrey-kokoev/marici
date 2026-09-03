# Remainder positivity plus decay forces the endpoint atom

## Question

Must endpoint subtraction be proved by a separate Schur estimate once the gamma-plus-prime localizer is known positive?

## Remainder moments

Fix `t,h>0`, put `s_n=t+nh`, and define

\[
a_n=H_{\Gamma+\mathbb P}(s_n)-H_{\Gamma+\mathbb P}(s_{n+1}).
\]

Since

\[
H_{\Gamma+\mathbb P}(s)=H(s)-e^{s/4},
\]

we have

\[
a_n=H(s_n)-H(s_{n+1})+c_h(t)y_E^n,
\]

where

\[
y_E=e^{h/4},
\qquad
c_h(t)=(e^{h/4}-1)e^{t/4}.
\]

If the completed source satisfies `H(s)->0`, then

\[
\frac{a_n}{y_E^n}\longrightarrow c_h(t).
\]

## Moment consequence

Assume the remainder Hankel matrices `(a_(i+j))` are PSD at every rank. The Hamburger theorem supplies a positive representing measure `mu_R`.

The even-moment growth

\[
\limsup_{n\to\infty}a_{2n}^{1/(2n)}=y_E
\]

forces support in `[-y_E,y_E]`, hence compact determinacy. The same normalized limit along even and odd indices then forces

\[
\mu_R(\{y_E\})=c_h(t),
\qquad
\mu_R(\{-y_E\})=0.
\]

Interior mass disappears after division by `y_E^n`; a negative-edge atom would produce parity oscillation.

Therefore

\[
\mu_{\rm full}=\mu_R-c_h(t)\delta_{y_E}
\]

is automatically positive. Its moments are exactly the completed localizer sequence

\[
H(s_n)-H(s_{n+1}).
\]

## Compression

Subject to a source proof of `H(s)->0`, there is no independent endpoint Schur gate. The all-rank remainder Hankel cone forces the exact endpoint atom and its exact mass by asymptotic rigidity. The collapsing finite-rank Schur margins are the Christoffel kernels converging to reciprocal atom mass.

The sole source positivity target becomes

\[
\bigl(H_{\Gamma+\mathbb P}(t+(i+j)h)-H_{\Gamma+\mathbb P}(t+(i+j+1)h)\bigr)_{i,j}\succeq0
\]

for every `t,h>0` and every finite rank, together with independently proved decay of `H`.

By single-localizer telescoping, positivity of completed localizers then reconstructs the sampled Hankel cones and positive semigroup.

## Falsifiers

The reduction fails if completed heat decay is unavailable, if remainder Hankel positivity does not hold at all ranks, or if moment growth cannot be bounded sharply enough to obtain compact support and determinacy.

## Boundary

Remainder positivity remains unproved. Existing scans through rank four are uncertified. The decay premise must be derived from an admitted source representation and cannot be inferred from the target positive measure.

## Disposition

Replace the two-part `background PSD plus endpoint Schur bound` programme by `background PSD plus completed-source decay`. The endpoint feature and exact residue then follow rather than being separately constructed.