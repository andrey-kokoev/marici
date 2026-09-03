# Quarter Bernstein endpoint profile fails the uniform gate

## Question

Do exact finite Hausdorff weights exhibit the endpoint signature required by inverse-square moments uniformly across shifts zero through four?

## Claim boundary

The preregistered degree-28 gates required endpoint-estimator spread below \(0.1\) and agreement with the tail amplitude within \(0.1\) at every tested shift. Failed gates remain failed; low-shift success does not narrow the scope retrospectively.

## Disposition

Every Bernstein weight is strictly positive and each weight family sums exactly to the initial moment. The uniform endpoint test fails: at shift four and cutoff 28, the relative estimator spread is \(0.23247\), and its mean differs from the tail amplitude by \(0.13428\). Both improve with cutoff but miss the fixed gates. Thus finite Hausdorff reconstruction survives, while a uniform linear endpoint density is unverified. Further endpoint fitting is deferred. Work reallocates to `quarter-cross-ratio-stieltjes-j-fraction`, an independent construction using the positive Hankel data.
