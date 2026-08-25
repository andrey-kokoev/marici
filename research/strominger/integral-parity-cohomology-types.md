# Typed objects for the integral parity-cohomology programme

This packet freezes the categories and maps used by the programme.  It is an
engine-side specification.  No physical source constructor, target
truncation, or physical readout pairing is supplied.

## 1. Coefficient objects

Treat `z` and `bar(z)` as independent formal variables and put

\[
K=\mathbb Q(z,\bar z),\qquad u=z\bar z.
\]

Fix a grade `g>=2`, a finite pole-depth constructor

\[
A\subset\mathbb Z_{\ge0},
\]

and a finite Laurent window `I=[m_min,m_max] cap Z`.  The integral source
lattice and its rationalization are

\[
S_{\mathbb Z}(A,I)
=\bigoplus_{(a,m)\in A\times I}\mathbb Ze_{a,m},
\qquad
S_{\mathbb Q}=S_{\mathbb Z}\otimes\mathbb Q,
\]

with monomial realization

\[
e_{a,m}\longmapsto z^{-a}\bar z^m.
\]

The proved kernel theorem uses the even constructor
`A subset 2*Z_{>=0}`.  Other sets are **constructor extensions** and require a
separate theorem.  Merely writing fractional or odd exponents in a scalar
formula does not authorize such an extension.

## 2. Full integral target

After multiplication by the common denominator `(1+u)^(g+1)`, every electric
or magnetic readout has a finite Laurent numerator with integral
coefficients.  Let

\[
Y_{g,\mathbb Z}=\bigoplus_{(r,t)\in\mathbb Z^2}\mathbb Ze_{r,t}^{target}
\]

be the free full-target lattice; each individual column has finite support.
The sparse numerator maps are

\[
E_{g,\mathbb Z},M_{g,\mathbb Z}:S_{\mathbb Z}(A,I)
\longrightarrow Y_{g,\mathbb Z}.
\]

All kernel statements in this programme retain every target row.  A target
cutoff composes these maps with another projection and defines a different
operator.

## 3. Folded one-form and sheet packet

The covariant fold produces a rational one-form

\[
F_g:S_{\mathbb Q}\longrightarrow\Omega_K^1,
\qquad
D\longmapsto\omega_D=f_D\,dz+\bar f_D\,d\bar z.
\]

Its mixed-derivative sheet packet is

\[
J_g:S_{\mathbb Q}\longrightarrow K\oplus K,
\qquad
D\longmapsto(A_D,B_D)
=\left(\partial_{\bar z}f_D,\partial_z\bar f_D\right).
\]

Reflection exchanges the two entries.  The character ports are

\[
E_g=A_D+B_D,
\qquad
M_g=A_D-B_D.
\]

The half-Hadamard inverse reconstructs `(A_D,B_D)` from `(E_g,M_g)`.  The
one-sheet theorem proves `J_g` injective on the admitted Laurent source.

The commuting hinge between parity and cohomology is

\[
d\omega_D
=\left(\partial_z\bar f_D-\partial_{\bar z}f_D\right)
dz\wedge d\bar z
=-M_g(D)\,dz\wedge d\bar z.
\]

Thus

\[
K_g^M=\ker M_g
\]

is exactly the source subspace whose folded forms are closed.  The electric
kernel is a complementary parity-blind sector, not a de Rham-closed sector.

## 4. Exact and residue objects

Rational exactness is defined only after restricting to `K_g^M`:

\[
K_g^{rat}
=\{D\in K_g^M:F_g(D)=d\Phi\text{ for some }\Phi\in K\}.
\]

The ordinary rational quotient is

\[
H_g^{rat}=K_g^M/K_g^{rat}.
\]

For visible positive-depth towers, Hermite reduction gives

\[
[F_g(D_{g,a})]
=r_{g,a}[\eta],
\qquad
\eta=d\log\frac{u}{1+u},
\]

\[
r_{g,a}=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

The integral tower lattice maps to the primitive ambient divisor lattice by
the global augmentation

\[
\rho_{g,A}:\bigoplus_{a\in A_+}\mathbb ZD_{g,a}
\longrightarrow\mathbb Z\eta,
\qquad D_{g,a}\mapsto r_{g,a}\eta.
\]

The integral exact lattice is the kernel of this augmentation together with
the visible depth-zero and exceptional exact classes.  Its rationalization is
`K_g^rat`.

A depth-labelled residue object

\[
\bigoplus_{a\in A_+}\mathbb Z\eta_a
\]

is a valid associated grade, but it is not ordinary rational cohomology.  Its
codiagonal to `Z*eta` authorizes cross-depth cancellation.

## 5. Morphisms and naturality boundary

At fixed grade, an inclusion of constructors and Laurent windows

\[
(A,I)\hookrightarrow(A',I')
\]

induces a column inclusion

\[
j:S(A,I)\hookrightarrow S(A',I').
\]

Because the target is full and unchanged,

\[
E_{g,A',I'}j=E_{g,A,I},
\qquad
M_{g,A',I'}j=M_{g,A,I}.
\]

The fold, sheet packet, parity transform, closedness map, and residue
augmentation commute with this inclusion wherever their domains are defined.
Grade change is not such a morphism: it changes every transport factor.

An authorized constructor extension must therefore provide:

1. the new exponent set;
2. its inclusion or covering map from the old set;
3. the transported differential and reflection action;
4. the target representation and allowed adapters;
5. the comparison map on residue lattices.

Without these data, scalar continuation is algebraic description only.

## 6. Explicit exclusions

The following are not asserted:

- that the engine source is physically constructible;
- that a physical target equals the full Laurent target;
- that target truncation preserves the theorem;
- that odd, fractional, or cover exponents are authorized states;
- that a kernel circuit is a homology class without a preceding repair map;
- that a Hall or Plucker certificate selects a physical coefficient.

Hall, transfer, and Plucker data certify transport rank and presentation
charts.  They neither collapse a lens fiber nor choose a physical readout
point.
