# Existing identity constructors attached to the original five-role source

## Source and exact scope

This experiment REUSES Nima's actual `SpectralLedger`, triangle spectral
projectors and barycenter helper rather than inventing another identity theory.
The existing3D barycenter helper is explicitly extended to the retained fourth
coordinate; the old source files and their receipts are not rewritten.

The actual source module is `demos/particle-overlap-tetrahedron/model.mjs`,
imported via Node. Its original walk is

    C0 -> M0 -> C1 -> M1 -> C1 -> C2.

P is C0/M0/C1 (CMC), N is M0/C1/M1 (MCM), E is M1/C1/C2 (MCC).
The repeated C1 is one vertex identity with two occurrences. C2 is the original
fifth pentachoron vertex, NOT the new outer C2 of the recent glide chain.
The code detects that distinction explicitly. This supersedes using the glide
candidate as though it already implemented the original continuation.

Fourth coordinates are stored as rational coefficients of sqrt(5), with metric
G=diag(1,1,1,5). All ten original squared distances are exactly8. The source
JS literal Math.sqrt(5) is checked before applying this exact encoding.
The five-vertex lift is a configuration-space presentation, not a claim of four
physical spatial dimensions.

## Barycenter development with retained identity

For first-seen vertices, the prefix center follows the existing law

    b_(n+1)=b_n+(x_(n+1)-b_n)/(n+1),
    x_(n+1)=(n+1)b_(n+1)-n b_n.

Every step displacement and the exact reverse reconstruction are checked.
Separately, averaging all six chronological occurrences gives a DIFFERENT result
because C1 is visited twice. That occurrence-weighted readout must not replace
the geometric center of the five-vertex body.

The outer tetrahedron center, whole pentachoron center and fifth vertex are
respectively(0,0,0,0),(0,0,0,1/5),(0,0,0,1) in this encoding. All project to the
same3D point. They remain three distinct retained objects; point projection does
not identify their source roles or information.

Each particle window also has its own three-vertex anchor. Their sequential
updates are genuine vector displacements:

    bP=(1/3,1/3,-1/3,0),
    bN=(-1/3,-1/3,-1/3,0),
    bE=(-2/3,0,0,1/3),
    deltaPN=(-2/3,-2/3,0,0),
    deltaNE=(-1/3,1/3,1/3,1/3).

These are specified barycenter readouts/coordinate comparisons, not physical time
or a force equation. The entire source and its marks remain accessible.

## Retained spectral identity: actual old constructor, not a renamed loop bit

The original windows have TWO directed source steps. Nima's spectral constructor
requires THREE composable steps forming a closed triangle. Direct promotion of
the open windows is therefore tested and REJECTED. The positive adapter adds a
marked geometric closing edge for each original triangular face. It is explicit
extra adapter data, not a previously supplied native particle command.

Using that declared adapter, the old ledger constructs all three modes for every
face, retaining each actual source occurrence and its distinct closing seam.
Their projectors are idempotent, eigenvalues/phases retained, and the ledger's
history windows recover the exact entry, continuation and both fold structures.
Repeated promotion gets a fresh label and the same spectral projector while
recovering its unchanged root. Equal coefficient projectors across P and N do
not identify their different source histories.

## Exact metric-compatible geometric realization of all modes

Let b5 be the full five-vertex center. Map five label coefficients lambda to
centered geometry r and total coefficient s by columns

    H_i=(v_i-b5,1).

The existing counting metric has the exact decomposition

    4 sum |lambda_i|^2 = r^*G r+(4/5)|s|^2,
    H^* diag(G,4/5) H=4I5.

The final scalar is retained, not discarded by centering. Its metric weight is
computed from the regular simplex Gram matrix, not a physical fitted weight.
This is a chosen counting-metric realization, not the native particle metrics.

For ordered face-column matrix Z and old spectral projector E_lambda, construct

    P_lambda=Z E_lambda Z^* diag(G,4/5)/4.

All three geometric mode projectors are rank one, idempotent, self-adjoint in
that retained metric, and have the actual cyclic eigenvalue. Thus the common
identity mode as well as both complex modes survive geometric realization.

For arbitrary five-coordinate source inputs, keep ALL three projected face
components AND the two outside-face coefficients. Every original five-label
basis input reconstructs exactly. Neither the selected rank-one projector nor
the visible barycenter is misrepresented as a decoder of all source information.

## A concrete overlap-preserving transport and its phase result

The comparison rule swaps the exiting and entering vertices and fixes every
shared and uninvolved vertex:

    P->N: swap C0 and M1; fix M0,C1,C2,
    N->E: swap M0 and C2; fix C0,C1,M1.

This maximal-fixed-complement rule is explicitly DECLARED, not uniquely derived
from native particle dynamics. It supplies exact affine isometries of the
original simplex. Their centered homogeneous matrices preserve the above metric;
barycenter, spectral projector and full source-coordinate squares commute.
Two-step frame composition is invertible on every original parent basis state.

With omega=exp(2pi i/3), the fixed source mode references give

    P positive -> omega * N positive,
    N positive -> omega^2 * E negative.

The conjugate source branch has conjugate factors. Common modes retain phase1.
The second shared edge is traversed oppositely in the original source walk;
therefore its fixed forward complex branch switches. Treating both transitions
as preserving the positive branch is an exact failed rival, not a reason to
relabel the original source after the fact.

The FULL cyclic operation squares are also checked. P->N intertwines the
forward cyclic operations. N->E intertwines the target INVERSE cyclic operation,
not its forward operation. The inverse is available as two retained forward
cycles (C^-1=C^2), but that is a different command history and must not be counted
as the same primitive step. The mode switch and its phase are retained identity
development, not erasure of identity.

## The fifth mark changes the global duality scope

The four-role facet's earlier C/M-swapping anti-map fixes C2. The FULL source
has three C vertices and two M vertices, so no bijection can swap C/M everywhere.
The map is a RELATIVE facet duality with a retained fifth mark, not a uniform
global exchange of all C and M roles. A physical carrier-relative grading would
need to specify this distinction; the code does not silently supply it.

## DPC, verification and next attachment

Problem: attach already constructed identity persistence to the CMC/MCM picture
without replacing its source. Candidate: retained source windows, barycenter
steps, spectral modes and explicit frame comparisons coexist faithfully.
Falsifiers: open-window promotion, lost fifth coordinate, repeated-occurrence
deduplication, wrong glide C2, lost mode/phase, moved shared identities and a
false forward N/E operation square. Positive and negative tests are both retained.

    python research/aspect/scc/scc.py check cmc-mcm-identity-attachment-v1 --verbose

Receipt: `results/cmc-mcm-identity-attachment/verification.json`.

The result is a CONDITIONAL geometric/spectral attachment, not a derivation of
physical P/N/E or a replacement of the original native1836 proton/neutron
preparation and command protocols. Next: compare these explicit closures and
frame/branch adapters with those actual native sources at the full reader,
metric and primitive-history level. Any non-admissibility or changed-task
obstruction must survive; matching ranks or words is insufficient.
