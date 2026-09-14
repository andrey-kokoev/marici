# Coarse shell and scale modulations detect route residue on finite arithmetic cutoffs

## Question

Does route-residue detection require independent control of every edge, or can coarser shell-only or theta-scale-only interventions suffice?

## Claim boundary

A finite-cutoff census shows that both coarse families are jointly faithful on all tested cycle spaces. More strongly, one shell-index-coded modulation and one scale-coded modulation are each individually injective on the tested cycle spaces. This is a finite-cutoff discovery, not an unbounded theorem and not evidence that either modulation is physically realizable.

## Combinatorial reduction

Because completed history has the same kernel as graph incidence \(\partial\), detection of cycles by a diagonal modulation \(D\) reduces to

\[
\ker(\partial D|_{\ker\partial})=0.
\]

This can be tested exactly with integer matrices, without numerically approximating the completed-theta columns.

## Probe classes

For shell index \(j\), let \(D_j^{\rm shell}\) select all edges belonging to the consecutive-prime shell \((p_j,p_{j+1})\). For theta multiplicity \(k\), let \(D_k^{\rm scale}\) select all edges with that common scale.

The census tests:

1. the stacked shell family \((\partial D_j^{\rm shell})_j\);
2. the stacked scale family \((\partial D_k^{\rm scale})_k\);
3. one coded shell modulation with edge weight \(j+1\);
4. one coded scale modulation with edge weight \(k\).

At product cutoffs \(120,240,480\), the cycle dimensions are respectively \(3,9,20\). Every tested probe class has full rank on the corresponding cycle space. The largest graph has 136 edges.

## Four-edge mechanism

On a multiplicative rectangle built from two shells, a shell-coded modulation weights the two path decompositions differently unless the two shell amplitudes coincide. A scale-coded modulation similarly distinguishes the four dilation labels. The observed full-rank result says that, within the tested cutoffs, these contrasts also separate linear combinations of overlapping rectangles.

## Experimental consequence

The initial all-edge intervention is sufficient but stronger than necessary in the census. A laboratory interface could first attempt one calibrated analog modulation whose amplitude depends only on shell index, followed by differential common-history readout. This preserves no individual edge readout and therefore tests a genuinely compressed coupling.

The amplitude code must be physically defined. Numerical distinctness of assigned weights is not itself a source mechanism.

## Hostile boundary

Finite full rank does not prove one fixed finite probe family detects the unbounded completion. New large-cutoff cycles could lie in the kernel of a coded modulation. Promotion requires either:

- an arithmetic proof that \(\ker\partial\cap\ker(\partial D)=0\) for the infinite graph; or
- a completed lower-frame estimate controlling cycle norm by modulated response.

Without one of these, the coded probe remains a finite-cutoff discovery.

## Disposition

Coarse pre-codiagonal modulation is a viable and substantially weaker experimental target than edge-by-edge control. The next mathematical test is to characterize the joint incidence equations for shell-coded or scale-coded weights and search for the first large-cutoff countercycle.
