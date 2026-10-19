# Reading: Garai, The double tetrahedron structure of the nucleus

Source: `references/0309035v2.pdf`,15 pages. Ran `pnpm pdf:reindex` FIRST:
4706 pages from46 PDFs indexed. Then used
`pnpm pdf:search 'tetra' -Book 0309035v2`, read all15 extracted pages and visually
inspected Figs1,2,3,S1 on PDF pages5,6,7,9. Figures rendered with an ephemeral
uv/PyMuPDF environment into `temp/strominger/garai-0309035v2/`; project package
manifests/dependencies were not changed.

## What is actually proposed

Garai treats each nucleon as an equal SPHERE and constructs an FCC aggregate
whose overall shape develops as a DOUBLE TETRAHEDRON around a four-nucleon core.
It is not our model of whole tetrahedral nucleons centered on diamond A/B sites.
FCC has12 nearest neighbors and triangular cycles; diamond has4 and is bipartite.
An alternating FCC P/N assignment cannot mean unlike species on EVERY nearest
neighbor edge, because an FCC triangle cannot be two-colored. Do not substitute
one connectivity for the other while importing counts.

## The useful counting constructor (pp2,5; Fig1)

Write T_k=k(k+1)/2. The paired layers have

    T_(2n-1)+T_(2n)=4n^2 nucleons.

Assuming half are protons gives2n^2:2,8,18,32. This is a BOUNDARY-LAYER count,
not the whole tetrahedral-cluster count C(k+2,3) used in our earlier numerology.
That earlier count's mismatch does NOT refute Garai's different counting policy.

Fig1C gives paired layers1+3,6+10,15+21,28+36. The text on p2 and Fig1B print54
for the last pair; this is an arithmetic typo for64, which Fig1C gives correctly.
No change to the formula is needed to identify this source discrepancy.

## Subshell counts (pp3,6; Fig2)

A layer of a vertex cap consists of two triangular edges meeting at their apex:
2ell+1 positions. Four equivalent caps, with half the spheres designated protons,
give2(2ell+1)=2,6,10,14,... . Summing ell0through n-1 gives2n^2.

The factor2 here comes from FOUR caps times HALF protons. It is not a derivation
of spin degeneracy. Labels -ell through+ell have the right cardinality, but the
paper supplies no rotation-group action or angular-momentum operators proving
that these spatial positions are physical m_ell states.

## Three different sequences must remain distinct

1. Principal electronic shell capacities:2,8,18,32,... .
2. Atomic period lengths:2,8,8,18,18,32,32,... . The paper proposes alternating
   double-tetrahedral growth to repeat the shell sizes (p3; FigS2 on p10).
3. Nuclear major magic numbers:2,8,20,28,50,82,126. Fig3 includes oscillator
   cumulative counts2,8,20,40,70,112,168 and a comparison energy-level diagram;
   counting alone does not derive the physical split ordering.

Counting PROTON sites to reproduce ELECTRONIC quantum-state capacities requires
an explicit nuclear-to-electronic state/readout correspondence. Neutrality gives
electron NUMBER=Z; it does not supply electron states or their energy ordering.
The author's assertion that coincidence is excluded is stronger than the
provided counting evidence.

## Supplementary coordinate audit (pp12-15)

The reproducible checker `checkers/check_garai_0309035_counts.py` parsed all172
numbered rows. Period totals are4,16,16,36,36,64 nucleons, and assuming P=N gives
2,8,8,18,18,32 protons, cumulatively86. Each listed subshell has4(2ell+1) sites,
consistent with the four-cap assignment. Audit and exact source hashes:
`results/garai-0309035v2/count-audit.json`.

The table is an equal-P/N construction: its radon endpoint is86P+86N, not common
radon222 with86P+136N. It therefore does not solve neutron-excess occupation.

A separate coordinate issue needs reconciliation before copying the geometry:
FigS1 quotes consecutive-layer separation d sqrt(2/3), while the table's twelve
z planes are about d/sqrt(2) apart (d=1 by the stated sphere radius0.5). Those
are different FCC section directions. They may reflect different presentation
conventions, but cannot be silently treated as one numbered-layer coordinate map.

## What to transfer, without adding forces

Keep the explicit paired-triangle and four-cap growth rules as mathematical
rivals. They give the requested layer structure and nontrivial exact identities.
Do not import the paper's physical identification as an established result.

Next source question: can these boundary/cap counts be realized on OUR fixed
reciprocal diamond coordination network, with its actual barycenter incidences
and A/B role information preserved? Count independent reconstructible interface
modes, not just colored positions. If reproduction requires replacing diamond
with FCC packing, record this as a different model rather than a success of the
original one. Neither an interaction potential nor fitted forces are needed to
perform that structural test; it still requires a fixed allowed-map/readout rule.
