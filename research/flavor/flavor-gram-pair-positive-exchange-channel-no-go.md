# Positive exchange channels on the Gram pair are trivial or phenomenologically wrong: WP949

## Question

Can a positive conditional expectation acting directly on the faithful left-handed Gram pair provide the source-derived proper noncommutative selector missing after WP948?

## Correct quotient carrier

Use

\[
(H_u,H_d),
\qquad
H_f=Y_fY_f^\dagger.
\]

Under the full weak-basis groupoid the right-handed frames cancel and the pair transforms by simultaneous conjugation:

\[
(H_u,H_d)\longmapsto
(U_QH_uU_Q^\dagger,U_QH_dU_Q^\dagger).
\]

Consider the strongest canonical two-sector channel that introduces no matrix direction: a real stochastic mixing

\[
\mathcal E_K(H_u,H_d)
=
(aH_u+bH_d,bH_u+aH_d),
\qquad
K=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]

Nonnegative coefficients give positivity, `a+b=1` gives unitality, and the displayed form is equivariant under sector exchange and weak-basis conjugation.

## Exact classification

Idempotence requires `K^2=K`. Together with positivity and unitality, the only solutions are

\[
(a,b)=(1,0)
\]

and

\[
(a,b)=\left(\frac12,\frac12\right).
\]

The first is the identity and selects nothing. The second is sector averaging:

\[
(H_u,H_d)
\longmapsto
\left(\frac{H_u+H_d}{2},\frac{H_u+H_d}{2}\right).
\]

Its image is a proper noncommutative copy of the positive matrix cone, but both output Grams are equal. Their commutator vanishes, their spectra coincide, and the CKM distinction is erased.

## Exact hostile pair

For

\[
H_u=\operatorname{diag}(1,2,4),
\qquad
H_d=\begin{pmatrix}2&1&i\\1&3&1\\-i&1&5\end{pmatrix},
\]

both inputs are positive and

\[
\operatorname{Tr}[H_u,H_d]^3=-36i.
\]

Sector averaging maps them to one positive matrix in both slots and sends the invariant to zero. It is therefore a genuine quotient-descending positive selector, but selects an experimentally wrong equal-Gram locus.

## Source and instrument boundary

Even this wrong selector is only conditional. Exact up/down exchange is not a declared Standard Model flavor symmetry: the two sectors carry different right-handed gauge representations and different measured spectra. Adding it as an authority would change the source domain rather than derive a selector from the admitted source.

The channel has a formal randomization realization—choose identity or sector swap with equal probability—but no admitted physical operation swaps the full up and down Gram sectors while preserving their gauge typing. Formal stochastic compilation is not a calibrated flavor instrument.

## Disposition

Within positive unital exchange-equivariant idempotents on the faithful Gram pair, the only choices are no selection and phenomenologically wrong equalization. A viable source operation must act asymmetrically on the two correctly typed sectors while remaining full weak-basis covariant. Its asymmetry must arise from declared dynamics or geometry, not measured mass differences. No physical time or causal order is assigned to channel composition.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp949_gram_pair_positive_exchange_channel_no_go.py

Generated result: `research/flavor/results/wp949_gram_pair_positive_exchange_channel_no_go.json`.
