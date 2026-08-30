# Theta source-relative integrality

Author: `marici.Grothendieck`

## 0. Question

The operator suggested that projected meaning becomes undefined through a
loss of integrality after the spectral half-planes acquire distinct
orientations.  The divisor-current formulation makes that intuition
testable.  This packet asks which notion of integrality could actually force
critical-line localization.

## 1. Ordinary divisor integrality is insufficient

Let `X` be any real even entire function and choose `a` with both nonzero real
and imaginary parts.  Define

\[
P_a(z)
=\frac{(z^2-a^2)(z^2-\bar a^2)}{|a|^4}.
\]

Then

\[
P_a(-z)=P_a(z),
\qquad
P_a(\bar z)=\overline{P_a(z)},
\qquad
P_a(0)=1.
\]

Moreover, on the real axis,

\[
P_a(x)=\frac{|x^2-a^2|^2}{|a|^4}>0.
\]

Thus

\[
\widetilde X(z)=P_a(z)X(z)
\]

preserves evenness, reality, normalization at the origin, entire order, and
the sign of the boundary readout, while inserting the off-axis quartet

\[
\{a,-a,\bar a,-\bar a\}.
\]

Every new zero still has an integer multiplicity.  Therefore the following
data do not imply RH, separately or jointly:

1. functional-equation symmetry;
2. real structure;
3. integral winding and divisor multiplicity;
4. positivity of the multiplier on the critical line;
5. the usual quartet symmetry of off-line zeros.

The operator's integrality cannot mean bare integrality of the final divisor.
Off-line defects are perfectly integral.

## 2. What the hostile multiplier destroys

The completed readout is not an arbitrary real even entire function.  It is
the Fourier transform of one fixed positive theta source:

\[
X(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du.
\]

Multiplication by `P_a(z)` corresponds on the source side to applying a
fourth-order constant-coefficient differential operator to `Phi`.  Such an
operation need not preserve positivity, theta-label coefficients, the heat
equation, or reciprocal modular sewing.

Hence the surviving candidate is source-relative integrality:

\[
\boxed{
\text{the divisor class must be induced by the integer theta-label Carrier,
not merely have integer coefficients after projection.}
}
\]

This is analogous to the programme's earlier faithfulness rule: a finite
fiber is not a singleton fiber.  Many integral divisors project to the same
coarse symmetry data; only the source-labelled lift can distinguish which
one is admissible.

## 3. Integrality as protection under deformation

There is one mechanism by which integrality can genuinely prevent defect
creation.  For a bounded chamber domain `Omega` whose boundary contains no
zero, define

\[
N_\Omega(X)
=\frac1{2\pi i}\oint_{\partial\Omega}\frac{X'}X\,dz.
\]

This is a nonnegative integer counting the interior divisor.  Along a
continuous source-derived family `X_tau`, the integer cannot change unless a
zero crosses the domain boundary.

This yields a theorem architecture matching the operator's ordering:

\[
\boxed{
\begin{array}{c}
\text{distinguish the two chambers;}\\
\text{start from a chamber-trivial primitive source;}\\
\text{assemble the completed theta source through admissible integral
transport;}\\
\text{prove defects may cross only through the fixed seam, never through
the chamber boundary at infinity.}
\end{array}
}
\]

Then `N_Omega` begins at zero and remains zero.  The invariant content is not
that winding numbers are integers; it is that an integer index is locally
constant under the particular source-generated transport.

## 4. The required admissible homotopy

A useful homotopy cannot be chosen after looking at the zeros.  It must be
derived from the labelled theta construction.  Candidate parameters include
ordered activation of reciprocal label pairs or a modular heat-flow
parameter with the seam completion retained at every stage.

For an exhaustion `Omega_R` of the upper half-plane, the required assertions
are:

\[
N_{\Omega_R}(X_0)=0,
\]

\[
X_\tau(z)\ne0
\qquad
(z\in\partial\Omega_R\setminus\mathbb R),
\]

and every real-boundary crossing is typed through the reciprocal fixed
sector.  A uniform primitive-tail estimate must prevent entry from infinity.
Homotopy invariance then gives

\[
N_{\Omega_R}(X_1)=0
\]

for every `R`, hence no upper-chamber zeros.

This route asks for boundary nonvanishing along a one-parameter arithmetic
transport, rather than a two-dimensional Hermite--Biehler inequality for the
final function.  It is potentially much weaker.

## 5. Loss of integral trivialization

The operator's phrase “loss of integrality” can now be made precise without
claiming that a zero has fractional multiplicity.  Each chamber begins with
an integral trivialization class.  An interior defect would change its
integer index.  If the source transport permits no boundary crossing, that
change is forbidden.

Thus the proposed explanation is

\[
\boxed{
\text{zeros retain integral charge, but an off-seam zero would violate
source-relative conservation of the chamber index.}
}
\]

At the fixed seam, the two chamber orientations meet and boundary phase
trivializations may fail to glue.  Integral defect charge may therefore be
supported there without appearing inside either chamber.

## 6. Sharp falsifier

### Heat-flow collision with the Newman frontier

The most obvious continuous source transport is

\[
X_t(z)=\int_{\mathbb R}e^{tu^2}\Phi(u)e^{izu}\,du,
\qquad
\partial_tX_t=-\partial_z^2X_t.
\]

This is the de Bruijn--Newman deformation, up to normalization conventions.
Its zero-crossing threshold is already a classical reformulation of the RH
frontier.  Proving that the heat path reaches `t=0` without creating an
off-real pair does not simplify the missing theorem; it restates it in
dynamical language.

Moreover, the factor `exp(tu^2)` does not transparently preserve the exact
prime-label modular sewing used elsewhere in this programme.  Therefore heat
flow is a useful comparison and falsifier, but not yet the desired
source-relative integral transport.

The potentially new object would have to activate canonical reciprocal
label packets while retaining the completed seam at every stage.  Even then,
boundary nonvanishing must be proved rather than inferred from integer index.

### Exact label-homotopy obstruction

That candidate is ruled out if “retaining completion” includes the standard
recursion at every prime.  For a weighted packet

\[
\Phi_w=\sum_{n\ge1}w_n\phi_n,
\]

the exact `p`-scale recursion holds if and only if

\[
w_{pm}=w_m
\qquad(m\ge1).
\]

Imposing this for every prime forces

\[
w_n=w_1
\qquad(n\ge1).
\]

Thus every all-prime-compatible coefficient homotopy is merely

\[
\Phi_\tau=c(\tau)\Phi.
\]

Its transform rescales by the same nonzero scalar and its projective Carrier,
zero divisor, and chamber index do not move.  There is no simpler endpoint
from which to transport zero-freeness.

The same obstruction is visible before coefficient rigidity: reciprocal
reflection is implemented by the full Poisson-resummed lattice, and no
nonempty finite raw-label packet is modularly closed.  Ordered finite-label
activation therefore leaves the physical source category.

Hence the proposed homotopy route bifurcates sharply:

\[
\boxed{
\begin{array}{ll}
\text{preserve all arithmetic sewing} &\Rightarrow
\text{projectively trivial homotopy},\\
\text{activate proper label subsets} &\Rightarrow
\text{leave the modularly completed category}.
\end{array}
}
\]

This closes the naive reciprocal-label transport.  Source-relative
integrality, if useful, must be extracted statically from the fully completed
source rather than inherited from a simpler source through admissible label
activation.

### Minimal falsifier

The homotopy programme fails if the smallest source-admissible interpolation
develops a zero on a non-seam part of the chamber boundary, or if its
primitive starting member already has an interior zero.  Neither event may
be repaired by changing the interpolation after inspecting its zeros.

The hostile polynomial `P_a` is the standing scope test: any proposed
“integrality theorem” that also admits multiplication by `P_a` has forgotten
the theta source and cannot localize the divisor.

## 7. Scope

The hostile quartet construction, homotopy invariance of the argument index,
finite-packet modular obstruction, and all-prime coefficient rigidity are
exact.  Together the last two falsify the naive reciprocal-label homotopy.
Source-relative integrality must now be sought as a static invariant of the
completed source.  It remains a theorem target, and RH is not proved.
