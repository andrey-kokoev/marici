# Adjacent-band Remez transfer cannot control the Weibull endpoint

## Question

Can the missing cross-region coupling be supplied by transferring polynomial control from the first far band \([Y,2Y]\) back to the endpoint window \([0,Y]\)?

## Exact obstruction

Consider

\[
p_K(y)=(1-y/Y)^K.
\]

Then \(p_K(0)=1\), while the unweighted norms on the two adjacent bands are exactly

\[
\int_0^Y|p_K(y)|^2dy=\frac{Y}{2K+1},
\qquad
\int_Y^{2Y}|p_K(y)|^2dy=\frac{Y}{2K+1}.
\]

Every shifted Weibull weight is bounded above on \([0,2Y]\). Consequently the weighted norm on the union is at most a fixed multiple of \(2Y/(2K+1)\), which tends to zero. Endpoint evaluation is therefore unbounded even when the local window and its first adjacent far band are coupled.

Equivalently, any Remez-type endpoint transfer restricted to these fixed compact bands must carry a constant that grows with degree. It cannot furnish the uniform-degree endpoint cap needed for atomic coercivity.

## Why the infinite tail differs

Beyond \(2Y\), \(|1-y/Y|^K\) grows polynomially. The full subexponential Weibull tail detects that growth and is precisely the part omitted by a compact-band transfer. Any successful estimate must use all far annuli or an equivalent global object such as recurrence coefficients, a Nevanlinna matrix, or the full orthogonal kernel.

## Disposition

Reject adjacent-band Remez transfer as the cross-region constructor. Retain `entire-tail-kernel-transfer`: seek a global inequality that sums all far bands without degree-dependent loss.

## Claim boundary

The witness rules out fixed compact two-band control. It does not rule out a degree-adaptive split or a global infinite-tail transfer.
