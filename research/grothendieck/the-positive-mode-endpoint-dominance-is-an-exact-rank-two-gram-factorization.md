# The Positive-Mode Endpoint Dominance Is an Exact Rank-Two Gram Factorization

## Setup

For a positive exponential packet, retain

\[
K_z(0)=\sum_n\frac{c_n}{\alpha_n^2-z^2},
\qquad
c_n>0,
\qquad
\alpha_n>0.
\]

Write

\[
z=a+it,
\qquad
d_n=\alpha_n^2-z^2,
\qquad
w_n=\frac{c_n}{|d_n|^2}.
\]

Let

\[
S_z
=
\sum_{m<n}
\frac{c_mc_n(\alpha_m-\alpha_n)^2}
{|d_m|^2|d_n|^2}.
\]

## Exact factorization

The endpoint-minus-pair expression factors as

\[
\begin{aligned}
|K_z(0)|^2-4t^2S_z
={}&
\left(
\sum_nw_n(\alpha_n^2-|z|^2)
\right)^2\\
&+
\left(
2t\sum_nw_n\alpha_n
\right)^2.
\end{aligned}
\]

The proof is coefficientwise.  After multiplying the `(m,n)` kernel by
`|d_m|^2|d_n|^2`, it becomes

\[
(\alpha_m^2-|z|^2)(\alpha_n^2-|z|^2)
+4t^2\alpha_m\alpha_n.
\]

This is the Gram kernel of the two-dimensional vectors

\[
v_n=
\left(
\alpha_n^2-|z|^2,
2t\alpha_n
\right).
\]

Therefore endpoint dominance is not an estimate.  It is a rank-two Gram
identity.

## Strict orientation

If `t` is nonzero, positivity of every `c_n`, `w_n`, and `alpha_n` gives

\[
2t\sum_nw_n\alpha_n\ne0.
\]

Hence

\[
|K_z(0)|^2>4t^2S_z.
\]

Combining this with the pair-separation formula for the Wronskian yields

\[
\Delta_{\mathrm{face}}
=
2a
\left(
|K_z(0)|^2-4t^2S_z
\right).
\]

For every nonzero positive packet and `t != 0`, the face orientation has
exactly the sign of `a`.

## Conditional zero-confinement theorem

Suppose a completed two-sector zero-state in this positive-mode class makes
the total oriented face flux vanish.  If its imaginary coordinate is nonzero,
then strict Gram positivity forces

\[
a=0.
\]

Thus the three-sector architecture proves zero confinement for the entire
positive exponential cone, conditional only on the already typed bridge from
the scalar zero to vanishing total oriented flux.

This is not RH.  The actual theta forcing has polynomially differentiated
Gaussian modes and has not yet been placed in this cone.

## Real-axis boundary

When `t=0`, the second Gram coordinate vanishes and the first square can in
principle vanish.  The theorem therefore treats nonreal zeros.  Exclusion of
nontrivial real zeros remains a separate source fact, as required by the
earlier support audit.

## Deutschian content

The explanation is hard to vary:

1. positive source modes create pairwise squared separations;
2. reciprocal resolvents orient every pair coherently;
3. the endpoint and pair current assemble into a rank-two Gram vector;
4. a nonreal off-seam null orientation is impossible because its second Gram
   coordinate is strictly nonzero.

A hostile signed source fails at step one: its weights no longer define a
positive Gram combination.

## Next gate

Determine whether each differentiated theta summand admits a source-authorized
positive-mode representation, perhaps after adjoining derivative labels, or
locate the first negative coefficient in the corresponding Gram kernel.

## Result

Endpoint dominance on the positive exponential cone is proved exactly by a
rank-two Gram factorization.  Together with the Wronskian pair formula, it
orients the full cross-face instrument by the sign of the centered real part.
The sole remaining transfer problem is theta cone membership.

