# A positive archimedean summand cannot repair prime-product disjointness

## 1. One-particle divergence

For the prime geometric vacuum,

\[
  \Omega_p
  =
  \sqrt{1-r_p}
  \sum_{a\ge0}r_p^{a/2}e_a,
\]

the leading transported difference is

\[
  (U_{p,\theta_p}-I)\Omega_p
  =
  r_p^{1/2}(e^{-i\theta_p}-1)e_1
  +O(r_p).
\]

In the reference infinite tensor product, one-prime excitations for distinct
primes are mutually orthogonal. Hence the leading global norm is

\[
  \sum_p
  r_p|e^{-i\theta_p}-1|^2
  +\text{higher occupation terms}.
\]

At critical half-density \(r_p=p^{-1/2}\), this is the previously identified
implementability obstruction.

## 2. Positive enlargement no-go

Suppose one appends an independent archimedean Hilbert sector
\(\mathcal K_\infty\) and a repair vector \(h_\infty\). In the orthogonal
direct sum,

\[
  \left\|
  \bigoplus_p h_p\oplus h_\infty
  \right\|^2
  =
  \sum_p\|h_p\|^2+\|h_\infty\|^2.
\]

If the prime sum diverges, the enlarged norm still diverges. More generally,
an isometric embedding of the prime one-particle space into any larger
positive Hilbert space preserves the divergent norm.

\[
\boxed{
\text{an independent positive gamma/endpoint sector cannot cancel
orthogonal prime divergence}.}
\]

Adding positive degrees of freedom cannot subtract a positive infinite
energy.

## 3. Consequence for completion

The familiar scalar factorization

\[
  \xi(s)
  =
  \text{endpoint}\times\Gamma\text{-factor}\times\zeta(s)
\]

must not be read as an orthogonal tensor product of three positive operator
sectors. Such a product cannot restore implementability of the critical
prime transport.

The operator completion must instead do at least one of:

1. introduce cross-place inner products;
2. quotient a source-derived null/degree direction;
3. use a relative or indefinite form before taking a positive quotient; or
4. change to a non-product representation in which prime excitations are not
   orthogonal.

This is the precise sense in which completion changes the admissible space
first.

## 4. Product-formula covariance, not yet a null vector

The logarithmic place vector satisfies

\[
  \sum_v\log|q|_v=0.
\]

It supplies the source-derived charge covector

\[
  \varepsilon((x_v)_v)=\sum_vx_v,
\]

and says that rational displacement vectors lie in

\[
  \ker\varepsilon.
\]

It does **not** supply a canonical vector representing the normal direction
to this hyperplane. Turning \(\varepsilon\) into a vector requires a metric,
which is precisely the missing cross-place datum.

\[
\boxed{
\text{the product formula selects a charge constraint,
not a null vector or quotient metric}.}
\]

Declaring a shared degree vector null after observing divergence would
therefore be circular.

## 5. Minimal uniqueness gate

Let \(V_{\mathrm{alg}}\) be the finite-support place-current space. Derive a
sesquilinear form

\[
  \langle\cdot,\cdot\rangle_{\mathrm{comp}}
\]

directly from the completed theta/Poisson source such that:

1. it includes finite-prime Fock currents;
2. rational displacement currents lie in the charge-zero subspace
   \(\ker\varepsilon\);
3. its radical, if nonzero, is derived independently and the quotient is
   positive;
4. rational and Fourier transport descend isometrically; and
5. its Hilbert completion is independent of prime exhaustion.

If these properties determine the form up to a scalar unitary equivalence,
the relative representation is source-selected.

## 6. Falsifiers

The programme fails if:

1. a supposed degree radical is obtained by silently identifying the charge
   covector with a vector;
2. quotient positivity requires zero information;
3. multiple inequivalent cross-place forms satisfy the same source laws;
4. prime transport remains nonimplementable after quotient; or
5. the theta overlap is inserted only after the representation is chosen.

## 7. Scope

Orthogonality of one-prime excitations and the positive-enlargement no-go are
exact. They rule out a naïve tensor-product interpretation of archimedean
repair. No source-derived cross-place form, positive quotient, unique
relative representation, or RH result is constructed.
