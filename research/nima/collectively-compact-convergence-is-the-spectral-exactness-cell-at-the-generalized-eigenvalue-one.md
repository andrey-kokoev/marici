# Collectively compact convergence is the spectral-exactness cell at the generalized eigenvalue one

## Fixed reduced carrier

After radical reduction, positive-angle comparison, and determinant-frame
control, transport every reduced cutoff carrier to one fixed Hilbert carrier
\(H_C\) over a compact spectral set \(C\).

Let

\[
K_X(s):H_C\longrightarrow H_C
\]

be the transported positive compact Birman--Schwinger operators.

This common-carrier step is prior to spectral convergence. Strong convergence
between operators acting on unrelated cutoff supports has no meaning.

## Exact finite gate

At finite cutoff, residual nonvanishing is

\[
1\notin\sigma(K_X(s)).
\]

Completion requires that this exclusion survive \(X\to\infty\). Pointwise
finite exclusion is insufficient.

The relevant failure is an eigenvalue sequence

\[
\lambda_X(s_X)\longrightarrow1
\]

with \(s_X\in C\), even though \(\lambda_X(s_X)\ne1\) at every finite cutoff.

## Strong-convergence hostile

On \(\ell^2\), let \(P_n\) project onto \(e_n\), and define

\[
K_n=\left(1-\frac1n\right)P_n.
\]

Then

\[
K_n\longrightarrow0
\]

strongly. Every finite operator excludes one:

\[
1\notin\sigma(K_n).
\]

But

\[
\operatorname{dist}(1,\sigma(K_n))
=
\frac1n
\longrightarrow0.
\]

Thus strong convergence neither gives a uniform gap nor prevents
near-collisions hidden in escaping directions.

The family is not collectively compact: the set
\(\{K_nx:\lVert x\rVert\le1\}\) contains the noncompact sequence
\((1-1/n)e_n\).

## Collective compactness

A family \(\{K_X(s)\}_{X,s\in C}\) is collectively compact when

\[
\bigcup_{X,s\in C}
K_X(s)\{h:\lVert h\rVert\le1\}
\]

has compact closure.

This condition forbids normalized image states from escaping through
orthogonal cutoff directions. It is the spectral counterpart of graph-carrier
stabilization.

Assume additionally that

\[
K_X(s)h\longrightarrow K(s)h
\]

uniformly in \(s\in C\) for every fixed \(h\), with the same property for
adjoints when self-adjointness is not already fixed.

Then nonzero spectral points are spectrally exact: isolated nonzero
eigenvalues of the limit are approximated with multiplicity, and finite
nonzero eigenvalue clusters cannot appear away from the limit spectrum.

Since one is nonzero, this is the relevant theorem.

## Gap transfer

Suppose:

1. \(K_X(s)\) are positive compact and collectively compact on \(C\);
2. \(K_X(s)\to K(s)\) strongly, uniformly in \(s\) on each fixed vector;
3. \(K(s)\) depends norm-continuously on \(s\);
4. \(1\notin\sigma(K(s))\) for every \(s\in C\).

Then compactness of \(C\) and spectral exactness imply an eventual gap

\[
\operatorname{dist}
\left(
1,\sigma(K_X(s))
\right)
\ge\varepsilon_C
\]

for all sufficiently large \(X\) and all \(s\in C\).

The finitely many earlier cutoffs must be audited separately. If each excludes
one, the minimum of their finite gaps and the eventual gap gives a uniform
bound over every cutoff.

This turns completion stability into a theorem rather than an assumption.

## Norm convergence route

A stronger sufficient condition is

\[
\sup_{s\in C}
\lVert K_X(s)-K(s)\rVert
\longrightarrow0.
\]

For self-adjoint operators, spectra vary upper-semicontinuously in Hausdorff
distance under norm convergence. If

\[
\inf_{s\in C}
\operatorname{dist}
\left(
1,\sigma(K(s))
\right)
=
\delta_C>0,
\]

then for large \(X\),

\[
\operatorname{dist}
\left(
1,\sigma(K_X(s))
\right)
\ge
\frac{\delta_C}{2}.
\]

Norm convergence is easier to apply but may be stronger than the source
provides.

## Norm-resolvent pencil route

One may avoid square-root normalization and work directly with reduced pencils

\[
\mathcal P_X(s,\lambda)
=
F_X(s)-\lambda B_X(s).
\]

Choose a circle

\[
|\lambda-1|=r_C
\]

that avoids the limit generalized spectrum. If the reduced pencil resolvents
converge uniformly on this circle,

\[
\mathcal P_X(s,\lambda)^{-1}
\longrightarrow
\mathcal P(s,\lambda)^{-1},
\]

then the Riesz projections around one converge.

If the limit projection is zero, the finite projections are eventually zero.
This directly excludes generalized eigenvalues near one without choosing
independent Green square roots.

For reciprocal comparison, this pencil route is canonical because congruence
transports the entire resolvent family.

## Parameter-uniform requirement

Pointwise collective compactness in \(s\) is insufficient. A collision can move
with the spectral parameter.

The correct compact-local package requires:

- collective compactness of the union over \(s\in C\);
- equicontinuity or holomorphic normal-family control in \(s\);
- uniform strong or norm convergence on \(C\);
- reciprocal compatibility of the parameter transport.

A sequence \(s_X\) approaching a moving near-collision is the finite hostile
for any merely pointwise statement.

## Determinant convergence

Spectral exactness excludes pollution at one but does not by itself define the
relative determinant.

For an order-three determinant one additionally needs convergence in the
appropriate Schatten ideal, for example

\[
\sup_{s\in C}
\lVert K_X(s)-K(s)\rVert_3
\longrightarrow0,
\]

after primitive and square anomaly-line normalization.

Then

\[
\det_3(I-K_X(s))
\longrightarrow
\det_3(I-K(s))
\]

uniformly on \(C\).

The spectral and determinant cells are related but distinct:

- collectively compact or norm-resolvent convergence controls eigenvalue
  pollution;
- Schatten convergence controls determinant-line continuity.

Neither should be inferred from the other without a source theorem.

## Reciprocal transport

Let \(J_X(s)\) implement the source congruence between reciprocal reduced
pencils. The fixed-carrier embeddings must satisfy the cutoff--reciprocal
commuting cube already required by determinant-frame control.

Then spectral exactness in one sector transfers to the other. If the embeddings
or polar frames differ by uncontrolled cutoff maps, separate convergence
proofs are required.

## Hostile tests

1. \(K_n=(1-1/n)P_n\) converges strongly to zero while the gap at one
   collapses.
2. Pointwise compactness without collective compactness permits escaping
   eigenvectors.
3. Pointwise parameter convergence permits moving near-collisions.
4. Stable spectra without Schatten convergence need not yield determinant-line
   convergence.
5. Schatten convergence on unstable carrier frames does not repair rotating
   supports.
6. Scalar determinant convergence can hide spectral pollution through
   cancellation.
7. Reciprocal scalar equality does not transport resolvents.

## Ordered completion gate

The complete order is:

1. source-authorized radical reduction;
2. stable reduced carrier;
3. positive Friedrichs angle;
4. determinant-class natural comparison and orientation;
5. collectively compact or norm-resolvent spectral exactness near one;
6. compact-local gap from one;
7. Schatten determinant convergence;
8. invertible line identification with \(\Xi\).

This sequence keeps carrier, spectral, and determinant claims typed
separately.

## Consequence for categorical RH

The spectral-pollution hazard now has a precise sufficient repair. Once the
reduced carrier and determinant frame are stable, collectively compact
convergence prevents nonzero eigenvalues from escaping or appearing
spuriously. A limit exclusion of one then promotes to a uniform finite-cutoff
gap on compact open-sector sets.

The remaining mathematical core is still the limit exclusion

\[
1\notin\sigma(K(s)).
\]

Spectral exactness ensures that finite approximations neither fake nor destroy
that statement.

## Verdict

Strong convergence is too weak for the RH pencil. Collectively compact
convergence, or norm-resolvent convergence of the reduced pencil near one, is
the correct spectral-exactness cell. It separates the genuine limit
eigenvalue-one problem from cutoff pollution and escaping-state artifacts.
