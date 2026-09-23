# Sufficient state is relative to permitted continuations

## Exact owning-source example

In the m=3 tail box, consider two admitted rational linear histories:

    E: x1=1, x2=1, 0<=x0<=1;
    F: x1=0, x2=257/129, 1/129<=x0<=130/129.

They describe entire line segments, not asserted actual source points. Their parameterizations for 0<=t<=1 are

    e(t)=(t,1,1),
    f(t)=(t+1/129,0,257/129).

Both obey the owning caps. Their difference lies in the kernel of the two-moment map: its total is zero and its weighted total with slopes (1,1/128,1/16384) is zero. Both public images are exactly

    U=t+2, V=t+1/128+1/16384, 0<=t<=1.

Consequently all queries determined by the public (U,V) possibility set agree, including exact membership, support, and possible/forced public predicates. The histories have different hidden audit fibers everywhere on that segment.

## Public continuations preserve equivalence

For any source subset C, public observer L, and predicate f on its codomain,

    L(C intersect L^-1(f)) = L(C) intersect f.

Hence equal public images remain equal after any finite sequence of public evidence additions. If a procedure chooses its next public frame using only earlier public answers, both histories also follow the same adaptive branch and remain indistinguishable. This covers refinements by arbitrary public predicates at the semantic level; executable completeness remains limited to each backend's declared query and frame languages.

Backend replacement and representative-producing queries do not affect this statement provided they do not change the represented state or expose additional witness data. Certificate bytes or selected source coordinates can differ. The equivalence here is public mathematical-answer equivalence, not equality of packet contents or confidentiality.

## A fine continuation distinguishes immediately

Expose x1 and accept the frame x1<=0. For E the new carrier is empty; for F it is unchanged and nonempty. Even exposing x1 and asking its possible values distinguishes {1} from {0}, without adding evidence.

Thus identifying E and F is safe for the public-only continuation contract but unsafe for a contract allowing this audit to be re-exposed. Exact current projection is not sufficient state for arbitrary future operations.

Re-exposure without knowing the old hidden restrictions cannot recover the original refined carrier. Reopening the full source fiber would be a deliberate weakening, not an inverse of hiding. A truthful future interface must either retain adequate hidden information, deny that continuation, or explicitly change its semantics.

## Continuation-relative state equivalence

Fix a permitted continuation language K and terminal query semantics. Define

    E equivalent_K F

when every permitted continuation gives the same terminal answers on both states. Public-image equality is a congruence for public-only refinement by the identity above. Enlarging K can split equivalence classes. A compressed representation is sufficient only if its state identification respects this continuation equivalence.

This does not imply a canonical finite minimal implementation for arbitrary query languages, or identify the syntactic history with its semantic quotient. Independent statement binding can remain deliberately sensitive to history syntax even where semantic states agree.

## Storage consequence

A future-capable interface may need information that no current public query can distinguish. Discarding that information is sound only under an explicit restriction of future capabilities or a verified sufficient substitute. This is why present-day answer equality is not by itself an evidence-compression theorem.

The result strengthens the criterion for safe summaries: certify not only equality of current projected images, but preservation of the admitted continuation operations. For permanently retired audits, exact projected state can suffice; for re-exposable audits, it generally cannot.

## Reproduction and scope

    python research/voevodsky/checkers/check_continuation_relative_forgetting.py

Artifact: `results/continuation-relative-forgetting.json`.

Twenty public-refinement controls pass. The all-parameter source equality and the general continuation law follow from the affine and image/preimage identities above, not sampling. This is a direct exact mathematical checker, not a separate packet verifier or a fresh upstream source-admission replay. No observational authentication or actual-source inference is claimed.
