# C10 — exact depth-zero obstruction to the raw-amplitude readout

## Fixed records and map

The candidate's two support pairs contain twelve distinct displayed directed occurrences, indexed by (support,triangle,edge), with eighteen primitive usages in their expanded words. Duplicate-looking edges are not identified and their history labels are not discarded.

Construct D[b,a]=1 exactly when the two records have the same support and the completed word a ends at the start of word b. The exact squared column norms are

    [1,2,2,1,2,2,1,2,2,1,2,2].

Take zero-based slot a=1: the support-zero, triangle-zero edge B->C. It has two allowed next records, slots 2 and 3: C->A (primitive expansion C->B->A) and C->E (expansion C->D->E). Thus

    D e_1 = e_2 + e_3,       ||D e_1||²=2.

The source coordinates here have the explicitly declared counting metric; this is not a derived physical energy norm.

## C10 fails before any recursive history construction

The specified append isometry keeps the initial history slot and appends each allowed next slot with amplitude 1/sqrt(d_a). Different initial slots have disjoint history supports, and each appended column has squared norm d_a/d_a=1. In particular

    A_0 e_1 = (|1,2>+|1,3>)/sqrt(2),       ||A_0 e_1||²=1.

C10 requires R_0=I and R_1 A_0=D R_0=D with R_1 contractive. It would follow that

    sqrt(2)=||D e_1||=||R_1 A_0 e_1||<=||A_0 e_1||=1,

a contradiction. No family (R_n) satisfying the specified all-depth equations exists. This is a finite exact witness, not an asymptotic estimate or a failed search for an encoder.

## Scope

This refutes only deterministic contractive reproduction of the **unweighted** fixed D in the declared metrics. A normalized/weighted map, amplification, heralding/postselection, a different metric, or a joint comparison certificate is a different proposition. Deleting one continuation would change D and is not a valid repair within C10. The result does not refute the generation and reuse of a richer retained construction and does not decide C8's reducing tensor-carrier question.

`check_raw_macro_readout.py` reconstructs all records, primitive words, twenty one-step histories and twelve columns directly from the candidate, verifies append normalization with rational arithmetic, and records the witness. No source dynamics or physical outcome is admitted.
