# Packet handoff ground naturality — iteration 9/10

Owner: `marici.Strominger`. [Live net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [prospective contract](contracts/packet-handoff-naturality-09.v1.json) · [checker](checkers/check_packet_handoff_naturality_09.py) · [receipt](results/packet-handoff-naturality-09-v1.json).

## Disposition

**The directed geometric prescription reconstructs the complete native baryon L/G/N without fitted per-port phases. Native symmetry plus local selected lines does not uniquely determine those full protocols.** Two independently geometric neutron patch matchings have the same original metric, G and N but different full L readers. A nonconstant native-C3-equivariant phase preserves every local line and G yet changes both L and N.

This rejects the uniqueness half of the frozen conjecture, not the forward reconstruction. Character polarity, grouping, coherent geometric representatives and primitive phase/history remain different kinds of retained data. None selects a physical M/C grading or observation origin.

## 1. Forward source reconstruction, not fitting from N

For each retained directed baryon triangle, construct

    omega=(-1+i sqrt(3))/2,
    q_t=x0+omega*x1+omega^2*x2.

The fixed complex embedding is the actual producer convention. The full independently retained selected vector equals one global scalar times the geometric stack: **proton -1/10, neutron 1**. There are no extra fitted relative phases or amplitudes once the full directed point/character prescription is retained. Earlier local-line receipts recorded scales without establishing this common global relation.

For proton put X_t=[x0,x1,x2], derive R_t=X_t X_0^-1 and verify the supplied frame family up to its common reference frame. Then

    L=direct_sum Q(q_t),
    G_(t,s)=R_t R_s*/12,
    N=Q(stack_t q_t).

For neutron write q=r+i sqrt(3)s, a=s.s, b=r.s, v=r-(b/a)s and beta=v.v. The independently reconstructed native plane columns are s/a and v/beta, with original metric diagonal (1/a,1/beta) and native selected coordinates (b+i sqrt(3)a,beta). These reproduce the entire original intrinsic embedding, denominators and selected numerators, not merely its image. No free ambient normal preparations are introduced.

The producer's first C3-invariant adjacent-face matching gives three patches of six triangles. L is the sum of the three metric projectors onto their actual geometric mode fields. **G is exactly the Reynolds projector of the actual native C3 action**, independent of that matching. N is the metric projector onto the complete mode field. These constructions reproduce every native matrix entry:

| Source | L support | G support | N support |
|---|---:|---:|---:|
| Proton |108|432|1296|
| Neutron |432|108|1296|

On all36 proton and48 neutron directed geometric seams, q_i q_j*/||q_j||² agrees with the normalized native N block and maps q_j to q_i. Here the normalization and phase are constructed from directed geometry before comparing N, unlike a factorization fitted to N.

## 2. Actual source orientation and ambient extension matter

The pure proton assembler runs **in memory only**, on original six arrows and on their reversals. Both have1836 typed transfers. Under the explicit outer-edge adapter `new ba -> original ab`, the entire reversed L/G/N protocol is the complex conjugate of the original. G is unchanged after this adapter; L/N are not. Reversing arrows changes the directed source, not just its printed character label.

The actual proton source also uses a homogeneous inverse corner permutation

    A_source=X_t [[0,1,0],[0,0,1],[1,0,0]] X_t^-1,
    A_source q_t=omega q_t.

Iteration8 instead explicitly constructed a centered, normal-fixing forward cycle C, with Cq_t=omega²q_t. **A_source and C^-1 agree on the tangent plane but differ by rank1 in the ambient3-space at all12 proton ports.** A_source fixes the triangle centroid, whereas the centered extension fixes its Euclidean normal. Their different character labels include this inverse-generator convention; their full ambient actions must not be identified. This refines the iteration8 construction rather than replacing its declared metric by a different one. Neither derived non-Euclidean corner action is automatically a native primitive command.

## 3. Two intrinsic neutron grouping choices give different readers

The actual belt has exactly two adjacent-face choices incident to reference face0 whose C3 translates partition all six panels into three pairs. Both yield three congruent six-triangle patches and valid native-rank closures in the **same** original coordinate/metric embedding:

    G L_first = L_first G = N,
    G L_second = L_second G = N,
    rank(L_first-L_second)=4.

Each L still has432 nonzero transfers. The receipt retains an allowed raw coordinate input with different L outputs. Thus not even original metric, native rotations, all directed local geometric modes, full G and full N determine the full local preparation stage without the selected grouping rule. This is a source-geometric rival, not the old arbitrary dormant extension or an averaged-metric replacement.

## 4. Local projectors erase consequential coherent phase

Actual native spatial port-action orbit counts are proton1, neutron6, electron1. These are the supplied operation scopes, especially neutron C3, **not every possible symmetry of the unmarked belt**. Consequently native-equivariant scalar port phases have1/6/1 parameters, or0/5/0 relative parameters after one global phase is removed.

On one neutron C3 triangle orbit multiply q_t by omega, leaving all other ports unchanged. The induced native T is metric unitary, commutes with every actual native geometry action and G, and preserves every local selected projector. Nevertheless

    L'=T L T^-1,  N'=T N T^-1,
    G L'=L' G=N',
    rank(L'-L)=6,  rank(N'-N)=2.

All stage supports are unchanged. A full raw N-reader witness is retained. The fixed literal geometric vectors q_t distinguish this rival: **local lines alone do not retain those coherent representatives**. Simultaneously transporting all preparations and readers is a different equivalence question; the test does not call a basis gauge physically observable by itself.

## 5. Inverse characters and electron polarity retain different task types

Complex conjugation gives valid original-metric baryon protocols, commuting with the same real native actions. Their residual ranks are:

| Compared branch | rank(delta L) | rank(delta G) | rank(delta N) |
|---|---:|---:|---:|
| Proton inverse character |24|0|2|
| Neutron inverse character |6|0|2|
| Electron opposite Pauli polarity |8|4|4|

Both baryon return/conjugate overlaps are exactly **tr(N conjugate(N))=16/25**, although the neutron local circularity defects are not constant. This newly observed common global value motivates the next general centroid-fan test; the current receipt establishes it on the two actual fixtures, not on arbitrary geometries.

For electron, use P_f^+=I-P_f^- with the same normals and native spin actions. Both four-face systems have sum2I and give coherent rank2 codes, but their return images are orthogonal. The retained face polarization operator H=I-2L^- has eigenvalue-1 on the native return and+1 on the opposite return.

Put epsilon=[[0,1],[-1,0]]. The antiunitary `J=(direct_sum epsilon) complex_conjugation` intertwines all24 actual native spin/face actions and exchanges the two protocols; **J²=-I**. Baryon plain-conjugation branch reversal instead squares to+I. These are branch comparisons with explicit antilinear type, not given complex-linear primitive moves, physical time reversal, or a derivation of spin/statistics. In particular J does not preserve the selected negative-polarity preparation task or its retained polarization reader. The outward spatial Fourier/negative-Pauli sign distinction from iteration8 remains intact.

## Iteration10 executable frontier

`source-branch-descent-of-indexed-role-windows`: construct the retained-source descriptor and test its character/grouping/coherent-phase forgetful comparisons on the actual rivals above. A concrete new conjecture is that complete directed centroid-edge fans force the baryon conjugate-return overlap16/25. Prove or falsify this with general zero-sum face coordinates, then challenge it with native-equivariant neutron orbit phases; do not infer universality from two matching outputs. Test which full-reader and role-window statements descend, keeping the three primitive occurrences separate from character polarity. This can delimit the maximal common source interface; it cannot manufacture a physical event-boundary witness.

## Verification boundary

30 exact groups pass on the first prospective frozen run and same-checker challenge, freeze `825f3493e61f7a9e191227f4bbc36f5321e94c564cd02874f81971728e8a6fad`. The challenge accepts the scoped reconstruction/counterexample packet, **not** the rejected symmetry/local-line uniqueness conjecture.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-09-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

Execution uses the admitted structured-command surface. No producer entrypoint, other-owner source edit, proof compilation, commit, push or publication is performed. Pure proton assembly is an explicit, in-memory exception, not regeneration of shared producer artifacts. These are bounded exact source-envelope findings, not formal or physical certification. Objective remains in progress.
