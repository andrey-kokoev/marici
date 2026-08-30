# Boundary charge and comoving window residual require opposite reflection channels

## Exact parity audit

Let reciprocal reflection be
\[
(Rf)(q)=f(-q).
\]

The canonical jump potential is
\[
O(q)=\operatorname{sgn}(q),
\]
so
\[
RO=-O.
\]
Its derivative incidence is even:
\[
DO=2\delta_0,
\qquad
R(DO)=DO.
\]

By contrast, every comoving endpoint window
\[
W_t(q)=H(q+t)-H(q-t)
\]
is even:
\[
RW_t=W_t.
\]
Its derivative incidence is odd:
\[
R(DW_t)=-DW_t.
\]

The ordered port anticommutes with reflection,
\[
RSR=-S,
\]
and returns
\[
S(DO)=-2O,
\qquad
S(DW_t)=-2W_t.
\]

Thus the two source pieces have opposite character profiles:

\[
\begin{array}{c|cc}
&\text{incidence}&\text{ordered return}\\
\hline
\text{boundary charge}&\text{even}&\text{odd}\\
\text{window residual}&\text{odd}&\text{even}
\end{array}
\]

## Correction to rank-three language

The phrase “odd zero-charge residual” is ambiguous and can be wrong depending on whether “odd” refers to the incidence or the ordered return.

The canonical charge representative \(O\) is odd as a potential but has even derivative incidence. The natural zero-charge window \(W_t\) is even as a potential but has odd derivative incidence.

Therefore they cannot be added inside one reflection-homogeneous scalar potential without losing typing:
\[
\chi O+W_t
\]
has no definite reciprocal character.

The minimum faithful constructor is a graded two-channel bundle:
\[
\mathcal J_{\mathrm{charge}}^{-}
\oplus
\mathcal J_{\mathrm{window}}^{+},
\]
or, at the incidence level,
\[
D\mathcal J_{\mathrm{charge}}^{-}
\oplus
D\mathcal J_{\mathrm{window}}^{+}
=
\mathcal I_{\mathrm{charge}}^{+}
\oplus
\mathcal I_{\mathrm{window}}^{-}.
\]

Together with the even overlap coordinate, this yields three scalar coordinates but not one ungraded rank-three scalar space.

## Consequence for the Adams edge

The reciprocal seam orientation is carried by the odd jump return \(O\). The comoving windows supply even endpoint energy and a separately odd derivative incidence. Their coupling can generate an oriented mixed form, but only through a typed cross-pairing between the two reflection sectors.

This matches the earlier Wronskian no-go:
\[
\mathcal W(W_L,W_{2L})=0.
\]
Both windows are even. A nonzero Wronskian orientation requires one independently odd feature, supplied naturally at the incidence level by \(DW_t\) or at the return level by \(O\), with the source formula deciding which pairing is authorized.

## Canonical zero-charge residual candidate

For each \(t\),
\[
\partial_\infty W_t=0.
\]
Hence \(W_t\) is eligible for exact inverse-derivative localization:
\[
S(DW_t)=-2W_t.
\]

Differences such as
\[
W_{2L}-W_L
\]
remain even, zero-charge, prime-labelled, and cutoff-natural. Their derivative histories remain odd and localized.

This does not yet prove that the arithmetic odd incidence equals \(D(W_{2L}-W_L)\), but it identifies an existing source-native candidate with the correct zero-charge and scale labels.

## Hostile

Treating
\[
\chi O+(W_{2L}-W_L)
\]
as one reciprocal-odd potential silently mixes reflection characters. Scalar endpoint or norm readout may hide the defect, but the typed constructor is invalid.

## Revised frontier

The first Adams edge should now seek a cross-character Green/Stokes identity:
\[
\text{even charge incidence }(\chi_p\delta_0)
\quad\leftrightarrow\quad
\text{odd window incidence }D(W_{2L}-W_L),
\]
or the adjoint orientation fixed by the source.

The source must keep the two channels separate through pushforward and only combine them through an authorized polarized pairing.
