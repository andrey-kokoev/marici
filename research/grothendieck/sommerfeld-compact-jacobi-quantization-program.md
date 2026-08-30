# Sommerfeld attack: compact Jacobi dynamics and prime-phase quantization

## Structural target

The compact spectral coordinate is

\[
 u_k=(1/4+\gamma_k^2)^{-1}.
\]

Thus any completed positive Jacobi operator realizing the Riemann spectrum
must be positive and compact, with pure-point eigenvalues accumulating only at
zero. Its recurrence

\[
 \sqrt{b_{n+1}}\psi_{n+1}+a_n\psi_n+sqrt{b_n}\psi_{n-1}=u\psi_n
\]

must have `a_n->0` and `b_n->0`. A nonzero constant/free Jacobi tail would
produce an essential spectral interval and is therefore immediately
incompatible with the desired arithmetic spectrum.

The first coefficients show the expected finite signature after an initial
transient:

\[
 a_1>a_2>a_3>a_4,qquad b_1>b_2>b_3>b_4>0.
\]

Five values do not prove either limit. They only reject constant-tail modeling
as the natural first ansatz and identify decay as the quantity to explain.

## Quantization law to derive

The Riemann--von Mangoldt asymptotic implies, after `u=(1/4+T^2)^(-1)`, the
conditional compact-edge counting law

\[
 N_J(u):=\#\{k:u_k\ge u\}
 \sim \frac{u^{-1/2}}{2\pi}
 \log\frac{u^{-1/2}}{2\pi}
 \qquad(u\downarrow0),
\]

up to the standard linear and fluctuating corrections. This is the Jacobi
analogue of a Sommerfeld action law. The smooth gamma factor supplies the main
action; the prime/Euler term must supply the oscillatory phase defect.

The research target is now:

1. derive asymptotics of `a_n,b_n` from the completed source moments;
2. perform discrete WKB for the decaying recurrence;
3. recover the counting action above;
4. identify the explicit-formula prime phase as its boundary phase;
5. prove that the resulting boundary condition is self-adjoint rather than
   merely restating the zero equation.

## Sharp falsifiers

- If certified coefficients stabilize at nonzero limits, compact-Jacobi
  quantization is false.
- If the WKB counting exponent disagrees with `T log T`, the proposed
  recurrence asymptotics are false.
- If the prime phase has to be inserted from zero data rather than derived
  from the source Euler term, the explanation fails Deutsch's criterion.
- If the boundary form is not symmetric/closable, this does not produce a
  Hilbert--Polya operator even if its finite poles fit zeros.

The first obstruction is already sharp: the raw Euler prime phase exists
absolutely only for `sigma>1`, while quantization needs `sigma=1/2`. A
canonical regularized Abel boundary must be derived; inserting `arg zeta` on
the line merely restates the spectral data. See
`sommerfeld-prime-phase-abel-boundary-obstruction.md`.

Finite Jacobi--Pade phases provide a canonical bypass. The real polynomial
`Q_n(h)=det(I+hJ_n)` has one `pi` jump at each negative Pade pole, with prime
data entering through regular completed source moments rather than a divergent
critical-line Euler phase. The remaining theorem is convergence to an infinite
self-adjoint Weyl function. See `sommerfeld-jacobi-pade-phase-bypass.md`.

## Trace and multiplicity

Since `sum u_k` converges, the desired positive Jacobi operator is trace class.
For a simple-support scalar Jacobi realization,

\[
 \operatorname{tr}J=\sum_na_n=\sum_ku_k.
\]

The source mass `A_0=sum m_k u_k` agrees with this trace only when atom
multiplicities are one. This explains why residue convergence and trace
completion jointly probe simplicity, while finite scalar moments alone cannot
certify eigenspace dimension.

## Scope

This is a conditional asymptotic program and falsifier map. The five observed
coefficients do not prove compactness, a WKB law, self-adjointness of the
infinite closure, simplicity, or RH.

## Durable verification

- Checker: `checkers/sommerfeld_jacobi_attack.py`
- Result: `results/sommerfeld-jacobi-attack.json`

All-order positivity would force weak Gaussian-measure convergence and locally
uniform Weyl convergence by Hausdorff determinacy. WKB explains counting; it
is not needed to rescue limit existence. See
`jacobi-gaussian-measure-to-weyl-limit-theorem.md`.
