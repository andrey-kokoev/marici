# Common-core density reduces to Gaussian injectivity on the form dual

## Question

Can simultaneous endpoint--gamma density be proved without separately approximating in two incompatible norms?

## Combined form space

Let `H_W` be the intersection domain with inner product obtained by summing:

- the base `L^2` norm;
- the gamma logarithmic form norm on the spectral side;
- the two-sided exponential endpoint norm on the Fourier side;
- the bounded fixed-width prime-row norm.

Let `T` denote the positive form operator formally associated with this sum, so that

\[
\langle f,h\rangle_{H_W}
=
\langle Tf,h\rangle
\]

in the dual pairing between the form domain and its continuous dual.

## Orthogonality reduction

Suppose `f in H_W` is orthogonal in the combined graph norm to every real translate of the fixed Gaussian:

\[
\langle f,\tau_ag_\sigma\rangle_{H_W}=0
\qquad\text{for every }a.
\]

Equivalently, the dual element `Tf` annihilates every Gaussian translate. This says

\[
(Tf)*\widetilde g_\sigma=0
\]

as a function or generalized function of the translate parameter.

If Gaussian convolution is injective on the actual form dual `H_W'`, then `Tf=0`. Pairing with `f` gives

\[
\|f\|_{H_W}^2=0,
\]

so `f=0`. Hahn--Banach then implies that the Gaussian translate span is dense in the simultaneous graph norm.

## Exact remaining theorem

On tempered distributions, Gaussian convolution is injective because its Fourier multiplier never vanishes. The endpoint exponential topology may enlarge the dual beyond tempered distributions. Division by the rapidly decaying Gaussian multiplier can fail to preserve that larger generalized-function class.

Therefore the missing statement is not ordinary Fourier injectivity but:

> Gaussian convolution is injective on the dual of the chosen endpoint--gamma form domain.

A Gelfand--Shilov test space is a plausible setting because Gaussian convolution and Fourier transform are native there, but the exact indices must accommodate the endpoint exponential weights and gamma logarithmic multiplier simultaneously.

## Correction to the bounded-endpoint shortcut

Endpoint rows cannot be declared bounded merely because point evaluation is bounded in an abstract Fock space. The actual endpoint functional must be intertwined with a Fock kernel vector. Without that map, adjoining the endpoint row can change the graph topology and invalidate a gamma-only core proof.

## Disposition

Simultaneous core density reduces to one dual uniqueness theorem. Prove Gaussian-convolution injectivity on the selected form dual, and the common-core result follows directly from orthogonality. Failure of injectivity would exhibit an invisible dual residual missed by every translate observer.
