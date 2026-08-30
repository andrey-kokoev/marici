# Charged-cycle low-energy matching

## Bounded question

Can WP635's cycle be transported past WP637's heavy-transition support fiber
by integrating out the messenger stages and retaining a low-energy charged
operator?

## Two complete messenger paths

Use external fields \(Q_L,\widetilde H^u,\chi,S,X,d_R\). There are two
tree-level paths through the heavy messenger graph.

The first crosses at the \(A\) stage:

\[
Q_L\to A^u\to A^d\to B^d\to d_R.
\]

The second crosses at the \(B\) stage:

\[
Q_L\to A^u\to B^u\to B^d\to d_R.
\]

After exact zero-momentum tree elimination, their scalar coefficients are

\[
L_A={Y_H^uY_X^dC_AY_S^d\over
M_{A^u}M_{A^d}M_{B^d}},
\qquad
L_B={Y_H^uY_X^dY_S^uC_B\over
M_{A^u}M_{B^u}M_{B^d}}.
\]

All common endpoint factors cancel in the ratio, giving

\[
{L_B\over L_A}=\mathcal I_\chi.
\]

Both paths contain three heavy propagators and multiply the same canonical
dimension-seven operator

\[
\bar Q_L\widetilde H^u\chi SXd_R.
\]

Its total hypercharge is zero. After the connector and adjoint acquire their
declared vacuum values, it becomes an effective charged-scalar quark portal.

## Exact phase response

At unit magnitudes, the matched coefficient squared is four for
\(\mathcal I_\chi=1\) and zero for \(\mathcal I_\chi=-1\). The distinction is
unchanged by a common endpoint rephasing and does not require an on-shell heavy
messenger decay. Thus WP637's particular support obstruction is bypassed by a
source-derived off-shell messenger operation.

## Remaining physical gates

This is a matched low-energy probe, not a selector. The invariant remains a
free coupling coordinate, and the overall coefficient depends on three heavy
masses. The operation also lies outside the Standard Model `physical16`
coordinate: it adds a charged-scalar portal rather than selecting the quark
Yukawa point.

A physical instrument now requires a charge-preserving \(\chi\) pole, an open
production or decay route involving its quark portal, finite-width and QCD
transport, competing branching fractions, detector acceptance, and a
likelihood in the same normalization. If \(\chi\) is itself inaccessible, it
must be integrated out and the resulting loop or contact response audited.

## Reproduction

Run:

    python research/flavor/checkers/wp638_charged_cycle_low_energy_matching.py

The generated result is
`research/flavor/results/wp638_charged_cycle_low_energy_matching.json`.

