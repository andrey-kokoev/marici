# Contextual cascade quotient: WP677

## Admitted domain and four native levels

The WP675 analyzer is admitted only on the real-positive, narrow-width,
open-threshold slice. Its two kernels are

\[
W=A(u+v)+C\sqrt{uv}\cos\phi,
\qquad
N=L(u-v).
\]

The cascade must be typed at four distinct levels.

1. The unsigned endpoint distribution identifies neither chirality ordering
   nor the exchange (u\leftrightarrow v).
2. The signed analyzer has rank two on the real-positive slice with
   \(\phi=0\) and \(L>0\).
3. On the complex domain, two real ports cannot identify three real coupling
   coordinates. Complex conjugation \(\phi\leftrightarrow-\phi\) is an exact
   surviving stabilizer.
4. Equality of composite distributions does not identify the ordered decay
   factorization modulo any currently authorized process equations.

The Kallen threshold (L=0) is a boundary of the analyzer domain.

## Exact hostile fibers

At (A=3,C=4,L=1), the points ((u,v)=(4,1)) and ((1,4)) have the same
unsigned rate. Their signed moments are opposite, so the ideal analyzer breaks
this fiber.

The points \(\phi=\pi/3\) and \(\phi=-\pi/3\), at identical \((u,v)\), have the
same complete two-port record. Thus the real-positive rank theorem does not
extend to complex source identification.

Two physically realizable ordered constructor packets give the same complete
record. Their mass triples and balanced coupling strengths are

\[
(M_A,M_B,m_n;u,v)=(5,3,1;1,1),
\qquad
(M_A,M_B,m_n;u,v)=(4,2,1;9/5,9/5).
\]

Both give \(W=126,N=0\). Endpoint equality therefore does not identify cascade
factorization.

## Calibration and contextual closure

For detector precision \(W_d=\operatorname{diag}(1,\epsilon)\),

\[
\det(J^T W_dJ)=\epsilon(\det J)^2.
\]

The algebraic response has full rank for every (epsilon>0), while its
calibrated determinant tends to zero as chirality precision is erased. No
independently calibrated lower bound on (epsilon) is currently admitted.

The presently declared upstream preparation family on this slice contains
only the identity. Its context saturation is therefore the slice itself, but
this grants no stability under a future source-authorized preparation. Before
cascade substitution is admitted, the saturation under the named preparation
monoid must remain inside a compact calibrated domain separated from (L=0).

## Disposition

Existence is established algebraically on the conditional real-positive
slice. Pole-basis synthesis, physical instrument execution, complex-phase
recovery, detector calibration, and ordered-factorization identification are
not established. The maximal uniformly observable coupling domain is not yet
authorized.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp677_contextual_cascade_quotient.py

Generated result: results/wp677_contextual_cascade_quotient.json.
