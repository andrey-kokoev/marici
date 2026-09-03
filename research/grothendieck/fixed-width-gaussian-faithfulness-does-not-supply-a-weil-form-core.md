# Fixed-width Gaussian faithfulness does not supply a Weil-form core

## Question

Does positivity on every finite fixed-width Gaussian translate packet automatically imply positivity on the full Weil test-function domain?

## Two distinct density statements

Let

\[
\mathcal G_\sigma
=
\operatorname{span}\{\tau_ag_\sigma:a\in\mathbb R\}.
\]

Because the Fourier transform of a Gaussian never vanishes, translates of `g_sigma` are cyclic for the translation representation in `L^2(R)`. Their span is `L^2`-dense. The same nonvanishing multiplier also makes Gaussian convolution injective on suitable distribution spaces.

Neither statement proves that `G_sigma` is a form core for the completed Weil quadratic form.

## Topology mismatch

The completed form contains endpoint evaluation, archimedean weights, and prime-translation terms. Endpoint evaluation at imaginary arguments is not continuous in the ordinary real-line `L^2` norm. Therefore an `L^2` approximation

\[
f_n\longrightarrow f
\]

does not imply

\[
W(f_n-f,f_n-f)\longrightarrow0.
\]

Positivity on an `L^2`-dense subspace can fail to extend to an unbounded or nonclosable form. Distributional injectivity establishes uniqueness of the source, not continuity of its quadratic form.

## Required form-core theorem

To promote Gaussian translate positivity to the full Weil criterion, one needs:

1. a declared Hilbert or locally convex test space `H_W` on which endpoint, gamma, and prime terms are continuous or define a closable Hermitian form;
2. closed or closable source feature operators `A` and `B`, or an associated closed operator, giving a genuine graph norm such as

\[
\|f\|_{\rm graph}^2
=
\|f\|_{H_W}^2+\|Af\|^2+\|Bf\|^2;
\]

The scalar expression `||f||^2+|W(f,f)|` is not assumed to be a norm for an indefinite form;
3. graph-norm density of `G_sigma` in the form domain;
4. compatibility of the Gaussian synthesis maps with completion in that topology.

Only then does positivity on every finite Gaussian packet extend by closure.

## Alternative bounded route

If the entire completed kernel construction is first realized as a bounded Hermitian operator on a source Hilbert space for which the Gaussian is cyclic, ordinary Hilbert density suffices. But boundedness must include the endpoint channel; it cannot be inferred from bounded prime truncations.

A reproducing-kernel or Fock-type analytic Hilbert space may make endpoint evaluation continuous, but its translation action, prime sums, and density theorem must all be proved in that same space.

## Consequence for joint faithfulness

Fixed-width translate observers can be jointly faithful for recovering a distribution while still failing to be positivity-complete for an unbounded quadratic-form domain. These are different arrows:

\[
\text{observer injectivity}
\not\Rightarrow
\text{form-core density}.
\]

## Disposition

Retain fixed-width Gaussian observers as a faithful source probe. Add a separate Weil-form-core theorem before promoting their finite Gram positivity to the full criterion. The first missing typed object is the completed test space and graph topology in which all three source sectors coexist continuously.
