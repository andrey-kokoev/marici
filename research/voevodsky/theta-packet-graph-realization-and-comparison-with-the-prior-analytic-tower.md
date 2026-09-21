# Theta packet graph realization and comparison with the prior analytic tower

## Search conclusion and scope correction

The prior research already constructs an analytical coherent presentation system on its admitted observer-generated source. The blanket statement that an analytical realization was missing was too broad.

The relevant established constructions are:

- `the-joint-source-graph-makes-the-chamber-twistor-tower-analytically-equivariant.md`: complete charts S_i with source inverses R_i give C_ij = S_j R_i and transported successors T_i = S_i' U R_i. Edge naturality and order-four chart rotation hold on the declared essential-image topologies. Admission of the charts and source successor is part of the hypothesis.
- `the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md`, sections “Global retained-source completion” and “Higher simplicial realization and coherence defects”: source-retaining graphs J_i x = (x,T_i x) give complemented presentations and strict comparisons. Scalar theta synthesis is a downstream observer.
- `five-sort-markov-analytic-section.md`: all five object sorts, six cell classes, and five law classes are realized on the stated Markov domain. Uniform completion and bounded inverse gauge conditions are essential.

The closed-cone note `the-analytic-realization-of-the-prior-two-segal-baseline-is-the-waldhausen-s-construction-of-closed-cone-packages.md` proposes the stable analytical category and identifies its S-construction target. Its source-derived realization functor and completion seam remain explicit tasks. This statement has a different scope from the established signed presentation tower.

The Markov section checker was rerun successfully during this audit. It checks the signature and eight stored evidence records; this run is an evidence-consistency check, not a fresh execution of all underlying analytical fixtures. The realization registry still records cross-sector global realization as open.

## Direct finite theta realization

Let X = C^24 with the route-counting inner product, and let Y be the specified unweighted direct sum of the two-point and four-point L2 observation spaces. Set

    F = (H^{tensor 2} K_2, H^{tensor 4} K_4),
    Gamma = F* F,
    J c = (c,Fc),
    V = J(X) subset X direct-sum Y.

All statements below also apply packetwise with a subscript k. Since X is finite dimensional and the theta atoms lie in L2, F is bounded. V is closed. The bounded idempotent J pi_X has range V. Its restriction pi_X:V -> X is the inverse of J.

The inherited product Hilbert norm is exactly

    ||Jc||^2 = c* G c,       G = I + Gamma.

Thus the graph construction is an explicit instance of the prior retained-source presentation mechanism. Identifying this instance with the earlier observer source requires the comparison maps specified below.

## Growth and every source composition identity

For any admitted finite-packet source map U:X_k -> X_l, including fixed-slot insertion or deletion, define

    T_U = J_l U pi_X : V_k -> V_l.

Then

    T_U J_k = J_l U,
    T_V T_U = T_(VU),
    T_I = I.

Consequently every already verified source diagram lifts to a commuting diagram of bounded analytical graph maps. This includes insertion/deletion identities wherever their source domains and slots match. It requires no additional coherence choices.

For several bounded observations F_i on the same X, put J_i c = (c,F_i c). The comparisons C_ij = J_j pi_X obey C_jm C_ij = C_im. Their naturality with transported growth is the same calculation as in the prior tower.

## Explicit Hilbert adjoints

The graph norm fixes the adjoint without an independent choice. For U:X_k -> X_l,

    T_U* J_l d = J_k G_k^(-1) U* G_l d,
    ||T_U|| = ||G_l^(1/2) U G_k^(-1/2)||.

These are adjoints for the positive product graph inner products. Comparison with the prior signed Green adjoints requires a separate form-preservation identity.

## Parity readout and forgetting the source coordinate

Let B = K*/2 as in `theta-parity-channel-transport-and-absolute-noise-obstruction.md`; BB* = I_6. On V define

    D_graph Jc = Bc.

Then

    ||D_graph||^2 = lambda_max(B (I+Gamma)^(-1) B*) <= 1.

This readout uses the retained source coordinate. Its input norm contains ||c||^2.

Let p_Y:V -> Y be the output projection. Factoring D_graph through p_Y means finding D:Y -> C^6 with

    D F = B.

Such a bounded decoder with norm at most C exists exactly when

    B*B <= C^2 Gamma.

Necessity follows by applying ||DFc|| <= C||Fc||. Sufficiency follows by defining Fc -> Bc on ran(F), using the inequality for well-definedness and boundedness, and extending by zero on its orthogonal complement.

The previously exhibited counting-unit parity vector u satisfies

    Bu = e_5,       ||Fu|| < 10^(-67000).

Hence every such output decoder has norm greater than 10^67000. The graph readout and the output readout therefore solve precisely specified, different observation problems. The graph construction supplies no improved estimate for the fixed output-only L2 decoder.

If Gamma is invertible, the least possible squared output-decoder norm is

    lambda_max(B Gamma^(-1) B*).

These statements require no numerical inversion of the ill-conditioned Gram matrix.

## Exact comparison with the earlier analytical source

Write E_k for the earlier admitted source, U_old for its successor, and O_k for a proposed bounded observation from E_k into the current multipoint observation space Y_k. The comparison requires explicit maps A_k:X_k -> E_k satisfying

    O_k A_k = F_k,
    U_old A_k = A_l U_packet.

The first equation must identify the event-segmented multipoint theta tensors, their label ordering, and their L2 normalization. The second must use the actual earlier successor and the actual fixed-slot packet map. Defining a successor by conjugation alone establishes neither comparison with an independently specified successor.

For any earlier continuous signed form q_old, the induced packet form is

    q_packet(c,d) = q_old(A_k c,A_k d).

If q_old is represented by W in a declared Hilbert realization, this is A_k* W A_k. Neither the counting form I nor the observation Gram Gamma has yet been identified with that pullback. Form comparison is needed before identifying the corresponding adjoints.

Thus the remaining work for this theta packet has explicit equations: construct A_k and O_k, prove the observation and growth squares, and compute the pulled-back form. The prior analytical coherence is available once these maps are supplied. The separate full closed-cone realization and its completion seam retain the scope stated in their own note.
