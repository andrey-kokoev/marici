# 1882 — The Source Regulator Activates the Surviving Triple Fold

## Final local gate

Entry 1881 leaves one interior, positive-loop-sheet, ordinary \(A_1\) fold
with a nonzero frozen-source residue.  Its active walls are

\[
q_{12}=q_{34}=q_5=0.
\]

Does the original Bunch--Davies \(i\epsilon\) prescription approach this
fold from the pinching side selected by its Landau multipliers?

## Source regulator map

Keep independent positive site regulators:

\[
X_i\longmapsto X_i-i\epsilon_i,
\qquad \epsilon_i>0.
\]

The active partial energies then have imaginary parts

\[
\operatorname{Im}(q_{12},q_{34},q_5)
=
\bigl(
-(\epsilon_1+\epsilon_2),
-(\epsilon_3+\epsilon_4),
-\epsilon_5
\bigr).
\]

Entry 1879 gives projective multiplier signs \((-,-,-)\).  After one
common projective rescaling, write

\[
\alpha_{12},\alpha_{34},\alpha_5>0.
\]

The regulator's pairing with the Landau normal is therefore

\[
-\alpha_{12}(\epsilon_1+\epsilon_2)
-\alpha_{34}(\epsilon_3+\epsilon_4)
-\alpha_5\epsilon_5<0
\]

throughout the complete positive regulator cone.  No regulator hierarchy
or equal-regulator specialization is required.

## Picard--Lefschetz consequence

The critical point is interior to the positive loop-coordinate chamber,
the transverse singularity is \(A_1\), and its local source residue is
nonzero.  The strict regulator pairing is exactly the local physical-sheet
pinch criterion.  Hence the continued Bunch--Davies cycle meets the local
fold thimble with

\[
\boxed{|\langle\Gamma_{\rm BD},\delta_{D_4}\rangle|=1.}
\]

The sign depends on the retained ordered-residue and thimble orientation;
its nonvanishing and absolute value do not.

## Narrow result

\[
\boxed{
D_4(z)=
202304-231696z+95289z^2-16576z^3+1024z^4
}
\]

supports a source-activated five-site cosmological singularity on its
earlier \(+\sqrt5\), positive-loop-sheet root.

This is coefficient support on the already frozen occurrence-labelled
three-wall incidence \(g_{12}\mid g_{34}\mid g_5\).  No new carrier cell or
cosmology-specific incidence generator is required.

## Epistemic effect

The full hostile filtration has now been traversed:

\[
\text{source incidence}
\to\text{saturated divisor}
\to\text{real Galois sheet}
\to A_1
\to\text{positive multipliers}
\to\text{signed loop sheet}
\to\text{nonzero source residue}
\to\text{physical }i\epsilon\text{ activation}.
\]

This is positive evidence for H2: the existing Carrier and support calculus
host a genuinely new five-site physical singularity through a
sector-specific coefficient object.

## Durable verification

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_d4_iepsilon_pairing.rs`
- `research/benincasa/results/five-site-cyclic-triple-d4-iepsilon-pairing.json`
- allocator claim: `seqclaim-f03907ed5c9a92fc33a1da04`
- epistemic event: `ev-000000002240-b0b829fe-31e1-43cb-88cd-a46d6910735c`
