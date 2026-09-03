# Frequency-filter Beta coherencer

## Question

Can the high-difference frequency filter be normalized into an exact probability object whose concentration is uniform in rank?

## Claim boundary

After the change of variables \(z=e^{-hr}\), the radial filter is exactly a transformed Beta distribution. Its normalization, mean, variance, and fixed-ratio concentration follow explicitly. The additional factor arising from the frequency measure and the prime distribution remain to be controlled.

## Radial filter

Write

\[
r=\xi^2
\]

and

\[
w_{q,t,h}(r)
=
e^{-tr}(1-e^{-hr})^q.
\]

Set

\[
a=\frac th,
\qquad
z=e^{-hr}.
\]

Since

\[
dr=-\frac{dz}{hz},
\]

one obtains

\[
\int_0^\infty
w_{q,t,h}(r)\,dr
=
\frac1h
\int_0^1
z^{a-1}(1-z)^q\,dz
=
\frac1hB(a,q+1).
\]

Thus the normalized variable

\[
Z=e^{-hR}
\]

has distribution

\[
Z\sim\operatorname{Beta}(a,q+1).
\]

This is an exact pushforward, not a saddle approximation.

## Logarithmic moments

Because

\[
R=-\frac1h\log Z,
\]

the Beta logarithmic moments give

\[
\mathbb E[R]
=
\frac{
\psi(a+q+1)-\psi(a)
}{h}
\]

and

\[
\operatorname{Var}(R)
=
\frac{
\psi_1(a)-\psi_1(a+q+1)
}{h^2}.
\]

Here \(\psi_1\) is the trigamma function.

## Fixed-ratio asymptotic

For

\[
h=\kappa t,
\qquad
a=\frac1\kappa,
\]

and fixed \(\kappa>0\),

\[
\mathbb E[R]
=
\frac{
\log q-
\psi(1/\kappa)+o(1)
}{
\kappa t
}
\]

while

\[
\operatorname{Var}(R)
=
\frac{
\psi_1(1/\kappa)+o(1)
}{
\kappa^2t^2
}.
\]

Therefore

\[
\frac{
\sqrt{\operatorname{Var}(R)}
}{
\mathbb E[R]
}
=
O_\kappa\left(\frac1{\log q}\right).
\]

The radial observer becomes relatively concentrated as rank grows, although its absolute width remains of order \(1/h\).

## Relation to the saddle

The mode satisfies

\[
r_*
=
\frac1h
\log\left(1+\frac{qh}{t}\right).
\]

Both the exact mean and the mode have leading scale

\[
\frac{\log q}{h}.
\]

The Beta representation supplies the fluctuation law around the previously derived saddle.

## Frequency-measure correction

The Fourier integral uses \(d\xi\), not \(dr\). Since

\[
d\xi=
\frac{dr}{2\sqrt r},
\]

the actual frequency measure contains an additional factor \(r^{-1/2}\). Relative concentration suggests that this factor is slowly varying on the principal window, but a uniform replacement by its value at the mean requires a quantified tail estimate.

## Coherence interpretation

The transformed Beta law is a higher coherencer connecting:

- difference order \(q\);
- heat scale \(t\);
- mesh \(h\);
- observed frequency \(R=\xi^2\).

Its residue is no longer an unspecified localization error. The exact first two cumulants identify the scale on which the archimedean symbol and regularized prime cosine distribution must be compared.

## Disposition

The rank dependence of the frequency observer is explicit and relatively concentrated. The next test is to bound the \(r^{-1/2}\) frequency-measure correction and prime distribution on a Beta-probability central window, with tails controlled separately. This still requires a source-valid regularization of the critical-line prime cosine sum.

## Verification

- `research/voevodsky/checkers/check_frequency_filter_beta_coherencer.py`
- `research/voevodsky/results/frequency_filter_beta_coherencer.json`
