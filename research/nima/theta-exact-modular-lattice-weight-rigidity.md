# Exact modular lattice duality rigidly selects the weights

## Result

Finite reciprocal-seam jets cannot determine positive square-mode weights.
The full distributional modular law can.

Let

\[
\mu=\sum_{n\in\mathbb Z}a_n\delta_n
\]

be a tempered measure supported on the integer lattice. Suppose its Fourier
transform is an order-zero measure, rather than a distribution with
derivative atoms, and is supported on the dual integer lattice:

\[
\operatorname{supp}\widehat\mu\subseteq\mathbb Z.
\]

Then the weights \(a_n\) are constant. The same conclusion holds under the
stronger source condition of exact Fourier self-duality. If the self-dual
normalization is fixed, \(\mu\) is the standard Dirac comb.

## Proof

Because \(\widehat\mu\) is an order-zero measure supported on integers,

\[
e^{-2\pi i\xi}\widehat\mu(\xi)=\widehat\mu(\xi)
\]

as measures, hence as distributions. Fourier inversion converts multiplication by
\(e^{-2\pi i\xi}\) into translation by one:

\[
\tau_1\mu=\mu.
\]

But

\[
\tau_1\mu
=\sum_{n\in\mathbb Z}a_n\delta_{n+1}
=\sum_{n\in\mathbb Z}a_{n-1}\delta_n.
\]

Uniqueness of the coefficients of the point masses gives

\[
a_n=a_{n-1}\qquad\text{for every }n.
\]

Hence all weights are equal.

The converse is Poisson summation: the constant-weight integer comb is
Fourier self-dual under the standard normalization.

The order-zero qualification is essential. Mere distributional support is
not enough: polynomially varying lattice weights can transform into
derivatives of the dual comb. A smooth multiplier that vanishes on the
support does not annihilate derivative delta distributions. Such sources are
excluded by the measure-valued dual law and, a fortiori, by exact
self-duality of the theta comb.

## Typed interpretation

The rigidity uses the complete support statement in Fourier space, not a
finite list of derivatives at the reciprocal seam. It is an infinite,
source-authorized coherence law:

\[
\text{integer support}
+\text{dual integer measure support}
\Longrightarrow
\text{translation invariance}
\Longrightarrow
\text{constant weights}.
\]

Any nonconstant weight perturbation that remains inside the order-zero dual
class necessarily leaks Fourier mass outside the dual lattice. A perturbation
may avoid leakage only by producing forbidden derivative atoms. Thus the
finite conceptual falsifier is: find either a nonintegral dual frequency or
a positive-order dual atom.

## Finite cyclic model

On \(\mathbb Z/N\mathbb Z\), take a subgroup \(H\). A vector supported on
\(H\) whose discrete Fourier transform is supported on the annihilator
\(H^\perp\) is constant on \(H\). For \(N=8\) and

\[
H=\{0,2,4,6\},
\]

the annihilator is \(\{0,4\}\). Equal weights on \(H\) have Fourier support
exactly there. Perturbing one weight while preserving positivity creates
nonzero Fourier coefficients outside \(\{0,4\}\).

This finite model verifies the support-rigidity mechanism without pretending
to prove the infinite Poisson theorem computationally.

## Consequence for the RH lane

Within the lattice-comb source class, exact modular duality does select the
standard primitive weights. This is stronger than the finite-jet no-go and
explains why arbitrary positive weight perturbations are not faithful theta
sources.

But the result is a constructibility theorem:

\[
\text{full modularity selects which source exists}.
\]

It does not prove

\[
\partial_y|X(x+iy)|^2>0.
\]

Indeed the selected source is precisely the completed theta/Xi source for
which that normal-current inequality is RH-equivalent. Weight rigidity
removes hostile coefficient freedom without supplying the missing
two-copy orientation.

## Durable three-layer conclusion

1. **Integrality:** forces all-order labelled spectral sign regularity.
2. **Exact modular duality:** rigidly selects the constant lattice weights.
3. **Normal-current orientation:** remains a separate global interaction
   law and is not implied by the first two results.

This is the sharpest form of the source-grammar versus completed-interaction
separation in the theta programme.

