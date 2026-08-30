# Equivariant phase reference needs a primitive two-real-dimensional port

## Question

What source action must a reference port carry to distinguish a residual
\(U(1)\) phase orbit while commuting with transport?

## Claim boundary

A continuous real equivariant reference cannot be both one-dimensional and
phase-sensitive. The smallest faithful linear carrier is the two-dimensional
rotation representation of primitive weight \(1\) or \(-1\). This classifies
the abstract carrier; it does not construct a physical port in any sector.

## One real dimension is necessarily blind

Any continuous real one-dimensional representation is a continuous
homomorphism

\[
\rho:U(1)\longrightarrow GL(1,\mathbb R)=\mathbb R^\times.
\]

The image of the connected compact group \(U(1)\) is connected and compact.
The only compact connected subgroup of \(\mathbb R^\times\) is the identity.
Therefore \(\rho\) is trivial. A real scalar transforming linearly and
equivariantly under phase cannot carry phase information.

This is stronger than the topological embedding obstruction. It says one real
coordinate fails before injectivity is tested: there is no nontrivial
continuous one-dimensional real action for it to carry.

## Two-dimensional weight representations

On \(\mathbb R^2\), \(U(1)\) acts by

\[
\rho_k(e^{i\theta})=
\begin{pmatrix}
\cos(k\theta)&-\sin(k\theta)\\
\sin(k\theta)&\cos(k\theta)
\end{pmatrix},
\qquad k\in\mathbb Z.
\]

The orbit of a nonzero vector records phase modulo the kernel
\(\mu_{|k|}\). It is faithful exactly when \(|k|=1\). Weight zero is blind;
higher weights retain a finite ambiguity.

Thus two quadratures are not sufficient merely because there are two of them.
Their source transport must carry a primitive character.

## Categorical formulation

Let \(F=U(1)\) be the unresolved fiber and let \(W\) be a real representation
object. An admissible reference is an equivariant map

\[
r:F\longrightarrow W.
\]

Faithfulness requires the stabilizer of \(r(1)\) to be trivial. The minimum
real representation dimension is two, and the admissible irreducible weights
at that dimension are \(k=\pm1\).

The source therefore has to provide both:

1. a two-quadrature carrier;
2. a primitive equivariant incidence into that carrier.

An apparatus with two channels but weight \(2\) still identifies opposite
phases. Port dimension and coefficient character are independent gates.

## Cross-sector interpretation

- In optics, a phase reference must retain an ordered in-phase/quadrature pair
  with primitive phase transport. Intensity and second-harmonic readouts are
  insufficient.
- In flavor, interference observables must carry the primitive relative phase
  rather than only squared amplitudes or even harmonics.
- In reciprocal boundary normalization, a proposed complex augmentation must
  intertwine the primitive residual \(U(1)\) action. A higher-power determinant
  character leaves a finite normalization ambiguity.

## DPC

For a proposed phase-sensitive reference:

1. derive its real representation \(W\) from source operations;
2. compute the \(U(1)\) weights;
3. reject a purely trivial representation;
4. reject weights with \(|k|>1\) when full phase faithfulness is claimed;
5. verify equivariance of the incidence map;
6. verify constructibility of both quadratures and their common frame.

## Disposition

The minimum faithful equivariant phase reference is a primitive complex line,
equivalently a two-real-dimensional weight-\(\pm1\) carrier. Two real outputs
without primitive transport do not solve the reference problem.

## Verification

The checker check_equivariant_phase_reference.py verifies exact rational
rotation composition, trivial scalar action, the weight-two antipodal
collision, and primitive weight-one separation on an exact finite orbit.
