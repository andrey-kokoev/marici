# Pentagon coherence does not imply source-preserving strictification

## Question

If a weak transport system passes the pentagon, can its associator always be
removed by changing comparison frames?

## Claim boundary

Not while preserving a fixed skeletal object set and composition law. The
associator may define a nontrivial third cohomology class. This does not deny
general categorical strictification by equivalence to a larger strict
category; it obstructs killing the associator by source-local scalar
rephasing on the declared carrier.

## Associator cocycle

Let \(G\) label composable source sectors and let an associator phase be

\[
\omega:G^3\longrightarrow U(1).
\]

The pentagon is the normalized three-cocycle identity

\[
\omega(b,c,d)\omega(a,bc,d)\omega(a,b,c)
=
\omega(ab,c,d)\omega(a,b,cd).
\]

Passing this identity proves coherence of the weak composition. It does not
prove that \(\omega\) is trivial.

## Source-local frame changes

A scalar redefinition of binary comparison maps is a normalized two-cochain
\(\beta:G^2\to U(1)\). It changes the associator by the coboundary

\[
(\delta\beta)(a,b,c)
=
\frac{\beta(b,c)\beta(a,bc)}
{\beta(ab,c)\beta(a,b)}.
\]

The associator can be removed within the same skeletal source presentation
exactly when \(\omega=\delta\beta\). Its obstruction is the class
\([\omega]\in H^3(G,U(1))\).

## Smallest exact witness

For \(G=C_2\), written additively with elements \(0,1\), define

\[
\omega(a,b,c)=(-1)^{abc}.
\]

It satisfies the pentagon for all sixteen quadruples. But every normalized
\(\{\pm1\}\)-valued two-cochain has

\[
(\delta\beta)(1,1,1)=1,
\]

whereas \(\omega(1,1,1)=-1\). No source-local sign rephasing on the fixed
\(C_2\) carrier removes it.

## Strictification qualification

Mac Lane strictification allows replacement by a monoidally equivalent strict
category, generally changing the presentation and enlarging the objects to
formal words. That theorem does not authorize erasing a source-labelled
associator while claiming to retain the same physical or operational carrier.

Marici therefore needs two distinct questions:

1. Is the weak category abstractly equivalent to a strict one?
2. Does a strictification descend through the declared source identities,
   ports, supports, modalities, and readouts?

Only the second question permits treating the original source system as
strict.

## Projection trap

The absolute-value projection sends both \(+1\) and \(-1\) to \(1\). It makes
the nontrivial \(C_2\) associator appear strictly trivial while deleting its
cohomology class. A scalar output that passes every projected pentagon is
therefore insufficient unless it is faithful on associator phases.

## Cross-sector consequences

- Topological phases and anyon associators may be coherent yet carry
  nontrivial anomaly data that cannot be removed within the labelled sector
  system.
- Software constructor trees cannot be flattened merely because an abstract
  strict replacement exists; authority roots and support contracts must
  survive the equivalence.
- Flavor matching phases and optical calibration phases require a
  source-preserving coboundary witness before they may be normalized away.
- Boundary-line anomalies that satisfy coherence may still obstruct a common
  determinant frame through a nontrivial third class.

## DPC

For a coherent weak associator:

1. verify the pentagon;
2. freeze the source object set and composition law;
3. enumerate or characterize admissible two-cochain frame changes;
4. solve \(\omega=\delta\beta\);
5. retain \([\omega]\) when no solution exists;
6. reject strictification through a projection that kills the residual;
7. distinguish source-preserving strictification from abstract categorical
   equivalence.

## Disposition

Pentagon coherence is not the end of the audit. The next invariant is the
associator cohomology class. Vanishing permits source-local rephasing;
nonvanishing is durable weak-composition data on the fixed carrier.

## Verification

The checker check_c2_associator_cohomology.py verifies the cocycle identity on
all \(C_2^4\), exhausts all normalized sign-valued two-cochains, proves that
none has the required coboundary, and confirms that absolute-value projection
erases the obstruction.
