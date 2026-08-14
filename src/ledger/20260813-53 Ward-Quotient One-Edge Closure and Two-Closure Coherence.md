# Ward-Quotient One-Edge Closure and Two-Closure Coherence

## Record

Date: 2026-08-13

Status: the unrestricted arbitrary-environment one-edge closure statement is
false.  Null on-shell momentum is not enough to make physical-projector sewing
reference independent.  A corrected one-edge theorem holds in the physical
polarization quotient under an aligned Ward condition, and its two-edge
coherence is the ordinary interchange law for two categorical traces.  This
does give an induction on graph cycle rank, but only conditionally on an
all-graph realization hypothesis that entry 52 proves for the marked-theta
cell, not for arbitrary graph environments.

The main conclusions are:

1. the free resolved curve-cover gluing theorem of entry 52 remains strict;
2. physical Gram specialization is natural for one closure only after passing
   to the correct Ward quotient;
3. two closures commute even when the product of their longitudinal projector
   terms is nonzero;
4. a proof based on universal vanishing of nested longitudinal terms is false;
5. premature replacement of resolved closed carriers by (D) still cannot be
   used in any statement that must later commute with Cuts.

Reproducible certificates:

```text
research/nima/check_one_edge_closure_ward.rs
research/nima/check_marked_handle_symbolic_identity.rs
research/nima/check_marked_handle_x_dictionary.rs
```

## The four levels that must remain separate

Let (E) be a set of unsewn edge pairs.

The resolved strand/curve-cover object is the free module

\[
\mathsf{Cov}^{\rm res}(G\setminus E),
\]

whose generators retain actual open strands and tagged closed curves.  Its
gluing maps

\[
\operatorname{Gl}_e^{\rm res}:
\mathsf{Cov}^{\rm res}(G\setminus E)
\longrightarrow
\mathsf{Cov}^{\rm res}(G\setminus(E\setminus\{e\}))
\]

are topological sewing of embedded one-manifolds.  For distinct open pairs,

\[
\operatorname{Gl}_e^{\rm res}
\operatorname{Gl}_f^{\rm res}
=
\operatorname{Gl}_f^{\rm res}
\operatorname{Gl}_e^{\rm res}.
\]

This is a statement before Gram specialization and before any closed carrier
is evaluated.

Physical Gram specialization lands first in a multilinear physical-state
quotient, not directly in a scalar polynomial ring.  For a null momentum
(p), define

\[
H_p=p^\perp/\langle p\rangle.
\]

A reference vector (q), with (p\cdot q\ne0), chooses the familiar tensor
representative

\[
\Pi_p(q)^{\mu\nu}
=
-\eta^{\mu\nu}
+\frac{p^\mu q^\nu+q^\mu p^\nu}{p\cdot q},
\]

but the sewn state is the reference-independent trace in (H_p).  The
projector is a choice of representative of that trace.

The resolved closed-curve counit is still

\[
\operatorname{ev}_\rho
[\gamma;\nu_\gamma,\Delta_\gamma]
=\nu_\gamma-\Delta_\gamma=D.
\]

This evaluation belongs after the relevant closures.  It must not be moved in
front of possible later Cuts.  Entries 49 and 50 already exhibit the resulting
nonzero raw Cut curvature if it is moved.

## The unrestricted lemma is false

Let (B_{\mu\nu}) be a two-index tensor surrounding a pair of null legs with
momenta (p,-p).  Physical sewing gives

\[
\operatorname{Sew}_{\Pi_p(q)}B
=
-\eta^{\mu\nu}B_{\mu\nu}
+\frac{q_\nu p_\mu B^{\mu\nu}
+q_\mu B^{\mu\nu}p_\nu}{p\cdot q}.
\]

Take four-dimensional rational Minkowski space with

\[
\eta=\operatorname{diag}(1,-1,-1,-1),
\quad
p=(1,0,0,1),
\quad
r=(1,0,0,0),
\]

and (B=r\otimes r).  For the two null references

\[
q_0=(1,0,0,-1),
\qquad
q_1=(1,1,0,0),
\]

the exact sewings are

\[
\operatorname{Sew}_{\Pi_p(q_0)}B=0,
\qquad
\operatorname{Sew}_{\Pi_p(q_1)}B=1.
\]

Thus no reference-free resolved scalar can equal both sewings.  All three
momenta are null where required; what fails is the Ward condition.  This is
the smallest counterexample: one pair of legs and a rank-two tensor.

Even the scalar condition

\[
p_\mu p_\nu B^{\mu\nu}=0
\]

does not imply Ward alignment as a matter of linear algebra.  With the same
(p,r), take (t=(0,1,0,0)) and (B=r\otimes t).  Then
(pBp=(p\cdot r)(p\cdot t)=0), but (p_\mu B^{\mu\nu}=t^\nu) is not
proportional to (p^\nu).  The two projector sewings are again different,
now (0) and (-1).  Therefore the passage from a double contraction identity
to the aligned equations requires the physical Ward statement for the blob;
it is not a consequence of (pBp=0) alone.

It also identifies a scope error to avoid.  An arbitrary tensor built from
on-shell momenta, an individual metric-pairing sector, or an individual
off-shell cubic Feynman diagram is not automatically an on-shell physical
blob.  Ward invariance cannot be assigned to it merely because the full
amplitude or completed sector sum is gauge invariant.

## Corrected one-edge theorem

Let (R) denote all other open physical legs, and quotient tensors in those
legs by their gauge ideal.  Write this quotient as (Q_R).  A two-index cut
blob (B_{\mu\nu;R}) is **Ward aligned at (e)** if there are classes
(N_e,N'_e\in Q_R) such that

\[
p_\mu[B^{\mu\nu}] = N_e p^\nu,
\qquad
[B^{\mu\nu}]p_\nu = N'_e p^\mu
\quad\text{in }Q_R.
\]

This is weaker than literal transversality of the two-index tensor.  It is the
condition used in equations (39)--(41) of Carrôlo--Figueiredo for closing two
legs of the same on-shell object.

### Theorem: Ward-quotient one-edge closure

For a Ward-aligned blob,

\[
\boxed{
\operatorname{Sew}_{\Pi_p(q)}[B]
=
-\eta^{\mu\nu}[B_{\mu\nu}]+N_e+N'_e
}
\]

in (Q_R), independently of (q).

### Proof

Insert the two aligned Ward identities into the longitudinal part of the
projector:

\[
\frac{q_\nu p_\mu[B^{\mu\nu}]}{p\cdot q}
=
\frac{N_e q\cdot p}{p\cdot q}
=N_e,
\]

and similarly the reverse term is (N'_e).  The remaining term is the metric
contraction.  No Ward identity for an individual contraction sector has been
used.  The theorem applies to the completed on-shell blob class in (Q_R).

For a separating tree sewing (B=A_\mu C_\nu), the two completed on-shell
subobjects obey the ordinary Ward identities, so (N_e=N'_e=0).  For a
nonseparating closure of two legs of one object, these coefficients can be
nonzero and are precisely the longitudinal correction that must be represented
by the surface rule.

## Exact factorization of the obstruction

Choose proposed aligned parts (N_ep^\nu,N'_ep^\mu) and define the Ward
remainders

\[
W^\nu=p_\mu B^{\mu\nu}-N_ep^\nu,
\qquad
W'^\mu=B^{\mu\nu}p_\nu-N'_ep^\mu.
\]

Then the exact defect from the reference-free Ward formula is

\[
\boxed{
\Omega_e(q;B)
=
\frac{q\cdot W+q\cdot W'}{p\cdot q}.
}
\]

Consequently the obstruction factors entirely through the Ward remainders.
For a physical blob they vanish in (Q_R), even when a chosen tensor
representative has terms in the gauge ideal of other still-open legs.

The curve-cover identity needs one additional, genuinely geometric
realization condition.  If (F_E) denotes physical Gram specialization of the
resolved open cover, require

\[
\boxed{
F_{E\setminus\{e\}}
\operatorname{Gl}^{\rm res}_e(x)
=
-\eta:F_E(x)+N_e(F_E(x))+N'_e(F_E(x)).
}
\tag{ER_e}
\]

Under ((ER_e)), the desired formula follows:

\[
\operatorname{Sew}_{\Pi(p;q)}
\operatorname{sp}\widetilde\Phi_{G\setminus e}
=
\operatorname{sp}\operatorname{ev}_\rho
\widetilde\Phi_G.
\]

This is a conditional all-environment theorem.  The universal endpoint
quadratic identity of entry 52 proves the open-strand metric part.  The
marked-theta symbolic checker proves the complete condition, including the
longitudinal coefficients, for that graph.  Those facts do not by themselves
prove ((ER_e)) for every cubic graph and every partially sewn environment.

## Two-edge closure coherence

Let (e=(p,-p)) and (f=(k,-k)) be two distinct open pairs of a tensor
(T_{\mu\nu\alpha\beta;R}).  On tensor representatives,

\[
\begin{aligned}
\operatorname{Sew}_e\operatorname{Sew}_fT
&=
\Pi_p(q_p)^{\mu\nu}
\Pi_k(q_k)^{\alpha\beta}
T_{\mu\nu\alpha\beta},\\
&=
\operatorname{Sew}_f\operatorname{Sew}_eT.
\end{aligned}
\]

This is strict interchange of contractions on disjoint index pairs.  The
resolved gluing maps obey the same interchange law before evaluation.

The exact additional condition needed for an edgewise proof is not vanishing
of the double-longitudinal term.  It is **closure stability of Ward
alignment**: the Ward equations for (f) must hold in the quotient by all
other open-leg gauge ideals before closing (e), and their coefficient maps
must be natural,

\[
N_f(\operatorname{Sew}_eT)
=
\operatorname{Sew}_eN_f(T),
\qquad
N'_f(\operatorname{Sew}_eT)
=
\operatorname{Sew}_eN'_f(T),
\]

with the analogous equations after exchanging (e) and (f).  These
identities are automatic when the Ward equations are identities in the
multi-leg physical quotient and sewing is the categorical trace there.  They
are not automatic for arbitrary unreduced tensor representatives.

Equivalently, the required square is

\[
\begin{array}{ccc}
\mathsf{Cov}^{\rm res}(G\setminus\{e,f\})
&\xrightarrow{\operatorname{Gl}^{\rm res}_e}&
\mathsf{Cov}^{\rm res}(G\setminus f)
\\[3pt]
\big\downarrow{F_{e,f}}
&&
\big\downarrow{F_f}
\\[3pt]
Q_{e,f}
&\xrightarrow{\operatorname{Sew}_e}&
Q_f,
\end{array}
\]

together with the corresponding (f)-square.  Their common composite is the
two-edge coherence condition.

Expanding each projector as (M+L), both orders contain

\[
M_eM_f,
\qquad
L_eM_f,
\qquad
M_eL_f,
\qquad
L_eL_f.
\]

The (L_eL_f) term can be nonzero.  The new small checker has an exact example
with (L_eL_f=1) and a commuting final square.  More importantly, the
marked-theta certificate has four spanning-tree presentations with

\[
[M,L_1,L_2,L_1L_2]=[-2056,8,8,-8].
\]

Thus nested longitudinal vanishing is neither the coherence law nor a valid
universal induction hypothesis.

## What happens to cycle-rank induction

Choose a spanning tree of a connected graph of cycle rank (L), leaving
(L) edge pairs to close.  The corrected one-edge theorem yields an induction
on (L) if all of the following hold:

1. the tree-level resolved curve map realizes the physical tree blob;
2. every partially sewn blob is a class in the multi-leg physical quotient;
3. Ward alignment is stable under every remaining closure;
4. ((ER_e)) holds for every edge in every such environment;
5. resolved carriers are retained until all required Cut operations are past.

Under these hypotheses, one-edge naturality and the two interchange laws make
the result independent of closure order, and induction proves the fully sewn
identity.

This is a valid conditional theorem, not yet an unconditional all-graph
theorem in the present ledger.  The missing step is exactly hypothesis 4 in an
arbitrary multi-leg environment.  Testing more final closed graphs cannot
replace it; the decisive next certificate must retain at least two open state
pairs and verify the quotient-valued Ward/naturality equations before either
closure.

## A representative-level two-closure warning

The new checker also gives a minimal reason not to scalarize intermediate
representatives.  Take

\[
T=(r\otimes r)\otimes(k\otimes k).
\]

The first factor has the reference-dependent one-edge values (0) and (1)
above, while the second factor is pure gauge and is annihilated by
(Pi_k).  Hence both final double closures are zero and the physical square
commutes, but one intermediate representative depends on the first reference.
The correct intermediate object is its class in the remaining physical
quotient, where the pure-gauge factor is already zero.

This is the two-edge analogue of the resolved-circuit warning: equality after
final evaluation does not justify forgetting the structure required by the
next operation.

## Necessary clarification to entry 52

Entry 52 says, immediately after the endpoint identity, that multiplication
over strands gives the metric-sector tensor contraction.  Read literally as
the full cubic all-metric network, this conflicts with its later theorem and
with its checker.

The checker has two distinct handle functions:

```text
full_handle       -> naive_metric_polynomial
reduced_handle    -> graphical_polynomial
```

and verifies that the two polynomials are unequal.  The curve-cover endpoint
identity realizes the **gauge-reduced graphical network**.  It does not equal
the naive full-handle all-metric network; the physical projectors supply the
longitudinal correction that relates the full cubic tensor calculation to the
reduced graphical result.  Entry 52 should be read with this qualification.
No change to entry 52 is made here.

## Evidence and scope

Proved here:

- the unqualified rank-two arbitrary-tensor lemma has an exact null-kinematic
  counterexample;
- the Ward-quotient one-edge formula;
- exact factorization of its defect through Ward remainders;
- strict two-projector interchange;
- nonvanishing nested longitudinal terms are compatible with coherence;
- the precise hypotheses under which cycle-rank induction is valid.

Evidence, not an all-graph proof:

- entry 52's 24 symbolic marked-theta presentations realize the complete
  physical/curve identity;
- its exact denominator cancellation shows reference independence on that
  cell;
- the source paper supplies the graphical left-turn rule for the one-loop
  Ward coefficients in arbitrary on-shell attachments.

Not proved:

- that every origin-resolved cubic graph cell lands in the required multi-leg
  physical quotient before all loop closures;
- ((ER_e)) for every edge and arbitrary partially sewn environment;
- an all-graph induction from the marked-theta result alone;
- any Cut-commuting theorem after premature (D)-evaluation.

## Next executable test

Use the smallest tree leading singularity with four distinguished forward
legs (p,-p,k,-k) and at least one generic physical external attachment.
Retain the rank-four tensor and the origin-resolved curve cover.  Verify:

1. the Ward equations for the (p)-pair modulo the gauge ideal of the
   (k)-pair, and conversely;
2. the two coefficient naturality equations for (N,N');
3. both one-edge realization squares before the second closure;
4. the complete (M_eM_f,L_eM_f,M_eL_f,L_eL_f) decomposition;
5. equality of the two closure orders without evaluating any carrier needed by
   a later Cut.

The smallest failure among these equations is the true obstruction to the
all-graph induction.  A nonzero (L_eL_f) by itself is not a failure.

## Primary source

- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*, especially equations (39)--(41), the exclusively-left-turning
  rule, the arbitrary on-shell attachment statement at one loop, and the
  higher-loop projector discussion:
  <https://arxiv.org/html/2512.17019>.

## Internal dependencies

- Entry 46: resolved closed-circuit carrier.
- Entry 49: premature-evaluation Cut defect.
- Entry 51: exact nonzero nested marked-theta correction.
- Entry 52: symbolic marked-theta physical realization and strict resolved
  Cut/gluing naturality.
