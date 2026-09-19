# The ordered port enters Evans promotion through the source codiagonal and Xi divisibility

## Correction to componentwise promotion

The completed Green return has five retained residual ports:

\[
R_{\mathrm{sat}}(z)
=
\bigl(
 r^{(0)},r^{(1)},r^{(\mathrm{wall})},
 r^{(\mathrm{recip})},r^{(\mathrm{link})}
\bigr)(z).
\]

The ordered Fourier--Tate current belongs to the reciprocal/linking part of
this packet. Promotion does not require every component to vanish separately.
Indeed, prior asymptotics prove that the ordinary tail component is nonzero
for every parameter, including every Xi zero:

\[
r^{(0)}(z)\ne0.
\]

Therefore the unchanged Evans state can never be a kernel vector of a
faithful direct-sum five-port residual.

## Source codiagonal

The lower arithmetic equation uses the adjoint of the joint source incidence,
not the faithful observation of all five outputs. Let

\[
C:
U^{(0)}\oplus U^{(1)}\oplus U^{(\mathrm{wall})}
\oplus U^{(\mathrm{recip})}\oplus U^{(\mathrm{link})}
\longrightarrow U_{\mathrm{ar}}
\]

be the source-weighted codiagonal with the fixed Green metric, reciprocal
signs, and wall/Wronskian normalization. Define

\[
r_U(z)=C R_{\mathrm{sat}}(z).
\]

Equivalently, `r_U` is the complete centered Green-incidence adjoint applied
to the split Evans history. The codiagonal is intentionally nonfaithful on
the saturated output: cancellation may occur in `ker C` without erasing the
ports from the retained graph.

The ordered port therefore contributes one fixed summand to `r_U`; it is not
a scalar counterterm and is not required to vanish on its own.

## Holomorphic divisibility

The split stable-history section is entire in its wall graph, and the complete
Green adjoint is bounded there. Hence

\[
r_U:\mathbb C\longrightarrow U_{\mathrm{ar}}
\]

is an entire vector-valued section.

Let the Xi/Evans section be `tau`. Exact chain promotion with multiplicity is
equivalent to

\[
r_U(z)=\tau(z)h_U(z)
\]

for an entire `U_ar`-valued section `h_U`. At a zero `z_0` of order `m`, this
is equivalent to

\[
r_U^{(j)}(z_0)=0,
\qquad 0\le j<m.
\]

Thus the precise remaining theorem is

\[
r_U\in\tau\,\mathcal O(U_{\mathrm{ar}}),
\]

not componentwise five-port cancellation and not an ordinary Fredholm
identity.

## Ordered-current test

Because the ordered coordinate is cutoff-independent and Fourier-natural on
the retained graph, its contribution to every residual jet is well-defined.
A valid proof of divisibility must nevertheless exhibit cancellation against
the eventually sign-definite ordinary tail through the already fixed source
codiagonal. The Evans seam mismatch alone cannot produce this vector identity.

For each consecutive prime shell and every required jet, one must verify the
sum of all five normalized contributions before prime codiagonalization. A
scalar aggregate or a ratio fitted at Xi zeros is inadmissible.

## Current disposition

The carrier, ordered transport, endpoint packet, source codiagonal type, and
holomorphic division criterion are constructed. The unresolved content is the
residual-jet identity itself. Existing work proves neither its vanishing nor
an impossibility after the source codiagonal; it proves only that faithful
componentwise promotion is impossible.
