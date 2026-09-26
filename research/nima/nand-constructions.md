# NAND from indexed E/P constructions

## Problem and scope

Can the constructors form NAND, and which structure does each route consume?
SCC obligations: **forward realization**, **route/coherencer compatibility**, and
**readout descent**. Model: `nima-nand-constructions`. Its finite checker passed;
the formal runner separately checked the Agda closure and two rejection controls.
This packet does not derive a Boolean domain for unrestricted Q. The subsequent
[general converse and Boolean operation roundtrips](wolfram-nand-equivalence.md)
are now formally checked. The September binary grammar already supplies Bool;
its fixed binary indexing is narrower than the arbitrary indexed constructors
used here.

The comparison domain is the family

\[
T(0)=\mathbf0,\qquad T(1)=\mathbf1.
\]

These are truth **types**. An empty truth type has no inhabitant. A false bit is
still a value of Bool; these two uses must not be conflated. The finite checker
also tests actual function spaces for input cardinalities zero through three.

## 1. Joint input followed by an empty-target product

Use E to form the joint input and P to form its refutations:

\[
Z=\sum_{i:\varnothing}\mathbf1,
\qquad
J(A,B)=\sum_{a:A}B,
\qquad
N(A,B)=\prod_{j:J(A,B)}Z.
\]

Thus

\[
N(A,B)\simeq(A\times B)\to\mathbf0.
\]

When the joint index is empty, the product has its unique empty function. When
both truth types are inhabited, a function to the empty target is impossible.
The resulting Boolean table is

| A | B | N(A,B) |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No NOT operation is primitive here. The requirements are an **empty index** and
permission for the P index to depend on the joint input. Forming the empty sum
uses E but still requires admitting the empty index; emptiness has not been
generated from exclusively inhabited fixed indices.

`NandConstructions.agda` instantiates the existing `E` and `Pi` constructors,
checks the empty-sum equivalence and proves

\[
N(T(a),T(b))\simeq T(\operatorname{nand}(a,b)).
\]

The Boolean function is a reference table whose connection to the constructed
type is proved, rather than used as the definition of that type. An actual
seed-free `Pi-rule` derivation over the empty joint index is also included.

## 2. Nested P route

\[
N'(A,B)=\prod_{a:A}\prod_{b:B}\mathbf0.
\]

The comparison is currying:

\[
\Phi(f)(a)(b)=f(a,b),
\qquad
\Psi(g)(a,b)=g(a)(b),
\qquad
\Psi\Phi=1,
\qquad
\Phi\Psi=1.
\]

This is an equivalence of retained value types for arbitrary small A and B,
without decidability. The Agda module retains the comparison through the existing
resolution constructor and forms another complete Q containing its derivation.
The comparison instance takes an explicit joint-refutation witness; no witness
for the inhabited/inhabited case is asserted.

Requirements are the same as route 1. This comparison is currying; it is not a
claim that fixed-index EP and PE commute without the required reindexing.

## 3. Alternative refutations

\[
D(A,B)=(A\to\mathbf0)+(B\to\mathbf0).
\]

A tagged refutation maps to a joint refutation. On the supplied decidable truth
types its inhabitation agrees with NAND. At A=B=0, however,

\[
D(\mathbf0,\mathbf0)\simeq\mathbf1+\mathbf1,
\qquad
N(\mathbf0,\mathbf0)\simeq\mathbf1.
\]

The tag records which input was refuted. There are two retained choices on the
left, and one joint-refutation function on the right. A Boolean inhabitation
readout identifies those choices. Propositional truncation also removes their
distinction; E itself retains it. A general constructive inverse into the raw
sum is not supplied. Deciding one input is sufficient to choose a side from a
joint refutation; that choice does not make the raw sum equivalent to N.

## 4. Marked-square and subset-complement routes

Let

\[
V=\{(0,0),(0,1),(1,0)\},
\qquad
p:V\hookrightarrow\{0,1\}^2,
\qquad
F(a,b)=\sum_{v:V}(p(v)=(a,b)).
\]

The fibre is inhabited precisely at the NAND-true corners. This construction
requires choosing (1,1) as the forbidden corner. The unmarked square does not
select it: the four possible excluded corners give four different tables,
and rotating the square changes this chosen V. The negative boundary is
supplied in the source relation.

For a universe U, another realization is

\[
N_U(A,B)=U\setminus(A\cap B).
\]

The checker tests the powerset of a three-element U: 512 triples satisfy the
stated Wolfram identity, with Boolean NAND at each membership coordinate. This
route requires relative complement. Membership complementation is decisive;
intersection alone does not supply it.

## 5. Fixed positive E/P test and non-Boolean hostile

In the finite Boolean inhabitation shadow, fixed-index E is OR and fixed-index
P is AND. Start with two input projections and constants 0 and 1. Exhaustive
closure gives exactly six functions:

\[
0,\quad1,\quad a,\quad b,\quad a\wedge b,\quad a\vee b.
\]

Every expression in this fixed covariant fragment is monotone, by structural
induction. NAND is absent. Coherence rearrangements preserving the interpreted
construction do not change this readout. Allowing an input type to become the
**domain** of P changes that condition: the domain occurs contravariantly. The
empty-target routes exploit precisely that permission. The six-function result
is not a no-go theorem for arbitrary dependent E/P constructors.

Starting with NAND and the two projections gives all sixteen two-input Boolean
functions. Explicit formulas checked in the finite model are

\[
\neg a=a\mid a,
\qquad
a\wedge b=(a\mid b)\mid(a\mid b),
\qquad
a\vee b=(a\mid a)\mid(b\mid b).
\]

General constructive truth types need not form a Boolean algebra. The upward
closed sets of the chain 0<1 form a three-element Heyting algebra. Use joint
refutation as NAND there and take

\[
a=b=\varnothing,\qquad c=\{1\}.
\]

Then

\[
((a\mid b)\mid c)\mid(a\mid((a\mid c)\mid a))=\{0,1\}\ne c.
\]

Thus constructing joint refutation does not establish Booleanity of arbitrary
Q. The Agda proof of this identity is explicitly restricted to Bool. It does
not show that the identity alone axiomatizes Boolean algebras.

## Verification and scientific delta

- `agda/NandConstructions.agda`: constructor instances, empty-target comparison,
  curry isomorphism, four Boolean realization equivalences, eight identity
  cases, retained resolution derivation, and a vacuous Pi-rule derivation.
- `checkers/check_nand_agda.ps1`: shell-run fresh positive closure; rejects a
  false NAND value and identification of the two tagged alternatives. Both
  controls failed with the expected unequal-term diagnostic.
- `checkers/check_nand_constructions.py`: 16 finite function-space comparisons,
  four marked-corner alternatives, 512 powerset identity cases, positive closure,
  NAND closure, and the explicit non-Boolean hostile.
- `results/nand-formal-audit.json`, `results/agda-NandConstructions.json`,
  `results/nand-constructions.json`: receipts and bounded outcomes.

The construction is now explicit inside the full indexed E/P signature: P over
an E-constructed joint input, with an empty E target. Its Boolean behavior is
proved on the declared truth family. The source requirements are visible, and
the alternative-refutation route demonstrates where a Boolean readout loses
retained derivation choices. The next open constructor question is whether the
intended source specification itself selects the empty/input-dependent indices
and a Boolean comparison domain.
