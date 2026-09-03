# Scalar Bernstein measure to all-character Gram lift

## Question

What exact arrow would upgrade scalar heat complete monotonicity to every finite translate Gram inequality?

## Claim boundary

The all-rank factorization is conditional on identifying one positive scalar Bernstein measure with the source spectral pushforward. That identification is not proved.

## Local projection

Let

\[
K_\sigma(d)=
\langle\rho,e^{-2\sigma u^2}e^{-idu}\rangle
\]

and

\[
\Theta(t,0)=\langle\rho,e^{-tu^2}\rangle.
\]

Then

\[
\partial_d^{2m}K_\sigma(0)
=
\left.\partial_t^m\Theta(t,0)\right|_{t=2\sigma}.
\]

Thus scalar heat complete monotonicity gives the necessary coincident-translate jet signs and, by Bernstein's theorem, an abstract positive measure \(\mu\) on \(\lambda\geq0\).

## Required source lift

The missing arrow must identify that same measure with the \(u^2\)-pushforward of the completed even spectral distribution and prove

\[
K_\sigma(d)=
\int_0^\infty e^{-2\sigma\lambda}
\cos(d\sqrt\lambda)\,d\mu(\lambda).
\]

Once this identity exists, all ranks follow simultaneously:

\[
\sum_{i,j}c_i\overline{c_j}K_\sigma(a_i-a_j)
=
\int_0^\infty e^{-2\sigma\lambda}
\left|\sum_i c_i e^{-ia_i\sqrt\lambda}\right|^2d\mu(\lambda)
\geq0.
\]

The rank-two inequality \(|K_\sigma(d)|\leq K_\sigma(0)\) follows as a special case.

## Typing consequence

Existence of a Bernstein measure representing only \(\Theta(t,0)\) does not establish that it is the source pushforward or that it represents the imaginary-character kernel. Reconstructing Gram atoms from presumed zeros would reverse the required direction.

## Disposition

Matrix-by-matrix positivity can be replaced by one source-measure lift theorem. This is not a weaker gate: proving the all-character representation with the same positive measure is the full nonlocal arithmetic content.

## Verification

- `research/voevodsky/scalar-bernstein-to-all-character-gram-lift-v1.json`
- `research/voevodsky/checkers/check_scalar_bernstein_to_all_character_gram_lift.py`
- `research/voevodsky/results/scalar_bernstein_to_all_character_gram_lift.json`
