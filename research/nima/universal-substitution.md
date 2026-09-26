# Selecting obligations by universal substitution

## Result and its boundary

A stronger requirement than identity, inverse and composition laws is:

**Admit a comparison exactly when substitution along it is reversible in every
specified typed continuation, while respecting the selected-value boundary.**

The equivalence with actual invertibility is now proved in Agda for all small
value types. The same substitution framework gives the dependent E/P
adjunctions and uniqueness of candidate sums/products by their universal
properties. These results constrain the semantic roles of the constructors;
they do not derive type theory or all twelve resolution schemas from a bare Q.

SCC obligations: forward realization, route/coherencer compatibility and
readout descent. Model: `nima-universal-substitution`.

## Comparison selection: all continuations reduce to two targets

For f:A to B, substitution is

\[
f_X^*:(B\to X)\to(A\to X),
\qquad f_X^*(h)=h\circ f.
\]

The checked theorem is

\[
\left(\prod_{X:\mathcal U}\operatorname{isEquiv}(f_X^*)\right)
\simeq\operatorname{isEquiv}(f).
\]

It suffices to have reversibility at targets A and B. The proof constructs the
inverse rather than assuming it:

1. Invert substitution at target A on the identity map to obtain g:B to A
   with g composed with f equal to the identity of A.
2. At target B, substitution of f composed with g and of the identity of B
   gives equal maps out of A.
3. Injectivity of that substitution gives f composed with g equal to the
   identity of B.

Conversely, an inverse to f supplies inverses to every substitution map.
`universal-characterization` checks an equivalence of the property types,
not only a one-way implication.

With the selected-value condition

\[
f(v_a)=v_b,
\]

the module reconstructs the existing comparison filler K(a,b). It does not
assume an equivalence witness in this selection interface.

This rejects the previous identity-only policy **if admission is required to
include every map meeting the universal condition**. A policy required only
to admit sound comparisons may still omit some. Completeness of admission is
an explicit part of the proposed requirement, not a consequence of soundness.

## E and P as universal context extensions

For a context extension indexed by a family A over I, the proved adjunctions
are

\[
\prod_{i:I}\left(\left(\sum_{a:A(i)}B(i,a)\right)\to C(i)\right)
\simeq
\prod_{i:I}\prod_{a:A(i)}(B(i,a)\to C(i)),
\]

\[
\prod_{i:I}\prod_{a:A(i)}(C(i)\to B(i,a))
\simeq
\prod_{i:I}\left(C(i)\to\prod_{a:A(i)}B(i,a)\right).
\]

E and P are respectively the left and right adjoints to substitution along
this context projection. Both maps and inverse laws are explicit in Agda.

There are also candidate-selection theorems:

- If a type S with injections from each A(i) gives unique extension of every
  typed family of maps, its induced map from the dependent sum is an equivalence.
- If a type P with projections into each A(i) gives unique assembly of every
  typed family of maps, its projection into the dependent product is an
  equivalence. Testing maps from Unit already suffices in this ambient type
  setting.

Uniqueness means an equivalence of map types, retaining the maps. Existence
alone permits surplus data; uniqueness without existence can miss required
assignments. The finite controls test both failures separately.

These theorems characterize candidate values up to equivalence. They neither
select the index family nor force equality of retained constructor syntax.

## Three checks against overstatement

### 1. Truth-only continuation tests are too weak

The collapse from Bool to Unit passes substitution tests into every
proposition P: a function into P cannot distinguish its arguments. Agda proves
this quantified statement, and also proves that the collapse is not invertible.

This must not be confused with **Bool-valued functions**. Bool is a type with
two distinguishable values, not a proposition. The Bool-valued identity test
detects the collapse, and its substitution map is formally proved noninvertible.
A single inhabitation readout and the whole space of Boolean-valued predicates
carry different information.

### 2. Value contexts and full retained contexts differ

The unit package and its unit-indexed E assembly pass every value-level
continuation test. Their retained constructor tags are different, and Agda
proves that the full packages are not equal.

If a proposed transport works for every family P over complete packages,

\[
\prod_{P:\operatorname{Complete}\to\mathcal U_1}P(a)\to P(b),
\]

then applying it to the family

\[
P(q)=(a=q)
\]

produces a path a=b. A path conversely supplies all these transports. The
module proves these two implications; it does not identify arbitrary families
of transport witnesses with paths.

Thus unit-to-E-assembly passes the value criterion and fails this full-retained
criterion. The preservation requirement must specify its context language.

### 3. Retaining the input cannot alone select operations

For every map f, form its graph

\[
\Gamma_f=\sum_{a:A}\sum_{b:B}(f(a)=b).
\]

The map

\[
a\longmapsto(a,f(a),\operatorname{refl})
\]

is an equivalence from A to its retained graph. This universe-polymorphic
statement and exact input recovery are checked. It applies even when f itself
loses information. Reversible embedding into a package retaining the input
must therefore be distinguished from reversible passage to the output B.

## Remaining source obligation

“All continuations” in the proved selection theorem means all functions in
the ambient type theory. It does **not** mean that the existing resolution
closure has generated all those functions from a given seed family S.

The comparison rule can consume the reconstructed evidence once it is supplied.
A derivation of the required continuation tests from the operating structure
remains a separate obligation. The two-target theorem gives exact interfaces
for this investigation: reversibility of substitution into A and into B.
It is not a finite decision procedure for arbitrary types.

The subsequent [generated-context audit](generated-continuation-contexts.md)
constructs these certificates for swap and currying in an explicit typed
program fragment, and identifies how the original rule parameters can carry
already-supplied functions.

The common candidate principle is now universal solution of typed substitution
problems, with the boundary and solution retained. To turn this into a
source-derived rule-selection theorem, we still need the source's admissible
context language and derivations of the corresponding universal witnesses.
The distinction between value contexts, retained contexts and generated
contexts cannot be omitted.

## Verification

- Formal source: `agda/UniversalSubstitution.agda`.
- Shell runner: `checkers/check_universal_substitution.ps1`.
- Intended rejection: `negative/SubstitutionBadTruthTest.agda`, where a
  purported inverse fails to recover an arbitrary Bool-valued continuation.
- Audit: `checkers/check_universal_substitution.py`, including all 60 maps
  between finite carriers of cardinalities zero through three; sum/product
  existence and uniqueness controls; graph retention and context separation.
- Receipts: `results/agda-UniversalSubstitution.json`,
  `results/universal-substitution-formal-audit.json`, and
  `results/universal-substitution.json`.

Fresh safe/cubical compilation, the intended rejection, and the SCC audit
passed. The finite tests are controls; the universal results are Agda proofs.
