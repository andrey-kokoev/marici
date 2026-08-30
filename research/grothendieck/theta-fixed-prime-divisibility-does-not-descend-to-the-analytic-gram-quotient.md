# Fixed-prime divisibility does not descend to the analytic theta Gram quotient

## Deutsch discriminator

The analytic Gram kernel makes adjacent labels asymptotically indistinguishable:

\[
 \lVert e_{n+1}-e_n\rVert_K^2
 =2\left[A(0)-A\!\left(\log(1+1/n)\right)\right]\longrightarrow0.
\]

Test this quotient against an independently authorized arithmetic constructor.

## Fixed-prime valuation projector

For a fixed prime `p`, define

\[
 \boxed{P_pe_n=\mathbf1_{p\mid n}e_n.}
\]

This projector is source-derived: the theta prime-scale recursion separates
labels divisible by `p` from the `p`-free remainder, and the positive Fock
grammar retains `v_p(n)`.

## Exact discontinuity witness

Take

\[
 x_k=e_{pk+1}-e_{pk}.
\]

Since `log(pk+1)-log(pk)->0`,

\[
 \lVert x_k\rVert_K\longrightarrow0.
\]

But `pk` is divisible by `p` and `pk+1` is not, so

\[
 P_px_k=-e_{pk},
 \qquad
 \boxed{\lVert P_px_k\rVert_K^2=A(0)>0.}
\]

Therefore

\[
 \boxed{P_p\text{ is discontinuous in the analytic Gram topology}.}
\]

It cannot descend to the completion determined only by
`K(n,m)=A(|log(n/m)|)`.

## Consequence

The pure analytic redundant-frame model erases source-relevant information.
The completed object needs at least

\[
 \boxed{
 \text{analytic tail--seam Gram state}
 +\text{discrete valuation/type register}.}
\]

The minimal discrete port need not be an orthogonal basis indexed by every
integer. It may be the prime-valuation/Fock module from which all `P_p` arise.

## Mellin compatibility

Mellin characters commute with fixed-prime divisibility:

\[
 M_tP_p=P_pM_t,
\]

because both are diagonal on integer labels. Thus the valuation port restores
lost arithmetic information without obstructing vertical transport.

## Minimal mixed topology gate

For a proposed valuation/Fock port `V`, the combined map

\[
 c\longmapsto(Uc,Vc)
\]

must make every `P_p` continuous, retain unitary Mellin action, support finite
Euler cutoff convergence, and couple to declared Green/boundary currents. An
unused orthogonal label register added solely to force a norm is inadmissible.

The same witness applies to prime-power type, the `p`-free projector, and any
nonconstant bounded function of `v_p(n)`.

## Typed disposition

```json
{
  "code": "authorized_prime_projector_discontinuous_in_analytic_gram",
  "constructor": "P_p e_n = 1_(p divides n) e_n",
  "witness": "x_k=e_(pk+1)-e_(pk)",
  "input_gram_norm": "tends to zero",
  "output_gram_norm_squared": "A(0)",
  "pure_analytic_quotient": "rejected",
  "discrete_valuation_port": "required"
}
```

## Honest frontier

Neither a pure diagonal label Hilbert space nor a pure analytic Gram quotient
is sufficient. The source requires a mixed object carrying continuous
tail--seam geometry and discrete prime-valuation information. The next
construction is the minimal positive Fock/valuation port and its coupling to
the full Green system.

