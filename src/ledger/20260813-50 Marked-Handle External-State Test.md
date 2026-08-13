# Marked-Handle External-State Test

## Record

Date: 2026-08-13

Status: the resolved surface counit now passes a nonvacuum handle test with
open physical state flags.  On the two-loop cubic theta family obtained by
placing labelled external insertions on distinct theta roads, the complete
resolved circuit polynomial is

\[
\boxed{
P_n(D)
=
3^{n+2}+(2n+3)(D-1),
\qquad 0\leq n\leq3.
}
\]

Here \(n\) is the number of marked roads, \(n+2\) is the number of cubic
vertices, and all \(3^{n+2}\) local cyclic-counit sectors have been retained.
For the first member with three external legs,

\[
P_3(D)=234+9D.
\]

Termwise Brauer augmentation sends this to \(243\), so the normalized marked
graph coefficient is exactly one.  All 64 iterated Cuts commute with the
augmentation, including connected nonseparating Cuts and Cuts that disconnect
the graph.  Evaluating state circuits before opening a single edge instead
produces the nonzero defect

\[
\boxed{
\Omega_e^{\rm raw}
=
\frac{2(D-1)}{81}
\prod_{f\ne e}x_f.
}
\]

This is an exact graph-cell result in the resolved modular carrier.  It is not
yet a differential operator acting on a published, already-sewn two-loop
Yang--Mills surface integrand, and it is not yet a comparison with the complete
mapping-class sum.

Reproducible certificate:

```text
research/nima/check_marked_handle_counit.rs
```

## The marked theta family

Begin with two trivalent core vertices joined by three theta roads.  Choose
\(n\) distinct roads, subdivide each chosen road by a trivalent vertex, and
attach one labelled external flag at the subdivision.  Call the resulting
ribbon graph \(\Gamma_n\).  Its combinatorial data are

\[
V_n=n+2,
\qquad
E_n=n+3,
\qquad
b_1(\Gamma_n)=E_n-V_n+1=2.
\]

Use the same cyclic orientation at the two core vertices, and at an insertion
vertex use the order

\[
(\text{left core},\text{ external flag},\text{ right core}).
\]

The boundary permutation \(\sigma\alpha\) has one cycle.  Since

\[
V_n-E_n=-1=2-2g-b,
\]

the thickened graph has

\[
\boxed{(g,b)=(1,1)}
\]

for every \(n=0,1,2,3\).  Thus these graphs add external marked states without
changing the handle topology tested in entry 49.

The three-leg member \(\Gamma_3\) is the symmetric graph with one external
insertion on each road.  It has five cubic vertices, six internal edges, and
three external flags.  It is the first member of this family whose local
source is a nonzero cubic scattering configuration.  Its integrated massless
on-shell value is still scaleless because three-point kinematics carries no
Mandelstam scale; the marked rational integrand is nevertheless nonzero.

## Local physical input

At every cubic vertex use the actual scalar-scaffolded three-gluon polynomial

\[
\begin{aligned}
A_3^{\rm YM}
={}&X_{14}X_{26}+X_{36}X_{24}+X_{25}X_{46}\\
&-X_{25}X_{36}-X_{14}X_{36}-X_{14}X_{25}.
\end{aligned}
\]

The three cyclic local sectors are

\[
U_0=\partial_{14}\partial_{26},
\qquad
U_1=\partial_{36}\partial_{24},
\qquad
U_2=\partial_{25}\partial_{46},
\]

and the executable verifies separately that

\[
U_iA_3^{\rm YM}=1.
\]

The cyclic representative at each vertex is

\[
u_3^{\rm cyc}=\frac13(U_0+U_1+U_2).
\]

For a sector word

\[
\mathbf s=(s_v)_{v\in V(\Gamma_n)}
\in\{0,1,2\}^{n+2},
\]

let \(\kappa_{\mathbf s}\) be the resolved Brauer state obtained by sewing the
local sectors through the internal edges.  Before state evaluation the marked
graph operation is

\[
\boxed{
\mathcal U_{\Gamma_n}^{\rm res}
=
\frac1{3^{n+2}}
\left(\prod_{e\in E(\Gamma_n)}x_e\right)
\sum_{\mathbf s\in\{0,1,2\}^{n+2}}
[\kappa_{\mathbf s}].
}
\]

For \(n\geq1\), the external labels make the nonvacuum cell's automorphism
factor one.  For \(n=0\), the extra theta factor \(1/3\) recovers the vacuum
normalization of entry 49.

## Closed-circuit theorem

Label the theta roads by \(r=0,1,2\), and let

\[
w_r=
\begin{cases}
3,&r\text{ carries an external insertion},\\
1,&r\text{ is unsubdivided}.
\end{cases}
\]

A closed polarization circuit exists precisely as follows.

1. The singleton sectors at the two core vertices agree on one road \(r\).
2. The circuit then runs around the other two roads.
3. Every insertion on either circuit road has its external flag as singleton,
   thereby pairing its two internal flags.
4. If the omitted road \(r\) is marked, its insertion sector is arbitrary and
   supplies a factor three.  If it is unmarked, there is no such choice.

Consequently the number of one-circuit sectors is

\[
C_n=\sum_{r=0}^2w_r=3n+(3-n)=2n+3.
\]

No sector contains two circuits.  Hence

\[
\begin{aligned}
P_n(D)
&=\sum_{\mathbf s}D^{c(\kappa_{\mathbf s})}\\
&=\bigl(3^{n+2}-C_n\bigr)+C_nD\\
&=\boxed{3^{n+2}+(2n+3)(D-1)}.
\end{aligned}
\]

The complete table is

| External insertions \(n\) | Vertices | Internal edges | Resolved sectors | \(P_n(D)\) |
|---:|---:|---:|---:|---:|
| 0 | 2 | 3 | 9 | \(6+3D\) |
| 1 | 3 | 4 | 27 | \(22+5D\) |
| 2 | 4 | 5 | 81 | \(74+7D\) |
| 3 | 5 | 6 | 243 | \(234+9D\) |

This supplies a concrete warning about genus normalization.  Every graph in
the family has graph Betti number two, yet the maximum state-circuit degree is
one.  Neither division by \(D^2\) nor extraction of a \(D^2\) coefficient can
define the scalar counit.

## Exact formula for every iterated Cut

Let \(R\subseteq E(\Gamma_n)\) be a set of opened edges, and let
\(\rho(R)\) be the set of theta roads containing those edges.  A circuit that
omits road \(r\) survives exactly when every opened edge lies on \(r\).  Define

\[
C_n(R)=
\begin{cases}
C_n,&R=\varnothing,\\
w_r,&\rho(R)=\{r\},\\
0,&|\rho(R)|\geq2.
\end{cases}
\]

The opened resolved state polynomial is therefore

\[
\boxed{
P_{n,R}(D)
=
3^{n+2}+C_n(R)(D-1).
}
\]

This formula covers both kinds of topology change.

- Opening one edge leaves the graph connected and lowers \(b_1\) from two to
  one.
- Opening both halves of one marked road disconnects its external insertion
  while the complementary two-road loop survives.
- Opening edges on two different roads destroys every state circuit.
- Further Cuts produce forests with progressively more components.

Termwise scalar augmentation gives

\[
P_{n,R}(1)=3^{n+2}
\]

for every \(R\).  Thus

\[
\boxed{
\Delta_R\epsilon_{\rm Br}(\mathcal U_{\Gamma_n}^{\rm res})
=
\epsilon_{\rm Br}\Delta_R(\mathcal U_{\Gamma_n}^{\rm res})
=
\prod_{e\notin R}x_e.
}
\]

The Rust audit checks all

\[
2^3+2^4+2^5+2^6=120
\]

Cut squares in the family.

## Raw Cut curvature

If the circuit factors are evaluated before the Cut, differentiation retains
the closed coefficient \(P_n(D)/3^{n+2}\).  Cutting the resolved patterns first
gives \(P_{n,R}(D)/3^{n+2}\).  Their exact difference is

\[
\boxed{
\Omega_R^{\rm raw}
:=
\left(\partial_R\operatorname{ev}_D
-
\operatorname{ev}_D\Delta_R\right)
\mathcal U_{\Gamma_n}^{\rm res}
=
\frac{C_n-C_n(R)}{3^{n+2}}(D-1)
\prod_{e\notin R}x_e.
}
\]

For \(\Gamma_3\), every road has \(w_r=3\).  A single-edge Cut therefore has

\[
P_{3,e}(D)=240+3D
\]

and

\[
\Omega_e^{\rm raw}
=
\frac{(9-3)(D-1)}{243}
\prod_{f\ne e}x_f
=
\boxed{
\frac{2(D-1)}{81}
\prod_{f\ne e}x_f}.
\]

Two Cuts on different roads give the larger coefficient
\((D-1)/27\).  Two Cuts on the same road leave the one-edge defect because the
complementary state circuit remains closed.

This nonzero raw curvature is good evidence for the resolved construction: it
shows that the order of operations is doing mathematical work.  The curvature
vanishes exactly after \(D\mapsto1\), as required of the scalar state functor.

## Complete three-leg Cut atlas

The 64 cut subsets of \(\Gamma_3\) fall into eight exact classes.  The last
column is the number of surviving \(D\)-valued sectors.

| Cut edges | Components | Remaining \(b_1\) | \(D\)-sectors | Number of masks |
|---:|---:|---:|---:|---:|
| 0 | 1 | 2 | 9 | 1 |
| 1 | 1 | 1 | 3 | 6 |
| 2 | 2 | 1 | 3 | 3 |
| 2 | 1 | 0 | 0 | 12 |
| 3 | 2 | 0 | 0 | 20 |
| 4 | 3 | 0 | 0 | 15 |
| 5 | 4 | 0 | 0 | 6 |
| 6 | 5 | 0 | 0 | 1 |

The second row contains the six nonseparating one-edge Cuts.  The third row
contains the three Cuts that open both halves of one road and isolate its
marked vertex.  Thus the audit covers connected and disconnected targets, not
only the easiest nonseparating channel.

## External support is nontrivial but cyclic

The three physical external endpoints and five auxiliary coefficient endpoints
induce a perfect matching with eight open ends.  Before scalar-state
realization, the 243 sectors split as

| Closed circuits | Physical--physical pairs | Number of sectors |
|---:|---:|---:|
| 0 | 0 | 174 |
| 0 | 1 | 60 |
| 1 | 0 | 9 |

The 60 sectors with a physical--physical pair are distributed exactly as

\[
N_{01}=N_{02}=N_{12}=20.
\]

Thus the open state support is not uniform and is not being replaced by a
single count.  Nevertheless it has no cyclic asymmetry.  Simultaneously
rotating the three theta roads, the three external labels, both core singleton
sectors, all three marked vertices, and every selected Cut gives an exact
resolved matching square.  The executable checks 15,552 such populated
squares, and three rotations return every state and Cut mask exactly.

The absence of cyclic asymmetry is expected and desirable.  A nonzero
fixed-label asymmetry here would signal a convention error or an anomaly in the
purported cyclic counit.  Nonuniform support across different matching types is
the substantive information.

## Physical polarization-projector audit

The physical state sum on a loop-closing gluon edge is not always the naïve
metric contraction.  Carrôlo and Figueiredo write it as

\[
-\eta^{\mu\nu}
+
\frac{p^\mu q^\nu+p^\nu q^\mu}{p\cdot q}.
\]

They prove that the second, \(N\)-type term is nonzero precisely when the two
legs being sewn are joined inside the on-shell object by an exclusively
left-turning path.  After sewing, this path is a purely left-turning closed
curve, equivalently a curve homotopic to an internal boundary.

No such curve occurs in the marked-theta family.  Every simple cycle in
\(\Gamma_n\) uses two of the three theta roads.  With the cyclic orders fixed
above, an orientation around such a cycle encounters both kinds of turn.  At
the two core vertices the turns are opposite; marked subdivision vertices can
add turns but cannot remove that mixed pair.  Reversing the orientation swaps
left and right and therefore does not change the conclusion.

Equivalently, the thickened graph has one boundary, whose boundary walk uses
fatgraph edges more than once.  It is not one of the simple closed contraction
curves allowed on a maximal residue.  The three simple theta cycles are all
nonseparating and not boundary-homotopic.

This can be made independent of the sewing history.  For road lengths
\(\ell_r\in\{1,2\}\), the number of spanning trees is

\[
\tau(\Gamma_n)
=
\ell_0\ell_1+ell_0\ell_2+ell_1\ell_2.
\]

For every spanning tree and each of its two loop-closing edges, the fundamental
cycle has both an \(L\) and an \(R\) turn.  The executable checks all twelve
simple cycles in the four-member family and all 56 spanning-tree closure
channels.  Therefore

\[
\boxed{N_{\Gamma_n}=0}
\]

at every loop-closing step, and the nested \(N\)-term vanishes a fortiori.

For these cycles the physical closed-curve exponent is consequently

\[
\Delta_\gamma=-D,
\qquad
\nu_\gamma=0.
\]

The resolved state value used above is exactly

\[
\nu_\gamma-\Delta_\gamma=D.
\]

Thus the \(D\)-sectors in \(P_n(D)\) are the resolved form of the physical
polarization-projector circuits, with the orientation/parity convention
already isolated in entry 46.  There is no omitted gauge-reference correction
on this graph.  What remains for a full numerator comparison is the global
map from the open coefficient paths to surface \(X_C\) variables and the
associated extension signs and cancellations.

## Marked momentum specialization

For \(\Gamma_3\), orient each road from the left core to the right core.  Let
\(p_r\) be the momentum on its left segment and let the external momentum
\(q_r\) enter at the marked vertex.  Momentum conservation reads

\[
\sum_{r=0}^2p_r=0,
\qquad
\sum_{r=0}^2q_r=0,
\]

and the right segment carries \(p_r+q_r\).  The marked scalar specialization is

\[
x_{Lr}\longmapsto\frac1{p_r^2},
\qquad
x_{Rr}\longmapsto\frac1{(p_r+q_r)^2}.
\]

Consequently the augmented graph cell becomes

\[
\boxed{
\epsilon_{\rm Br}(\mathcal U_{\Gamma_3}^{\rm res})
\longmapsto
\prod_{r=0}^2
\frac1{p_r^2(p_r+q_r)^2},
}
\]

the labelled two-loop cubic scalar cell with three external legs.  This
specialization must be performed before any mapping-class identification of
edge variables.  No symmetry factor is inserted because the external labels
fix the nonvacuum fatgraph.

## Relation to the published two-loop units obstruction

Backus and Figueiredo observe that the naïve external differential-operator
extension already fails by units at two loops.  In their one-external-gluon
example, the all-scalar-singularity term has five denominator variables and a
cubic numerator, so at least three derivatives would be needed while only one
external \(W_e\) is available.

The one-leg member \(\Gamma_1\) makes the structural issue visible.  It has
four internal post-scaffolding edges; restoring its scaffolding pole gives the
same count of five denominator factors.  But its resolved modular presentation
has three cubic vertices and retains internal state circuits.  The higher-loop
counit therefore cannot be generated only by operators indexed by external
gluons.

This does not solve the point-set differential-operator problem.  It explains
why the units obstruction points toward a vertexwise/modular operation rather
than falsifying transmutation itself.  We do not identify a particular planar
term in their integrand with the handle cell \(\Gamma_1\).

## What is proved and what remains open

Proved in this entry:

- the marked theta family has ribbon signature \((g,b)=(1,1)\);
- the actual three local derivatives each send the scaffolded YM cubic vertex
  to the scalar cubic vertex;
- the closed-circuit formula
  \(P_n(D)=3^{n+2}+(2n+3)(D-1)\);
- the all-Cut formula
  \(P_{n,R}(D)=3^{n+2}+C_n(R)(D-1)\);
- all 120 resolved Cut/counit squares for \(0\leq n\leq3\);
- all 64 connected and disconnected Cut patterns for the three-leg cell;
- the exact raw Cut curvature and its annihilation by \(D\mapsto1\);
- nontrivial open-end matching support and exact cyclic balance;
- absence of all physical \(N\)-corrections, for every spanning-tree sewing
  history, because all twelve simple cycles have mixed turns;
- the labelled momentum-space scalar specialization of \(\Gamma_3\).

Not proved:

- that these 243 resolved sectors are the image of one point-set differential
  operator on an already-sewn two-loop YM integrand;
- equality with the complete two-loop three-gluon surface function, rather
  than one marked maximal cell in its modular presentation;
- derivation of the open coefficient-path monomials and their extension signs
  directly from the full physical YM leading singularity, instead of from
  modular extension of the verified local counits; the state-projector
  \(N\)-corrections themselves are now proved absent on this cell;
- a scale-carrying four-point integrated test;
- descent after summing all mapping-class-related cells and quotienting
  cut-invisible/scaleless terms.

The next decisive comparison is to construct the explicit five-vertex YM
leading singularity for \(\Gamma_3\), expand the open coefficient paths into
surface \(X_C\) variables with their extension signs, and show that the
resolved local counit selects precisely the 243-state carrier above.  The
polarization-projector correction is no longer part of that gap.  This would
turn the exact modular-carrier result into a direct physical-numerator
comparison.

## Primary sources

- Backus and Figueiredo, *Surface Gauge Invariance, Soft Limits and the
  Transmutation of Gluons into Scalars*, especially the one-loop operator and
  the two-loop units obstruction: <https://arxiv.org/abs/2505.17179>.
- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*, especially the higher-loop gluing corrections and the all-loop
  closed-curve rule: <https://arxiv.org/abs/2512.17019>.
- Arkani-Hamed, Frost, and Salvatori, *The Cut Equation*, for marked surface
  functions, nonvacuum automorphism factors, and physical specialization on a
  marked cover: <https://arxiv.org/abs/2412.21027>.
- Getzler and Kapranov, *Modular operads*, for the graphwise extension of cyclic
  operations: <https://arxiv.org/abs/dg-ga/9408003>.
