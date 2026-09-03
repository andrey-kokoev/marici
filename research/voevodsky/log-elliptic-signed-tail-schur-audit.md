# Log-elliptic signed-tail and Schur audit

## Question

Can archimedean logarithmic ellipticity turn fixed-support Weil positivity into a finite verification problem?

## Claim boundary

This packet verifies the periodic signed-tail mechanism and the exact finite/tail Schur gate. It does not prove the required interval Gårding estimate or source constants.

## Periodic mechanism

In a frequency-diagonal fixture, write

\[
q(n)=\log n+p(n)-C_\gamma,
\qquad |p(n)|\le C_{\rm prime}(L).
\]

Then

\[
q(n)\ge \log n-C_\gamma-C_{\rm prime}(L).
\]

Every mode above

\[
n>\exp(C_\gamma+C_{\rm prime}(L))
\]

has positive tail energy. For \(C_\gamma=1\) and \(C_{\rm prime}=2\), the checker verifies positivity from mode 21 onward.

Endpoint terms are finite rank and can be included in the trial space, eliminating their pure-tail contribution.

## Interval gate

For the actual interval core, sine modes do not diagonalize the zero-extended Fourier multiplier. The required source theorem is

\[
\Gamma_L(f,f)\ge(c\log M-C_L)\lVert f\rVert_2^2
\]

on the high Dirichlet subspace. Boundary and commutator leakage must be included in \(C_L\); the periodic calculation does not bound it.

## Off-diagonal Schur gate

Suppose the finite block has lower bound \(a>0\), the tail reserve has lower bound \(d>0\), and the finite/tail coupling norm is at most \(b\). Positivity requires

\[
b^2\le ad.
\]

The checker verifies an admitted fixture and a hostile fixture with positive tail but insufficient finite pivot. Thus tail positivity alone does not close the proof.

## Disposition

Log-ellipticity supplies a viable sign-sensitive replacement for unsigned compactness on each fixed support window. It reduces positivity to finitely many modes only after two independent source estimates are proved:

1. an explicit interval logarithmic Gårding bound;
2. a finite/tail Schur budget.

The global support limit remains separate because \(C_{\rm prime}(L)\) grows as additional prime powers enter.

## Verification

- `research/voevodsky/checkers/check_log_elliptic_signed_tail_schur.py`
- `research/voevodsky/results/log_elliptic_signed_tail_schur.json`
- `research/grothendieck/archimedean-log-ellipticity-may-supply-the-missing-signed-weil-tail.md`
