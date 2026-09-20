# Xi-torsion lift iteration 9: the mixed p-minus-three-halves loading has no Bohr recovery strip at the seam, while the superexponential loading would

## Authority audit

The arithmetic assembly theorem lists two analytically admissible loadings:

\[
\omega_p^{\rm mix}(\sigma)
=\frac12p^{-3/2-\sigma}
\]

and the source Euler--theta coefficient

\[
c_p
=2(\log p)\sum_{k\ge1}p^{-k/2}\Phi'(k\log p),
\]

which has superexponential prime-power decay. It explicitly states that no
current interface selects which one is the canonical G4/bordered loading.

The independent-defect packet refers to “frozen prime weights” without fixing
that choice. Therefore objective 2 cannot yet be assigned one numerical strip
budget from the source record.

## Mixed-loading budget

For the outgoing endpoint frequency `b_p=log q(p)~log p`, the mixed model is

\[
G(z)
=\sum_p\frac12p^{-3/2-\sigma}e^{zb_p}.
\]

Absolute convergence holds for

\[
\operatorname{Re}z<A,
\qquad A=\frac12+\sigma.
\]

Bohr extraction on `z=R+it` gives

\[
|d_p|e^{Rb_p}\le S_R(G).
\]

To control the weighted `ell^1` seminorm

\[
q_\delta(d)=\sum_p|d_p|e^{\delta\log p},
\]

this coefficientwise estimate yields the numerical majorant

\[
q_\delta(d)
\lesssim
S_R(G)\sum_pp^{-(R-\delta)}.
\]

The prime sum requires

\[
R-\delta>1.
\]

At the same time the observer line must satisfy

\[
R<A=\frac12+\sigma.
\]

Hence a recovery line exists only if

\[
\delta+1<\frac12+\sigma,
\qquad\text{i.e.}\qquad
\sigma>\delta+\frac12.
\]

At the seam `sigma=0` this is impossible, even for `delta=0`. Thus the mixed
`p^(-3/2)` assembly is absolutely convergent but its raw vertical-line sup norm
does not continuously recover the coefficient `ell^1` topology.

This is the same distinction as injectivity versus stable reconstruction.

## Superexponential-loading budget

For `c_p`, completed-theta decay beats every `e^(delta log p)` weight. The
endpoint exponential sum is entire with all weighted coefficient moments.
Arbitrarily large observer lines are available, so the Bohr recovery estimate
closes for every `q_delta`.

Therefore the superexponential Euler--theta loading does place the bordered
endpoint packet in the all-order Fourier-recoverable Köthe range.

## Consequence

There is a sharp coefficient-dependent fork:

- **If the canonical independent bordered assembly uses `c_p`:** objectives
  1--3 can use the all-order strict horizontal graph argument.
- **If it uses `omega_p^mix`:** the proposed `ell^1` Bohr graph is not strict at
  the seam; a weaker coefficient topology or a stronger observer is needed.
- **Without coefficient selection:** membership of `H_border` in either range
  is not a typed theorem.

## Why changing the topology is delicate

One can define a graph norm that includes the coefficient `ell^1` norm by
fiat, but it will not descend continuously from the unlabelled bordered packet
under the mixed loading. Alternatively, an `ell^infinity` coefficient topology
is controlled by Bohr extraction, but it is too weak to justify the arithmetic
sum and cutoff completion.

## Next gate

First determine the actual loading of the independently assembled
`H_border`. If the mixed loading is mandatory, search for a stronger
source-derived observer—such as an `L^2` mean-square Bohr norm with a weighted
large-sieve estimate—rather than another vertical-line sup estimate.