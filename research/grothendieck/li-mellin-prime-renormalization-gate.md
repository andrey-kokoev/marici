# Mellin transport exposes a necessarily renormalized prime sum

## Exact inverse Mellin kernels

For `k>=1`, define

`Phi_k(x)=(-log x)^(k-1)/(k-1)!` for `0<x<1`,

and

`Phi_k(x)=x^(-1)(log x)^(k-1)/(k-1)!` for `x>1`.

Then, in the fundamental strip `0<Re(s)<1`,

`integral_0^infinity Phi_k(x)x^(s-1)dx`

` =s^(-k)+(1-s)^(-k)`.

The kernel obeys the multiplicative reflection law

`Phi_k(1/x)=x Phi_k(x)`.

This is the exact Mellin image of the canonical symmetric principal-part
basis.

## Prime-side divergence

For integer `n>1`,

`Phi_k(n)=n^(-1)(log n)^(k-1)/(k-1)!`.

The formal prime-power contribution therefore contains

`sum_n Lambda(n) n^(-1)(log n)^(k-1)/(k-1)!`,

which is not convergent. Under the prime number theorem, its cutoff through
`X` has leading growth `(log X)^k/k!` (with the same statement at `k=1`).

Thus transporting the endpoint jets does not produce an independently
defined positive prime series. The contour transport must provide a
canonical subtraction of this polynomial logarithmic divergence, coupled to
the pole and archimedean terms.

## Required renormalized source formula

For each basis index `k`, derive a finite limit of the form

`C_k = lim_(X->infinity) [P_k(X)+G_k(X)+Q_k(X)]`,

where:

- `P_k(X)` is the truncated von Mangoldt sum;
- `G_k(X)` is the gamma/archimedean contribution under the same cutoff;
- `Q_k(X)` is the endpoint/pole counterterm forced by contour transport.

The combined limit must equal the fixed completed-xi jet value
`-ell_(k-1)`. None of the three summands is separately canonical after the
cutoff is removed.

For a polynomial `p`, the energy is then

`E(p)=sum_k A_k(p) C_k`.

The subtraction scheme must be independent of `p` and compatible across all
`k`; otherwise it reintroduces the forbidden rank-dependent freedom.

## Positivity target

The plausible universal coupled positivity theorem must act on the combined
renormalized functional. The isolated prime sector is both indefinite and
divergent, so assigning it a positive Gram interpretation is ruled out twice.

## Falsifiers

- Treating the raw von Mangoldt series as convergent.
- Subtracting only its leading term without deriving the full contour
  completion.
- Choosing different cutoffs for prime and gamma contributions.
- A subtraction depending on `p` rather than only on the universal basis
  index and common transport.
- Failure of the combined limit to reproduce a completed-xi jet.
