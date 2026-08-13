# Punctured-Torus Hostile Test of the Resolved Surface Counit

## Record

Date: 2026-08-13

Status: the smallest genuine handle test closes coefficient by coefficient,
without reconstructing the answer from Cut-equation uniqueness.  On the
once-punctured torus, two cyclic three-point counits sew through the theta
fatgraph in nine resolved sectors.  Three sectors contain one closed
polarization circuit and six contain none.  Termwise Brauer augmentation sends
all nine sectors to the scalar state and gives

\[
G_{T_{1,1}}^\phi=\frac13x_{11}^3.
\]

The nonseparating orbit Cut gives the annulus function \(x_{11}^2\) directly.
By contrast, evaluating the \(D\)-circuits before cutting fails to commute with
the Cut by

\[
\frac{2(D-1)}9x_{11}^2.
\]

Thus this example does not merely agree with the general theorem.  It exposes
the obstruction that the resolved order of operations removes.

Reproducible certificate:

```text
research/nima/check_punctured_torus_counit.rs
```

## Why this is the first hostile topology

The planar one-loop one-point test of entry 46 contains a closed polarization
circuit, but its surface is a punctured disk or annulus.  It has no handle and
does not support the one-holed-torus \(3S\) relation.

The first scalar surface in the published Cut-equation examples that does both
jobs is the torus with one puncture.  It has a single theta fatgraph.  The three
edges of a marked theta presentation lie in one mapping-class orbit, and the
ribbon automorphism group has order three.  Consequently its scalar surface
function is

\[
\boxed{
G_{T_{1,1}}^\phi
=
\frac1{3}x_{11}^{3}.
}
\]

Cutting one representative of the orbit opens the handle to the annulus.  The
published Cut equation reads

\[
\partial_{x_{11}}G_{T_{1,1}}^\phi
=
G_{\rm annulus}^\phi
=
x_{11}^{2}.
\]

We use these formulas only as target data.  The calculation below derives both
coefficients from the resolved tree sectors and their sewings; it does not use
the uniqueness argument of entry 48.

## The local three-point input

In scalar-scaffold variables, the three-gluon amplitude is

\[
\begin{aligned}
A_3^{\rm YM}
={}&X_{14}X_{26}+X_{36}X_{24}+X_{25}X_{46}\\
&-X_{25}X_{36}-X_{14}X_{36}-X_{14}X_{25}.
\end{aligned}
\]

Its three cyclic pairwise-counit sectors are

\[
U_0=\partial_{X_{14}}\partial_{X_{26}},
\qquad
U_1=\partial_{X_{36}}\partial_{X_{24}},
\qquad
U_2=\partial_{X_{25}}\partial_{X_{46}}.
\]

They obey, separately,

\[
\boxed{
U_iA_3^{\rm YM}=1,
\qquad i=0,1,2.
}
\]

Rotation by two scaffold labels cyclically permutes both the amplitude and the
three sectors.  Over the rational coefficient ring appropriate to a surface
function, the manifestly cyclic local representative is therefore

\[
u_3^{\rm cyc}=\frac13(U_0+U_1+U_2).
\]

The integral deletion resolution of entry 43 is still the chain-level source.
The average is used here because the target theta graph already carries the
rational symmetry factor \(1/3\).

## The resolved theta sewing table

The state part of \(U_i\) pairs two of the three polarization flags and sends
the remaining flag into the coefficient strand.  Call that remaining flag the
singleton of sector \(i\).  Sew two three-point vertices along the three theta
edges, and denote the resolved result for local sectors \((i,j)\) by
\(\kappa_{ij}\).

There are two cases.

1. If \(i=j\), the common singleton makes a through coefficient strand, while
   the other two theta edges close into one polarization circuit.
2. If \(i\ne j\), all three theta edges belong to the through strand and no
   polarization circuit closes.

Thus the circuit number is exactly

\[
\boxed{
c(\kappa_{ij})=\delta_{ij}.
}
\]

The raw Brauer evaluation table is

\[
\left(
\begin{array}{ccc}
D&1&1\\
1&D&1\\
1&1&D
\end{array}
\right).
\]

This is already a useful falsifier.  The number of state circuits is not the
graph Betti number and is not constant across resolved sectors.

Let \(a,b,c\) denote the three marked theta edges.  Including the two local
cyclic averages and the theta automorphism factor gives the resolved surface
coefficient

\[
\boxed{
\mathcal U_{\Theta}^{\rm res}
=
\frac1{27}x_ax_bx_c
\sum_{i,j=0}^{2}[\kappa_{ij}].
}
\]

If the state patterns are evaluated prematurely, this becomes

\[
\operatorname{ev}_D(\mathcal U_{\Theta}^{\rm res})
=
\frac{3D+6}{27}x_ax_bx_c
=
\frac{D+2}{9}x_ax_bx_c.
\]

The resolved augmentation instead acts on each pattern before forgetting it:

\[
\begin{aligned}
\epsilon_{\rm Br}(\mathcal U_{\Theta}^{\rm res})
&=
\frac1{27}x_ax_bx_c\sum_{i,j}1\\
&=
\boxed{\frac13x_ax_bx_c}.
\end{aligned}
\]

After mapping-class quotient,

\[
x_a=x_b=x_c=x_{11},
\]

this is the published scalar surface function \(x_{11}^3/3\).  The equality
has been obtained by explicit local differentiation and state sewing, not by
integrating its Cut.

## The nonseparating Cut, before and after resolution

Open theta edge \(k\).  A closed polarization circuit survives precisely when
both local singleton sectors equal the opened edge:

\[
\boxed{
c_k(\kappa_{ij})
=
\delta_{ik}\delta_{jk}.
}
\]

For each marked edge, the raw opened table therefore contains one \(D\)-valued
sector and eight circuit-free sectors.  The orbit Cut sums the three edge
representatives.  After termwise augmentation its coefficient is

\[
\frac1{27}
\sum_{k=0}^{2}\sum_{i,j=0}^{2}1
=
\frac{27}{27}
=1.
\]

The two uncut theta edges give \(x_{11}^2\), so directly

\[
\boxed{
\Delta_{x_{11}}
\epsilon_{\rm Br}(\mathcal U_{\Theta}^{\rm res})
=
x_{11}^2
=
G_{\rm annulus}^\phi.
}
\]

The factor three in the orbit Cut cancels the theta automorphism factor.  This
is the coefficient-level orbit--stabilizer mechanism behind
\(\partial_x(x^3/3)=x^2\).

## The obstruction seen by premature state evaluation

The same calculation before \(D\mapsto1\) does not form a Cut square.

Evaluate first and then differentiate the orbit variable:

\[
\partial_x
\left(
\frac{3D+6}{27}x^3
\right)
=
\frac{D+2}{3}x^2.
\]

Cut the resolved patterns first and then evaluate their remaining circuits:

\[
\frac{3D+24}{27}x^2
=
\frac{D+8}{9}x^2.
\]

Their difference is

\[
\boxed{
\left(
\partial_x\operatorname{ev}_D
-
\operatorname{ev}_D\Delta_x
\right)
\mathcal U_{\Theta}^{\rm res}
=
\frac{2(D-1)}9x^2.
}
\]

This is nonzero for the physical polarization dimension.  It vanishes exactly
after the scalar state augmentation \(D\mapsto1\).  Therefore:

> The resolved state cover is not dispensable bookkeeping.  Cutting can open a
> circuit, so a circuit evaluated before the Cut cannot be recovered from the
> already-summed coefficient.

This gives an explicit reason that a global genus normalization or a naïve
substitution on an already-sewn function cannot define the surface counit.

## Coefficient-level \(3S\) covariance

Take primitive slopes \(a,b\in\mathbb Z^2\) with \(\det(a,b)=1\), and set

\[
c=a+b.
\]

The three slopes form a Farey triangle.  Transport around its three \(S\)-moves
simultaneously permutes:

- the three marked theta edges;
- the singleton sector at the left vertex;
- the singleton sector at the right vertex;
- the edge selected by a Cut.

Both tables are invariant under every simultaneous permutation:

\[
\delta_{ij}
=
\delta_{\rho(i)\rho(j)},
\]

\[
\delta_{ik}\delta_{jk}
=
\delta_{\rho(i)\rho(k)}\,
\delta_{\rho(j)\rho(k)}.
\]

The second displayed product is ordinary multiplication; it records the same
single surviving circuit after relabelling.  Hence the complete coefficient
carrier, not merely its augmented scalar value, is transported consistently.

For the oriented chart frames

\[
F_a=(a,b),
\qquad
F_b=(b,-a),
\qquad
F_c=(c,-a),
\]

the transition matrices still obey

\[
F_a^{-1}F_c\,F_c^{-1}F_b\,F_b^{-1}F_a=1.
\]

Thus there is no \(3S\) holonomy in the explicitly populated coefficient
table.  This is stronger than the earlier empty chart check: the state and Cut
coefficients have now been carried around the triangle.

## Marked physical specialization

The mapping-class-quotiented surface function has only one variable \(x_{11}\).
As emphasized in the Cut-equation paper, a general nonplanar surface function
is not by itself a conventional loop integrand: distinct propagators in one
mapping-class orbit need distinct momentum assignments.

The physical specialization must therefore be made on the marked cover before
the orbit variables are identified.  With theta-edge momenta \(P_a,P_b,P_c\),

\[
x_a\mapsto\frac1{P_a^2},
\qquad
x_b\mapsto\frac1{P_b^2},
\qquad
x_c\mapsto\frac1{P_c^2},
\]

the augmented coefficient becomes

\[
\boxed{
\frac1{3P_a^2P_b^2P_c^2}.
}
\]

For a vacuum routing one may take \(P_c=-(P_a+P_b)\).  This is scaleless after
massless loop integration, but the marked rational integrand identity is exact.
No additional contact monomial is generated because the counit acts on the
resolved coefficient carrier and leaves the three propagator variables
untouched.

This also identifies a necessary refinement of the slogan “physical
specialization”: beyond the planar limit it is a map from the marked MCG cover,
not from the one-variable surface-function quotient.

## What this proves and what it does not

Proved directly in this entry:

- all three local three-point counit sectors give the scalar cubic vertex;
- the complete nine-sector theta sewing table;
- the pattern-dependent circuit count \(c(\kappa_{ij})=\delta_{ij}\);
- the scalar coefficient \(1/3\) without Cut-equation reconstruction;
- the nonseparating torus-to-annulus Cut coefficient \(1\);
- the raw pre-augmentation Cut defect \(2(D-1)/9\);
- covariance of the populated coefficient and Cut tables under \(3S\);
- exact marked momentum specialization of the scalar image.

Not proved:

- existence of one differential operator acting on an already-sewn two-loop
  Yang--Mills vacuum integrand and producing the scalar integrand;
- derivation of the resolved nine-sector carrier from such a post-sewing
  operator rather than from the established local tree counits;
- a nonvacuum genus-one example with external physical gluon states;
- survival of a strict point-set representative after forgetting the marked
  cover and imposing momentum homology.

The first two omissions are the strictification problem already isolated in
entry 48.  The third is now the next genuinely stronger physical test.  The
vacuum theta graph tests the modular state algebra, the nonseparating Cut, the
automorphism factor, and \(3S\), but not an external S-matrix element.

## Executable evidence

The Rust certificate verifies:

- exact action of the three second-order transmutation sectors on
  \(A_3^{\rm YM}\);
- cyclic invariance of the six-term three-point polynomial;
- all nine closed theta sewings;
- all twenty-seven opened-edge sewings;
- 162 simultaneous slope/state/Cut covariance squares;
- 308 oriented Farey \(3S\) chart triangles.

The finite enumeration audits signs, normalization, circuit opening, and orbit
factors.  The Kronecker-delta formulas above are the all-sector proof.

## Primary sources

- Arkani-Hamed, Frost, and Salvatori, *The Cut Equation*, especially the
  annulus and punctured-torus surface functions, the symmetry-factor
  discussion, and the warning that nonplanar surface functions are not already
  conventional integrands: <https://arxiv.org/abs/2412.21027>.
- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*, for the resolved contraction-curve interpretation of gluon state
  sums and the all-loop closed-curve rule:
  <https://arxiv.org/abs/2512.17019>.
- Backus and Figueiredo, *Scaffolding Residues and Transmutations*, for the
  tree and one-loop transmutation operators used in entries 42 and 46:
  <https://arxiv.org/abs/2505.17179>.
- Hatcher, *Pants Decompositions of Surfaces*, for the one-holed-torus
  \(3S\) relation: <https://arxiv.org/abs/math/9906084>.
