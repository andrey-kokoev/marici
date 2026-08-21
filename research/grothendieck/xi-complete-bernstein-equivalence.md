# The centered squared xi logarithm should be a complete Bernstein function

## Definition

Let

`B(x)=log[xi(1/2+sqrt(x))/xi(1/2)]`.

Evenness of completed xi in the centered coordinate makes this a
single-valued analytic germ in `x`. Its derivative is exactly the squared
Stieltjes target:

`B'(x)=S(x)`

`     =[xi'/xi(1/2+sqrt(x))]/[2sqrt(x)]`.

## RH representation

Under RH, the paired Hadamard product gives

`B(x)=sum_(gamma>0) m_gamma log(1+x/gamma^2)`.

Each summand is a complete Bernstein function. Its derivative is the
Stieltjes atom `1/(x+gamma^2)`.

Equivalently, Frullani's formula gives

`log(1+x/gamma^2)`

` =integral_0^infinity (1-exp(-xt))exp(-gamma^2t) dt/t`.

Therefore

`B(x)=integral_0^infinity (1-exp(-xt))Theta(t) dt/t`,

where `Theta(t)=sum m_gamma exp(-gamma^2t)` is the positive heat trace.

## Equivalence target

With the completed analytic continuation, growth, and normalization fixed,
RH is equivalent to `B` being a complete Bernstein function whose meromorphic
Stieltjes derivative has positive integer residues. The implications are:

- complete Bernstein `B` gives Stieltjes `B'`;
- the Stieltjes pole locus puts squared zeros on the negative real axis;
- pulling back by `x=(s-1/2)^2` gives the critical line;
- residues recover divisor multiplicity.

## Unified explanation

One function now carries every requested readout:

- `B` is the completed determinant logarithm;
- `B'` is the squared resolvent trace;
- its Lévy density is `Theta(t)/t`;
- its Stieltjes measure is the squared spectral measure;
- Möbius transport of that measure gives Li Toeplitz moments;
- the associated multiplication operator gives the conditional
  Hilbert--Pólya spectrum.

This is more rigid than asking separately for positivity, heat flow, and an
operator.

## Hostile-factor rejection

An off-line quartet introduces logarithmic factors with branch/pole data at
`x=a^2` and `x=conjugate(a)^2`, rather than on the negative real axis. Its
derivative is not a Stieltjes function of the admitted type, so the complete
Bernstein property rejects it.

## Source-side attack

Prove directly from the completed arithmetic factorization that `B` has a
positive Lévy--Khintchine representation. The representation must be derived
without using zero locations and must reproduce:

1. the Abel-renormalized prime germ;
2. the archimedean and endpoint completion;
3. the logarithmic heat Weyl law;
4. positive integer spectral residues.

The central missing object is a source-positive Lévy density whose Laplace
transform is `B'`.

This is an RH-equivalent conjecture, not an RH proof.
