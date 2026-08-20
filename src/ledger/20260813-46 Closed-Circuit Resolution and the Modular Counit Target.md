# Closed-Circuit Resolution and the Modular Counit Target

## Record

Date: 2026-08-13

Status: the state-contraction part of the all-topology lift is now constructed.
The resolved polarization-contraction category has a canonical cyclic monoidal
augmentation to the scalar line: resolve individual contraction circuits first,
then send the Brauer loop value \(D\) to \(1\).  This reproduces the exact
one-loop one-point surface transmutation and is compatible with arbitrary
composition and disjoint union.

This is not yet the full surface-function counit.  The missing object is a
coefficient cosheaf of resolved contraction covers whose forgetful map to scalar
surface cells satisfies the two genuinely new Hatcher coherence relations,
\(3S\) and \(6AS\).  The tree \(A\)-move relations are already supplied by the
deletion/associahedral resolution of entries 42--45.

Reproducible certificate:

```text
research/nima/check_surface_counit_brauer.rs
```

## Why the naive genus normalization is wrong

The first guess suggested by the published one-loop identity is

\[
u^{(L)}\stackrel{?}{=}D^{-L}\widetilde u^{(L)},
\]

where \(L\) is loop order and \(\widetilde u\) is an unnormalized
post-sewing transmuter.  This works at one loop because the surviving
transmutation sector contains one closed polarization trace.

It is not the all-topology definition.  At higher topology a resolved
contraction pattern can contain a number

\[
c(\kappa)=\#\{\text{closed polarization circuits in }\kappa\}
\]

which depends on the pattern \(\kappa\), not only on the loop number of the
ambient surface.  Composing the same source and target arities in the Brauer
category can create different numbers of internal circles.  The non-overlap
rule for surface contraction curves makes the same distinction physically:
not every independent graph cycle can be represented by a simultaneously
disjoint closed contraction curve.

Thus neither

\[
D^{-L}
\]

nor extraction of the top \(D^L\) coefficient retains the full putative scalar
image.  Top-\(D\) extraction selects the large-dimension scalar-loop sector; it
can discard valid resolved patterns with fewer closed circuits.

The required operation is termwise in the resolved cover complex.

## The Brauer state layer

Let \(V\) be the polarization-state fiber with symmetric metric and formal
dimension

\[
D=\operatorname{ev}_V\circ\operatorname{coev}_V.
\]

Pairings and copairings generate the Brauer category
\(\operatorname{Br}_D\).  A morphism is represented by a perfect matching of
its incoming and outgoing endpoints.  When two matchings are composed, middle
components can close into circuits.  Each newly closed circuit contributes one
factor of \(D\).

If \(f,g\) are composable, write \(c(f,g)\) for the number of circuits created
by their composition.  Associativity of graph gluing gives the exact cocycle
identity

\[
c(f,g)+c(g\circ f,h)
=
c(g,h)+c(f,h\circ g).
\]

This is not merely equality of total evaluations.  The two parenthesizations
produce the same external matching and the same total number of internal
circuits.

For disjoint union,

\[
c(f_1\boxtimes f_2,g_1\boxtimes g_2)
=
c(f_1,g_1)+c(f_2,g_2).
\]

Cyclic relabelling of all three boundaries in a composition square preserves
both the external matching and \(c\).

The Rust certificate constructs all perfect matchings in the audited arities
and verifies:

- 5,376 associative triple composites and the circuit cocycle;
- 7,119 cyclic base-change squares;
- 441 tensor/interchange squares.

The equalities are elementary all-arity graph facts.  The bounded enumeration
audits the implementation and conventions.

## The normalized loop-forgetting augmentation

Resolve a contraction pattern before evaluating its closed components.  Then
base change along

\[
\mathbb Z[D]\longrightarrow\mathbb Z,
\qquad
D\longmapsto1.
\]

Equivalently, at a fixed nonzero physical value of \(D\), a resolved pattern
with \(c(\kappa)\) circuits is normalized by \(D^{-c(\kappa)}\).  The formal
base-change version is preferable because it introduces no denominators and
continues to make sense before choosing spacetime dimension.

The cocycle and tensor identities prove that this is a cyclic monoidal
augmentation of the resolved state-contraction category:

\[
\boxed{
\epsilon_{\rm Br}:
\operatorname{Br}_D^{\rm resolved}
\otimes_{\mathbb Z[D],\,D\mapsto1}\mathbb Z
\longrightarrow
\operatorname{Br}_1.
}
\]

Since the one-dimensional scalar state has evaluation--coevaluation loop value
one, \(\operatorname{Br}_1\) is precisely the state layer required for scalar
sewing.

This is the exact modular correction to the tree counit.  A cap joining the
two retained tree polarizations is the state part of the pairwise operator
\(U_{ef}\).  Sewing a cup to that cap creates a closed circuit and hence \(D\).
The augmentation sends that circuit to the scalar loop value one.

## Exact first closed-circuit surface check

Backus and Figueiredo give the one-point surface integrand

\[
\mathcal I_1
=
\frac{
2X_{1,2}-(1+\Delta)(X_{2,p}-X_{1,p})
}{X_{1,p}},
\]

with the planar closed-curve exponent

\[
\Delta=1-D.
\]

Their surface operator is

\[
\mathcal W_2^{(1)}
=
\partial_{X_{1,2}}
+\partial_{X_{2,1}}
+\partial_{X_{2,p}}.
\]

Acting directly gives

\[
\mathcal W_2^{(1)}\mathcal I_1
=
\frac{2-(1+\Delta)}{X_{1,p}}
=
\frac{1-\Delta}{X_{1,p}}
=
\frac{D}{X_{1,p}}.
\]

After the resolved loop augmentation,

\[
\boxed{
\epsilon_{\rm Br}
\bigl(\mathcal W_2^{(1)}\mathcal I_1\bigr)
=
\frac1{X_{1,p}},
}
\]

the one-loop one-point \(\operatorname{Tr}\phi^3\) surface integrand.

The boundary-curve derivative \(\partial_{X_{1,2}}\) is essential.  Omitting
the surface boundary variable would destroy the loop value and is therefore
incompatible with a surface counit.  This is the smallest exact
closed-circuit normalization test, not merely a maximal-residue check.  It is
not a one-holed-torus \(3S\) test: the planar one-loop surface here is a
punctured disk/annulus, not a genuine genus-one handle.

## Uniformity of the all-loop closed-curve value

Carrôlo and Figueiredo determine the exponent of every closed contraction
curve contributing to a leading singularity.  Let

\[
\nu_\gamma=
\begin{cases}
1,&\gamma\text{ is purely left-turning, equivalently boundary-homotopic},\\
0,&\text{otherwise}.
\end{cases}
\]

Their theorem is

\[
\Delta_\gamma=\nu_\gamma-D.
\]

Therefore the resolved contraction value is independent of the curve type:

\[
\boxed{
\nu_\gamma-\Delta_\gamma=D.
}
\]

This matters.  The raw surface exponents are \(1-D\) or \(-D\), but the
difference is the separately resolved correction \(\nu_\gamma\).  After that
correction is retained, every closed polarization circuit carries the same
central value \(D\).  Hence the Brauer augmentation can be mapping-class
covariant.

One must not implement the counit by naively substituting \(D=1\) into the
already-summed surface function.  The required order is

\[
\boxed{
\text{resolve contraction covers and the }\nu\text{ correction}
\ \longrightarrow\
D\mapsto1
\ \longrightarrow\
\text{forget the cover}.
}
\]

Resolution before specialization is the loop analogue of extraction before
modular completion elsewhere in the Marici program.

## Correct all-topology target

For a marked surface \(\Sigma\), let

\[
\mathfrak C_{\Sigma}^{\rm YM,cov}
\]

denote the sought coefficient cosheaf whose generators are:

1. a scalar surface cell or stable ribbon graph;
2. a non-overlapping contraction-curve cover of its fatgraph;
3. the tree deletion-simplex data at open ends;
4. an orientation/extension-parity line;
5. one formal Brauer loop factor for each closed cover component.

Let

\[
F_\Sigma:
\mathfrak C_{\Sigma}^{\rm YM,cov}
\otimes_{D\mapsto1}\mathbb Z
\longrightarrow
\mathfrak C_{\Sigma}^{\rm scalar}
\]

forget the contraction cover after applying its parity sign and the loop
augmentation.  The desired surface counit is

\[
\boxed{
u_\Sigma
=
H_0(F_\Sigma).
}
\]

Its defining relations are, for a separating Cut,

\[
\operatorname{Cut}_C u_\Sigma
=
(u_{\Sigma_L}\boxtimes u_{\Sigma_R})
\operatorname{Cut}_C,
\]

and, for a nonseparating Cut which opens a closed circuit,

\[
\operatorname{Cut}_C u_\Sigma
=
u_{\Sigma_C}\operatorname{Cut}_C.
\]

Before \(D\mapsto1\), the second relation carries the raw trace factor \(D\).
The Brauer cocycle theorem proves that removing it circuit by circuit is
compatible with every order of iterated Cut.

On a disk this construction must restrict to the deletion-simplex counit of
entries 42--45:

\[
u_{D_n}=u_n,
\qquad
\Delta_Du_n=u_L\boxtimes u_R.
\]

## Global coherence reduces to two new local cells

An all-topology definition initially appears to require comparing infinitely
many cut systems.  Hatcher's pants-decomposition theorem makes the problem
finite and local.

Maximal cut systems are connected by:

- \(A\)-moves on a four-holed sphere;
- \(S\)-moves on a one-holed torus.

All relations are generated by five types of 2-cells:

\[
3A,
\qquad
5A,
\qquad
3S,
\qquad
6AS,
\qquad
C,
\]

where \(C\) is commutation of disjointly supported moves.  The corresponding
pants complex is simply connected.

The existing Marici results already supply the tree part:

- \(3A\) and \(5A\): deletion-simplex/associahedral coherence;
- disjoint \(A\)-move squares in \(C\): strict tensor functoriality;
- physical Cut against tree refinement: the rooted-spine base-change theorem.

The Brauer theorem in this entry supplies the closed-state trace and its tensor,
associative, and cyclic coherences.  Therefore the genuinely new
surface-kinematic calculations are reduced to:

1. the \(3S\) triangle on a one-holed torus;
2. the mixed \(6AS\) hexagon on a genus-one surface with two boundary
   components.

If these two cells close in a resolved coefficient cosheaf, Hatcher simple
connectivity promotes the result to a cut-system-independent, mapping-class
covariant operation on every orientable surface.  Entry 47 subsequently
sharpens this statement: the derived modular envelope fills these cells
automatically on the universal surface-presentation complex; \(3S\) and
\(6AS\) remain tests only for descent to a chosen physical surface-function
quotient.

## What is proved

Proved here:

- closed-circuit count is an associative composition cocycle in the Brauer
  state category;
- it is additive under disjoint union and invariant under cyclic relabelling;
- resolving circuits and applying \(D\mapsto1\) is a cyclic monoidal state
  augmentation;
- the one-loop one-point surface integrand realizes exactly one \(D\)-valued
  circuit and maps to its scalar integrand;
- the all-loop closed-curve exponent rule gives the same resolved value \(D\)
  for both mapping-class types of closed curve;
- global pants-decomposition independence reduces to the five Hatcher cells,
  of which only \(3S\) and \(6AS\) are new beyond the established tree
  coherence.

## What remains open

Not yet proved:

- existence of \(\mathfrak C_{\Sigma}^{\rm YM,cov}\) as a full surface-function
  coefficient cosheaf rather than only a state/leading-singularity resolution;
- the \(3S\) surface-kinematic triangle;
- the mixed \(6AS\) surface-kinematic hexagon;
- compatibility of the forgetful map with cut-invisible topology-local and
  scaleless terms;
- an all-topology point-set differential operator in the surface \(X_C\)
  variables.

The one-loop operator

\[
\prod_e\mathcal W_e^{(1)}
\]

does not by itself define the higher-loop operation.  Backus and Figueiredo
already identify a units obstruction at two loops.  The resolved-cover target
explains why: higher topology needs internal circuit data, not only derivatives
indexed by external gluons.

## Next executable test

Use the three slope classes in the pants complex of the one-holed torus.  For
each slope \(\beta_i\):

1. cut the surface to its genus-zero four-flag presentation;
2. apply the tree deletion counit before re-sewing;
3. retain the boundary/tadpole variables and the resolved
   \(\nu_\gamma-\Delta_\gamma\) term;
4. transport between adjacent slopes by the local \(S\)-move;
5. compute the three-step holonomy
   \[
   \Omega_{3S}=T_{31}T_{23}T_{12}-1;
   \]
6. determine whether \(\Omega_{3S}\) vanishes strictly, by a total derivative,
   or only after quotienting a hereditary scaleless ideal.

A nonzero admitted class is the first true obstruction to the all-topology
counit.  If \(3S\) closes, the next and final new local coherence generator is
the \(6AS\) hexagon.

## Subsequent refinement

Entry 47 constructs the universal surface-presentation lift as the derived
modular envelope of the resolved tree counit and the Brauer augmentation.  In
that universal complex, \(3S\) and \(6AS\) are already higher coherence cells,
so their holonomies vanish by construction.  The remaining physical problem
is the exact descent condition

\[
u^{\rm univ}(\ker q_{\rm YM})\subseteq\ker q_\phi
\]

for the comparison from resolved surface presentations to the selected
\(X_C\)-surface-function model.

## Primary sources

- Backus and Figueiredo, *Surface Gauge Invariance, Soft Limits and the
  Transmutation of Gluons into Scalars*, especially equations (134)--(137):
  <https://arxiv.org/html/2505.17179>.
- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*, especially the all-loop closed-curve rule in section 5.1:
  <https://arxiv.org/html/2512.17019>.
- Cao and Zhu, *All-loop planar integrands in Yang--Mills theory from
  recursion*, for the forward-limit state sum and the distinction between the
  full refined integrand and its leading large-\(D\) sector:
  <https://arxiv.org/html/2503.15860>.
- Hatcher, *Pants Decompositions of Surfaces*, for the \(A\)- and \(S\)-move
  presentation and the five simply-connected coherence cells:
  <https://arxiv.org/abs/math/9906084>.
- Getzler and Kapranov, *Modular operads*, for the graph-over-tree modular
  framework: <https://arxiv.org/abs/dg-ga/9408003>.
