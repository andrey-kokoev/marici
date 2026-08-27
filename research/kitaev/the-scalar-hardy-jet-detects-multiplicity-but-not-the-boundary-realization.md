# The scalar Hardy jet detects multiplicity but not the boundary realization

## Question

Does the complete Hardy–Fock jet of the scalar completed section control the
operator-valued boundary Schur complement strongly enough to establish stable
invertibility?

## What the scalar jet does prove

For a holomorphic scalar function \(F\), its factorial jet at \(z_0\),

\[
J_rF(z_0)
=
\left(
\frac{r^k}{k!}F^{(k)}(z_0)
\right)_{k\ge0},
\]

is faithful to the analytic germ. It detects every finite zero multiplicity,
and it vanishes only when the germ is identically zero.

This closes a scalar observability question: scalar silence at grade zero
does not erase all transverse analytic information.

It does not reconstruct the operator realization producing \(F\).

## Determinant forgets the boundary frame

Let \(S(z)\) be a finite-dimensional analytic Schur complement and

\[
F(z)=\det S(z).
\]

The determinant records the product of eigenvalue directions. It forgets:

- right and left kernel vectors;
- nonnormal shear;
- singular-value margins;
- the decomposition into direct and returned boundary action;
- the typed primitive, square, seam, and archimedean ports.

Taking every derivative of \(F\) does not restore information already erased
by the determinant map.

## Exact same-germ hostile family

For any complex number \(M\), set

\[
S_M(z)=
\begin{pmatrix}
z&M\\
0&1
\end{pmatrix}.
\]

Every member has exactly the same determinant:

\[
\det S_M(z)=z.
\]

Therefore every scalar derivative at every parameter is independent of
\(M\). The complete scalar Hardy–Fock jet is identical for the whole family.

But away from zero,

\[
S_M(z)^{-1}
=
\begin{pmatrix}
z^{-1}&-Mz^{-1}\\
0&1
\end{pmatrix},
\]

so the inverse norm can grow arbitrarily with \(|M|\). At the zero, the
right kernel is fixed while the left-kernel frame and nonnormal geometry vary
with \(M\).

Thus complete scalar-germ equivalence does not imply stable realization
equivalence.

## Same determinant, different kernel attachment

Let \(U(z)\) and \(V(z)\) be analytic invertible matrices with determinant
one. Then

\[
\widetilde S(z)=U(z)S(z)V(z)
\]

has the same scalar determinant as \(S(z)\), while its right and left kernel
bundles are transported by \(V(z)^{-1}\) and \(U(z)^{-*}\).

Unless those transformations are authorized boundary equivalences, the two
families implement different constructors despite having identical complete
scalar jets.

This is the analytic-jet version of constructor equivalence versus scalar
equivalence.

## Required operator-valued lift

The Hardy–Fock construction must be applied before determinant compression.
For an analytic operator family \(S(z)\), define

\[
\mathcal J_rS(z_0)
=
\left(
\frac{r^k}{k!}\partial_z^kS(z_0)
\right)_{k\ge0}.
\]

At finite boundary dimension this is an operator-valued Hardy packet. In an
infinite-dimensional boundary space it requires a declared operator norm,
graph topology, or ideal norm.

The lift should retain at least one of the following equivalent forms of
realization data:

1. the analytic Schur-complement family itself in operator norm;
2. its graph or gap-continuous family;
3. a Rosenbrock pencil with typed input and output ports;
4. the loop operator and a quantitative resolvent margin.

Only after this object is controlled may one take its regularized
determinant as a scalar diagnostic.

## Operator Hardy identity

For Hilbert–Schmidt-valued analytic families, Parseval extends directly:

\[
\sum_{k\ge0}
\frac{r^{2k}}{(k!)^2}
\|\partial_z^kS(z_0)\|_{\mathrm{HS}}^2
=
\frac1{2\pi}
\int_0^{2\pi}
\|S(z_0+re^{i\theta})\|_{\mathrm{HS}}^2\,d\theta.
\]

This is useful for compact perturbation channels. It does not control
invertibility by itself, because a small or bounded Hilbert–Schmidt norm is
not a lower singular-value estimate.

For invertibility, the appropriate analytic object is often the inverse or
resolvent on a zero-free parameter circle. If \(S(z)\) is invertible there,
then a bound on

\[
\sup_\theta
\|S(z_0+re^{i\theta})^{-1}\|
\]

controls interior inverse behavior through operator-valued analytic
principles. Establishing the zero-free boundary circle and its inverse bound
is already a source-bearing theorem, not a consequence of the determinant
jet.

## Completion hierarchy

The corrected hierarchy is:

1. scalar value detects grade-zero transmission;
2. scalar Hardy jet detects analytic multiplicity;
3. operator Hardy jet retains the local realization germ;
4. graph or resolvent bounds control stable invertibility;
5. typed colligation data establish source authority.

Each level forgets information when projected downward. No amount of
differentiation after a lower projection reverses that loss.

## Consequence for the boundary programme

The scalar Clark jet remains valuable: it proves that simple scalar silence
is visible in the source endpoint packet and supplies a coherent analytic
jet topology.

But the RH-bearing gate remains operator-valued:

\[
S_s=D_s-C_s(I-K_s)^{-1}B_s.
\]

The next lift must put \(B_s,C_s,D_s\), or \(S_s\) itself, into the
Hardy–Fock radius rigging before taking the determinant. The desired
certificate is a uniform lower singular-value or resolvent bound on that
operator packet.

## Falsifiers

- Two analytic Schur families with identical determinant germs but
  unauthorized different kernel frames.
- Uniform scalar Hardy norms with diverging operator inverse norms.
- An operator-jet norm that controls only upper size and is reported as an
  invertibility margin.
- Recovery of boundary blocks by factorizing the desired scalar determinant.
- A regularized determinant identity with no graph-continuous operator
  family underneath it.

## Disposition

The Hardy–Fock jet solves the multiplicity-adaptivity problem at the scalar
level. It does not solve the boundary realization or completion-stability
problem. The correct fifth-level constructor is an operator-valued
Hardy–Fock Schur or Rosenbrock correspondence, followed by a separate
resolvent certificate.

## Claim boundary

This packet proves a finite analytic no-go and states the required operator
lift. It does not construct the theta boundary Schur family or establish an
operator-valued Hardy or resolvent estimate.
