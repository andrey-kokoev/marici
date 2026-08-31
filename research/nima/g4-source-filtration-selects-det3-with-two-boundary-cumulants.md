# G4 source filtration selects det3 with two boundary cumulants

## Correction of the determinant target

The three-grade Euler filtration does not primarily select an ordinary
Fredholm determinant.  Primitive and square currents are separate boundary
data, while the connected grades begin at order three.  The matching bulk
object is therefore the order-three regularized determinant.

For a finite operator \(K\),

\[
\det_3(I+K)
=
\det(I+K)
\exp\left(-\operatorname{Tr}K+
\frac12\operatorname{Tr}K^2\right).
\]

Equivalently,

\[
\det(I+K)
=
\exp\left(\operatorname{Tr}K-
\frac12\operatorname{Tr}K^2\right)
\det_3(I+K).
\]

Thus the linear and quadratic cumulants removed from \(\det_3\) are exactly the
two low-grade boundary slots.

## Typed finite factorization

Let \(u^{(1)}(s)\) and \(u^{(2)}(s)\) be the source primitive and square
boundary factors.  The finite G4 compiler must prove

\[
\log u^{(1)}(s)=\operatorname{Tr}K(s),
\]

\[
\log u^{(2)}(s)=-\frac12\operatorname{Tr}K(s)^2
\]

with the source branch and normalization fixed.  Then

\[
u^{(1)}(s)u^{(2)}(s)\det_3(I+K(s))
=
\det(I+K(s))
\]

at every finite cutoff.

The signs change in the standard way if the pencil is written as \(I-K\)
rather than \(I+K\).  That convention must be frozen before comparing source
currents.

## Completed Xi target

The source-typed G4 identity is consequently

\[
u^{(1)}(s)u^{(2)}(s)
\det_3(I+K(s))
=E(s)\Xi(s),
\]

where \(E(s)\) is holomorphic and nowhere zero.  This is stronger and more
accurate than asking an unadorned Fredholm determinant to equal \(\Xi\).

It preserves:

- primitive current as the first cumulant;
- square current as the second cumulant;
- connected prime-power tail in the order-three determinant;
- seam and archimedean factors in the nonvanishing comparison unit only after
  their source normalization is derived.

## Completion requirements

The infinite identity requires:

1. \(K(s)\in\mathcal S_3\) on a fixed reduced carrier;
2. local \(\mathcal S_3\)-norm convergence uniformly on compact parameter
   sets;
3. holomorphic dependence in \(\mathcal S_3\);
4. convergent, source-normalized primitive and square factors;
5. an inverse gap excluding untracked crossings during completion;
6. convergence of \(E_X(s)\) to a nowhere-zero \(E(s)\);
7. multiplicity preservation.

The adelic-vacuum trace-class sandwich is a different possible compiler.  It
must first prove survival of the mixed incidence through the integral-sector
projector.  It cannot silently replace the three-grade regularized
architecture.

## Rigid two-sheet no-go remains

The intrinsic two-by-two reciprocal sewing determinant contains the product
\(m_+m_-\) and is not proportional to the even Xi coefficient.  Regularization
does not remove this finite algebraic mismatch.  A valid \(K(s)\) must come
from a larger typed boundary complex, bordered determinant, or independently
source-derived arithmetic constitutive relation.

## Exact remaining G4 calculations

The next finite-cutoff audit is now:

1. construct the source operator \(K_X(s)\);
2. compute \(\operatorname{Tr}K_X(s)\) and
   \(\operatorname{Tr}K_X(s)^2\);
3. compare them with the primitive and square boundary currents;
4. compute \(\det_3(I+K_X(s))\);
5. prove that the product equals the finite completed section up to a declared
   nonzero unit;
6. only then pass to the completed \(\mathcal S_3\) limit.

No current packet constructs all six arrows.  G4 remains open, and no RH
conclusion is authorized.
