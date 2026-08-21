# Zeta zeros are poles of the continued prime-power trace

Epistemic-graph event: 1392.

## Prime-side trace

For `Re(s)>1`, Ledger 1365 gives

`T_P(s)=sum_(p,k>=1)(log p)p^(-ks)`

`=-zeta'(s)/zeta(s)`.

This is the logarithmic derivative of the intrinsic-prime Fredholm
determinant.

## Completed continuation

With

`xi(s)=(1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)`,

logarithmic differentiation gives

`xi'(s)/xi(s)=1/s+1/(s-1)-(1/2)log pi`

` +(1/2)psi(s/2)-T_P(s)`.

Theta completion continues the left side meromorphically.  Therefore this
identity supplies a meromorphic continuation of the prime-power trace after
the explicit archimedean terms are included.

Because `xi` is entire of order one, its Hadamard product gives

`xi'(s)/xi(s)=B+sum_rho(1/(s-rho)+1/rho)`,

with the standard symmetric limiting convention over zeros.  Each zero
`rho` of multiplicity `m` is therefore a pole of `xi'/xi` with residue `m`,
and a pole of the continued `T_P` with residue `-m` after archimedean terms
are separated.

## Interpretation

This is the first exact location of the nontrivial zeros inside the present
construction:

`intrinsic prime-power trace -> meromorphic continuation -> zero poles`.

The zeros are resonances of the analytically continued logarithmic trace.
They are not eigenvalues of the prime-diagonal operator `N`, whose spectrum
is `{p}`, and not eigenvalues of the unmodified dilation generator, whose
spectrum is continuous.

Calling them a self-adjoint spectrum would require an additional theorem
constructing an operator with compact resolvent and identifying its trace
formula with this meromorphic continuation.  No such operator is presently
derived.

## Provenance boundary

The prime trace uses conditional intrinsic primes.  Its continuation and the
Hadamard expansion use the archimedean theta completion and complex analysis.
Thus the resonance statement is conditional on the analytic inputs audited
in Ledger 1362.

## Scope

This derives a meromorphic trace-resonance interpretation, not the Riemann
hypothesis or a Hilbert--Polya spectrum.
