# Formal derived-affine Q-space and Bruce product

Date: 2026-09-08

## Construction

Let `QD_k -> D_k` be a semi-free replacement over the native node ring `B`. The replacement is taken before dualization; this avoids treating the conductor-supported terms of `D_k` as projective. Define

\[
\mathcal O_k=\operatorname{Sym}_{B}((QD_k)^\vee),\qquad
\mathfrak X_k=\operatorname{RSpec}_{B}(\mathcal O_k),\qquad k=35,04.
\]

The dual of the strict differential on `QD_k` extends uniquely as an odd derivation `Q_k` of the free graded-commutative algebra `O_k`. Since the strict `D_k` differential squares to zero, so does this derivation. Thus `(X_k,Q_k)` is a formal derived-affine Q-space over the singular node.

This construction is replacement-independent up to derived affine equivalence when morphisms are interpreted in the derived category. A particular strict coordinate presentation still depends on the selected semi-free replacement.

## Algebraic Bruce product

Bruce's associativity proof uses only graded commutativity, the derivation law and `Q^2=0`. It therefore applies algebraically to `O_k`, without smoothness or functional analysis. Put

\[
a\star b=(-1)^{|a|+1}Q_k(a)b.
\]

For homogeneous `a,b,c`, both `(a star b) star c` and `a star (b star c)` equal

\[
(-1)^{|a|+|b|}Q_k(a)Q_k(b)c.
\]

Hence the formal function algebra has Bruce's odd associative product. The product is nonunital in Bruce's sense even though `O_k` has its ordinary commutative unit.

## Maps and symmetry

Each strict spatial chain map induces, contravariantly, a morphism between the corresponding free formal dg function algebras. The eight zero chain defects therefore give eight formal Q-morphisms. Chain endomorphisms implementing the native operations extend to derivations; chain homotopies extend to derivation homotopies. The marked reflection comparison exchanges the two presentations

\[
(\mathfrak X_{35},Q_{35})\longleftrightarrow
(\mathfrak X_{04},Q_{04}),
\]

rather than acting internally on either fixed marked object. The decomposable antipode terms remain part of the induced algebra maps.

## What this does and does not prove

This closes the existence of an algebraic/formal Q-object carrying the Bruce derived product. It does not turn the singular node into a smooth supermanifold and does not invoke Bruce's nuclear Frechet topology.

Most importantly, the Berezin trace theorem does not follow formally. It requires either:

1. a compact, superoriented, unimodular smooth realization and invariant Berezin volume; or
2. an algebraic trace/residue functional on `O_k`, together with direct proofs of shifted cyclicity, Q-invariance, convergence/completion where relevant, and independence of the semi-free presentation.

The existing primitive sixfold residue is a promising linear functional on the conductor-dual sector, but it has not yet been extended to the full symmetric dg algebra or shown to define the requested P24 cyclic class.

## Verification

Run:

```sh
python research/voevodsky/check_marici_formal_q_space_bruce_extension_20260908.py \
  --root . \
  --output research/voevodsky/marici_formal_q_space_bruce_extension_certificate_20260908.json
```

The checker audits the strict input, all parity cases in Bruce associativity, eight induced formal Q-morphisms, and the marked reflection pairing. It performs 66 integration checks.
