# The symbolic tail section can preserve explicit atom audits

## Result

The symbolic tail section now has an explicitly declared audit-aware extension. It fixes the supplied audit coordinates and applies the existing greedy construction only to the remaining box. Independent verification passes for 32 conditional sections and 128 contraction instances, including nine nontrivial contractions with nonempty audit sets.

This turns the observation boundary into an implementation rule: do not identify witnesses while changing a declared audit. Enlarge the observed fiber instead, and refuse a proposed target whose common audit fiber is empty.

The ordinary two-coordinate query API remains unchanged. It does not silently acquire atom-reading authority.

## 1. The enlarged observation

The owning source is

    B_m = product_j [0,100+2j],
    L(t) = (sum t_j, sum 128^-j t_j).

Declare a finite set A of audited atom indices and retain their raw values h_j. All rational threshold predicates on an audited coordinate are preserved precisely by preserving that coordinate's value.

The enlarged observation is

    L_A(t) = (U,V,(t_j)_(j in A)).

The new values must be supplied as observations or proposed coordinates. The constructor does not infer actual h_j from a previously chosen feasibility witness.

## 2. A conditional generative section

For valid pins 0<=h_j<=100+2j, subtract their moment contributions:

    U' = U - sum_(j in A) h_j,
    V' = V - sum_(j in A) 128^-j h_j.

The remaining coordinates still form an independent admitted box. Its cumulative mass and weighted-cap sums are obtained from the original closed sums by subtracting the audited capacities. No missing coordinate is assigned a new independently chosen witness at a join.

The existing greedy membership construction applies to the remaining ordered slopes. Reinsert the fixed audit values after constructing its lift. This gives

    s_A(U,V,h)

with L_A(s_A(U,V,h))=(U,V,h).

Zero and one remaining free coordinate are handled as degenerate point and segment cases. Invalid or duplicate audit declarations are rejected. An inconsistent joint moment/audit proposal receives a separating source inequality, not a guessed adjusted audit value.

## 3. Audit-preserving contraction

For an admitted source x define

    H_A(x,t)=(1-t)x+t*s_A(L_A(x)).

Both endpoints are in the same box and have the same enlarged observation. Therefore every point of the segment is source-admitted and preserves U, V and each audited raw coordinate. It preserves every rational threshold audit on those coordinates.

For fixed m and A, the section is continuous. Removing fixed coordinates leaves either a positive-cap box with distinct ordered slopes, a one-coordinate segment, or a point. In the first case the same greedy-profile continuity and tip estimates used for the original section apply; the latter cases have a unique residual lift. The pin contributions depend affinely on their values.

The contraction fixes section points. Its restriction to any possibility set defined solely through L_A is literally the same formula, regardless of which visible frames describe that set. The visible set need not be convex: the contraction never changes the enlarged observation.

These continuum conclusions follow from the source-box and linear identities. The finite controls check the implementation; they are not a substitute for the argument.

## 4. The original audit failure is repaired without changing the audit

At m=3, take the admitted source (0,1,0). Its moments are (1,1/128).

The ordinary two-moment section has strictly positive coordinate zero. Contracting to that section changes the truth of the audit t_0<=0.

With t_0=0 explicitly retained, the conditional section preserves it. The remaining two moments determine the other two coordinates, so the section is exactly (0,1,0).

For larger boxes the repair need not make the contraction trivial. Nine tested cases keep nonempty audit sets fixed while changing unobserved source coordinates.

## 5. A missing common audit fiber is rejected

Still at m=3, retain the audit t_2=0 and propose the observable base of the all-cap source (100,102,104).

That base is admitted without the audit. But with t_2 fixed to zero, the maximum possible total is 202, whereas the proposed total is 306. The conditional section rejects it and exports the corresponding exact support inequality.

It does not normalize the audit coordinate, transport it to 104, or identify the two values. This is the executable common-audit-fiber gate. It is not an authorization to execute a reverse source operation.

## 6. Verification and limits

The test covers m=2,3,4,8,16,64,1024, multiple audit sets, and all-fixed or one-free-coordinate controls at small m. An independent verifier imports neither the section constructor nor the query engine. It expands the free profiles, checks their source caps and both moments, and checks every audited coordinate throughout the contractions. It also replays the missing-common-fiber separator.

Pinned indices and values remain retained information. The frame history or residual relation identifying the run's visible possibility set remains independently necessary. The construction does not apply to additional hidden restrictions merely because they hold at one selected lift.

Ordinary Euclidean paths are explicitly the comparison identity here. Literal point equality, arbitrary new atom audits, source authentication and physical action authority are not inferred. This is a conditional section and contraction constructor, not yet a general optimizer for every enriched audit language.

## Reproduction

    python research/nima/checkers/check_audited_tail_section.py
    python research/nima/checkers/verify_audited_tail_section.py

Artifacts:

- `research/nima/results/audited-tail-section-contract.json`
- `research/nima/results/audited-tail-section-packet.json.gz`
- `research/nima/results/audited-tail-section.json`
- `research/nima/results/audited-tail-section-verification.json`
