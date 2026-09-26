# Wolfram's identity and Boolean NAND: checked converse and roundtrips

## Result

For a nonempty set A with a binary operation satisfying

\[
((a\mid b)\mid c)\mid\bigl(a\mid((a\mid c)\mid a)\bigr)=c,
\]

we construct a complemented bounded distributive lattice on A and prove that
its NAND is the original operation. Conversely, NAND in any such Boolean
algebra satisfies this identity. Reconstructing its negation, meet, join, zero,
and one returns the original operations/constants pointwise.

These are quantified Agda proofs with no finite-carrier assumption. The
Boolean algebra may be trivial. Nonemptiness supplies an element from which
the constants are constructed; the constants are independent of its choice.
The `isSet` hypothesis places the result in ordinary algebra. The underlying
equational derivations themselves work with path equalities of types.

SCC obligations: forward realization in both directions and operation-roundtrip
compatibility. Model: `nima-wolfram-converse`.

## Reconstruction

Writing the formulas in the original stroke notation, derived commutativity
identifies the constructed operations with

\[
\neg a=a\mid a,
\qquad
a\wedge b=(a\mid b)\mid(a\mid b),
\qquad
a\vee b=(a\mid a)\mid(b\mid b).
\]

For any chosen e in A,

\[
1=e\mid(e\mid e),
\qquad
0=1\mid1.
\]

The implementation initially reverses the stroke to match the published
certificate. Commutativity is derived before using that identification; it is
not an additional assumption.

`WolframBooleanAlgebra.agda` proves commutativity, associativity, idempotence,
absorption, both distributive laws, the unit laws, and the complement laws.
`BooleanNandEquivalence.agda` packages these in `BooleanStructure`, whose fields
are the explicit bounded distributive lattice and complement equations. It
then proves

\[
a\mid b=\neg(a\wedge b).
\]

The converse module assumes only `BooleanStructure`, derives complement
uniqueness, double negation and De Morgan, and proves Wolfram's identity.
Its `Roundtrip` module checks all five operations/constants. No Boolean law is
assumed in the forward reconstruction from the single identity.

## Equational certificate provenance

The identity is the mirror of Sh_2 in:

William McCune, Robert Veroff, Branden Fitelson, Kenneth Harris, Andrew Feist,
and Larry Wos, *Short Single Axioms for Boolean Algebra*, Journal of Automated
Reasoning 29 (2002), 1–16.

Published certificates:

- <https://www.cs.unm.edu/~mccune/papers/basax/Sh-2.proof>
- <https://www.cs.unm.edu/~mccune/papers/basax/Sh-1.proof>
- Source index: <https://www.cs.unm.edu/~mccune/papers/basax/>

The preserved certificates are `results/Sh-2.proof` and `results/Sh-1.proof`.
The first reaches enough positive equations to derive Sh_1; the second reaches
the three classical Sheffer axioms. The final refutation clauses are not used
as assumptions. The bridge from the first certificate to Sh_1 is explicit.

`checkers/build_wolfram_converse.py` replays 92 and 67 positive equations,
including their starting equations, and emits `agda/WolframConverse.agda`.
Paramodulation becomes substitution and congruence; demodulation becomes an
explicit equality rewrite; reversals and chains become symmetry and
transitivity. Agda independently checks every generated term. The generator
and the downloaded proof annotations are not trusted inference primitives.
There are no postulates or unchecked solver results in the formal modules.

## Connection to Q/E/P

The earlier construction remains

\[
N(A,B)=\prod_{x:\sum_{a:A}B}\mathbf0,
\qquad
T(0)=\mathbf0,
\qquad T(1)=\mathbf1.
\]

`QBooleanNandBridge.agda` instantiates the general converse using the previously
proved Boolean identity, and composes the existing realization equivalence with
the recovered-operation path:

\[
N(T(a),T(b))\simeq T\bigl(\neg_B(a\wedge_B b)\bigr).
\]

Thus the actual indexed constructor realization and the Boolean structure
reconstructed from Wolfram's axiom are connected by a checked equivalence.
A subsequent [Boolean reflection construction](q-booleanity.md) supplies a
nontrivial Boolean truth domain and proves exactly what retained information
it loses. Empty/input-dependent indexing remains an admitted constructor
capability.

## Controls and scope boundaries

`checkers/check_wolfram_converse.ps1` runs a fresh headless compilation of
`QBooleanNandBridge`, including all converse and roundtrip dependencies. It
then checks two intended failures:

1. Boolean conjunction substituted for the axiom's stroke fails at 0,0,1.
2. Replacing the commutativity derivation by reflexivity is rejected even with
   Wolfram's identity available as a hypothesis.

`checkers/check_wolfram_converse.py` checks source hashes against that fresh
receipt, replays the certificates, and enumerates finite hostile models:

| Carrier size | Operations satisfying the identity | Enumeration scope |
|---|---:|---|
| 0 | 1 | all operations; the identity is vacuous |
| 1 | 1 | all operations; trivial Boolean algebra |
| 2 | 2 | all 16 operation tables |
| 3 | 0 | all 19,683 operation tables |
| 4 | 12 found | Boolean NAND under every relabeling; not all size-four operations |

On the fixed labels 0,1, the two tables are literal NAND and literal NOR.
Reconstruction assigns the latter the opposite zero/one labels. The identity
therefore specifies Boolean NAND structure, not an external truth labeling,
nontriviality, or a two-element carrier. The empty model explains the explicit
inhabitant parameter needed to reconstruct constants.

Formal root: `agda/QBooleanNandBridge.agda`.
Fresh receipt: `results/agda-QBooleanNandBridge.json`.
Control receipt: `results/wolfram-converse-formal-audit.json`.
Combined audit: `results/wolfram-converse.json`.

All formal checks and the SCC audit passed. The finite enumeration supplies
controls; the quantified equivalence is established by the Agda proofs.
