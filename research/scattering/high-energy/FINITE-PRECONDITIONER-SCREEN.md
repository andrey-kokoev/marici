# H6 — fixed-response Woodbury inverse-certificate screen

This is a test of the actual 548-direction finite-response system, not H7's raw omitted model. At radial K=3.30 the source entrance matrix is

    A=I-G V+g² G S Z S*,

where Z is the retained downstream response. The channel-diagonal radial preconditioner Dpre=I-G diag(V) and Woodbury correction give M=(Dpre+g² G S Z S*)^-1. Hence

    I-M A = M G Voff = T-U C S* T,
    T=Dpre^-1 G Voff, U=Dpre^-1 G S,
    C=(I+g² Z S*U)^-1 g² Z.

A verified norm ||I-MA||<1 would imply invertibility and ||A^-1||<=||M||/(1-||I-MA||). This is a sufficient certificate route, not a claim that GMRES convergence requires a contraction in this norm.

The checker evaluates the defect Frobenius norm by its channel-local structure and port-rank contractions, without constructing a dense 35,072-square matrix. It independently checks selected columns of S*T and T*U. It also reports defect action/input norm ratios on the four already stored corrected columns. These ratios are numerical lower tests for the operator norm; a Frobenius norm greater than one alone is not such a lower bound.

No entrance stationary solve is repeated. The downstream response is reconstructed for inverse analysis. All results are floating, not outward-rounded operator norms. This is one energy, not a full-band certificate. Even a successful norm test would need a bound on M, controlled field/output reconstruction, source arithmetic and all packet nodes before accepting H6.

## Measured result

The Woodbury defect Frobenius norm is about 98.6503. More importantly, its action/input ratios on all four stored corrected columns lie near 1.20 (>1). The floating action test therefore gives evidence against even the spectral below-one condition, not merely against the loose Frobenius sufficient bound. This does not constitute a directed norm certificate, but it makes outward-rounding this particular preconditioner into a Neumann contraction implausible. Successful GMRES solves are consistent with this: nonnormal Krylov convergence does not imply Euclidean contraction. No source singularity or counterexample to H6 follows.

Five of the six H6 cycles are spent; one remains. The remaining cycle should respond to the measured contraction result rather than replay this screen. H6 remains open and H7's exhausted budget is unchanged.
