# 1851 — The Region-Pair Pinch Reaches Total Soft Support with Integral Radial Weight

## Source-defined physical family

Take the certified positive region-pair pinch of Entries 1827--1828 and scale
the complete physical configuration uniformly:

\[
(\ell,C_i,t,y_i)
=
\lambda(\ell_*,C_{i,*},t_*,y_{i,*}),
\qquad
\lambda>0.
\]

All distance and energy walls are homogeneous of degree one.  The two active
walls remain zero, all source signs and positive edge-energy inequalities are
preserved, and \(\lambda\to0^+\) reaches Entry 1835's existing four-edge
multi-soft/external-collapse stratum.

Unlike the polar branch, this supplies an explicit physical specialization
family from the frozen source.

## Exact OFPT homogeneity

Exactly ten terms in the five-cycle OFPT source contain both

\[
g_{123},\qquad g_{125}.
\]

After taking their ordered double residue, every term has exactly eight
remaining linear denominators: the six common prefactors and two additional
term denominators.  Therefore the scalar residue coefficient obeys

\[
\boxed{
C_{123,125}(\lambda)
=
\lambda^{-8}C_{123,125}(1).
}
\]

Entry 1828 certifies

\[
C_{123,125}(1)\neq0,
\]

so no cancellation changes this order.

Retaining the remaining one-dimensional differential in the double-Leray
residue contributes one power of \(\lambda\).  Hence the complete residue
one-form scales as

\[
\boxed{\lambda^{-7}.}
\]

## Classification

The radial monodromy is trivial because the exponent is integral.  The
total-soft specialization therefore contributes a Tate/integral grading, not
a new square-root Kummer character:

\[
\boxed{
\text{existing total-soft carrier}
+
\text{source-defined physical scaling family}
+
\text{integral radial coefficient weight}.
}
\]

No new carrier datum or sector-specific branch character appears.

## Scope

This result controls the radial homogeneity of the ordered region-pair residue.
It does not compute the full angular/projective coefficient system on the
exceptional all-soft divisor, nor its sewing to other wall-pair orbits.

## Next falsifier

Projectivize the uniform all-soft scaling and restrict the ten-term residue to
the exceptional shape space.  Test whether its angular coefficient has poles
only on already frozen projective wall incidences and whether cyclic assembly
requires any additional support cell.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_total_soft_homogeneity.py`
- `research/benincasa/results/five-site-region-pair-total-soft-homogeneity.json`
- `research/benincasa/results/five-cycle-ofpt-packet.json`
- Entries 1827--1828 and 1835
- allocator claim: `seqclaim-d3c381679e641fe2bd60e71f`
