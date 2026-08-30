# RH infinite output rank forbids a finite scalar coherence repair

## Result

Grothendieck's unreduced constructor graph is canonically typed but informationally tautological. After adjoining the Evans scalar wall, its kernel condition reduces to the original question of whether one scalar functional is injective on the constructor image.

Adding finitely many further scalar coherence equations cannot repair this on an output image of unbounded rank.

Let \(Y_X=\operatorname{Ran}T_X\) have dimension \(r_X\). The Evans readout contributes at most one observation rank. If \(k\) additional scalar coherence rows are added, their joint rank is at most \(k+1\). Injectivity on \(Y_X\) requires

\[
k+1\ge r_X.
\]

Therefore

\[
k\ge r_X-1.
\]

Since the moment and seam-jet ranks grow with cutoff, no fixed finite scalar packet can become jointly faithful.

## Exact hostile

At rank three, take the Evans row

\[
\ell=(1,0,0)
\]

and one coherence row

\[
c=(0,1,0).
\]

The state

\[
v=(0,0,1)
\]

is invisible to both. A second independent coherence row is necessary.

The checker verifies the lower bound through rank eight.

## Typing consequence

The phrase “one missing coherence relation” must not be interpreted as one scalar equation. The surviving possibilities are:

1. one operator-valued constructor whose codomain grows with the source image and whose full incidence is independently derived;
2. a source-selected admissible orbit or cone of genuinely smaller dimension;
3. an infinite compatible family of scalar rows with a source topology making the joint observation continuous and uniformly faithful.

Packaging infinitely many fitted scalar equations under one constructor name does not satisfy the first option.

## Relation to the seam-jet tower

The complete seam-jet tower has exactly the required growing-rank shape. But graphing it as dependent coordinates adds no constraint. It becomes a genuine coherencer only if the source supplies an independent relation among tail, reciprocal, seam, primitive, square, and archimedean outputs.

That relation must have operator rank growing with the moment cutoff, or it cannot eliminate the expanding scalar kernel.

## DPC verdict

Candidate: unreduced product graph of all known constructors.

Verdict: canonically typed but tautological.

Candidate: add one or finitely many scalar conservation identities.

Verdict: rejected by the rank lower bound.

Surviving candidate: an independently sourced operator-valued coherence relation with growing rank, or a source theorem restricting admissible states to a lower-rank orbit before evaluation.

## Immediate finite audit

At cutoff \(X\):

1. compute \(r_X=\operatorname{rank}T_X\);
2. compute the joint rank of the Evans row and every independently sourced coherence row;
3. exhibit a basis for the residual invisible subspace;
4. compare rank growth across cutoffs.

If the residual dimension grows, the proposed coherence packet is structurally too small. If a single typed operator row closes it, verify that its component equations are generated from source incidence rather than fitted to the kernel.
