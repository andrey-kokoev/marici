# Endpoint attachment has a unique uniform candidate and one trace gate

Date: 2026-09-08

## Forced candidate

The retained endpoint incidence is

\[
V_p=\frac12\begin{pmatrix}1&p^{-1}\\p^{-1}&1\end{pmatrix}.
\]

It is invertible for every prime, with

\[
V_p^{-1}=\frac{2}{1-p^{-2}}
\begin{pmatrix}1&-p^{-1}\\-p^{-1}&1\end{pmatrix}.
\]

Therefore the missing typed endpoint comparison, if its analytic trace is
defined, has only one possible value:

\[
A_p=V_p^{-1}\operatorname{Tr}_{\rm end}T_{{\rm hist},p}J_P.
\]

This is not a fitted choice: it is forced by the established endpoint matrix
and the commuting-square equation.

## Uniform control

On wall and jump coordinates, the singular values of `V_p^-1` are

\[
\frac{2}{1+p^{-1}},\qquad \frac{2}{1-p^{-1}}.
\]

Hence, uniformly for all primes,

\[
\frac43\le\sigma_{\min}(V_p^{-1})
\le\sigma_{\max}(V_p^{-1})\le4.
\]

Consequently `A_p` is defined, injective, or bounded below exactly when the
analytic endpoint trace is, up to these explicit prime-uniform constants.
There is no additional endpoint-matrix conditioning obstruction.

## Sharpened frontier

Prior research already supplies the bivariate graph domain and continuous
endpoint traces.  The nonredundant local question is now whether

\[
\operatorname{Tr}_{\rm end}T_{{\rm hist},p}J_P
\]

is faithful on the relevant Adams source-generated relation and whether its
polarized form agrees with the resolved Green boundary form.  If so, the
unique `A_p` propagates the split source port through endpoint attachment.

This does not yet prove injectivity or quadratic Green compatibility.

## Evidence

- `check_marici_rh_endpoint_comparison_unique_candidate_20260908.py`
- `marici_rh_endpoint_comparison_unique_candidate_certificate_20260908.json`
