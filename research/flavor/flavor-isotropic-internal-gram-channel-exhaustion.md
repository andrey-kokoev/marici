# Isotropic internal Gram channels are identity or scalarization: WP951

## Question

After WP950 closes scalar mixing between sectors, can a positive source-neutral operation acting inside each Gram matrix select a viable proper `physical16` family?

## Full weak-basis-covariant channel

For one matrix under the conjugation action of `U(3)_Q`, every complex-linear equivariant endomorphism has the form

\[
\Phi_{a,b}(X)=aX+b\operatorname{Tr}(X)I.
\]

Trace preservation, equivalently unitality for this form, requires

\[
a+3b=1.
\]

Writing

\[
\Phi_a(X)=aX+(1-a)\frac{\operatorname{Tr}X}{3}I,
\]

idempotence gives `a^2=a`. Hence the only trace-preserving idempotents are

\[
\Phi_1(X)=X
\]

and

\[
\Phi_0(X)=\frac{\operatorname{Tr}X}{3}I.
\]

Both are completely positive: identity is trivial, while `Phi0` is the exact Haar conjugation twirl.

## Sectorwise exhaustion

Applying the two choices independently to `(H_u,H_d)` gives four channels. If both choices are identity, the full physical family survives and nothing is selected. If either Gram is scalarized, it commutes with the other Gram and every commutator invariant vanishes. Scalarization also replaces that sector's three eigenvalues by their mean and destroys its hierarchy.

For the exact positive comparator

\[
H_u=\operatorname{diag}(1,2,4),
\qquad
H_d=\begin{pmatrix}2&1&i\\1&3&1\\-i&1&5\end{pmatrix},
\]

the identity pair retains

\[
\operatorname{Tr}[H_u,H_d]^3=-36i.
\]

Each of the other three idempotents sends it to zero.

## Claim boundary

This exhausts sector-local linear channels with no internal source tensor beyond the `U(3)_Q`-invariant identity. It does not exhaust channels depending jointly and nonlinearly on both Grams, commutator gradients, or operations carrying a source-derived anisotropic tensor.

The scalar Haar twirl has a formal random-unitary realization, but no admitted flavor apparatus implements full family-basis randomization as a calibrated source operation. More importantly, it selects the experimentally wrong commuting locus.

## Disposition

The isotropic internal channel branch is closed negative. Full weak-basis covariance, linearity, trace preservation, and idempotence yield only no selection or scalarization. A viable operation must use a source-derived anisotropic relational tensor constructed from the pair itself or from an additional declared source object. If that tensor is a reference port, the resulting stabilizer groupoid and new experiment must be stated explicitly. No channel parameter is assigned physical time.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp951_isotropic_internal_gram_channel_exhaustion.py

Generated result: `research/flavor/results/wp951_isotropic_internal_gram_channel_exhaustion.json`.
