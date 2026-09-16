# A one-pole crossing family gives a local half-orbit hostile transition

## Status correction

The rank-one calculation below is exact in the open half-plane, but two qualifications are essential. First, it is one half-orbit and does not by itself impose the full conjugation plus functional-equation symmetry of the completed zeta divisor. Second, the family is not continuous through \(a=0\) in the endpoint-augmented graph topology: although the interior kernel tends to zero on fixed packets, its boundary phase current converges to a nonzero spectral-flow atom. Thus the crossing mode does not simply disappear at \(a=0\); it transfers from the interior model-space channel to the boundary/index channel. Claims below that describe a zero or degenerate filler at the crossing apply only to the unaugmented interior kernel.

## Purpose

Construct a fully explicit analytic family that is positive on one side, degenerate at the crossing, and has one negative square on the other side.

This is a hostile fixture for the architecture. It is not a statement about the actual zero set of the completed zeta function.

## Crossing family

Work in the upper half-plane and define, for real \(a\),

\[
\Theta_a(z)
=
\frac{z+ia}{z-ia}.
\]

For real \(t\),

\[
|\Theta_a(t)|=1
\]

for every \(a\). Thus boundary unitarity survives the entire crossing and cannot distinguish the three regimes.

Associate the de Branges--Rovnyak kernel

\[
k_a(z,w)
=
\frac{
1-
\Theta_a(z)
\overline{\Theta_a(w)}
}
{-i(z-\bar w)}.
\]

## Exact kernel

Direct simplification gives

\[
k_a(z,w)
=
\frac{-2a}
{(z-ia)(\bar w+ia)}.
\]

Hence \(k_a\) has rank one for every \(a\ne0\).

For a finite point packet \(Z=(z_1,\ldots,z_N)\), let

\[
u_a(Z)_j
=
\frac1{z_j-ia}.
\]

Then

\[
G_{a,Z}
=
-2a
u_a(Z)

u_a(Z)^*.
\]

Its only nonzero eigenvalue is

\[
\lambda_a(Z)
=
-2a
\|\nu_a(Z)\|^2.
\]

## Three regimes

### Positive side

If

\[
a<0,
\]

write \(b=-a>0\). Then

\[
\Theta_a(z)
=
\frac{z-ib}{z+ib},
\]

which is a one-zero Blaschke factor. The kernel is positive rank one:

\[
k_a\succeq0.
\]

### Crossing

If

\[
a=0,
\]

then

\[
\Theta_0=1
\]

and

\[
k_0=0.
\]

The positive feature collapses to the zero space.

### Hostile side

If

\[
a>0,
\]

then \(\Theta_a\) is the reciprocal of a Blaschke factor with a pole at \(ia\). The kernel is negative rank one:

\[
k_a\preceq0,
\qquad
\operatorname{ind}_-(k_a)=1.
\]

Its Krein--Langer denominator has degree one.

## Boundary phase channel

On the real axis,

\[
\frac1i
\partial_t
\log\Theta_a(t)
=
-
\frac{2a}
{t^2+a^2}
\]

with the displayed orientation.

Thus the boundary phase current changes sign at the crossing even though \(|\Theta_a|=1\) throughout.

As \(a\to0^\pm\), this Poisson profile concentrates at \(t=0\). Pointwise away from zero it tends to zero, but distributionally it carries a nontrivial spectral-flow mass with opposite signs on the two sides.

Therefore pointwise boundary convergence misses the crossing index.

## Krein--Langer channel

The factorization changes as follows:

| Regime | Schur numerator | Blaschke denominator | Negative index |
|---|---|---|---:|
| \(a<0\) | \(\Theta_a\) | constant | 0 |
| \(a=0\) | \(1\) | constant | 0, degenerate kernel |
| \(a>0\) | \(1\) | \((z-ia)/(z+ia)\) | 1 |

The model-space defect appears immediately after the pole enters the upper half-plane.

## Source-observation channel

Translated Gaussian observers are total on every finite evaluation packet. Hence for every \(a>0\), the source detects the rank-one negative direction.

For a fixed finite point packet, the negative eigenvalue tends to zero linearly as \(a\downarrow0\):

\[
\lambda_a(Z)
=
-2a
\|\nu_0(Z)\|^2
+O(a^2).
\]

Thus finite numerical margins collapse before the sign change. Immediately after crossing, the same source vector becomes a genuine negative witness.

A normalized reproducing witness becomes increasingly concentrated near the crossing point as \(a\to0\). This explains why fixed coarse packets may fail to resolve the hostile direction close to the transition.

## Douglas channel

On the hostile side, the factorization is pure defect:

\[
k_a
=
-
\frac{k_{B_a}}
{B_a\overline{B_a}}.
\]

The Schur feature is zero while the defect feature has rank one. Therefore

\[
A_S=0,
\qquad
A_B\ne0.
\]

No linear map, bounded or otherwise, can satisfy

\[
A_B=CA_S.
\]

At the crossing both features collapse. On the positive side, the same rank-one channel belongs to the positive Schur feature instead of the defect feature.

Hence the Douglas map does not become expansive continuously. Its domain capacity vanishes at the crossing, and the channel reappears with opposite metric sign.

## Endpoint-parity channel

The family models one index-one boundary crossing. In an endpoint-augmented presentation, its rank-one direction behaves like the odd endpoint line:

1. positive before crossing;
2. null at the crossing;
3. negative after crossing.

A fixed finite-rank endpoint correction can cancel it only if that correction tracks the moving reproducing direction. A stationary endpoint line cannot absorb an arbitrary moving pole family.

## Suzuki metric channel

The positive Suzuki-type Gram remains positive by construction. The arithmetic divisor metric changes to a hyperbolic or negative block after crossing.

Thus the comparison defect acquires a negative eigenvalue at the same parameter value. The positive carrier itself does not become singular; the source-authorized identification with the arithmetic metric fails.

This separates failure of a comparison edge from failure of the ambient positive carrier.

## Tetrahedral channel

The signed tetrahedral equation remains valid for every \(a\), because the defect face is retained:

\[
K_{arith,a}
=
K_{positive,a}
-
K_{defect,a}.
\]

What changes is the positive-lift fiber:

| Regime | Signed tetrahedron | Positive metric filler |
|---|---|---|
| \(a<0\) | exists | exists for the rank-one kernel |
| \(a=0\) | exists | degenerate zero filler |
| \(a>0\) | exists | empty on a source-faithful carrier |

Higher coherence does not jump. Only the metric-lift component changes.

## Polarity and dagger channel

Dagger sends the pole-crossing family to its opposite orientation. The two polarity sheets exchange the positive and negative regimes.

At \(a=0\), they meet on the dagger-fixed degenerate kernel. Therefore the crossing is the local fold locus of the polarity prism.

## Successor channel

Multiplication by an admitted nonvanishing analytic successor preserves the sign of the rank-one Gram by congruence. It transports the hostile witness but cannot remove it.

A successor with a zero exactly at the pole coordinate can annihilate the witness, but then source faithfulness is lost at that coordinate. Such annihilation must be recorded as a quotient, not as positivity improvement.

## What happens immediately before and after

For a small \(\varepsilon>0\):

| Channel | \(a=-\varepsilon\) | \(a=0\) | \(a=+\varepsilon\) |
|---|---|---|---|
| Boundary modulus | unitary | unitary | unitary |
| Boundary phase current | positive orientation | concentrated crossing index | negative orientation |
| Kernel rank | 1 | 0 | 1 |
| Kernel sign | positive | zero | negative |
| Krein negative index | 0 | 0 | 1 |
| Source witness | positive norm | null | negative square |
| Douglas comparison | trivial positive feature | zero map | impossible |
| Signed tetrahedron | coherent | coherent | coherent |
| Positive lift fiber | inhabited | degenerate | empty |
| Dagger sheet | negative counterpart | fixed fold | positive counterpart |

## Interpretation

This family gives an analytic failure movie:

1. a positive rank-one mode approaches zero;
2. its Gram margin collapses;
3. a boundary spectral-flow atom crosses;
4. the mode reappears as a Krein--Langer defect;
5. source faithfulness detects it;
6. the Douglas factorization becomes impossible;
7. signed and higher coherence remain intact.

## Disposition

The hostile mechanism can be made completely analytic without asserting an actual off-axis zeta zero. The one-pole crossing family isolates exactly which structures notice the transition and which remain blind to it.

It is an appropriate regression fixture for every proposed positive construction: any construction that remains positively filled for \(a>0\) has forgotten the divisor direction or collapsed the metric order.
