# C9–C11: explicit spectral, history-realization and threshold claims

These are mathematical statements about the fixed models in the v4 net. None admits physical species or grants apparatus authority.

## C9 — absence of singular-continuous spectrum

Let H be exactly the bounded self-adjoint operator defined by the eleven-state weighted core and three semi-infinite chain quadratic form in `native-port-scattering.md`. Work on that coupled Hilbert space, not a larger space with unspecified spectators.

**Claim:** P_sc(H)=0. Equivalently, for every vector psi, its spectral measure decomposes into a measure absolutely continuous with respect to Lebesgue measure plus pure point atoms, with no singular-continuous part anywhere on the real line.

This includes neighborhoods of 0 and 4. The reported bounded zero-energy threshold resonance is not a normalizable eigenstate and does not itself refute C9. A nonzero singular-continuous spectral measure for any vector refutes it.

C9 is a necessary subclaim in C2's proposed proof, not sufficient for outgoing completeness or the claimed eigenmode count. C2 is preserved as the stronger assembly proposition. Its planning prerequisite is C9's positive result; a refutation of C9 would also refute C2, but is not a successful construction prerequisite. Finite-rank perturbation alone is not an argument for C9.

**Bounded test:** derive the finite-core resolvent using the half-line Weyl function; analyze the algebraic boundary values and exceptional points on the band and at its edges. Establish the measure decomposition or exhibit a singular component. A finite-chain eigenvalue scan is insufficient.

## C10 — deterministic history-preserving realization of the raw macro map

**Refuted at depth zero in the stated operation class.** Slot 1 has ||D e_1||²=2 while ||A_0 e_1||²=1, excluding R_1 A_0=D with contractive R_1. [Exact reconstruction and proof](RAW-MACRO-READOUT-OBSTRUCTION.md). The specification below is retained; richer comparison constructions are not excluded.

Use precisely the twelve displayed occurrences a, their primitive words w(a), and same-support endpoint compatibility D[b,a] of C8. Let d_a=sum_b D[b,a]. No entry of D may be rescaled or fitted.

At depth n, the retained Hilbert space has orthonormal basis all admissible ordered displayed-occurrence histories h=(a0,...,an). Store also every expanded primitive word and clock phase as deterministic labels of that history. Different displayed occurrences remain orthogonal even if their primitive words overlap. This is a declared counting metric, not an asserted inherited physical Born metric.

The **allowed operations** are fixed equal-weight coherent appends:

    A_n |h> = sum_(b:D[b,last(h)]=1) |h,b>/sqrt(d_last(h)).

The old history is never overwritten. Each length-one primitive word uses C8's identity wait to synchronize the two-tick clock. No measurement, outcome conditioning, branch deletion, cloning, renormalization after success or extra transition is permitted. Orthogonality of distinct history prefixes makes each A_n an isometry.

**Claim:** There exists a sequence of linear contractions R_n from the full depth-n history space to C12 such that

    R_0=I12,
    R_(n+1) A_n = D R_n      for every n>=0.

A contraction means operator norm at most one in the stated counting metrics. It is the necessary amplitude-readout condition for a deterministic norm-preserving apparatus with retained complementary records; complementary records are not erased by this definition. Ancillas in fixed normalized states do not permit amplification. The claim asks whether this precise lossless history expansion can reproduce the **unweighted raw macro amplitudes** D, not merely a normalized transition law or an approximate selected carrier.

A norm obstruction at any finite depth refutes C10. In particular the depth-zero necessary condition is ||D||<=1; this should be checked before attempting any long-history construction. Conversely, matching endpoint probabilities or finding an arbitrary unbounded linear decoder does not establish the claim.

This is deliberately a sharp candidate, not a blanket assertion about every source operation. Failure would rule out the specified deterministic realization of raw D, not normalized weighted models, heralded filters, or C8's distinct invariant-carrier question. Even success would still require independent justification of the supplied history apparatus and source metric. No stronger source-authorization conclusion is hidden in the wording.

C8 -> C10 is a target-definition edge, **not** a positive-premise edge. C10 can be tested whether or not C8 has a carrier.

## C11 — three-port lower-threshold Householder limit

Use the same fixed three-port H, K, visible projection P and port metric H_port as C2. In the coefficient convention of `native-port-scattering.md`, let

    E(k)=2-2 cos(k),
    S(k)=I3-i(2 sin(k)) [E(k)I-K-P+exp(ik)P]^(-1)_PP.

**Claim:** K has a simple zero mode v with nonzero visible component v_P, the outgoing response is nonsingular for every 0<k<pi, and the metric-whitened scattering matrix satisfies

    lim_(k->0+) H_port^(1/2) S(k) H_port^(-1/2)
      = I3-2 w w*,
    w=H_port^(1/2)v_P/sqrt(v_P* H_port v_P).

The limit has eigenvalues (-1,1,1). A zero invisible mode, an interior real pole, or a different/nonexistent limit refutes this conjunction. The limit does not assign finite flux at k=0 and does not require C2's full wave-operator completeness.

This is already **reported** in `native-port-bound-spectrum.md`; in this net it starts open pending an explicit source-bound verification of the nullspace, visible coupling and Laurent/Schur expansion. Historical reporting is not silently promoted to a newly checked result.

C11 and established C1 are the precise premises of C6. C2 is no longer its prerequisite.
