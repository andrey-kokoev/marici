# Invariant complex-pole packet

Work package: WP534  
Owner: marici.Figueiredo

## Question

Can the exact WP533 channel support, WP517 partial widths, WP509/WP518
current residues, WP520 signed \(b\!-\!s\) kernel and WP525 Ward completion be
placed in one common pole ordering on the WP527 source witness?

## Admitted domain

The domain is the frozen WP516 existence witness embedded in WP527's
common-source completion. WP527 closes every declared nonquark two-body pair.
WP533 proves that the 34 WP517 rows are the complete threshold-open vector
support. Conclusions are restricted to the declared tree-level channel
grammar. Higher-order and radiative widths are not silently included.

## Invariant vector-width groups

The twenty coordinate rows with two quintet daughters are replaced by two
complete \(Q\wedge Q\) sums, one for each heavy parent. The other fourteen
rows have nondegenerate daughters and remain simple-pair groups. The reduction
is from 34 coordinate rows to 16 invariant width groups.

The sixteen group widths reproduce every WP517 parent sum. After adding the
independently normalized quark widths, the former WP518 lower bounds become
channel-complete declared tree widths on the WP527 domain.

This promotion is domain- and order-relative. It is not a claim that unknown
radiative corrections or an enlarged source grammar vanish.

## Projector and simple poles

The five degenerate mass-six coordinates are represented as one
projector-valued pole:

\[
R_Q=2P_Q,\qquad
\mu_Q^2=6-iM_Q\Gamma_Q,
\qquad
\Gamma_Q=\frac{\sqrt6}{2\pi}\,\mathrm{GeV}.
\]

The remaining nine cubic poles are simple. For every state the packet records
the mass, flavor-current trace residue, quark width, invariant vector width,
declared tree width and

\[
\mu_i^2=M_i^2-iM_i\Gamma_i^{\mathrm{tree}}.
\]

## Signed flavor-current residues

Positive trace residues do not determine the aligned \(b\!-\!s\) kernel.
WP520's exact rational function has six poles, in cubic sectors zero and one.
WP534 computes the signed residues by

\[
r_i=\frac{N(m_i^2)}{D'(m_i^2)}.
\]

The two light residues are approximately opposite and of magnitude \(0.248\),
while their pole squares differ by only \(2.5\times10^{-9}\)
\(\mathrm{GeV}^2\). Ordinary binary-float partial fractions lose the
cancellation. With 100-digit roots and 90-digit residues,

\[
\sum_i\frac{r_i}{-m_i^2}
=\frac1{19365120000}
\]

with zero residual at the working precision.

This is a concrete hostile precision gate: signed residues must remain
high-precision paired data rather than independent rounded table entries.

## Ward-complete insertion

For each of the six signed poles, the identical complex \(\mu_i^2\) must occur
in the transverse denominator, longitudinal normalization, unphysical
\(R_\xi\) denominator and Goldstone term. The checker rederives the exact
\(\xi\)-independent sum. A vector-only width insertion remains prohibited by
WP525.

## Classification and remaining instrument

WP534 is a channel-complete declared tree-width and signed-residue
complex-pole packet on one source witness. It is a rigidifier, not a selector.

The smallest falsifier is an omitted open declared tree channel, failure of an
invariant group to reproduce its WP517 parent sum, loss of the WP520
zero-momentum reconstruction, or residual \(\xi\) dependence after
complexification.

The missing physical arrow is now sharply downstream: renormalized
vector-plus-scalar \(B_s\) bilocal matrix elements with covariance, followed
by pole production, lineshape and detector response. Until that instrument is
constructed, the packet is source-side causal response rather than an
experimental identification.

## Reproduction

Run uv run --offline --with sympy python
research/flavor/checkers/wp534_invariant_complex_pole_packet.py.

The generated result is
research/flavor/results/wp534_invariant_complex_pole_packet.json.
