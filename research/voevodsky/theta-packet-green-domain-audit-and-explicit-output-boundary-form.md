# Theta packet Green-domain audit and explicit output boundary form

## Domain audit

The source comparison in `theta-packet-is-a-tensorized-localized-common-history-observation.md` constructs

    A:X -> L2(I^2) direct-sum L2(I^4),       OA=F.

The earlier full analytical system uses one-variable observers, their phase-energy Mellin realizations, and a relative second-order graph carrying seam value and flux. Its explicit response core has B_g=g, Q_g=Fourier(g), A_g=Volterra(g), and a principal-value response. It does not define a signed Green form on arbitrary two-variable and four-variable interval densities.

Consequently q_old(Ac,Ad) is presently undefined. The last proposed finite calculation requires a typed form-domain map before it can produce the earlier signed matrix. The observation identity OA=F remains valid.

There is also a concrete regularity obstruction to treating interval densities as the earlier graph vectors by zero extension. A nonzero compactly supported rectangular step function has a nonzero jump on some cell face. Its distributional gradient contains a face measure, so it is not in H1 of the ambient Euclidean space. If every face jump vanished, the function would be constant across the entire partition, including the exterior zero cell, and hence zero.

Thus, for the zero-extended packet image,

    ran(A) intersect (H1(R^2) direct-sum H1(R^4)) = {0}.

Here injectivity of A on the four-prime packet follows from the selected invertible matrix M. This excludes direct use of the zero-extended step densities as second-order graph vectors. It does not exclude a separately constructed distributional source map or smoothing incidence.

## Smooth theta outputs have explicit traces

Write phi=Phi_1 and use logarithmic endpoints A_i=log a_i, B_i=log b_i. Each output atom is

    h_i(s) = integral_(A_i)^(B_i) phi(v) phi(v+s) dv,       s>=0.

Differentiation under the finite integral gives

    h_i^(m)(s) = integral_(A_i)^(B_i) phi(v) phi^(m)(v+s) dv.

The explicit Gaussian formula bounds every such derivative near s=0 and gives superexponential decay as s tends to infinity. Therefore h_i belongs to H^m(R_+) for every integer m. Its two traces are

    alpha_i = h_i(0) = integral_(A_i)^(B_i) phi(v)^2 dv,
    beta_i = h_i'(0) = [phi(B_i)^2 - phi(A_i)^2]/2.

These are exact, unrescaled source formulas.

## A concrete boundary matrix on the output histories

For this section use conjugate-linear-first Hilbert pairings and define L=d_s^2-1/4. Integration by parts on these smooth decaying histories yields

    <f,Lg> - <Lf,g>
      = conjugate(f'(0)) g(0) - conjugate(f(0)) g'(0).

Let alpha and beta be the rows above and set

    W = i (beta* alpha - alpha* beta).

Then W is Hermitian, has rank at most two, and is the coefficient matrix of i times the displayed Green difference. The sign convention is declared here; identification with an earlier reciprocal boundary orientation requires its own comparison.

Let G=H*H be the unchanged one-point observation Gram. On r variables use the sum of the r copies of L. Integrating each variable separately gives the tensor boundary matrix

    W_r = sum_(j=1)^r G^(tensor(j-1)) tensor W tensor G^(tensor(r-j)).

All functions involved are smooth and decaying, so the integrations and boundary traces are justified on the finite tensor span. The route-packet matrix is explicitly

    Q_boundary = K_2* W_2 K_2 + K_4* W_4 K_4.

This is a well-defined 24-by-24 Hermitian form from the actual theta output histories and the specified differential operator. It is a newly specified boundary form. Equality to the earlier complete signed Green form has not been proved.

## Parity restriction and visible coupling

Let Z=K/2 denote the six orthonormal parity columns, so B=Z*, P=ZZ*, and K_2 Z=0. The exact parity block and its coupling to the counting-visible space are therefore

    Q_hidden = Z* K_4* W_4 K_4 Z,
    Q_hidden,visible = Z* K_4* W_4 K_4 (I-P).

The degree-two term vanishes in both expressions. These formulas preserve the original atom amplitudes and need only the one-point Gram G and the two endpoint rows alpha,beta.

Since alpha,beta,G and the signature matrices are real, Q_boundary and Q_hidden are purely imaginary Hermitian matrices with real skew-symmetric coefficients. Their diagonals vanish and their nonzero eigenvalues occur in opposite-sign pairs. In particular every real coefficient vector c satisfies

    c* Q_boundary c = 0.

The normalized real parity witness from the decoder estimate has zero value under this boundary form. Therefore this form cannot provide a positive lower bound for the six real parity coordinates. The earlier complete signed system also carries regular and endpoint contributions; the boundary difference alone cannot stand for their sum.

## Next map now precisely located

To compute the earlier signed form on the packet, one must supply a source-derived map from these multipoint histories into the earlier observer/relative graph, or an admitted tensor extension of that whole graph and its form. It must specify the regular term, reciprocal endpoint pairing, and boundary orientation. The explicit W_r above supplies the differential boundary contribution once such an extension is selected.

The finite observation bridge is complete. The proposed earlier-Green pullback is blocked by a form-domain and tensor-extension identification, already visible before completion or large numerical Gram inversion.
