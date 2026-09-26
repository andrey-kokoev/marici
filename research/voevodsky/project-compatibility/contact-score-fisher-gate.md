# Contact-infinity grading is not uniformly equivalent to the Gaussian score metric

## Source and scope

Freshly read ledger2214 (normalized Gaussian score),2219 (generic contact-grade/score commutation),2235 (quadrupole source),2236 (contact response matrix). Work in the declared independent real-mode Gaussian model, with three distinct mode representatives and normalized logarithmic-covariance tangent coordinates. The quadrupole tangent evaluations are Q below. Other real/complex mode conventions can change constants and must be declared separately.

For each mode, S_i=a_i X_i^2-1/2, E S_i=0 and E(S_i S_j)=delta_ij/2. This is a boundary-field score, not a postulated output-noise covariance. Contact-normal projection is used only where the source establishes its commutation with score insertion; no extension to nontransverse strata is assumed.

## Actual score metric on the retained ports

Let

    Q=[[1,2,0],[1,-1,-1],[1,-1,1]],
    U=Q^T S, F=E(U U^T)=Q^T Q/2=diag(3/2,3,1).

For the retained occurrence coefficients x, source response is

    r=gr_ct E(O U)_c=-8 Q^T diag(C) x.

These response covectors have squared dual Fisher norm

    ||r||_(F^-1)^2 = r^T F^-1 r
                     =128 sum_e C_e^2 x_e^2.

In particular, positivity of the score metric does not cancel contact suppression. The Gaussian metric is fixed while C_e can tend to zero.

The Riesz representative in the retained score span is

    f_x=-16 sum_e C_e x_e S_e,
    E(f_x U)=r, ||f_x||_L2^2=128 sum_e C_e^2 x_e^2.

This represents the retained response functional. It is not an identification of f_x with the complete physical observable O. Orthogonal components and other admitted physical channels have not been tested.

## Infinity and the precise cost of inversion

Use the source C_e=g_e h_e with labelled g=(s1*s2,s2*s3,s3*s1). Along s=(t,t,t^2), h=1 and x=e23,

    ||r||_(F^-1)^2=128 t^6 ->0.

The labelled graded response instead has squared dual Fisher norm128. Hence the retained-grade topology and the Gaussian response topology are not uniformly equivalent at this infinity face.

Within the retained score span, the uniquely normalized test extracting x_e from this response family is

    L_e=-S_e/(8 C_e),
    gr_ct E(O L_e)_c=x_e,
    ||L_e||_L2^2=1/(128 C_e^2).

Thus the source-selected asymptotic coefficient is algebraically recoverable, but its dual score test becomes unbounded. In the anisotropic23 direction the squared test norm grows as t^(-6)/128.

This is a rigorous score-norm amplification statement, NOT a universal sampling-complexity theorem. The variance of an empirical mixed-product estimator involves moments of O L_e, not just the variance of L_e. Nor does it exclude recovery through another observable outside the tested score span.

## Programme conclusion

The previous physical realization is retained, with a sharper boundary:

- finite nonzero contact factors: the source response is faithful with quantitative bounds;
- contact infinity in ordinary Gaussian response topology: noncollapse fails for these fixed score ports;
- labelled asymptotic coefficients: faithful recovery survives in a stronger retained-grade topology, with unbounded Gaussian dual-test cost.

Do not report this as a failure of all physical realization or as a newly discovered Carrier defect. It distinguishes exact asymptotic observability from uniformly bounded score observability using the source's own metric.

Next search the prior physical port family for a source-authorized, bounded alternative at contact infinity. If none is supplied, preserve the grade-realization result and register this norm-specific completion obstruction rather than altering the norm merely to obtain a positive conclusion. The triangle's analytic continuation and the owner's complex-typing handoff remain separate.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_score_fisher.py` checks Gaussian moments, exact port covariance, dual response norm, normalized extracting tests and reciprocal signal/test norms along the source path. This is finite source-score analysis, not a measurement protocol or a full physical completion theorem.
