# Last adjacent source merger contracts, with an exact positive fiber

Iteration 15, 2026-10-13. Freshly read the mutable work net's remaining (3,5)-with-(6,7,8) merger task.

## Actual positive source facet

Set alpha4=t*v, alpha7=r/t, alpha8=1/t, keep alpha3=u and alpha2,alpha5,alpha6 finite, and normalize source rows by diag(1,t). The resulting polynomial A/H source germs coincide. The ordered seven-log Jacobian in (t,alpha2,u,v,alpha5,alpha6,r) has determinant -1.

At t=0, only column4 vanishes; the merged parallel class is (3,5,6,7,8). The source boundary tangent rank is six and the full source germ rank is seven at both fixtures. All ordered source minors are nonnegative. This is a genuine primitive codimension-one source merger, not a lower-dimensional coordinate corner.

## Target contraction and incidence explanation

At both fixed positive external Z, the target boundary rank is five and the full target germ rank is six. On the boundary,

    Y row2 = -r*Z1-Z2.

Thus the target two-plane contains a line in the fixed two-space span(Z1,Z2). The incidence locus has dimension at most five: one parameter for that line, then four parameters for a second line in the five-dimensional quotient. All fifteen brackets Y12ij vanish at each fixture. This explains why a six-dimensional target boundary inverse cannot be inferred from the six-dimensional source cell.

## Explicit constant-target source fiber

Let k be the external kernel row on active labels {1,2,3,5,6,7,8}, embedded with k4=0. Adding lambda*k to source row1 preserves CZ. Restore source column2's zero first entry by adding lambda*k2 times row2, then restore column3's first entry 1 by dividing row1 by 1+lambda*k3.

The resulting canonical source parameters are

    alpha2'=(alpha2+lambda*k5)/(1+lambda*k3),
    u'=(u+lambda*k6)/(1+lambda*k3),
    v'=(v*r-lambda*(k1-r*k2))/(r*(1+lambda*k3)),
    alpha5'=(u*alpha5+lambda*k7)/(u+lambda*k6),
    alpha6'=(u*alpha6+lambda*k8)/(u+lambda*k6),
    r'=r.

The checker verifies the full symbolic matrix identity Cfamily*Z=G*(C0*Z), hence the normalized target is unchanged exactly. The source family is not GL-equivalent to the original source matrix. Its nonzero source tangent is killed by the target differential, but not by the full source Grassmannian differential.

At both external fixtures, positive and negative lambda=1/10000 controls give distinct positive source parameter points with identical target. Four positive radial-arc controls also reproduce the original finite source chart. This is an actual fiber obstruction, not just a rank estimate or failed tangent-plane candidate.

## Disposition and orientation

The source six-dlog residues retain coefficients -1/+1 after the derived log-wedge Jacobian and cancel symbolically. Reversing one source orientation gives a nonzero coefficient.

No ordinary target six-form density or residue square is declared for the rank-five image. Its target-density field is null/unavailable, not a false zero. The source facet maps to a codimension-two locus within the seven-dimensional internal target facet, rather than to a target divisor of that facet.

## Implementation corrections retained

An initial local name shadowed the imported parameter helper and caused an execution error; it was renamed. A second failure exposed misuse of the six-column target Jacobian helper on an eight-column source matrix: its truncated source-coordinate screen reported ranks 4/5. The checker now forms the twelve free source coordinates explicitly with the same exact normalization derivative, recovering source ranks 6/7. The target rank criterion and source chart were not altered. Both errors occurred before a passing receipt was published.

## Scope and next executable action

This constructs one primitive positive source merger, its log orientation, target contraction and exact fiber at the pinned external fixtures, with symbolic kernel/gauge identities. It does not prove a weighted cancellation theorem or complete invariant boundary census. Scientific gate verdicts remain open; historical replay inputs remain missing.

Next: assemble the rank-two primitive boundary census of this one source cell. Its active support has seven labels and cyclic direction classes (1),(2),(3,5),(6,7,8), dimension m+r-4=7. Enumerate member deletions from nonsingleton classes and adjacent direction mergers, attach the five finite and three compactified regular receipts plus this contracted merger, and prove the one-step codimension-one enumeration. Distinguish lower-dimensional coordinate contractions from primitive source facets. This would be a bounded atlas for the shared internal cell, not the complete three-composite or weighted nine-form atlas.

## Reproduction

    python research/benincasa/checkers/check_shared_facet_contracted_merger.py

Receipt: `research/benincasa/results/shared_facet_contracted_merger.json`.

Nine grouped checks pass; predecessor source/checker hashes are verified. Evidence is symbolic source/kernel identities and exact rational rank/positivity algebra, not a kernel proof or complete weighted theorem.
