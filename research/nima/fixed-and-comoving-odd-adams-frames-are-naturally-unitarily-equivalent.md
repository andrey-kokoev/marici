# Fixed and comoving odd Adams frames are naturally unitarily equivalent

## Two presentations

The odd auxiliary Adams sector has two source presentations.

### Fixed frame

At every grade \(k\), use the same local phase fiber

\[
F_k^{\mathrm{fix}}=F_0
\]

and let Adams relabel only the external grade.

### Comoving frame

Choose a scale \(a_k\in\mathbb Q_p^\times\) at grade \(k\) and set

\[
F_k^{\mathrm{mov}}
=
\mathcal D_{a_k}F_0.
\]

For an arrow \(k\to rk\), define the relative dilation

\[
a_{r;k}=a_{rk}a_k^{-1}.
\]

Then

\[
a_{s;rk}a_{r;k}=a_{sr;k}.
\]

## Natural comparison

Define

\[
\Theta_k
=
\mathcal D_{a_k}:
F_k^{\mathrm{fix}}
\longrightarrow
F_k^{\mathrm{mov}}.
\]

Let \(A_{r;k}^{\mathrm{fix}}\) be external grade relabelling with the phase vector unchanged. Let \(A_{r;k}^{\mathrm{mov}}\) use the relative local dilation \(\mathcal D_{a_{r;k}}\).

Then

\[
A_{r;k}^{\mathrm{mov}}\Theta_k
=
\Theta_{rk}A_{r;k}^{\mathrm{fix}}.
\]

Indeed,

\[
\mathcal D_{a_{r;k}}\mathcal D_{a_k}
=
\mathcal D_{a_{rk}}.
\]

Therefore \(\Theta\) is a natural isomorphism between the fixed and comoving odd Adams functors.

## Unitary equivalence

Every \(\mathcal D_{a_k}\) is unitary on the local additive Hilbert space. Hence

\[
\Theta_k^*\Theta_k=I
\]

and the natural comparison has condition number one at every grade and constructor depth.

No completion amplification arises from changing between the two frames.

This is stronger than mere algebraic naturality: coherent composites are isometrically identified.

## Weyl phase preservation

The comoving frame transports

\[
(\eta,B,h)
\mapsto
(a_k\eta,a_k^{-1}B,h/a_k).
\]

Therefore

\[
(a_k\eta)(h/a_k)=\eta h.
\]

The parity-conversion coefficient

\[
2\sin(\arg\psi_p(\eta h))
\]

is invariant under \(\Theta_k\).

Thus the fixed and comoving presentations carry the same odd orientation and the same primewise observer softness.

## Scalar Tate shadow

For any local test function \(f\),

\[
Z_p(\mathcal D_af,s)
=
|a|_p^{1/2-s}Z_p(f,s).
\]

The factor is entire and nowhere zero as a function of \(s\).

For the antisymmetric odd port,

\[
Z_p(f^{\mathrm{odd}},s)=0,
\]

so

\[
Z_p(\mathcal D_af^{\mathrm{odd}},s)=0.
\]

Hence the natural frame change preserves scalar invisibility exactly and imports no divisor.

## Fourier compatibility

The local Fourier relation

\[
\mathcal F_p\mathcal D_a
=
\mathcal D_{a^{-1}}\mathcal F_p
\]

shows that reciprocal Fourier transport sends the natural comparison to its inverse-scale counterpart.

Thus the positive and reciprocal charts have compatible natural transformations:

\[
\Theta_k^+
=
\mathcal D_{a_k},
\qquad
\Theta_k^-
=
\mathcal D_{a_k^{-1}}.
\]

No extra phase cocycle appears.

## Consequence for the source decision

Whether the odd port is described as a fixed observer or as a comoving state is a presentation choice, provided:

1. the grade scales \(a_k\) are source-derived;
2. the relative scale law holds;
3. all incidence and observation maps are transported by \(\Theta_k\);
4. reciprocal Fourier charts use inverse scales.

Under these conditions the two constructions are naturally unitarily equivalent.

The choice becomes substantive only if an operation is transported in one frame but not conjugated into the other.

## Grade-six comparison

Every path to grade six has the same natural comparison

\[
\Theta_6=\mathcal D_{a_6}.
\]

Therefore the fixed/comoving frame choice adds no grade-six holonomy and no pentagon obstruction. Coherence is inherited from multiplication of the scale factors.

## What remains open

This natural equivalence closes only the phase-frame presentation issue. It does not provide:

- the mixed theta wall–odd boundary return;
- a uniform Hilbert lower margin;
- the full primitive–square–connected type functor;
- endpoint or archimedean attachment;
- spectral identification with \(\Xi\).

## Hostiles

1. Compare fixed and comoving frames without conjugating observers.
2. use \(a_{rk}\) unrelated to \(a_{r;k}a_k\).
3. transport the positive Fourier chart but not the reciprocal inverse-scale chart.
4. treat the nowhere-zero Tate dilation factor as a new determinant divisor.
5. infer full RH constructor coherence from the odd subfunctor equivalence.

## Verdict

The fixed-observer and comoving-state realizations of the odd Adams phase fiber are naturally unitarily equivalent.

Their distinction is gauge-like at the typed source level, not a new obstruction. The remaining odd-sector problem is the actual mixed boundary return and its Green compatibility.
