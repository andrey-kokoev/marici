# Reciprocal covariance glues the two det2 relative-return charts

## Reciprocal chart data

Let \(\mathscr R_E\) and \(\mathscr R_I\) be the unitary reciprocal maps on the
coefficient and boundary-history carriers.  The retained construction gives
right and reflected incidences related by

\[
B_-(s)
=\mathscr R_I B_+(1-s)\mathscr R_E^{-1}.
\]

The boundary propagators satisfy the corresponding covariance

\[
G_-(s)
=\mathscr R_I G_+(1-s)\mathscr R_I^{-1},
\]

and the prime-loop factors obey

\[
L_-(s)
=\mathscr R_E L_+(1-s)\mathscr R_E^{-1}.
\]

These are transport identities under the reciprocal parameter involution, not
a temporal interpretation.

## Relative return covariance

Define

\[
R_\pm(s)=B_\pm(s)^\dagger G_\pm(s)B_\pm(s)
\]

and

\[
K_\pm(s)=(I-L_\pm(s))^{-1}R_\pm(s).
\]

Because the reciprocal maps are unitary and the adjoint is taken in the
source seam metric,

\[
B_-(s)^\dagger
=\mathscr R_E B_+(1-s)^\dagger\mathscr R_I^{-1}.
\]

Substitution gives

\[
R_-(s)
=\mathscr R_E R_+(1-s)\mathscr R_E^{-1}
\]

and hence

\[
K_-(s)
=\mathscr R_E K_+(1-s)\mathscr R_E^{-1}.
\]

Thus the two relative returns are similar after the declared reciprocal chart
identification.

## Regularized determinant gluing

The order-two regularized determinant is invariant under bounded similarity in
its \(\mathcal S_2\) domain. Therefore

\[
\det_2(I-K_-(s))
=
\det_2(I-K_+(1-s)).
\]

On the overlap

\[
\frac13<\operatorname{Re}s<\frac23,
\]

this is an exact reciprocal transition law.  After pulling the reflected chart
back along \(s\mapsto1-s\), the transition function is the constant unit one.
It is holomorphic and nowhere zero.

## First-trace anomaly

On the centered line, where \(K_\pm\) are trace class,

\[
\det_2(I-K_\pm)
=
\det(I-K_\pm)e^{\operatorname{Tr}K_\pm}.
\]

Similarity also gives

\[
\operatorname{Tr}K_-(s)
=
\operatorname{Tr}K_+(1-s).
\]

Hence the first-trace anomaly is reciprocal-covariant and introduces no
additional transition defect between the two relative charts.  It still must
be assigned correctly against the primitive Euler boundary current when the
relative and bare determinant compilers are multiplied.

## Scope qualification

This theorem glues only the boundary-mediated relative \(\det_2\) factor.  It
does not glue:

- the bare Euler \(\det_3\) section and its first two cumulants;
- the archimedean gamma line;
- projective-infinity boundary data;
- the closed-loop kernel state;
- the comparison with \(\Xi\).

If any of the displayed covariance identities fails for the actual completed
propagator, similarity and determinant gluing fail with it.  The identities
must be checked on the common reduced domain, not inferred from scalar
functional equations.

## G4 consequence

The relative determinant ideal and reciprocal transition are no longer the
principal G4 obstruction.  The remaining determinant-line problem is to
combine:

1. the bare Euler \(\det_3\) section;
2. its primitive and square cumulant lines;
3. the reciprocal relative \(\det_2\) section;
4. the archimedean completion;

and prove that the result equals \(E(s)\Xi(s)\) with \(E\) nowhere zero and
with matching kernel multiplicities.

No RH conclusion is authorized.
