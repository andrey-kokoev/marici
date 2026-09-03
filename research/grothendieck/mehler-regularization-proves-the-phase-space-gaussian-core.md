# Mehler regularization proves the phase-space Gaussian core

## Question

Do the five harmonic-regularizer conditions hold for the model intersection of logarithmic spectral control and exponential Fourier control?

## Model domain

Fix `beta>0` and define

\[
\|f\|_X^2
=
\int (1+\log^2(2+|u|))|f(u)|^2du
+
\int e^{\beta|x|}|\widehat f(x)|^2dx.
\]

Use the scaled harmonic oscillator whose ground state is the selected fixed-width Gaussian. Its Mehler semigroup is symmetric under Fourier transform.

## Boundedness and strong continuity

The Mehler kernel is a Gaussian kernel combined with a strict dilation. Exponential weights are submultiplicative up to the dilation factor, and Gaussian convolution has every exponential moment. Weighted Young estimates therefore make `S_epsilon` bounded on the Fourier exponential summand for each bounded epsilon interval.

The logarithmic weight is moderate under translation and dilation, so the same kernel estimate gives boundedness on the spectral summand. Density of smooth Gaussian-decay functions followed by dominated convergence proves

\[
S_\epsilon f\longrightarrow f
\]

in `X` as `epsilon->0`.

## Hermite truncation

For fixed `epsilon>0`, the Hermite coefficients of `S_epsilon f` acquire the factor `exp(-epsilon n)`. Weighted norms of the `n`th Hermite function grow at most subexponentially in `n` for the fixed exponential weight and polynomially for the logarithmic weight. Hence the exponential coefficient damping dominates, and Hermite partial sums converge in `X`.

## Recovery from real translates

Derivatives at zero of the real translation orbit of the matched Gaussian are polynomial--Gaussian functions spanning the Hermite family. The translation orbit is differentiable to every order in `X`: both the spectral logarithmic weight and the Fourier exponential weight are dominated by the Gaussian envelope after multiplication by any fixed polynomial.

Finite differences of real translates therefore converge in `X` to every Hermite function. Combining the three approximation stages gives

\[
\overline{\operatorname{span}\{\tau_ag_\sigma:a\in\mathbb R\}}^{\|\cdot\|_X}
=X.
\]

## Prime row

At fixed width, the labelled prime row is bounded in base `L2` by `sum q_n<infinity`. Since the `X` norm dominates `L2`, adjoining this bounded row does not change the core conclusion.

## Boundary

This is a form-core theorem for the displayed model norm. Promotion to the actual Weil domain still requires source identities establishing:

1. that endpoint evaluation is continuous under the chosen Fourier exponential component with the exact convention;
2. that the gamma row has the displayed logarithmic growth;
3. that the completed labelled prime row has the asserted fixed-width bound;
4. that no additional source-sector domain condition is omitted.

## Disposition

The simultaneous approximation problem is solved for the model phase-space domain. The remaining topology gate is no longer density but identification of the actual completed source-row domain with this model. Positivity and the Douglas contraction remain separate.
