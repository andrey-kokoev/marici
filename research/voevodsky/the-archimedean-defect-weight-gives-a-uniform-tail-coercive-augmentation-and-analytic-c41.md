# The archimedean defect weight gives a uniform tail-coercive augmentation and analytic C41

## Question

Is there a source-derived bulk weight, uniform across semilocal blocks, that repairs four-port observability without inserting the identity observer by hand?

## Claim boundary — corrected after interface audit

The exact archimedean matrix coefficient supplies a canonical defect weight with a block-independent tail margin on the doubled radial \(H^1\) model. It repairs observability of a radial field from its derivative, endpoint, and bulk value. It does **not** prove bounded recovery of the labelled semilocal source through the four-port synthesis. The required common graph domain connecting those carriers is explicitly missing in prior research, and the known Euler-weighted interface has zero Hilbert lower margin.

## Source-derived weight

Prior research derives the normalized archimedean matrix coefficient

$$
\Phi_\infty(r)=(\cosh r)^{-1/2}.
$$

Its canonical contraction-defect multiplier is

$$
w_\infty(r)
=\sqrt{1-|\Phi_\infty(r)|^2}
=\sqrt{1-\operatorname{sech}r}.
$$

This weight is real, bounded by one, and depends on neither the prime nor the grade. Use the same multiplier on the two radial orientations:

$$
D_{w_\infty}^+
=\operatorname{diag}(M_{w_\infty},M_{w_\infty}).
$$

The diagonal multiplier classification shows that it preserves reciprocal and Real structure.

## Uniform tail margin

For every chosen \(R>0\) and every \(r\ge R\), monotonicity of \(\operatorname{sech}\) gives

$$
w_\infty(r)
\ge
c_R:=\sqrt{1-\operatorname{sech}R}>0.
$$

Both \(R\) and \(c_R\) are independent of all semilocal block labels. Therefore the half-line estimate applies with one global constant

$$
M_R
=
\max\left\{2R,R^2+1,(1-\operatorname{sech}R)^{-1}\right\}.
$$

For each radial graph component,

$$
\|f\|_{H^1}^2
\le
M_R\left(
\|f'\|_2^2+|f(0)|^2+\|w_\infty f\|_2^2
\right).
$$

Summing over the semilocal Hilbert direct sum preserves the same constant \(M_R\).

## Radial-model augmentation

Define the explicit graph augmentation

$$
\widetilde q_4
=
(q_4,\partial,\operatorname{tr}_0,D_{w_\infty}^+).
$$

The retained radial Green ladder supplies the derivative and endpoint maps, while the defect channel supplies the missing tail margin. The displayed half-line estimate proves that \(\widetilde q_4\) is bounded below **as an observer of a radial \(H^1\) field**.

This estimate cannot presently be pulled back to the labelled source. The known synthesis

$$
U_4:\mathcal A_{\exp}\longrightarrow\mathcal G_4
$$

has Euler-weighted columns and zero lower margin on the labelled Hilbert module \(\mathcal H_0\). Prior research explicitly marks as missing a common graph domain \(D\) on which the labelled source, doubled derivative, all four traces, and tail channels are simultaneously continuous. Consequently, bounded \(\widetilde R_{43}\) and \(\widetilde C_{41}\) do not follow from the radial estimate alone.

For the smaller candidate

$$
q_4^{\mathrm{def}}=(q_4,D_{w_\infty}^+),
$$

the same conclusion would require a separately proved estimate showing that the `q_4` norm controls \(\|h'\|_2^2+|h(0)|^2\). No such estimate was found.

## Noncircularity boundary

The added channel is not \(h\mapsto h\). It is the defect of the independently source-derived archimedean cyclic matrix coefficient. Its tail coercivity is an explicit consequence of \(\Phi_\infty(r)=(\cosh r)^{-1/2}\), not a fitted lower bound.

## Disposition

The archimedean defect channel gives a uniform, symmetry-compatible observability repair on the doubled radial graph model. No analytic \(C_{41}\) from the semilocal labelled source is constructed: the common labelled-to-radial graph domain and a lower estimate overcoming the Euler-weighted zero margin remain absent. The unaugmented, defect-only, and graph-augmented semilocal \(C_{41}\) claims are all unpromoted.