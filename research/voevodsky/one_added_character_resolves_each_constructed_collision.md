# One added character resolves each constructed collision

## Question

Do the finite-probe ambiguities constructed from \(P_m(x)=\prod_{a=1}^m(x-a)\) disappear when the probe family is enlarged by the next setting?

## Claim boundary

The result concerns the explicit polynomial collisions for linear character probes. It does not show that every ambiguity is resolved by one arbitrary added probe, nor that additional readouts constitute physical records.

## Bold prediction

The routes \(u_m,v_m\) obtained from the positive and negative coefficients of \(P_m\) agree at settings \(1,\ldots,m\), but setting \(m+1\) separates them by exactly

\[
P_m(m+1)=m!.
\]

On their support of \(m+1\) shells, the enlarged \((m+1)\)-setting Vandermonde matrix is square and invertible. Thus the ambiguity is eliminated rather than merely reduced.

## Rivals

1. The collision remains invisible at setting \(m+1\).
2. The new setting distinguishes this pair but leaves a radical on the same support.
3. Separation changes total route length or relies on changing the routes.

## Test

For \(m=1,\ldots,10\), reconstruct \(u_m,v_m\) exactly. Verify agreement at the first \(m\) settings, equal route length, readout difference \(m!\) at setting \(m+1\), and full rank of the enlarged evaluation and Gram matrices on the original support.

Also track nullity along the nested family: on \(m+1\) shells it must fall from one under \(m\) settings to zero under \(m+1\) settings.

## Falsifier

Any residual equality at setting \(m+1\), nonzero enlarged nullity, or route modification falsifies the bounded resolution claim.

## Computed result

For every \(m=1,\ldots,10\), the original routes remain unchanged and agree at settings \(1,\ldots,m\). Their readout difference at setting \(m+1\) is exactly \(m!\). On the fixed support of \(m+1\) shells, evaluation rank rises from \(m\) to \(m+1\), while Gram nullity falls from one to zero. All enlarged Vandermonde determinants are nonzero.

## Disposition

The bounded resolution prediction survives exactly. Each constructed ambiguity is a projection artifact relative to the first \(m\) settings: one specified additional character removes it completely on its existing support. This is local resolution, not global finite faithfulness, because admitting shell \(m+2\) creates a new radical direction.
