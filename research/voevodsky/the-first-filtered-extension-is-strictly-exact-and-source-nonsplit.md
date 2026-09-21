# The first filtered extension is strictly exact and source-nonsplit

## Strength

A completed source extension theorem in a specified COMMON path-norm topology. The sequence

    0 -> I^2/I^3 -> I/I^3 -> I/I^2 -> 0

has a strictly exact Banach completion in that topology and remains nonsplit as a source module. The topology is not silently identified with the earlier factorization-presentation completion of each graded layer.

This constructs and detects actual extension data. It does not yet provide the analytical derived comparison for that extension.

## 1. One source norm for all terms

Fix p>=0, b>=1, and the existing a>=1. On finite marked paths of event length n use

    w(n)=(1+n)^p (b a)^n.

The weighted l1 sum over actual paths and typed endpoints is a Banach algebra after completion, with noncomposable products zero. Indeed w(n+m)<=w(n)w(m), and the l1 convolution estimate gives bounded multiplication. No infinite sum of vertex identities is adjoined as a unit.

For each stabilized finite endpoint corner c let S_c be its path space and I_c the terminal-record kernel. Its length n(c) is fixed. Let J_k be the l1 direct sum of the finite subspaces (I^k)_c, with the inherited path norm.

Each J_k is closed by bounded coordinate projections. It is the closure of the algebraic ideal power I^k, since finite endpoint support is dense. It is a closed ideal of the completed path algebra by continuity of multiplication and the finite ideal property. We do not assert that every element of J_k is a finite sum of products of completed J_1 elements.

## 2. Strict exactness

Because J_3 subset J_2 subset J_1 are closed subspaces of ONE Banach space, the canonical sequence

    0 -> J_2/J_3 -> J_1/J_3 -> J_1/J_2 -> 0

is strictly exact. More explicitly:

- The first arrow is isometric: distance to J_3 is computed with the same inherited norm.
- Its image is closed and is exactly the kernel of the last arrow.
- The last arrow is the quotient map, and its quotient norm is the given norm of J_1/J_2.

Endpointwise this agrees with the finite source sequence. The l1 quotient identification follows by choosing finite-corner lifts with summable norm errors. No bounded linear splitting is required or asserted.

Completed multiplication acts continuously on each term. The outer terms have zero I-action, while the middle term need not. Thus the middle term is a source module, not automatically a B=S/I module.

## 3. A finite witness prevents source-equivariant splitting

Take two consecutive forgotten diamond relations a and c on disjoint two-event blocks. Their product ac has four nonzero path coefficients and lies in I^2. In the four-event corner I^3=0, so [ac] is nonzero in I^2/I^3.

Suppose a source-linear section s:I/I^2 -> I/I^3 existed. In the two-event corner containing c, I^2=0. Endpoint idempotents force s([c]) to stay in that corner, so s([c])=[c]. But I acts trivially on I/I^2, and hence

    0 = s(a[c]) = a s([c]) = [ac],

a contradiction. The same finite witness survives completion. It excludes even an algebraic source-module section, not merely a bounded one.

At the four-event root corner the dimensions are 24 -> 234 -> 210. Vector spaces can split, but no such splitting is a source-equivariant replacement for the module extension.

## 4. The connecting data survives

The strictly exact sequence determines its usual source-extension class (and its connecting morphism in any specified exact/derived realization admitting this sequence). Its algebraic restriction to the finite source witness is nonzero by the preceding argument.

This does not by itself identify a topological Ext group, choose a derived tensor completion, or supply the analytical beta comparison. Those require a declared category and actual source-equivariant maps. In particular, assembling two already realized graded B-modules as a direct sum would make I act by zero on the entire target and erase this extension.

A faithful degree-zero source-equivariant embedding of the middle module into such an I-annihilated target is impossible: it would send [ac] to zero. The required analytical target must retain nontrivial source action or represent the extension through a derived attachment; the earlier shifted relation maps suggest the latter route but are not a proof of it here.

## 5. Comparison with the prior graded source scales

Multiplying an r-factor presentation into the path space is l1-contractive before weights. For fixed p and r, its additional path weight is paid by a fixed radius enlargement: for n>=1,

    (1+n)^p <= 2^(p n).

Thus the prior graded presentation scale at path radius 2^p b maps continuously to the corresponding path-norm quotient corner completion. The graph and (1+n)^r factors in its norm only strengthen this estimate.

The resulting comparison is injective by stabilized finite endpoint projections and has dense image because it contains all finite-support corners. It is not asserted onto or to have a continuous inverse. Therefore strict exactness proved here must NOT be transferred automatically to a sequence assembled using independently stronger factorization norms.

This explicit distinction avoids claiming exactness of a completion functor without checking its norms.

## 6. Next analytical construction

Use the source module resolution before taking endpoint corners or base change. Construct a completed common pre-quotient/derived receiver for J_1/J_3 whose connecting observation restricts to the nonzero finite product witness. Then compare its forcing and normalized Clark images with the existing balanced two-seam attachment, preserving the source action and relative currents.

The completed associated algebra remains valid; the present result says precisely which additional extension datum it does not determine on its own.

## Verification

`uv run python research/voevodsky/checkers/check_first_filtered_extension.py`

Passed: four-event dimensions (24,234,210), a selected nonzero product coefficient, and 2000 path-weight inequalities. Strict exactness and nonsplitting are the arguments above; the checker does not compute a completed derived functor.
