# Two-Open-Pair Ward Naturality and the Trace-Strict Surface Representative

## Record

Date: 2026-08-13

Status: the smallest nontrivial environment left open by entry 53 now passes
exactly.  For every spanning-tree presentation of the marked-theta carrier,
physical closure of either of its two open forward pairs agrees with the
gauge-reduced curve-cover representative **before** the other pair is closed.
Ward alignment survives the first closure, the two Ward coefficients are
reference independent, and both closure orders give the same result.

The result is stronger than the final closed-graph identity of entry 52.  It
proves the two one-edge realization squares on a rank-four open tensor in the
remaining physical polarization quotient.

Reproducible certificate:

```text
research/nima/check_two_open_pair_ward_naturality.rs
```

## The carrier under test

The marked-theta graph has five cubic vertices and six internal edges.  Each
of its twelve spanning trees contains four edges and leaves two edge pairs

\[
e=(p,-p),
\qquad
f=(k,-k)
\]

open.  Before either loop closure, the completed tree leading singularity is a
rank-four tensor

\[
T_{\mu\nu\alpha\beta;R},
\]

where \(R\) denotes the three generic physical scaffold attachments.

The audit contracts the four open indices with algebraically generic test
vectors

\[
a,b\in p^\perp,
\qquad
c,d\in k^\perp.
\]

Their Gram products are independent modulo only these four transversality
conditions.  The symbolic chart contains:

- thirteen independent base Gram variables;
- the formal closed-state variable \(D\);
- thirty-four independent Gram variables involving \(a,b,c,d\).

Thus the calculation takes place over a 48-variable Gram-free polynomial
ring.  No spacetime dimension, Gram determinant, or sampled kinematic point
is imposed.  Equality for the generic test vectors separates the corresponding
classes in

\[
H_p^{*\otimes2}\otimes H_k^{*\otimes2}\otimes Q_R,
\qquad
H_p=p^\perp/\langle p\rangle.
\]

## Exact tree Ward identities

For every spanning tree, replacing any one of \(a,b,c,d\) by the momentum of
its leg gives zero:

\[
T(p,b,c,d)=T(a,p,c,d)=T(a,b,k,d)=T(a,b,c,k)=0.
\]

These are quotient-valued Ward statements: the other three state vectors are
generic physical classes.  They prove the aligned equations required in entry
53 without using the invalid implication

\[
p_\mu p_\nu B^{\mu\nu}=0
\quad\Longrightarrow\quad
p_\mu B^{\mu\nu}\propto p^\nu.
\]

For a null reference \(q_e\), the two coefficients are extracted by

\[
N_e(c,d)
=
\frac{T(p,q_e,c,d)}{p\cdot q_e},
\qquad
N'_e(c,d)
=
\frac{T(q_e,p,c,d)}{p\cdot q_e}.
\]

The analogous formulas hold for \(f\).  Both cyclic null-reference choices in
the symbolic chart give the same \(N_e,N'_e\).

## One-edge realization theorem on the marked handle

Let \(T^{\rm full}\) be the rank-four tree tensor built from the ordinary
three-gluon cubic representative, and let \(T^{\rm red}\) be the
gauge-reduced graphical representative realized by the endpoint-extension
curve rule.  Then, for either open pair and in the physical quotient of the
remaining pair,

\[
\boxed{
\operatorname{Sew}^{\rm phys}_e
[T^{\rm full}]
=
-\eta_e:T^{\rm full}+N_e+N'_e
=
-\eta_e:T^{\rm red}.
}
\]

Equivalently, the square

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
&\xrightarrow{\operatorname{Sew}^{\rm phys}_e}&
Q_f
\end{array}
\]

commutes for the marked-theta carrier.  The same statement holds after
exchanging \(e\) and \(f\).

This equality is not caused by vanishing longitudinal data.  Across the
twelve trees, two closure pairs, two coefficient directions, and two null
references, all

\[
12\times2\times2\times2=96
\]

ordinary-representative Ward coefficients are nonzero.  In the corresponding
gauge-reduced graphical representative all 96 coefficients vanish.  The
surface rule has therefore transferred the physical longitudinal correction
into the choice of representative.

This is a precise sense in which the curve description is **trace strict**:
the physical trace of the ordinary cubic tensor is represented by ordinary
metric gluing after the gauge-reduced curve transformation.

## Closure stability and two-edge coherence

After physically closing \(e\), the remaining two-index tensor obeys both Ward
identities for \(f\):

\[
k_\alpha
\operatorname{Sew}^{\rm phys}_eT^{\mu\nu\alpha\beta}
\sim0,
\qquad
\operatorname{Sew}^{\rm phys}_eT^{\mu\nu\alpha\beta}k_\beta
\sim0
\]

in the remaining physical quotient.  The same holds with \(e\) and \(f\)
exchanged.  Consequently the Ward coefficient maps are natural under the
other closure.

The two physical traces commute exactly,

\[
\operatorname{Sew}^{\rm phys}_e
\operatorname{Sew}^{\rm phys}_fT
=
\operatorname{Sew}^{\rm phys}_f
\operatorname{Sew}^{\rm phys}_eT,
\]

and both equal the fully closed gauge-reduced graphical polynomial.  This is
true even though entry 52's complete projector expansion contains nonzero
nested longitudinal terms in four spanning-tree presentations.

## Certificate counts

The exact Rust audit checks:

- 12 spanning-tree rank-four carriers;
- 243 cubic sector words in each evaluation;
- 48 initial tree Ward contractions;
- 96 post-one-closure Ward contractions;
- 48 one-edge Ward formulas;
- 48 partial physical/graphical realization squares;
- 48 reference comparisons of the partial physical tensors;
- 48 reference comparisons of \(N,N'\);
- 24 two-closure order comparisons;
- 24 final physical/graphical comparisons;
- 96 reduced-representative Ward coefficients.

Every defect count is zero.  The largest partially sewn polynomial has 224
monomials.

## Relation to the source proof

Carrôlo--Figueiredo write the loop closure as

\[
-\eta:T+\mathcal N+\mathcal N'
\]

and later prove the aligned Ward equations recursively for objects built by
on-shell gluing.  The recursive argument, rather than the scalar condition
\(pTp=0\) by itself, supplies the required hypothesis.  Their graphical
left-turn rule identifies the nonzero one-loop coefficient and absorbs it
into the closed-curve exponent.

At higher loops their displayed argument uses a sewing presentation in which a
nested correction vanishes.  Entries 51--53 show that this vanishing is not
presentation independent: four marked-theta spanning trees have a nonzero
nested term.  The present result supplies the invariant replacement.  What is
presentation independent is the commuting pair of physical traces and its
resolved curve-cover realization, not the vanishing of each nested summand.

## What is established

For the complete marked-theta family:

1. Ward alignment before either closure;
2. reference-independent Ward coefficients;
3. the exact one-edge Ward formula;
4. both partial curve/physical realization squares;
5. Ward stability after either first closure;
6. closure-order independence;
7. equality with the final resolved graphical carrier.

This upgrades entry 52 from a closed scalar identity to a quotient-valued
two-stage identity on every sewing presentation of the cell.

## Epistemic boundary

This is not yet an all-graph theorem.  It proves the first environment in
which closure stability, partial realization, and nonzero nested terms coexist.
It does not prove that every trivalent ribbon graph admits the same trace-strict
representative.

The remaining universal statement can now be isolated cleanly:

> **Ward--Brauer trace-strictification problem.** Construct a natural
> transformation from the cubical physical-projector sewing object generated
> by \(M_e,L_e^+,L_e^-\) to the resolved curve-cover Brauer object, and prove
> that it intertwines every partial categorical trace before closed-carrier
> evaluation.

If this transformation is monoidal for disjoint open pairs, compact-closed
coherence gives the cycle-rank induction without any nested-term vanishing
hypothesis.

## Next executable test

Construct the Ward sewing cube for a general set \(E\) of open pairs:

\[
K_E
=
\bigotimes_{e\in E}
\langle M_e,L_e^+,L_e^-\rangle.
\]

At \(|E|=2\), lift the present polynomial equality to an origin-resolved map
that records which endpoint extension realizes each of the nine
\((M,L^+,L^-)^2\) sectors.  The decisive question is whether the map respects
the two edge augmentations termwise up to the local Ward/V relations.  That is
the smallest presentation theorem from which arbitrary cycle rank could
follow.

## Primary source

- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*, especially equations (39)--(49), the left-turn recursion, and the
  higher-loop discussion:
  <https://arxiv.org/html/2512.17019>.

## Internal dependencies

- Entry 46: resolved Brauer-state carrier.
- Entry 51: nonzero nested marked-theta projector term.
- Entry 52: symbolic final identity and strict resolved gluing.
- Entry 53: Ward-quotient one-edge theorem and conditional cycle-rank
  induction.
