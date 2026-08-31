# The outgoing half-density trace must be subtracted before prime summation

> **Withdrawn as a claim about the completed joint column.** The successor
> packet
> `correction-the-centered-joint-cut-column-has-a-bounded-common-mode-not-an-unbounded-outgoing-wall-column.md`
> shows that the growth calculation isolates the uncentered seam component and
> omits the joint tail channel, translated conjugator, wall port, and reciprocal
> pairing. It remains a falsifier for that incomplete realization only.

## Raw twisted history

For the completed theta forcing \(\Phi\), define

\[
(H_-\Phi)(t)
=
e^{t/2}
\int_{-\infty}^{t}e^{-v/2}\Phi(v)\,dv
\]

and its outgoing moment

\[
M_-
=
\int_{\mathbb R}e^{-v/2}\Phi(v)\,dv.
\]

Then

\[
e^{-t/2}H_-\Phi(t)\longrightarrow M_-
\]

as \(t\to+\infty\). The raw history therefore has an exponential outgoing
component \(M_-e^{t/2}\).

## Pairing with a moved seam atom

The seam component of the cut atom at scale \(a\) is

\[
h_a(t)=\mathbf1_{0\le t\le a}\Phi(a-t).
\]

Its raw pairing with the twisted history is

\[
I_a
=
\int_0^a
\Phi(a-t)H_-\Phi(t)\,dt.
\]

With \(r=a-t\),

\[
e^{-a/2}I_a
=
\int_0^a
\Phi(r)e^{-r/2}
\left(
\int_{-\infty}^{a-r}e^{-v/2}\Phi(v)\,dv
\right)dr.
\]

Rapid decay permits dominated convergence, giving

\[
e^{-a/2}I_a
\longrightarrow
M_-C_-,
\qquad
C_-=
\int_0^\infty e^{-r/2}\Phi(r)\,dr.
\]

For the positive completed theta profile, \(M_-C_->0\). Hence

\[
I_a\sim M_-C_-e^{a/2}.
\]

## Arithmetic consequence

At the primitive scale \(a=\log p\), the Euler-loaded column is

\[
b_p=p^{-1/2}u_{\log p}.
\]

The growth \(e^{a/2}=p^{1/2}\) exactly cancels the arithmetic half-density.
Thus the raw pairing satisfies

\[
\langle b_p,H_-\Phi\rangle
\longrightarrow M_-C_-
\]

up to the fixed source orientation and the non-dominant tail component.
The source-adjoint coordinate is then asymptotic to

\[
(B_\Sigma^\dagger H_-\Phi)_p
\sim
\frac{M_-C_-}{\log p}.
\]

Its source norm diverges:

\[
\sum_p(\log p)
\left|
(B_\Sigma^\dagger H_-\Phi)_p
\right|^2
\asymp
\sum_p\frac1{\log p}
=
\infty.
\]

Therefore the raw outgoing twisted history cannot be inserted into the mixed
all-prime Schur block.

## Relative subtraction

The source trace determines the renormalized relative representative

\[
\widetilde H_-\Phi(t)
=
H_-\Phi(t)-M_-e^{t/2}
=
-e^{t/2}
\int_t^\infty e^{-v/2}\Phi(v)\,dv.
\]

This representative has zero outgoing half-density trace and decays rapidly
for the theta profile. Pairings

\[
\langle u_{\log p},\widetilde H_-\Phi\rangle
\]

are therefore uniformly bounded and in fact decay with \(p\). The criterion

\[
B_\Sigma^\dagger\widetilde H_-\Phi\in U
\]

then follows from

\[
\sum_p\frac1{p\log p}<\infty.
\]

## Reciprocal channel

The \(H_+\) channel requires the reciprocal subtraction at its own outgoing
end. Reflection exchanges the two trace subtractions. Performing only one
would break reciprocal covariance.

## Constructor implication

The mixed G4 Weyl block must be formed on relative history classes after the
explicit outgoing half-density traces have been removed. The subtraction is
not a freely chosen regularization: its coefficient is the source moment
\(M_\pm\), already fixed by the Wronskian trace.

The removed trace remains in the separate wall/determinant-line coordinate;
it must not be discarded or counted again in the relative return.

## Disposition

The uniform mixed-pairing gate closes for the zero-trace relative
representatives, subject to the declared wall-extended pairing continuity. It
fails for the raw twisted causal histories. The scalar seam construction must
therefore separate outgoing trace lines before prime summation. Full
rigged-state reconstruction and the dressed-scalar/Xi identity remain open.
No RH conclusion is authorized.
