# Whole-row gain squares have a portable typed structural certificate

## Deliverable

A standalone exact-rational verifier now checks an invertible structural square in the existing finite commuting-action fixture. It checks source-action intertwining, observer transitions, the complete filtered subspaces, pushout relations, and agreement of both routes.

A square with commuting diagonal coordinate maps but incorrectly unchanged action matrices is rejected. Thus scalar route coherence is not substituted for structural compatibility.

This is a finite structural model of the whole-row gain theorem, not yet a certificate identifying a physical 270-row observer or composing with a numerical task square.

## 1. Explicit algebra and scope

The fixture is a bimodule over S=Q[t]/(t^2), with commuting left and right actions. The upper basis is (b,a,n,l,z):

    left t: b->a, n->l;
    right t: b->n, a->l, z->l.

All omitted images are zero. The lower observer has basis (b,a), and the transition kills n,l,z.

For this fixture the depth ideal is explicitly

    J=(t_left,t_right) in the enveloping algebra.

Thus

    M=J E=span(a,n,l), L=J^2 E=span(l),
    K=span(n,l,z), N=K intersect M=span(n,l).

This joint-action flag must NOT be confused with a proof that the fixture satisfies the actual observer's equality I E=E I. Its separate one-sided images need not coincide. The physical theorem retains its own inherited ideal-depth definition and source identification.

The source extension is fixed:

    A=(a,n,l), B=(l), G=(a,n),
    i(l)=l, q(a,n,l)=(a,n).

Left t sends n to l; right t sends a to l. The source flags are (A,A,B,0), (B,B,B,0), and (G,G,0,0). The target flag is (K,N,L,0).

## 2. Typed data and independent checks

`results/structural-gain-square.json` contains a pinned model contract, its digest, four nodes and four edges. Every matrix coefficient is a rational string.

Each node supplies upper/lower gain matrices, actions, the transition, bases for K,M,N,L, the source coefficient map f, an unfiltered nullhomotopy H, the normalized private row, and the pushout graph vector.

The standalone verifier independently checks:

- the algebra relations and evaluation/action compatibility;
- transition equivariance and compatibility with common source evaluation;
- K is the WHOLE kernel, by rank and nullity;
- M and L are the WHOLE declared ideal images;
- N is the WHOLE intersection, by containment and dimension;
- filtration inclusions and stability;
- H i=f, equivariance of H, and its image in K;
- the normalized private witness and its right-action obstruction.

It uses its own Fraction-based matrix arithmetic and rational elimination. It imports no producer, source recorder, discovery checker, SymPy or numerical integration package.

The digest binds the finite problem; it does not authenticate it or establish a physical interpretation.

## 3. Pushout verification without an arbitrary quotient basis

The pushout is represented by

    (K direct_sum A)/span(f(l),-i(l)),

inside the fixed ambient E direct_sum A. The supplied relation is checked, not trusted.

The three filtration levels are represented by

    K direct_sum A,
    N direct_sum A,
    L direct_sum B,

modulo that relation. Their verified dimensions are 5,4,1. Stability is checked under both actions. The graph relation is annihilated by both actions because its components are the socle inclusions.

For an edge with upper map U, the ambient pushout map must be diag(U,id_A). The verifier checks exact transport of the relation and equality of the transported filtration subspaces. Therefore it induces the required filtered pushout isomorphism.

The source remains fixed: these are identity source comparisons, not a certificate for arbitrary source-algebra changes.

## 4. Nonzero filtered class, zero underlying class

At every node the right action annihilates N, while

    right_t(a)=i(l), P(f(l))=1.

An equivariant extension A->N would therefore send f(l) to zero, a contradiction. Evaluation at filtration level two detects the nonsplit extension, as in the owning filtered exact-category argument.

The supplied H lands in K, is equivariant, and extends f, so the underlying unfiltered pushout splits. Both facts are checked at every node, and the edge maps transport the actual filtered extensions, not merely these status labels.

The categorical interpretation uses the standard levelwise exact category of finite flags. The program checks the finite linear-algebra hypotheses; it is not a proof assistant for arbitrary derived categories.

## 5. Coherence and adversarial tests

Both routes from 00 to 11 agree exactly on:

- the upper observer;
- the lower observer;
- the ambient filtered pushout presentation.

The test suite accepts a benign change of basis in N, confirming that displayed basis equality is not confused with subspace equality.

It rejects 12 structural corruptions and three malformed JSON inputs. The central negative test keeps all diagonal maps and route products intact but leaves upper action matrices in the original coordinates. Scalar coordinate routes still commute, yet source evaluation fails to intertwine the actions, and the structural certificate is rejected.

Isolated Python execution succeeds outside the repository using only the verifier and square bundle.

## 6. Relation to the numerical coherence certificates

Nima's `../nima/source-observer-change-squares-have-portable-coherence-certificates.md` checks a different layer: scalar tasks, priors, data intervals and compatible parameter changes. This structural certificate does not automatically identify its nodes with those numerical nodes. A combined certificate still needs the explicit physical/source identification tying them together.

The newer `../nima/vacuum-tail-splitting-has-an-order-independent-restriction-certificate.md` adds noninvertible aggregation restrictions and increasing coordinate counts. Those are outside this verifier's positive-diagonal isomorphism contract. Their structural extension would require typed module restriction maps and a fresh audit of the relevant filtration images; nonvanishing of an extension need not survive an arbitrary noninvertible restriction.

Thus this deliverable supplies one supported structural transition type rather than presenting a general observer-tower verifier.

## Reproduction

Generate the bundle:

    uv run --with sympy python research/voevodsky/checkers/export_structural_gain_square.py

Verify independently:

    python research/voevodsky/certificates/verify_structural_gain_square.py research/voevodsky/results/structural-gain-square.json

Run the adversarial and portability tests:

    python research/voevodsky/checkers/check_structural_gain_square_verifier.py

All pass. Test summary: `results/structural-gain-square-verifier-tests.json`.
