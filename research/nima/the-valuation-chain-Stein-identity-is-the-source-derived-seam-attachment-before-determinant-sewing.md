# The valuation-chain Stein identity is the source-derived seam attachment before determinant sewing

## Question

Does the declared arithmetic source supply a boundary attachment that survives the fixed-window hostile without importing the determinant or Haar readout?

## Source operation and type

For one prime valuation chain, let

\[
(J_pe_k)(u)=p^{-k/2}\Phi(u+k\log p),
\]

let `A_p=p^(1/2)S` be the weighted valuation shift, and let `B_p=R_(log p)J_p` restrict the translated tail to the newly exposed seam window.

The objects are differently typed:

- `J_p` maps the labelled valuation chain to the analytic tail;
- `A_p` transports the labelled base;
- `B_p` is a boundary observation, not an endomorphism or determinant.

## Composition and transport

For continuous tail shift `C_(log p)`, the source weights give

\[
p^{-1/2}C_{\log p}J_p=J_pS.
\]

Writing `G_p=J_p^*J_p`, removal of the first translated window gives the exact Stein identity

\[
G_p-A_p^*G_pA_p=B_p^*B_p.
\]

Iteration yields

\[
G_p-(A_p^*)^NG_pA_p^N
=
\sum_{j=0}^{N-1}(A_p^*)^jB_p^*B_pA_p^j.
\]

Thus attachment composition occurs over the transported valuation base. A single fixed-origin row is not the composition law.

## Finite falsifier

The exact rational fixture uses `p=4`, a finite supported forcing vector, and two labelled source coordinates. It verifies the forward intertwiner and Stein identity.

The state `(1,-1)` is invisible to the first window:

\[
B_pc=0,
\]

while its source Gram energy is

\[
\langle c,G_pc\rangle=\frac{15}{2}.
\]

The complete transported-window family recovers that energy exactly. Therefore any attachment using only one seam row is falsified even though its local formula is correct.

## Claim boundary

The source-derived attachment is the transported observability tower, not the universal truncated-Fourier bulk and not a fitted Schur complement. This advances the clutching problem from an absent boundary operation to an exact prime-orbit attachment law.

It does not construct:

- the determinant-line image of the observation tower;
- compatibility with the primitive, square, and connected order-three grades;
- adjacent-prime permutohedral sewing;
- a completion preserving both the noncoercive source Gram and labelled arithmetic predicates.

## Disposition

The fixed-window rival is falsified. The transported-window Stein attachment survives at finite cutoff and is source-derived. The next governing-order obligation is transport across adjacent prime orderings, where the ratio window must be retained before determinant packet sewing.

Verification:

- `research/nima/checkers/check_prime_seam_stein_attachment.py`
- `research/nima/results/prime-seam-stein-attachment.json`
