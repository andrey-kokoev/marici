# Two-order barycenter comparisons are necessarily planar

## Question

The operator proposed studying a retained barycenter walk as an edge of a comparison figure, with geometric characteristics encoding second-order comparisons. The combined conjecture asked whether native WG witness admission could be recognized from that figure without feeding witness status into its coordinates.

The executable first test is the proposed comparison of AB -> ABC -> ABCD with AB -> ABD -> ABCD. Active SCC obligation: forward geometric realization. The native-to-barycentric realization gate is kept separate.

## Claim boundary and derivation

Let s be the barycenter of n retained vertices. Append c or d, obtaining intermediate barycenters p and q, and then append both, obtaining t. Equal-weight averaging gives

\[
p=\frac{ns+c}{n+1},\qquad q=\frac{ns+d}{n+1},\qquad t=\frac{ns+c+d}{n+2}.
\]

Hence identically

\[
(n+1)(p+q)=ns+(n+2)t.
\]

The coefficients sum to zero, so this is an affine dependence. The proposed four-point comparison tetrahedron always has zero volume, for arbitrary source coordinates. In particular, for the edge prefix n=2,

\[
3p+3q=2s+4t.
\]

This is not a special property of regular tetrahedra. The exact checker verifies all 24 orders of the regular coordinates and all 24 orders of a distorted tetrahedron. An off-plane perturbation produces a nonzero determinant but violates the barycentric relation; it cannot serve as an admissible source comparison.

### What remains nonzero

For order ABCD,

    s = (1,0,0)
    p = (1/3,1/3,-1/3)
    q = (1/3,-1/3,1/3)
    t = (0,0,0).

The loop s -> p -> t -> q -> s has oriented area vector (0,1/3,1/3), with squared magnitude 2/9. Its affine rank is exactly two. Swapping the extension order reverses that area vector. All regular orderings have the same area magnitude, so that scalar also fails to distinguish the orders.

The recursively averaged three-state walks give

\[
\mu_p=\frac{s+2p+t}{4},\qquad
\mu_q=\frac{s+2q+t}{4},\qquad
\mu_p-\mu_q=\frac{p-q}{2}=\frac{c-d}{2(n+1)}.
\]

For n=2 the difference is (C-D)/6, nonzero despite the common terminal barycenter. Thus the comparison retains an oriented planar loop and a difference of averaged representatives, but not an independent volume direction. These are geometric records of order comparison, not yet obstruction classes or physical effects.

## Native comparison gate

`source-restricted-native-obstruction.md` supplies an existing rule-signature obstruction for bare atomic endpoints under source-only seeds. `meta-witness-native-bridge.md` supplies a conditional positive application bridge in a separately extended runtime. They do not supply a source-justified map from their terms, types and witnesses into these barycenter configurations, nor are their differing rule signatures a blind same-model comparison dataset. No coordinates were assigned by witness status and no fresh Agda verification was performed here.

The requested native blind test is therefore not performed. Its first missing object is a boundary-preserving native-to-barycentric realization with an independently specified admissibility domain. The geometric identity above cannot replace that map or decide native fillability.

## Disposition

The candidate independent-volume signal is eliminated for this entire two-extension construction by an affine identity, rather than merely by numerical samples. The broader conjecture that oriented comparison geometry encodes native fillability is unresolved. Planar oriented area and the averaged-state difference survive as computable comparisons; neither is promoted to a witness criterion.

Verification: `python research/aspect/scc/scc.py check nima-barywalk-comparison` passed, execution `structured_command_execution:e_32876_1791224049315267700_24`. Checker: `checkers/check_barywalk_comparison.py`; full coordinates and controls: `results/barywalk-comparison.json`; manifest: `scc-models/barywalk-comparison.json`. No commit or publication is claimed.
