# The identity wall residue and the causal seam history still live in different carriers

## What the existing wall theorem proves

The coefficient-valued multiplication-window history has a rank-one wall residue

\[
R_{\mathrm{coeff}}
=
|e_{\mathrm{wall}}\rangle
\langle e_{\mathrm{wall}}|.
\]

Under the quadratic multiplication representation,

\[
\Gamma_\pi(R_{\mathrm{coeff}})
=
I
\]

on the analytic \(q\)-state space. This fixes a unit identity residue for the multiplication-history Gram.

Therefore a coefficient-space wall normalization \(\lambda=1\) is available in that represented carrier.

## What it does not prove

The causal seam operator used in the shifted-history square is

\[
(H_+c)(t)
=
\int_0^\infty\Phi(r)c(t+r)\,dr
\]

on a translation-packet or seam-history carrier.

The multiplication-window history is instead

\[
(\mathcal H_p\psi)(t,q)
=
W_t(q)\psi(q)
\]

on analytic \(q\)-states.

These are different operators on different source objects. The identity residue of \(\mathcal H_p^{*}\mathcal H_p\) does not automatically supply the identity term in

\[
\frac12(I+H_+^{*}H_+).
\]

Thus the present wall theorem fixes \(\lambda=1\) only after multiplication representation, not yet in the causal seam auxiliary block.

## Missing comparison arrow

A source-authorized map must intertwine the two histories:

\[
J_{\mathrm{hist}}:
\text{coefficient-valued window history}
\longrightarrow
\text{causal seam history}.
\]

At the quadratic level it must compare:

\[
\Gamma_\pi(G_{\mathrm{window}})
\quad\text{with}\quad
I+H_+^{*}H_+.
\]

The comparison may be:

- unitary, transporting the unit wall exactly;
- uniformly bi-bounded, changing the absolute frame by controlled constants;
- a quotient, in which case wall mass may be lost;
- or nonexistent.

Scalar agreement of endpoint histories is insufficient.

## Required normalization diagram

The desired square is:

\[
\begin{array}{ccc}
R_{\mathrm{wall}}^{\mathrm{coeff}}+G_{\mathrm{window}}^{\mathrm{coeff}}
&\xrightarrow{\text{quadratic representation}}&
I+\Gamma_\pi(G_{\mathrm{window}})\\
\downarrow J_{\mathrm{hist}}&&
\downarrow \widetilde J_{\mathrm{hist}}\\
R_{\mathrm{wall}}^{\mathrm{seam}}+G_{\mathrm{seam}}
&\xrightarrow{\text{history realization}}&
I+H_+^{*}H_+
\end{array}
\]

with the actual source coefficients retained. Only a commuting or source-comparison cell authorizes transferring \(\lambda=1\).

## Consequence for the square law

The exact shifted-history square

\[
D_\pm
=
\frac12(I\pm iH_+)^{*}(I\pm iH_+)
\]

requires three terms in one carrier:

- identity wall \(I\);
- seam Gram \(H_+^{*}H_+\);
- odd history \(i(H_+-H_+^{*})\).

At present, the latter two are causal-history objects, while the established identity residue is a multiplication-window object. The square is algebraically canonical but source-heterogeneous.

## Minimal hostile

Construct two histories with identical scalar endpoint windows:

- the multiplication history has wall residue \(I\);
- the causal seam history has no retained wall coordinate.

All scalar Stokes and theta-mass tests agree, yet adjoining the multiplication identity to the seam Gram invents a new direct-sum channel.

A second hostile uses a nonunitary comparison that sends the wall vector to \(r_pI\) with \(r_p\to0\). Finite square laws exist after retyping, while the completed absolute frame collapses.

## Revised first obligation

Before extracting \((\lambda_p,\mu_p,\alpha_p)\), construct and classify the history-comparison arrow. The exact order is:

\[
\text{window-history wall theorem}
\longrightarrow
\text{window/seam comparison}
\longrightarrow
\text{common auxiliary carrier}
\longrightarrow
\text{coefficient extraction}
\longrightarrow
\text{weighted square law}.
\]

This restores the constructor-coherence principle locally: valid terms cannot be combined into one positive square until they are shown to inhabit one authorized system.
