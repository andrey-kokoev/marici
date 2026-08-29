# Magnetic bulk quotient with a filtered boundary-jet signature

The depth-resolvent, Euler-cap, and two-wedge results should not be collapsed
into one scalar rank. They define three differently typed boundary invariants.

For fixed \((\beta,g,q)\), write

\[
\Sigma_{\beta,g,q}=(p,h,w),
\]

where:

- \(p=g\) is the pole order of the persistent principal boundary current;
- \(h\) is the total number of Hall holes in the finite plus cap;
- \(w\) is the ordinary quotient observation width.

The principal current is covariant source data, the holes are presentation
defects with primitive relation witnesses, and the quotient width counts
independent observer directions. Equal integers across these coordinates do
not identify their types.

## Principal current

The branch-alignment resolvent has principal part

\[
\frac{Q\,y^{g-1}N^g}{(1-y)^g},
\qquad Q=q+2.
\]

Thus

\[
p=g
\]

on every admissible stratum. Its adjoint carries the dual principal part
\(Q(N^\ast)^g\). Removing this current is not ordinary quotienting; it would
require a separately authorized renormalization preserving the adjoint
pairing.

## Finite cap rank and quotient width

Rank-invariant exact elimination gives

\[
h=
\begin{cases}
0,&q<g+\beta-2,\\
1,&g+\beta-2\le q<2g+\beta-3,\\
2,&q\ge2g+\beta-3.
\end{cases}
\]

The missing depths are respectively

\[
\varnothing,\qquad \{a_\ast\},\qquad
\{a_\ast-1,a_\ast\},
\]

where \(a_\ast=q-g+3\).

The independently obtained observation law gives \(w=2\) on either

\[
g\ge4,\qquad \min(\beta-1,g-3)\le q\le g-3,
\]

or

\[
q\ge2g+\beta-3.
\]

Otherwise \(w=1\).

## Four joint strata

Across all \(945\) exact cases with
\(2\le\beta\le8\), \(2\le g\le10\), and \(1\le q\le15\), only

\[
(h,w)=(0,1),(0,2),(1,1),(2,2)
\]

occur. Their multiplicities are \(399,105,223,218\), respectively. The mixed
signatures \((1,2)\) and \((2,1)\) do not occur.

An earlier one-pass sparse eliminator falsely reported mixed signatures because
new pivots need not occur in monotone row order. Replacing it by a pivot-map
normal form restores exact agreement in all \(945\) cases. Thus the four
strata survive a direct hostile test, while the comparison-map theorem remains
to be proved.

## Completion statement

Let \(\widehat{\mathcal P}_\rho\) be the two-branch presentation completed in a
source depth norm with \(\rho>1\), and let
\(\widehat{\mathcal H}_\rho\) be the completed Hall carrier consisting of the
minus spine and finite plus cap. The candidate structure is:

\[
\widehat{\mathcal P}_\rho
\longrightarrow
\widehat{\mathcal H}_\rho
\longrightarrow
\mathcal J^{(g)}_{\beta,g,q},
\]

supplemented by the finite defect fiber \(\mathcal E_{\beta,g,q}\) of total
Hall rank \(h\), the two Euler-incidence coordinates, and observer fiber
\(\mathcal O_{\beta,g,q}\) of rank \(w\).

The first arrow is bounded only for \(\rho>1\). The boundary jet
\(\mathcal J^{(g)}\) records the nonremovable order-\(g\) principal current.
The finite fiber \(\mathcal E\) records the source-declared Hall holes. The
observer fiber \(\mathcal O\) records what survives ordinary quotienting.

This is not yet asserted as a split direct sum or exact sequence. The missing
theorem must construct the comparison maps and prove:

1. the bulk quotient is natural under depth shift;
2. the threshold-local Euler coordinates embed into, or fail to embed into,
   the total cap fiber by explicit comparison maps;
3. any relation between changes in \(\mathcal E\) and \(\mathcal O\) is
   derived rather than inferred from threshold coincidence;
4. the low width-two stratum maps to \(\mathcal O\) without creating a false
   cap hole;
5. the adjoint principal current pairs nondegenerately with the observer
   boundary jet.

This typed formulation prevents an arbitrary Hall basis from absorbing
source-declared cokernel directions and prevents a finite-rank cap correction
from erasing the persistent completion current.