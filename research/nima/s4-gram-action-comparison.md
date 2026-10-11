# What the full S4 operator Gram retains, and what its doublets mean

## Frozen question and closure condition

Does the original 24-by-24 Gram implement the claimed regular-representation
matter bridge, or a different action? How does the strongest existing
witness-fixed gauge construction compare with that SAME full Gram?

SCC obligation: forward realization and action/comparison compatibility. Keep
all 24 permutations, the original integer Gram, complex coefficient space,
counting/Hilbert-Schmidt pairings, and the completed witness construction.
Compare left translation and conjugation explicitly; do not silently switch
between state, coefficient and operator representations.

The natural four-point character error is ALREADY CLOSED in
`weak-doublet-singlet-weight-and-s4-representation-audit.md`. That packet also
constructs the witness S3 split, weak/charge actions, pinching and spectral
kinetic weights, and closes symmetry-only angle selection as underdetermined.
This turn reuses those results rather than rediscovering them or asking for an
already existing doublet.

**Conjecture:** the full old Gram is the coefficient Gram of the natural
permutation matrices, not a nondegenerate regular-representation pairing.
Its operator image is exactly the commutant of the completed carrier Gram
11I+J. Left translation and conjugation on this image have different irreducible
content; the witness construction embeds, without selecting physical charges.

**Rivals:** the larger Gram rescues all of the old matter assignments; the
four-point character mismatch excludes every doublet; or the completed witness
construction is incompatible with the original operator Gram.

**Risky consequences:** factor the ACTUAL old matrix through the 16-by-24
matrix-coefficient map; determine its kernel and exact spectrum; compute quotient
characters for BOTH actions; construct an explicit operator doublet; and lift
the existing weak/charge operators back through this map. Test the failed
unpinched witness charge too, not just the successful family.

**Closure:** an exact factorization, complete characters and lifts settle this
finite comparison. A different matter space, action or physical selection law
is a separate question. Neither successful lifts nor a conjugation doublet
retroactively validates the false natural-carrier decomposition or selects the
weak angle. No larger compatible construction is needed after this comparison.

## Exact comparison of the full old object

Let P_g be the ACTUAL natural permutation matrices from the old script, and
let V=C^4. Define

\[
\Phi:\mathbb C[S_4]\longrightarrow\operatorname{End}(V),\qquad
\Phi(c)=\sum_g c_g P_g.
\]

The original 24-by-24 matrix K is exactly Phi^* Phi for the declared counting
and Hilbert-Schmidt pairings. Its spectrum, including multiplicities, is

\[
\operatorname{spec}(K)=\{24^{(1)},8^{(9)},0^{(14)}\}.
\]

Thus K has rank 10 and kernel dimension 14, not the old advertised irrep-dimension
spectrum. Indexing a Gram by every group element does not make that Gram
nondegenerate or make its image the regular representation. The full original
matrix and all permutation labels were retained for this comparison.

Writing Pu=J/4 and Ps=I-Pu, the operator image is

\[
\mathcal A=\mathbb C\oplus\operatorname{End}(P_sV)
=\operatorname{Comm}(11I+J)\cong\mathbb C\oplus M_3(\mathbb C).
\]

Every P_g commutes with the supplied carrier Gram, and the image and block
commutant both have dimension 1+9=10. This compares operator spaces; it does
NOT derive the carrier Gram's supplied eigenvalues 15 and 11 from K's 24 and 8.

## Which action carries a doublet?

Use V2 for the two-dimensional S4 irrep, V3 for its natural standard irrep,
and V3' for the sign-twisted standard irrep.

| Space and action | Exact decomposition |
|---|---|
| Original four-state carrier, natural S4 | 1 + V3 (already established in the prior audit) |
| Image of K, induced LEFT translation | 1 + 3 V3 |
| SAME operator image, CONJUGATION | 2(1) + V2 + V3 + V3' |
| Four-state carrier restricted to witness stabilizer S3 | 1 + 1 + 2, with BOTH lines trivial (prior construction) |

The quotient characters are computed from the actual rank-ten projector,
not inferred from matrix size. Conjugation combines the left and right actions;
it is not another name for either one. The sign representation is absent in
both displayed operator-image decompositions.

There really IS an operator doublet. Take the three double transpositions d1,
d2,d3 and the plane spanned by P_d1-P_d2 and P_d1-P_d3. Conjugation permutes
these three matrices, and their difference plane has character V2. Its rank is
two and it is nonzero in the original Gram image. This rejects the overstrong
rival that the old carrier error forbids every doublet.

It does not turn the four-state carrier into 1+sign+2. Nor does an operator
sector automatically supply a weak matter doublet or a generation multiplicity.
Those assertions change the representation space and need their own comparison.

## Explicit lift of the strongest existing witness construction

Use the already supplied carrier metric and witness to take the orthonormal
basis consisting of u/2, v/sqrt(12), (0,1,-1,0)/sqrt(2), and
(0,1,1,-2)/sqrt(6), where u=(1,1,1,1) and v=(3,-1,-1,-1).
This is the completed constant-line, witness-line, contrast-plane decomposition,
not a substitute source.

For ANY X in A, an explicit coefficient lift is

\[
c_g(X)=\operatorname{Tr}\!\left[P_g^*
\left(\frac{P_uXP_u}{24}+\frac{P_sXP_s}{8}\right)\right],
\qquad \Phi(c(X))=X.
\]

The identity follows from matrix-coefficient orthogonality (the frame operator
has eigenvalues 24 on the constant block and 8 on the standard matrix block).
The exact checker constructs the original matrix factorization and verifies the
lifts of the existing Q0, Qw and T3, and all three Pauli generators on the
completed contrast plane, including their Lie brackets.

For general X this same formula reconstructs the block projection
E(X)=Pu X Pu+Ps X Ps. In particular, for the earlier centered witness charge
Y=Pw-I/4 it gives EXACTLY the already constructed pinched charge Qw/4, not Y.
The rejected part has squared Hilbert-Schmidt norm 3/8. Thus the old failed
fixed-Gram charge and its successful pinching have a concrete interpretation
inside the ORIGINAL full operator Gram.

This proves compatibility of the completed conditional construction. It does
not select the witness, hypercharge direction, relative kinetic coefficient,
physical matter map or gauging. In particular, the prior 4/7 result for the
pinched charge with every positive spectral weight f(G) remains closed; it is
not a new invitation to search powers of G for 3/13.

## Disposition and supersession

The finite operator comparison is **constructed**. The old physical-matter
identification is **withdrawn**, while the existing witness construction and
symmetry-only underdetermination are preserved. The additional Gram does not
rescue the original natural-carrier claim, and a conjugation doublet cannot be
substituted for a physical state doublet. No new SM impossibility theorem is
inferred.

Nine pre-correction inputs are byte-preserved under
`quarantine/20261007-s4-evidence/SHA256SUMS`. No old baryonic receipt existed.
The live baryonic checker keeps the full original matrix and now enforces the
correct finite character calculation; unused incorrect projection helpers and
fabricated physical metadata were removed. The old print-only connectivity
checklist is quarantined rather than left runnable as a verification claim.

The baryonic packet, foundational section 7, Gram index/session summary,
completion/landing pages and admission-request entry point visibly supersede
the dependent claims. No issue-tree transition recorded in that historical
request was executed by this turn. Other independent assertions in those
compilations are not validated here.

## Verification

`checkers/check_s4_gram_action_comparison.py` reruns all six existing exact
representation/witness/charge checkers and the original/current baryonic code.
Only the original output-write statement is suppressed; its matrix is compared
entry-for-entry with the corrected implementation. All arithmetic is exact.
The failure gate rejects the deliberately false nondegenerate-regular-Gram claim.

Frozen challenge `e_38524_1791396701643634800_53` passes against
`scc-freezes/nima-s4-gram-action-comparison.bfb65187c85df04f.json`.
Here `survives` names the new finite comparison conjecture, NOT the withdrawn
physical bridge. Receipt: `results/s4-gram-action-comparison.json`.
Scientific support comes from the factorization, characters and lifts, not SCC
or graph admission. Final fresh headless run
`e_38524_1791397165347039800_54` passes. Integrity check
`e_38524_1791397248683786600_55` confirms all eleven receipt inputs and nine
historical snapshots with no drift; the old receipt path remains absent.

Graph result and supersession:
`ev-000000015821-4c9300c5-e745-4e5a-8d73-ee099f8c24d6`, proposal
`ep_73f81579-4fa8-4cb8-ac9b-deac6f0b7784`. The accumulated audit/correction
interval [15815,15821] remains uncommitted. No commit, push or publication
occurred. A distinct larger-carrier source-comparison question is recorded in
that event, with relabelling-equivalent partitions explicitly excluded as
physical rivals; this does not reopen the present comparison.
