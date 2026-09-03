# Conductor-corona dominating-measure carrier

## Question

If multiplicative conductor energy is singular to the additive bulk measure, what is the minimal Hilbert carrier that contains both sectors without pretending one has a density in the other?

## Claim boundary

The sum measure gives a canonical direct-sum carrier. It includes the corona sector but supplies no completed-form action or bulk--corona coupling. Any nonzero cross term must be source-derived and nonlocal.

## Singular sectors

Let \(\mu_+\) be additive Haar measure and \(\mu_\times\) the multiplicative corona measure. Prior work establishes

\[
\mu_+
\perp
\mu_\times.
\]

Therefore no Radon--Nikodym density of \(\mu_\times\) with respect to \(\mu_+\) exists. A radial \(L^2(\mu_+)\) completion cannot contain the escaped unit energy as an ordinary bulk vector.

## Dominating measure

Define

\[
\nu=
\mu_++
\mu_\times.
\]

Both sectors are absolutely continuous with respect to \(\nu\). Mutual singularity gives measurable disjoint supports, modulo null sets, and hence the canonical decomposition

\[
L^2(\nu)
\cong
L^2(\mu_+)
\oplus
L^2(\mu_\times).
\]

The first summand is the additive bulk sector. The second is the conductor-corona boundary sector.

For

\[
f=f_+\oplus f_\times,
\]

the norm is

\[
\lVert f\rVert_{L^2(\nu)}^2
=
\lVert f_+\rVert_{L^2(\mu_+)}^2
+
\lVert f_\times\rVert_{L^2(\mu_\times)}^2.
\]

Thus escaped energy is retained rather than forced into a nonexistent bulk density.

## Form block structure

A completed quadratic form on the enlarged carrier would have block structure

\[
Q
=
\begin{pmatrix}
Q_{++}&C^*\\
C&Q_{\times\times}
\end{pmatrix}.
\]

A multiplication form with respect to \(\nu\) has

\[
C=0
\]

because the two supports are disjoint. Therefore any nonzero bulk--corona coupling cannot be inferred from measure domination alone. It must arise from a source-derived nonlocal operator, transport, or boundary trace.

If \(Q_{\times\times}\geq cI\) with \(c>0\), positivity again requires the Schur condition

\[
Q_{++}
-
C^*Q_{\times\times}^{-1}C
\geq0.
\]

The corona cannot be declared harmless merely because its norm is positive.

## Observer interpretation

Finite conductor observers see the bulk projection but lose a component whose norm survives in the corona. The higher observer is not another finite conductor limit in the same measure class. It is the direct-sum carrier formed after adjoining the singular boundary sector.

The inclusion maps are canonical:

\[
L^2(\mu_+)
\longrightarrow
L^2(\nu),
\qquad
L^2(\mu_\times)
\longrightarrow
L^2(\nu).
\]

The missing coherencer is the completed-form action relating these summands.

## SCC layer status

This construction can populate a layer such as `corona_boundary_carrier` with state `inhabited`. It cannot populate:

- `common_closed_form_domain`;
- `source_weil_comparison`;
- `semibounded_completed_form`;
- `rh_implication`.

Those require the domain and all three form blocks.

## Disposition

The corona boundary sector has a canonical minimal carrier, but no source-derived completed-form action on it is known. The next gate is to derive \(Q_{\times\times}\) and \(C\) from the order--Mellin or completed explicit formula and prove their closure and lower bounds. Without those maps, adjoining the corona records escaped energy but does not improve the RH positivity theorem.

## Verification

- `research/voevodsky/checkers/check_conductor_corona_dominating_measure.py`
- `research/voevodsky/results/conductor_corona_dominating_measure.json`
