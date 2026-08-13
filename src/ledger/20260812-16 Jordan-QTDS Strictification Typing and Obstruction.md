# Jordan-QTDS Strictification: Typing and Obstruction

## Record

Date: 2026-08-12

Status: a choice-valued QTDS operation on the bare half-class is obstructed. Entry 19 promotes the
complete period family to a pointed cohomological factorization lift. Entry 20 derives the exact
six-point QTDS redistribution from the scalar cubic-cell grade. A scalar dg/Jordan-colored chain
resolution remains open.

## Core verdict

The symbol

\[
\operatorname{Strict}_J:\mathsf J\longrightarrow
\text{one QTDS presentation}
\]

is not correctly typed if \(\mathsf J\) means only the permutation-covariant twisted-cohomology
class

\[
\mathsf J_n=[(\operatorname{Pf}'A_n)^2]\in H_n^+.
\]

The class fixes amplitudes and their factorization data. It does not fix a cyclic ordering, an
alternating polarity assignment, a target Jordan pair, or a local graph presentation. Calling the
identity map on \(\mathsf J\) a strictification would preserve the class but encode none of the
quartic grammar.

The corrected statement is:

> QTDS is an intrinsic finite presentation of an **order-enriched scalar rank sector**. It is not
> a canonical presentation selected by the bare universal half-class.

This is a constructive obstruction, not a failure of QTDS or of the three-generator CHY table.

## Where the cyclic order enters

The scalar pairing is typed as

\[
I_n:H_n^-\otimes H_n^+\longrightarrow K_n,
\]

and an ordered NLSM period is

\[
a_{R,n}(\alpha)
=
I_n(\operatorname{PT}_\alpha,\mathsf J_n).
\]

The QTDS rules begin with precisely this additional datum: a fixed planar cyclic ordering
\(\alpha\), around which adjacent legs receive opposite bookkeeping polarities. The source
explicitly says that the polarities are not physical charges and that QTDS is an auxiliary local
theory reproducing flavor-ordered amplitudes, not a conventional field redefinition.

For even labels \(L\), define the alternating cyclic cover

\[
\widetilde{\operatorname{Cyc}}(L)
=
\left\{
(\alpha,\varepsilon):
\varepsilon(\alpha_{i+1})=-\varepsilon(\alpha_i)
\right\}.
\]

The projection

\[
\pi:\widetilde{\operatorname{Cyc}}(L)
\longrightarrow
\operatorname{Cyc}(L)
\]

has a two-element fiber, exchanged by the global polarity flip \(\tau\).

## Symmetry no-go for an absolute choice

Suppose the bare, permutation-invariant \(\mathsf J_L\) naturally selected one QTDS fiber
\(s(\mathsf J_L)=(\alpha,\varepsilon)\). For every label permutation \(\sigma\), naturality would
give

\[
\sigma s(\mathsf J_L)
=
s(\sigma\mathsf J_L)
=
s(\mathsf J_L).
\]

No cyclic ordering with an alternating coloring is fixed by all of \(S_L\) when \(|L|\geq4\).
Therefore there is no permutation-equivariant operation that selects a single QTDS presentation
from the bare class.

This does not obstruct an equivariant object containing **all** fibers. It obstructs only the
unqualified choice-valued endomorphism previously denoted \(\operatorname{Strict}_J\).

## A second obstruction: target data are forgotten

For a rectangular Jordan pair,

\[
V^+=\operatorname{Mat}_{p\times q},
\qquad
V^-=\operatorname{Mat}_{q\times p},
\]

with trace pairing and

\[
Q_y(x)=yxy,
\]

the QTDS interaction can be written as

\[
2\left\langle
\partial\psi^+,
Q_{\psi^-}(\partial\psi^+)
\right\rangle.
\]

After target indices are stripped, different choices of \((p,q)\), and potentially different
Jordan-pair realizations, give the same universal kinematic vertex

\[
V_4(+,-,+,-)=-2k_1\!\cdot k_3.
\]

Thus the forgetful map from Jordan realizations to the stripped class \(\mathsf J\) is many-to-one.
The quadratic map \(Q\) cannot be reconstructed canonically from \(\mathsf J\); it must be
retained as rank-jump provenance or supplied as target data.

## The positive order-relative lift

Let \(\mathcal P^{\rm QTDS}_{n,\alpha,\varepsilon}\) be the module spanned by planar quartic trees
with:

1. alternating external polarities determined by \((\alpha,\varepsilon)\);
2. a \(+\!\! -\) propagator \(1/K^2\);
3. the quartic corolla \(-2k_1\cdot k_3\).

Let

\[
\operatorname{Ev}_{\alpha,\varepsilon}:
\mathcal P^{\rm QTDS}_{n,\alpha,\varepsilon}
\longrightarrow K_n
\]

sum and evaluate its trees. Combining scalar descent with the all-tree QTDS equivalence gives,
in the scalar-shift sign convention used by the exact audit,

\[
\operatorname{Ev}_{\alpha,\varepsilon}(q_n^{\rm QTDS})
=
(-1)^{n/2-1}
I_n(\operatorname{PT}_\alpha,\mathsf J_n).
\]

The overall sign is removed by the corresponding convention for the quartic coupling. The deck
flip obeys

\[
\operatorname{Ev}_{\alpha,\varepsilon}(q_n^{\rm QTDS})
=
\operatorname{Ev}_{\alpha,-\varepsilon}(q_n^{\rm QTDS})
\]

at tree level, although the individual diagram contributions generally differ.

This establishes a finite, uniform **relative presentation of every ordered period**. It does not
yet construct an object in \(H_n^+\) before attachment of \(\operatorname{PT}_\alpha\).

## What a genuine half-object strictification would be

Retain the scalar normal provenance and Jordan data in an enriched object \(\mathsf J^R_P\). A
non-vacuous strictification should begin as a two-colored cyclic factorization presentation

\[
\operatorname{Strict}^{\rm QTDS}_{P}(\mathsf J^R)
=
(\mathcal Q_P,a_P,T_\tau),
\]

where

\[
a_P:\mathcal Q_P\longrightarrow\pi^*\mathcal C^R_{J,P}
\]

is an augmentation into a declared chain model \(\mathcal C^R_{J,P}\), and \(T_\tau\) coherently
identifies the two global-polarity fibers. It may be called a quasi-isomorphism only after both
sides and their differentials are constructed and the full homology is compared. Equality of the
distinguished class against a complete period basis is enough for a pointed lift, not for that
stronger claim. For every compatible boundary \(D\), the augmentation must satisfy

\[
\rho_Da_P
=
(a_{P,L}\otimes a_{P,R})\Delta_D.
\]

The presentation kernel must also be a congruence under cutting and sewing. If

\[
\mathcal K_n=\operatorname{hofib}(a_{P,n}),
\]

then the minimum condition is

\[
\operatorname{Cut}_D(\mathcal K_n)
\subseteq
\mathcal K_L\otimes\mathcal Q_R
+
\mathcal Q_L\otimes\mathcal K_R.
\]

Without this condition, terms erased by the final tree sum may reappear after composition. QTDS
would then remain an excellent ordered-amplitude compiler, but not a reusable strictification of
the half-object.

## Jordan coherence and its perimeter

For rectangular matrices, the Jordan fundamental formula

\[
Q_{Q_x y}=Q_xQ_yQ_x
\]

is an exact matrix identity: both sides act on the complementary slot by the same alternating
matrix word. This validates the advertised special Jordan realization.

It does **not** prove that all Jordan pairs give the same NLSM half-object, nor that all
same-spectrum bi-polar quartic strictifications are Jordan pairs. The QTDS source does not make a
Jordan classification claim. The proposed eight-point coherence obstruction

\[
\mathfrak d^\sigma(x,y)
=
Q^\sigma_{Q^\sigma_x y}
-
Q^\sigma_xQ^{-\sigma}_yQ^\sigma_x
\]

is therefore a next falsifier, not yet a derived amplitude theorem.

## Constructor-theoretic reading

The useful task is not \(\mathsf J\mapsto\mathsf J\). It is a compiler with an explicit program
attribute

\[
p=(\alpha,\varepsilon,P,\nu),
\]

where \(P\) is the Jordan realization and \(\nu\) contains normalization and representative
conventions:

\[
(\mathsf J_n,p,0)
\longrightarrow
(\mathsf J_n,p,q_{n,p}).
\]

This is presently an algebraic analogy, not a proof of physical constructor-theoretic possibility.
Its explanatory gain is precise: one finite reusable grammar implements all multiplicities, while
all control data and all discarded presentation differences are explicit. A physical substrate
would additionally have to implement the task repeatably and make the discarded kernel stable
under every allowed composition.

## Decisive next tests

1. Construct a six-point augmentation from the three quartic trees into a twisted half-chain
   model and produce the Catalan contact cohomologically, before a single PT period is chosen.
2. Evaluate the same candidate against a complete PT basis. Agreement only with its defining
   order proves partner-relative status.
3. Compare the inequivalent eight-point nestings and identify whether their obstruction is the
   polarized Jordan defect.
4. Transport between adjacent cyclic orders and test braid or cocycle coherence of the required
   homotopies.
5. Pair the same enriched object with \(\mathsf G\) and \(\mathsf J\). Partner-dependent repair
   terms would locate QTDS in the \(\mathsf C\)-\(\mathsf J\) pairing rather than in \(\mathsf J\).
6. At surfaces, test whether the modular envelope reproduces the scalar-selected cut-free
   curvature, beginning with \(\omega_{1,2}=2\).

## Sources and provenance boundary

- [Cao, Han, and Zhu, *NLSM amplitudes from a quartic two-derivative theory*](https://arxiv.org/html/2607.27345v1)
  supplies the QTDS rules, tree proof, generalized-cut statement, and polarity qualifications.
- [Caveny and Smirnov, *Categories of Jordan Structures and Graded Lie Algebras*](https://arxiv.org/abs/1106.2447)
  supplies a categorical Jordan-pair/graded-Lie-algebra relation, not the Marici strictification
  theorem.
- [Deutsch and Marletto, *Constructor Theory of Information*](https://arxiv.org/abs/1405.5563)
  motivates the explicit task/program/kernel audit. The constructor-theoretic interpretation here
  is Marici's application, not a claim attributed to those authors.

## Decision

Replace the absolute primitive operation \(\operatorname{Strict}_J\) by the typed research target

\[
\operatorname{Strict}^{\rm QTDS}_{P}:
\mathsf J^R_P
\longrightarrow
\mathcal Q_P
\quad\text{over}\quad
\widetilde{\operatorname{Cyc}}_{\rm even}.
\]

The bare-class selection problem is closed negatively. Entry 19 establishes all-fibers descent at
the pointed cohomology and tree-factorization level. Entry 20 shows that the six-point flip flow
is invisible to the summed scalar amplitude but is exactly recovered from its cubic-cell grade
and alternating parity-core transfer. The scalar dg augmentation remains open. Entry 18
distinguishes the nonexistence of a natural section from all-fibers descent.
