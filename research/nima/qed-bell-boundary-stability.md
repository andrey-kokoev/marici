# Stability of the QED–Bell near-contact

The closed lower Bell boundary is

\[
r_B=\frac23(\sqrt2-1)=0.2761423749\ldots.
\]

For \(\alpha=1/137\), the one- and two-loop QED magnitudes are

\[
r_1=\frac3{11},
\qquad
r_2=\frac3{11}+\frac{130\alpha}{363\pi}
=0.2735593550\ldots.
\]

Thus

\[
r_B-r_2=0.00258301988\ldots>0.
\]

If a three-loop term is written as \(c_3\alpha^2\), reaching the boundary
would require

\[
\boxed{c_3=48.48070015\ldots.}
\]

Hence the near-contact is stable against the source's expected order-one
three-loop coefficient.  This is a conditional perturbative conclusion, not a
calculation of the unknown three-loop QED term.

## First higher-derivative sensitivity

At the transverse angle, write

\[
\Phi_1=\Phi_{1,0}(1+\epsilon\delta_1),
\qquad
\Phi_2=\Phi_{2,0}(1+\epsilon\delta_2),
\qquad
w=|\Phi_5/\Phi_1|^2.
\]

The exact lower Bell root becomes

\[
r_B(\epsilon,w)=
\frac23\left(\sqrt2-\sqrt{1-2w}\right)
\frac{1+\epsilon\delta_1}{1+\epsilon\delta_2}.
\]

Therefore

\[
r_B(\epsilon,w)=r_B+
\epsilon r_B(\delta_1-\delta_2)+\frac23w+cdots.
\]

Relative corrections to \(\Phi_1\) and \(\Phi_2\) are the first linear
sensitivity.  A newly generated mixed-helicity amplitude \(\Phi_5\) affects
the boundary only quadratically, and raises the required ratio.

This localizes the next coefficient calculation: derive the first
higher-derivative difference \(\delta_1-\delta_2\) from a source-normalized
photon amplitude.  Merely adding an unconstrained \(\Phi_5\) cannot explain the
QED–Bell proximity at first order.

Reproduce with:

```text
uv run --with sympy python research/nima/check_qed_bell_boundary_stability.py
```
