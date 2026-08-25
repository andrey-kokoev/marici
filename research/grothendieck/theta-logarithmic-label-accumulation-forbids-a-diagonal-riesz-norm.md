# Logarithmic theta-label accumulation forbids a diagonal Riesz norm

## Discrete labelled Gram kernel

For the full tail--seam atom at arithmetic label `n`, put

\[
 u_n=(g_{\log n},h_{\log n}).
\]

The exact cut decomposition gives

\[
 \boxed{
 K_0(n,m)=\langle u_n,u_m\rangle
 =A\!\left(\left|\log\frac nm\right|\right).}
\]

In particular,

\[
 \lVert u_n\rVert^2=A(0)
\]

is independent of `n`.

## Adjacent labels become parallel

Let

\[
 \delta_n=\log(n+1)-\log n
 =\log(1+1/n)\longrightarrow0.
\]

Continuity of the autocorrelation at zero implies

\[
 \lVert u_{n+1}-u_n\rVert^2
 =2\bigl(A(0)-A(\delta_n)\bigr)
 \longrightarrow0.
\]

If the source has one square-integrable derivative, then

\[
 A(0)-A(\delta)=O(\delta^2),
\]

so the collapse is at least quadratic in the logarithmic spacing.

Thus distinct arithmetic labels become arbitrarily close in the full
tail--seam state even though the seam has been retained.

## No diagonal two-sided frame inequality

Suppose positive diagonal weights `w_n` and constants `0<A_frame<=B_frame`
satisfied

\[
 A_{\rm frame}\sum_nw_n|c_n|^2
 \le\left\lVert\sum_nc_nu_n\right\rVert^2
 \le B_{\rm frame}\sum_nw_n|c_n|^2
\]

for every finite packet.

Apply the upper bound to the single atom `c=e_n`:

\[
 A(0)\le B_{\rm frame}w_n.
\]

Hence all `w_n` have one positive lower bound.

Now apply the lower bound to `c=e_{n+1}-e_n`:

\[
 A_{\rm frame}(w_n+w_{n+1})
 \le2\bigl(A(0)-A(\delta_n)\bigr)\longrightarrow0.
\]

The left side is bounded below by a positive constant, a contradiction.
Therefore

\[
 \boxed{
 \text{no positive diagonal arithmetic weight makes }\{u_n\}
 \text{a two-sided frame/Riesz sequence}.}
\]

This is a two-label finite falsifier visible at arbitrarily large `n`.

## Source amplitudes do not remove the obstruction

Suppose the physical atom is rescaled to `v_n=a_nu_n` with nonzero
source-derived amplitude `a_n`. If a diagonal frame inequality held for
`v_n`, the single-atom upper bound would control `w_n/|a_n|^2` from below.
Choosing coefficients

\[
 c_n=-1/a_n,
 \qquad
 c_{n+1}=1/a_{n+1}
\]

produces the same collapsing difference `u_(n+1)-u_n`, while its weighted
coefficient norm stays bounded below. The contradiction remains.

Hence scalar rescaling of continuously accumulating atoms cannot manufacture
a diagonal Riesz family.

## Effect of additional boundary rows

Adding primitive, square, or archimedean feature rows repairs the obstruction
only if at least one new row separates adjacent labels uniformly in its own
source norm. If every added feature depends continuously on `p=log n`, then
its adjacent difference also tends to zero and the same proof applies to the
augmented atom.

Therefore the required extra information must be genuinely label-discrete,
for example a prime-factorization, valuation, occurrence, or Fock port whose
distance does not vanish merely because `log(n+1)-log n` does.

This is a source-authority condition: one may not attach an orthogonal label
register solely to force a frame bound. The port must be generated and read by
the theta/Tate constructors.

## What remains possible

The synthesis family can still be complete, injective, or a continuous frame
after quotienting coefficient redundancy. What is impossible is treating all
arithmetic labels as a diagonally normed independent Riesz basis while their
physical atoms accumulate continuously.

The viable coefficient object may therefore be:

1. a quotient by the Gram-null completion;
2. a reproducing-kernel space with non-diagonal coefficient norm;
3. a discrete Fock/valuation module retaining an independent authorized label
   port alongside the tail--seam state;
4. a frame with redundant coefficients, where reconstruction uses a dual
   frame rather than a lower Riesz bound on coefficient sequences.

## Typed falsifier

```json
{
  "code": "log_label_adjacent_atoms_destroy_diagonal_riesz_bound",
  "labels": ["n", "n+1"],
  "log_spacing": "log(1+1/n) -> 0",
  "atom_difference_norm_squared": "2(A(0)-A(log(1+1/n))) -> 0",
  "single_atom_norm_squared": "A(0) > 0",
  "diagonal_weight_frame": false
}
```

## Honest frontier

The source-derived coefficient topology cannot be a diagonal Hilbert norm on
independent arithmetic labels if the readout retains only feature rows
continuous in logarithmic scale. The next constructive question is whether
the positive Fock/valuation grammar supplies an independently authorized
discrete port, or whether coefficient redundancy must be quotiented through
the full non-diagonal Gram kernel.

