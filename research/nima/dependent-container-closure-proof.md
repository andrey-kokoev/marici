# Dependent Sigma/Pi grammar: finite normal-form schemas and closure

## Input grammar

An expression is an atomic type, a dependent sum Sigma(i:I).E_i, or a dependent product Pi(i:I).E_i. The index I and family E are specified at that node. Branch families may depend on every surrounding index. The Python realization enumerates finite indices and uses labeled atomic types; the written argument concerns small types in a universe closed under these constructors, with function extensionality.

Normal data for an expression E consists of a type S of complete choices, positions P(s), atomic types A(s,p), and an equivalence

E ~= Sigma(s:S). Pi(p:P(s)). A(s,p).

The original expression, the child normalizations and the generating comparison at every node are retained alongside this presentation. No witness is reduced to a count.

## Three uniform schemas

### Atomic type A

S=Unit; P(*)=Unit; A(*,*)=A. The equivalence is the unit-indexed pair/function equivalence.

### Dependent sum

Assume each E_i has normal data S_i,P_i,A_i. For Sigma(i:I).E_i set

S := Sigma(i:I). S_i,
P(i,s) := P_i(s),
A((i,s),p) := A_i(s,p).

The equivalence associates the dependent sums and retains i. Its inverse restores the selected branch.

### Dependent product

For Pi(i:I).E_i set

S := Pi(i:I). S_i,
P(f) := Sigma(i:I). P_i(f(i)),
A(f,(i,p)) := A_i(f(i),p).

Its full comparison chain is

Pi(i:I). E_i
 ~= Pi(i:I). Sigma(s:S_i). Pi(p:P_i(s)). A_i(s,p)
 ~= Sigma(f:Pi(i:I).S_i). Pi(i:I). Pi(p:P_i(f(i))). A_i(f(i),p)
 ~= Sigma(f:Pi(i:I).S_i). Pi(z:Sigma(i:I).P_i(f(i))).
       A_fst(z)(f(fst(z)),snd(z)).

The middle step is constructive dependent distributivity. It selects the function f of branch choices; the final step changes the positions to a dependent sum. Forward and inverse maps are tuple projection and dependent function application. No propositionally truncated existence or additional choice axiom is used. Function extensionality supplies the requisite function inverse paths.

## Written closure argument

Structural induction on the input expression constructs this normal data and its equivalence. Each schema invokes only child expressions, so normalization terminates on finite syntax trees. The normal type itself is a Sigma/Pi expression with the same atomic leaves. It is therefore a valid input to the same construction again. A second normalization preserves all values through its specified equivalence; record shapes need not be literally equal because a new presentation includes new unit/position packaging.

This is a finite schema description at arbitrary expression depth. It extends the fixed-binary experiment by allowing variable and dependent choice and position types. An opaque atom need not be split or inspected.

Closure here is closure of the expression grammar. Freely varying equivalence proofs or asking the normalizer to process the whole proof record as an atomic source raises the separate higher-coherence semantics question. The retained record makes that question explicit rather than supplying an automatic answer.

## Concrete realization

`dependent_container_normalizer.py` uses three records: Atom, Binder and Normal. Normal stores its original source, all child normalizations, the rule name, complete choice shapes and positions with full source paths and atomic type labels. Encoding and decoding preserve the original payload references. Evaluation order of independent child normalizations can be reversed without changing the resulting record.

The earlier I,J,K,L,B example yields 8 dependent choice shapes and 18 values. The source and target value sets are independently enumerated and agree by reversible maps. Re-expressing the normal data as a new syntax tree passes a second round trip. Tests also cover 64 finite expression examples, empty sums (no shapes), empty products (one shape with no positions), opaque payload preservation and missing-witness refusal.

The executable realization is finite and set-valued. The general induction above is written mathematical reasoning, not a proof-assistant certificate. It establishes a normal presentation and reconstruction, rather than a complete classification of equivalences between arbitrary atomic types.

Implementation: `research/nima/checkers/dependent_container_normalizer.py`.
Checker: `research/nima/checkers/check_dependent_container_normalizer.py`.
Result: `research/nima/results/dependent-container-normalizer.json`.
