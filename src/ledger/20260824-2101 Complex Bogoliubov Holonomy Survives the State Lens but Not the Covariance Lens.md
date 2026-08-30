# 2101 — Complex Bogoliubov Holonomy Survives the State Lens but Not the Covariance Lens

## Hostile question

Entry 2100 found that a real collision Berry sign disappears from Gaussian
covariance coefficients.  Test whether complex Bogoliubov transport is erased
intrinsically or only by that particular readout.

## Frozen loop

Take the normalized squeezed-vacuum family

\[
|\zeta\rangle,
\qquad
\zeta=re^{i\theta},
\qquad
0\le\theta\le2\pi,
\]

at the exact rational hyperbolic point

\[
\cosh r=\frac53,
\qquad
\sinh r=\frac43,
\qquad
\tanh r=\frac45.
\]

No support divisor changes around the loop.

## State-line transport

In the standard even-Fock expansion, the phase exponent counts squeezed
pairs.  Hence

\[
i\langle\zeta|\partial_\theta\zeta\rangle
=-\frac12\sinh^2r
=-\frac89.
\]

After one turn the Berry phase is

\[
\gamma
=\int_0^{2\pi}i\langle\zeta|\partial_\theta\zeta\rangle d\theta
=-\frac{16\pi}{9},
\]

and therefore

\[
\boxed{
T_{\rm state}=e^{-16\pi i/9}\ne1.
}
\]

## Covariance transport

The real covariance depends on the squeezing angle only through its quadratic
rotation.  It returns exactly after \(2\pi\), remains pure, and has

\[
T_{\rm cov}=I.
\]

At the chosen base point,

\[
V(0)=
\begin{pmatrix}
1/18&0\\
0&9/2
\end{pmatrix},
\qquad
\det V=\frac14.
\]

## Narrow result

\[
\boxed{
\text{the same Carrier loop has trivial covariance transport but
nontrivial normalized-state-line transport.}
}
\]

Complex Bogoliubov holonomy is therefore not universally erased.  Whether it
survives depends on the coefficient/readout layer:

\[
\text{state line}\longrightarrow\text{nontrivial phase},
\qquad
\text{covariance lens}\longrightarrow\text{identity}.
\]

This strengthens H2.  The Carrier supplies the loop, while sector- and
layer-specific coefficient objects decide which transport is observable.  No
new Carrier incidence is implicated.

## Next falsifier

Test an interference-sensitive physical pairing of the state line.  A global
Berry phase of one isolated branch is not itself observable; a source-derived
relative phase between two Bogoliubov histories may be.  Freeze a two-branch
interferometric comparison and determine whether the holonomy survives the
physical quotient or again becomes presentation data.

## Durable evidence

- `research/benincasa/checkers/squeezed_vacuum_berry_vs_covariance.py`
- `research/benincasa/checkers/results/squeezed-vacuum-berry-vs-covariance.json`
- Ledger allocation: `seqclaim-b4d4e5f616fd402a28875b49`

