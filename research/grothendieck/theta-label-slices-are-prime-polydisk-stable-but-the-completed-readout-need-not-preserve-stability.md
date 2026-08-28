# Theta-Label Slices Are Prime-Polydisk Stable, but the Completed Readout Need Not Preserve Stability

## The actual labelled source cell

Write the positive theta summands on the positive chamber as

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

For the standard completed theta kernel, with `x=pi exp(2u)`, their exact
ratio to the vacuum label is

\[
\frac{\phi_n(u)}{\phi_1(u)}
=n^2\frac{2n^2x-3}{2x-3}\exp(-(n^2-1)x).
\]

For `u>=0`, one has `x>=pi>3`. Hence

\[
0<\frac{\phi_n(u)}{\phi_1(u)}
<2n^4\exp(-3(n^2-1))
<\frac{2n^4}{2^{3(n^2-1)}}.
\]

The majorant sums to less than `1/15` for `n>=2`. Therefore

\[
\sum_{n\ge2}\phi_n(u)<\frac1{15}\phi_1(u).
\]

## Full pointwise prime-polydisk theorem

Introduce one variable for each prime and the valuation monomial

\[
w^{v(n)}=\prod_p w_p^{v_p(n)}.
\]

At fixed `u>=0`, define

\[
\Theta_u(w)=\sum_{n\ge1}\phi_n(u)w^{v(n)}.
\]

If every `|w_p|<=1`, then

\[
|\Theta_u(w)|
\ge \phi_1(u)-\sum_{n\ge2}\phi_n(u)
>\frac{14}{15}\phi_1(u)>0.
\]

Thus every positive-chamber theta-label slice is uniformly zero-free on the
closed prime polydisk. This includes every finite two-prime coefficient cell.
No mixed-prime determinant audit is needed at the pointwise source level.

## The interaction determinant still has meaning

For two primes `p,q`, evaluation at fixed `u` gives

\[
\Delta_{p,q}(u)
=\phi_1(u)\phi_{pq}(u)-\phi_p(u)\phi_q(u).
\]

The prime weights cancel from its normalized ratio. If `L=log(phi_1)`, then

\[
\log\frac{\phi_1(u)\phi_1(u+\log p+\log q)}
{\phi_1(u+\log p)\phi_1(u+\log q)}
=\int_0^{\log p}\int_0^{\log q}L''(u+r+s)\,ds\,dr.
\]

Here

\[
L''(u)=-4x-\frac{24x}{(2x-3)^2}<0.
\]

Hence `Delta_{p,q}(u)<0`. The source square commutes exactly before scalar
evaluation, while the evaluation sees a strictly log-concave interaction.
The determinant therefore measures failure of the scalar readout to preserve
tensor products, not failure of coprime source interchange.

## Why this does not prove RH

The Riemann spectral parameter is not obtained by simply evaluating a fixed
`u` slice on the diagonal `w_p=p^{-z}`. It appears after transporting label
shifts through the completed Mellin/Fourier readout and sewing the moving
boundary. That readout aggregates different `u` slices with oscillatory
phases.

Stability is not preserved by an arbitrary oscillatory linear aggregation.
The elementary witness is

\[
P_+(w)=1+w,
\qquad P_-(w)=1-w.
\]

Both are zero-free in the open unit disk, but the phase-weighted combination
`P_+-P_-=2w` vanishes at the origin.

Therefore the source-slice theorem relocates rather than solves the RH
problem. The missing theorem is that the specific completed theta readout is
a stability-preserving operator on the source-authorized labelled class.

## The next categorical object

A linear stability preserver is controlled not merely by its values but by
its operator symbol: the object retaining how the readout acts on source
variables and their comparison variables simultaneously. In the current
language, this is the next comparison tower between:

- the incoming prime-labelled stable slice;
- the outgoing scalar spectral section;
- the moving-seam control channel.

The seam current is part of that symbol. Dropping it before testing stability
would test the wrong operator.

## Falsifier

Construct the finite-cutoff symbol of the completed theta readout, including
the moving endpoint. The route fails at the first cutoff where that symbol is
not stable, or where two stable labelled inputs are mapped to a scalar section
with an off-seam zero. Pointwise source stability alone is no longer admissible
evidence for RH.
