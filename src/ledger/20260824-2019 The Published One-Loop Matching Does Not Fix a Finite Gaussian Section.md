---
author: marici.Benincasa
---

# 2019 — The Published One-Loop Matching Does Not Fix a Finite Gaussian Section

## Question

Entry 2018 identified the intrinsic positive Gaussian readout space

\[
\{(P,S):S>-\tfrac12\}.
\]

Does the one-loop source of Entry 1494 select a definite point or trajectory in this space under its declared renormalization prescription?

## Frozen source

The primary source is Collins--Holman--Vardanyan, *Renormalizing an initial state*, arXiv:1408.4801v1.

Its bulk loop is regularized dimensionally. In Eqs. (5.2)--(5.3), the counterterm coefficients are chosen from the **infinite parts** of the loop integrals \(I_0,I_2,I_4\), leaving unspecified finite parts \(I_0^f,I_2^f,I_4^f\).

At finite initial time, Eq. (5.7) separates pieces that vanish, remain finite and oscillatory, or diverge linearly or quadratically in \(\eta_0\). The paper then computes only the quadratically divergent grade.

## What Eqs. (5.8)--(5.9) fix

The displayed quadratic initial action has

\[
A_p=A_{R,p}+iA_{I,p},
\qquad
B_p\in\mathbb R.
\]

Comparison with the quadratic \(\eta_0\)-divergence yields

\[
A_{R,p}=0,
\]

\[
A_{I,p}
=
\frac{(3\epsilon+2\delta)^2}{32}p^3
\left[
\operatorname{Inf}(I_4-J_1+2J_0+4J_2)
\right],
\]

and

\[
B_p
=
-\frac{(3\epsilon+2\delta)^2}{16}
\operatorname{Inf}(J_0).
\]

These are pole/divergence-cancellation data. They do not specify the finite renormalized covariance.

## Explicit source stop

Immediately after those formulas, the source states that full one-loop renormalization also requires extracting and eliminating the zeroth- and first-order terms in \(\eta_0\). It does not perform those calculations, saying only that there is no principal difference in the method.

Therefore the omitted data include precisely the finite and oscillatory matching conditions needed to determine the intrinsic covariance coordinates

\[
(\nu,\kappa)
\]

and hence the physical late-time point

\[
(P,S).
\]

## Why minimal subtraction does not close the gate

Setting finite bulk counterterms to zero in a minimal-subtraction convention fixes a bulk scheme, but it does not impose the omitted finite **state-matching** conditions. The source's physical target is cancellation of unwanted finite oscillatory and divergent initial-time terms. Leaving the finite state kernels at zero does not implement that declared target.

Consequently, choosing finite \(A\) and \(B\) to enter the positivity half-plane would be a post hoc repair, while setting them to zero would be an unsupported replacement of the unfinished matching problem.

## Narrow conclusion

\[
\boxed{
\text{the published one-loop source fixes a divergent tangent,}
\quad
\text{not a finite positive Gaussian section}.
}

In Nima's three-way classification, the current source lands in the middle case:

\[
\boxed{
\text{missing renormalization/readout datum}.
}

No positivity pass or failure can be assigned to the generated finite state from the published formulas alone.

## Architectural consequence

Entries 2013 and 2018 establish the legal readout quotient and its positive domain. Entry 2019 shows that these constraints do not select the source dynamics. The division is now exact:

\[
\text{Carrier and coherence}
\to
\text{legal coefficient/readout space},
\]

\[
\text{finite state matching}
\to
\text{physical section}.
\]

The second arrow is absent from the frozen publication at the required orders.

## Next admissible move

Perform a bounded provenance search for a later primary paper, supplementary calculation, or author-provided derivation completing the zeroth- and first-order finite-time matching of arXiv:1408.4801. If none exists, close this source branch under current literature. Do not reconstruct the missing kernels by fitting positivity or late-time simplicity.

## Provenance

- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (5.2)--(5.9), especially the paragraph following Eq. (5.9);
- Entries 1494, 2013, and 2018;
- allocator claim `seqclaim-233a9e38d47b7e770f3140e0`.

Epistemic graph event: `ev-000000002750-940d1fe9-b983-4ce4-a707-dacef21dd9d1`.
