# Booleanity from Q: exact reflection and retained-witness obstruction

## Checked result

The existing empty-target NAND constructor gives an exact constructive theorem:

\[
N(A,B)=(A\times B)\to\mathbf0,
\]

\[
N\bigl(N(N(A,B),C),N(A,N(N(A,C),A))\bigr)\simeq\neg\neg C.
\]

This holds for all small types A, B, C. No Boolean values, decidability, excluded
middle, or double-negation elimination are assumed in the proof.

Write W(A,B,C) for the left side. The explicit maps are:

\[
\begin{aligned}
\Phi(w)(n_C)
 &=w\bigl(\lambda(n_{AB},c).n_C(c),
          \lambda(a,h).h(\lambda(a',c).n_C(c),a)\bigr),\\
\Psi(d)(x,y)
 &=d\bigl(\lambda c.x(\lambda(a,b).y(a,\lambda(n_{AC},a').n_{AC}(a',c)),c)\bigr).
\end{aligned}
\]

Both types are propositions, so these maps supply an equivalence. Agda checks
the maps and their inverse laws.

Consequently W(A,B,C) is equivalent to C precisely when C is a proposition
with a double-negation eliminator. The forward direction also proves that C
must be a proposition; stability alone is insufficient for arbitrary types.

## A Boolean domain constructed without supplied Boolean indices

Define

\[
D(A)=\neg\neg A,
\qquad
\eta_A(a)(n_A)=n_A(a).
\]

The construction satisfies

\[
D(D(A))\simeq D(A),
\]

and, for every stable proposition P,

\[
(D(A)\to P)\simeq(A\to P).
\]

The equivalence restricts a function along eta. Its inverse extends f using
P's stability witness s:

\[
\overline f(d)=s\bigl(\lambda n_P.d(\lambda a.n_P(f(a)))\bigr).
\]

Thus D is a reflection into double-negation-stable propositions, with the
universal property checked rather than just an idempotence test.

The Agda carrier `StableTruth` consists of small propositions equipped with
stability witnesses. NAND always lands in this carrier: a negation is a stable
proposition. The exact W-to-double-negation theorem supplies Wolfram's identity
on this carrier. Univalence turns the value-type equivalence into a path of
stable propositions. The earlier general converse then constructs an actual
`BooleanStructure StableTruth`, including all lattice and complement laws.
The module also proves its zero and one distinct, so this Boolean algebra is
nontrivial.

The positive construction uses the admitted empty target and arbitrary indexed
P. It does not assume a pre-existing Bool index family or classical logic.
The imported Bool type is used only for a loss counterexample below.

Inside the existing Q code signature,

\[
\operatorname{negCode}(Q)=\prod_{x:\operatorname{El}(Q)}\mathbf0,
\qquad
\operatorname{booleanCode}(Q)=\operatorname{negCode}(\operatorname{negCode}(Q)).
\]

The assumption allowing the empty target remains part of this signature.

## What this changes

The Boolean join is a closed disjunction:

\[
N(N(A,A),N(B,B))\simeq D(A+B).
\]

This equivalence is also proved in Agda. Raw sums retain branch choices and
are not in general stable propositions. Booleanity has therefore been
established for the constructed truth domain and its operations, not for all
original E/P operations on retained data.

A finite Kripke fork makes the change visible. Its worlds are a root r and two
incomparable successors l,u. The upsets {l} and {u} are each double-negation
stable. Their union {l,u} is not; its double negation is {r,l,u}. The Boolean join
is the latter. In particular, stability here does not imply decidability in
the original Heyting logic with its original disjunction.

## Proven limits on retained Q

Agda proves

\[
\eta_{\mathrm{Bool}}(0)=\eta_{\mathrm{Bool}}(1),
\qquad
\neg\bigl(\mathrm{Bool}\simeq D(\mathrm{Bool})\bigr).
\]

Double negation forgets the two retained alternatives. The second result
excludes every equivalence, not just the canonical map eta. Keeping the
original Q alongside the truth result can preserve its data, but does not
make that entire retained package a proposition.

There is a stronger boundary for the current `Complete` representation. Such
a Q already contains a value q of its retained type A. Hence eta(q) inhabits
D(A), and D(A) is contractible. The module proves this for every complete Q.
Using the mere inhabitation of a complete Q as its truth readout always returns
true. A nontrivial truth question about such a Q must concern a specified
predicate or compatibility fibre, which may be empty.

## Verification

Formal source: `agda/QBooleanity.agda`.

The shell runner `checkers/check_q_booleanity.ps1` freshly compiles that module
and its dependencies. It rejects `negative/QBooleanityBadInverse.agda`, whose
proposed inverse of truth reflection fails to recover the true Bool branch.
The stronger impossibility statement is proved in the positive module.

`checkers/check_q_booleanity.py` checks the formal source hashes and finite
Heyting models on a chain, fork, and diamond. It checks W=double-negation for
all triples, stability of every NAND result, Boolean W on the stable subset,
idempotence, and the reflected-join formula. The chain retains a raw W≠C
counterexample; the fork retains the raw-union obstruction.

SCC obligations: forward realization and readout descent. Model
`nima-q-booleanity` passed. Receipts:

- `results/agda-QBooleanity.json`
- `results/q-booleanity-formal-audit.json`
- `results/q-booleanity.json`

The remaining source question is which predicate or compatibility fibre of a
retained Q should carry a particular nontrivial truth assertion. Unrestricted
retained Q cannot be identified with its Boolean truth reflection.
