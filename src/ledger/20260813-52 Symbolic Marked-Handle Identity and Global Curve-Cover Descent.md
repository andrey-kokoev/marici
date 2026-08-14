# Symbolic Marked-Handle Identity and Global Curve-Cover Descent

## Record

Date: 2026-08-13

Status: the finite marked-handle certificate of entry 51 is now a symbolic
identity on the universal Gram-free on-shell chart.  Its curve dictionary is
also proved to be natural under flip changes of spine, strict under Cuts before
closed-circuit evaluation, and equivariant under the mapping class group.
Consequently the resolved graph-cell numerators assemble into a
mapping-class-summed surface function satisfying the Cut Equation.

This closes the target stated at the end of entry 51:

\[
\text{finite graph cell}
\longrightarrow
\text{symbolic local identity}
\longrightarrow
\text{flip/Cut/MCG descent}.
\]

The conclusion has an important type qualification.  It is a theorem about the
resolved curve-cover surface object.  It does not say that the numerators of two
different flipped cubic graphs are equal.  Those graphs are distinct cells in
the surface sum.  It says that their curve labels use one intrinsic surface
alphabet, that their common Cut faces agree, and that the orbit sum is
well-defined.

Reproducible certificates:

    research/nima/check_marked_handle_symbolic_identity.rs
    research/nima/check_marked_handle_x_dictionary.rs
    research/nima/check_marked_handle_counit.rs

## Two symbolic levels

There are two different polynomial rings and they must not be conflated.

The free surface ring keeps an independent variable for every homotopy class of
curve,

\[
\mathcal R_{\rm surf}
=
\mathbb Z[
Y_{[C]},
[\gamma;\nu_\gamma,\Delta_\gamma]
].
\]

The numerator generator is normalized by

\[
Y_C=-2X_C.
\]

It is held independent from the denominator variable until physical
specialization.  With this convention one four-extension factor maps directly
to one handle contraction, without a graph-dependent overall normalization.

The physical specialization maps many such variables to the same momentum or
Gram invariant,

\[
\operatorname{sp}_{\rm hom}:
\mathcal R_{\rm surf}
\longrightarrow
\mathcal R_{\rm Gram}.
\]

This many-to-one map is expected.  Surface kinematics distinguishes homotopy
classes; conventional momentum kinematics remembers only their homology and
momentum routing.

The exact surface certificate of entry 51 remains the stronger statement about
the curve alphabet.  On the marked theta handle it has:

- 150 distinct homotopy-sensitive curve variables;
- 62,208 signed endpoint-extension origins;
- 10,317 generated monomials before cancellation;
- 5,616 nonzero monomials after cancellation;
- 5,424 circuit-free and 192 closed-circuit monomials.

The new symbolic physical image has only 30 monomials.  It is not a replacement
for the 5,616-monomial polynomial.  It proves the physical specialization of
that freer object.

## The resolved graph-cell polynomial

For a trivalent marked ribbon graph \(\Gamma\), let a sector word
\(\mathbf s\) choose one of the three metric-pairing terms at each cubic
Yang--Mills vertex.  Sewing the paired indices produces a finite family
\(\mathcal O(\mathbf s)\) of open strands and a family
\(\mathcal Z(\mathbf s)\) of closed strands.

For an open strand \(P\), independently extend its two endpoints by

\[
\epsilon=0:
\quad\text{turn right once and then left forever},
\]

\[
\epsilon=1:
\quad\text{turn left forever}.
\]

The four-extension operator is

\[
\Phi_\Gamma(P)
=
\sum_{\epsilon_L,\epsilon_R\in\{0,1\}}
(-1)^{\epsilon_L+\epsilon_R}
Y_{C_{\epsilon_L,\epsilon_R}(P)}.
\]

Do not yet replace a closed strand by \(D\).  Retain its curve and its two
physical exponent data as a generator

\[
[\gamma;\nu_\gamma,\Delta_\gamma].
\]

The origin-resolved graph-cell numerator is

\[
\boxed{
\widetilde P_\Gamma
=
\sum_{\mathbf s}
\left(
\prod_{P\in\mathcal O(\mathbf s)}
\Phi_\Gamma(P)
\right)
\left(
\prod_{\gamma\in\mathcal Z(\mathbf s)}
[\gamma;\nu_\gamma,\Delta_\gamma]
\right).
}
\]

There are two later evaluations.  The resolved counit is

\[
\operatorname{ev}_{\rho}
[\gamma;\nu_\gamma,\Delta_\gamma]
=
\rho_\gamma
:=
\nu_\gamma-\Delta_\gamma.
\]

For the generic and internal-boundary cases found in the physical gluing
analysis,

\[
(0,-D)\longmapsto D,
\qquad
(1,1-D)\longmapsto D.
\]

The equality of these two final values does not make their pre-Cut carriers
equal.  Their tags must survive until all relevant Cuts have been taken.

## Universal endpoint identity

The local algebra behind the curve rule is the free quadratic identity

\[
\boxed{
(b-d)^2+(a-c)^2-(b-c)^2-(a-d)^2
=
2(b-a)\mathbin{\cdot}(c-d).
}
\]

No momentum conservation, dimension choice, or sample point is used here.
With the endpoint orientations fixed by the three-point calibration, this
becomes the component identity

\[
\sum_{\epsilon_L,\epsilon_R}
(-1)^{\epsilon_L+\epsilon_R}
\,4X_{C_{\epsilon_L,\epsilon_R}(P)}
=
-2H_L\mathbin{\cdot}H_R.
\]

Equivalently,

\[
\operatorname{sp}_{\rm hom}\Phi_\Gamma(P)
=
-2\sum_{\epsilon_L,\epsilon_R}
(-1)^{\epsilon_L+\epsilon_R}
X_{C_{\epsilon_L,\epsilon_R}(P)}
=
H_L\mathbin{\cdot}H_R.
\]

Thus every four-extension factor is the polarization of one open contraction
strand.  Multiplication over disjoint strands gives the **gauge-reduced
graphical contraction network**, while closed strands give the corresponding
trace carrier.  It does not give the naive full-handle all-metric cubic
network: the physical projector supplies a nonzero longitudinal correction
between that network and the reduced graphical one.  This is the symbolic
reason that the curve-cover polynomial and the gauge-reduced graphical tensor
network agree before numerical specialization.

## Symbolic marked-handle theorem

Let \(\Gamma_3\) be the five-vertex marked-theta graph of entries 50 and 51.
Impose:

- the three simultaneous massless three-point momentum relations;
- momentum conservation at every cubic vertex;
- null external scaffold polarizations;
- external transversality.

A free chart for the resulting Gram-free on-shell variety has thirteen
independent Gram coordinates.  Adjoin the formal state-trace variable \(D\).
The physical-projector calculation initially lies in

\[
\mathbb Z[
\mathrm{Gram},D,A^{-1}
],
\]

where \(A=l\mathbin{\cdot}r\) is the reference denominator.  The graphical
curve-cover polynomial lies in

\[
\mathbb Z[\mathrm{Gram},D].
\]

### Theorem

For every one of the twelve spanning trees of \(\Gamma_3\), and for each of
the two cyclic null-reference prescriptions audited by the certificate,

\[
\boxed{
\operatorname{LS}^{\rm projector}_{\Gamma_3}
=
\operatorname{sp}_{\rm hom}
\operatorname{ev}_{\rho}
\widetilde P_{\Gamma_3}.
}
\]

All negative powers of \(A\) cancel.  The common result is a 30-monomial
polynomial in \(\mathbb Z[\mathrm{Gram},D]\).  It is invariant under the
order-three road rotation,

\[
\rho(P)=P,
\qquad
\rho^3=1.
\]

The all-metric network is not this polynomial.  Their difference is a nonzero
10-monomial polynomial.  Therefore the symbolic result retains the
longitudinal correction that was first detected numerically in entry 51.

### Proof certificate

The Rust audit performs the following exact computation.

1. It expands the five cubic tensors into all
   \(3^5=243\) metric/handle sector words.
2. It evaluates every connected index strand symbolically.  An open strand is
   a Gram product and a closed strand is the formal variable \(D\).
3. It inserts
   \[
   -g+\frac{lr+rl}{l\mathbin{\cdot}r}
   \]
   on the two loop-closing edges, producing nine projector terms per
   sector/tree.
4. It repeats the calculation for twelve spanning trees and two cyclic
   reference choices, for 24 symbolic presentations.
5. It compares every Laurent monomial coefficient to the graphically reduced
   curve-cover polynomial.
6. It separately verifies the universal four-extension identity and exact
   order-three covariance.

Equality holds on the dense chart \(A\ne0\).  Because every denominator
cancels and the result is polynomial, it extends across \(A=0\) by polynomial
continuation.  Unlike entry 51, no sampled kinematic points enter the proof.

## Flip naturality

Let \(T\) be a marked triangulation of an oriented surface \(S\), and let
\(G_T\) be its dual ribbon spine.  With the boundary endpoints included as
objects, the embedded spine gives an isomorphism of fundamental groupoids

\[
\iota_T:
\Pi_1(G_T,B)
\overset{\sim}{\longrightarrow}
\Pi_1(S,B).
\]

A signed reduced edge word is the unique reduced representative of its class
in the graph groupoid.  If a Whitehead flip changes \(T\) to \(T'\), define
the chart transport

\[
F_{T'T}
=
\iota_{T'}^{-1}\iota_T.
\]

The turn prescription also has an intrinsic interpretation.  Thicken the
ribbon spine to its oriented regular neighborhood.  Turning left forever
follows one boundary arc of that neighborhood; turning right once and then
left forever follows the adjacent boundary arc.  A Whitehead move is supported
in a disk and canonically identifies the regular-neighborhood boundary outside
that disk.  Thus these two extensions are topological boundary arcs, not extra
coordinates attached to one drawing of the graph.

This immediately preserves:

- concatenation and cancellation of immediate backtracking;
- path reversal;
- boundary endpoints;
- the cyclic order, because the surface orientation is fixed;
- left/right endpoint extension.

Therefore

\[
\boxed{
F_{T'T}\Phi_T(P)
=
\Phi_{T'}(F_{T'T}P).
}
\]

Every transition factors through the same intrinsic groupoid
\(\Pi_1(S,B)\).  Hence the cocycle relation is strict:

\[
F_{T''T'}F_{T'T}=F_{T''T}.
\]

There is no flip-path holonomy.  Hatcher's connectivity theorem says that any
two surface triangulations are related by elementary moves; in the standard
boundary-marked cases the triangulation complex supplies the corresponding
2-cell relations.  Here flatness is even more direct: all chart transitions
were defined through the identity intrinsic surface class.

This proves descent of the curve alphabet and endpoint-extension rule.  It
does not identify the two graph-cell polynomials
\(\widetilde P_T\) and \(\widetilde P_{T'}\).  A flip changes the cubic graph,
so those are generally distinct summands.  Their relationship is assembly
along their common Cut faces.

## Strict resolved Cut compatibility

Let \(\mathsf{Str}(G_T)\) be the free module on resolved strand diagrams:
sector words, actual open strands, and tagged closed strands are retained.
Let \(\mathsf{Cov}(S)\) be the free module on the corresponding intrinsic
curve-cover configurations.  Then

\[
\widetilde\Phi_T:
\mathsf{Str}(G_T)
\longrightarrow
\mathsf{Cov}(S)
\]

is the strandwise extension map used above.

For a propagator curve \(C\) dual to an edge \(e_C\), cutting \(S\) along
\(C\) deletes that sewing link.  A strand not using it restricts unchanged; a
strand using it opens or splits at the new boundary; a closed strand using it
becomes open.  Denote this operation by

\[
\Delta_C^{\rm str}
\quad\text{and}\quad
\Delta_C^{\rm cov}
\]

on the two modules.

### Cut theorem

\[
\boxed{
\Delta_C^{\rm cov}\widetilde\Phi_T
=
\widetilde\Phi_{T\setminus C}\Delta_C^{\rm str}.
}
\]

### Proof

Cutting is restriction of embedded one-manifolds to \(S\setminus C\).  It
commutes with disjoint union, path reversal, and graph-word reduction.
The cut surface inherits its orientation and a canonical collar at the new
boundary, so restriction also commutes with each left/right endpoint
extension.  A closed strand is still present as a tagged embedded curve when
it is opened.  The equality therefore holds on every strand generator and is
multiplicative.

For disjoint Cuts \(C_1,C_2\), restrictions commute:

\[
\Delta_{C_1}\Delta_{C_2}
=
\Delta_{C_2}\Delta_{C_1}.
\]

If \(C\) separates the surface, the target is the tensor product of the two
component cover modules.  The same generatorwise proof applies.

The order of operations is essential:

\[
\boxed{
\text{Cut resolved covers first, then evaluate closed carriers.}
}
\]

If a closed circuit is replaced prematurely by the scalar \(D\), a later Cut
cannot know how to open it.  Entry 49 computed the resulting punctured-torus
defect exactly:

\[
\frac{2(D-1)}9x^2.
\]

The resolved construction has no such defect.  The marked-handle counit audit
checks every subset of internal edges in its finite family, including 120
marked-theta Cut squares, all 64 three-leg Cut patterns, and 15,552 cyclic
state/Cut covariance squares.

## Mapping-class equivariance

An orientation-preserving mapping class \(m\) transports embedded strands,
curve endpoints, cyclic order, and closed-curve tags.  Hence

\[
\boxed{
m_*\widetilde P_\Gamma
=
\widetilde P_{m\Gamma}.
}
\]

After replacing the marked curve variables by variables indexed by
mapping-class orbits, the numerator of an orbit cell is independent of the
chosen representative.

Keep numerator variables \(Y_C\) independent from inverse-propagator variables

\[
x_C=X_C^{-1}.
\]

This separation is required because the Cut derivative acts only on the
denominator variables.  Define the resolved Yang--Mills surface function

\[
\boxed{
\mathcal G^{\rm YM,res}_S
=
\sum_{[\Gamma]\in
\operatorname{Tri}(S)/\operatorname{MCG}(S)}
\frac{1}{|\operatorname{Aut}\Gamma|}
\widehat P_\Gamma(Y)
\prod_{C\in\Gamma}x_{[C]},
}
\]

where

\[
\widehat P_\Gamma
=
\operatorname{ev}_{Y}\widetilde P_\Gamma
\]

but the closed tags remain resolved until after Cuts.

## Mapping-class Cut theorem

For every mapping-class orbit \([C]\),

\[
\boxed{
\partial_{x_{[C]}}
\mathcal G^{\rm YM,res}_S
=
\mathcal G^{\rm YM,res}_{S\setminus C}.
}
\]

For a separating curve, the right-hand side is the product of the two
component surface functions.

### Proof

Suppose a triangulation \(\Gamma\) contains \(k\) distinct curves in the
orbit \([C]\).  Its denominator monomial contains \(x_{[C]}^k\), so
differentiation produces \(k\) pointed choices of which representative to
cut.

These \(k\) pointed choices need not remain equivalent after cutting.  The
mapping class group of the cut surface is the stabilizer of the chosen curve.
Thus differentiation performs exactly the orbit-to-stabilizer passage
required for the cut surface.

The symmetry factors match by groupoid cardinality.  If
\(A=\operatorname{Aut}\Gamma\) acts on the \(k\) candidate curves, then

\[
\frac{k}{|A|}
=
\sum_{[e]\in E_C/A}
\frac{1}{|\operatorname{Stab}_A(e)|}.
\]

Each pointed stabilizer is the automorphism group of the corresponding cut
cell.  Finally, strict resolved Cut compatibility gives

\[
\Delta_C\widehat P_\Gamma
=
\widehat P_{\Gamma\setminus C}
\]

for each pointed choice.  The differentiated orbit sum is therefore exactly
the mapping-class sum on \(S\setminus C\), with its correct numerator and
symmetry factor.

The hostile torus factor is the smallest example:

\[
\partial_x\left(\frac{x^3}{3}\right)=x^2.
\]

The factor \(1/3\), the three pointed cuts, and the annulus result are one
orbit-stabilizer identity, not an ad hoc normalization.

## Final commutative structure

The genuinely commutative square is the resolved one:

\[
\begin{array}{ccc}
\mathsf{Str}(G_T)
&\xrightarrow{\ \widetilde\Phi_T\ }&
\mathsf{Cov}^{\rm res}(S)
\\[3pt]
\big\downarrow{\Delta_C}
&&
\big\downarrow{\Delta_C}
\\[3pt]
\mathsf{Str}(G_{T\setminus C})
&\xrightarrow{\ \widetilde\Phi_{T\setminus C}\ }&
\mathsf{Cov}^{\rm res}(S\setminus C).
\end{array}
\]

Only on the bottom, after affected circuits have opened, do we apply

\[
\mathsf{Cov}^{\rm res}(S\setminus C)
\xrightarrow{\ \operatorname{ev}_{\rho}\ }
\mathcal R_{\rm surf}(S\setminus C)
\xrightarrow{\ \operatorname{sp}_{\rm hom}\ }
\mathcal R_{\rm Gram}(S\setminus C).
\]

There is deliberately no asserted Cut-commuting square with a premature
\(D\)-evaluation on its top row.  Entry 49 proves that square is false.
Flip transport acts horizontally through the intrinsic surface groupoid, and
the mapping-class sum is the groupoid quotient of the same resolved object.

This gives the precise operation order:

\[
\boxed{
\text{resolve}
\;\longrightarrow\;
\text{Cut/assemble}
\;\longrightarrow\;
\text{MCG quotient}
\;\longrightarrow\;
\text{physical specialization}.
}
\]

## What is established

- The marked-handle projector identity is symbolic, not sampled.
- Every projector denominator cancels.
- All 24 audited tree/reference presentations give one polynomial.
- The nonzero longitudinal correction survives symbolically.
- The 30-monomial Gram result is correctly typed as the image of the freer
  5,616-monomial surface polynomial.
- Signed edge-word curve labels descend under all flip chart changes.
- The endpoint-extension rule is flip natural and mapping-class equivariant.
- The resolved cover map is strict for separating, nonseparating, and
  commuting multiple Cuts.
- The mapping-class orbit sum satisfies the Cut Equation with the exact
  orbit-stabilizer and automorphism factors.

## Scope

This entry does not claim:

- equality of distinct flipped graph numerators;
- a conventional nonplanar loop-momentum integrand after the MCG quotient;
- a symbolic physical-projector comparison for every cubic graph and every
  topology;
- an all-topology proof that every possible nested projector history evaluates
  to the same \(\nu-\Delta\) carrier;
- a scale-carrying integrated four-point amplitude.

The result is instead the exact local-to-global statement needed here: the
marked-handle physical identity is symbolic, and the curve-cover construction
that realizes it has the right flip, Cut, and mapping-class functoriality to
live in the scalar surface algebra.

## Primary sources

- Carrôlo and Figueiredo, How gluon leading singularities discover curves on
  surfaces, for the endpoint-extension identity, curve-cover rule, physical
  projectors, mapping-class selection, and closed-curve exponents:
  <https://arxiv.org/abs/2512.17019>.
- Arkani-Hamed, Frost, and Salvatori, The Cut Equation, for surface functions
  as MCG-inequivalent triangulation sums, independent numerator variables,
  orbit-stabilizer Cuts, and automorphism weights:
  <https://arxiv.org/abs/2412.21027>.
- Arkani-Hamed et al., Surface Kinematics and The Yang-Mills Integrand, for
  the distinction between homotopy-sensitive surface kinematics and its
  ordinary momentum/homology specialization:
  <https://arxiv.org/abs/2408.11891>.
- Hatcher, Triangulations of Surfaces, for connectivity by elementary flips
  and the contractible triangulation complex:
  <https://pi.math.cornell.edu/~hatcher/Papers/TriangSurf.pdf>.

## Internal dependencies

- Entry 46: resolved closed-circuit carrier.
- Entry 48: Cut-Equation descent and all-topology counit.
- Entry 49: punctured-torus orbit/Cut hostile test.
- Entry 51: free surface dictionary and finite marked-handle identity.
