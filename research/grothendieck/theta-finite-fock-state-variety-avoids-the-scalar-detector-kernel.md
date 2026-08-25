# Theta finite Fock state variety avoids the scalar detector kernel

## Generic coefficient kernels are not automatically admissible states

Packets 180 and 183 exhibit nonzero coefficient packets annihilated by a
scalar endpoint or fixed Mellin detector.  Those witnesses live in the full
linear coefficient module.  The distinguished Euler source occupies a much
smaller nonlinear subset fixed by positive Fock formation.

The RH detector must be tested on that source-admissible state variety before
generic linear kernels are promoted to physical counterexamples.

## Finite-prime Fock state

For a finite prime set `S`, the unramified local occupation state at `p` is

\[
 \Omega_{p,s}
 =\sum_{k\ge0}p^{-ks}e_{p,k}.
\]

The global finite-prime state is the rank-one tensor

\[
 \boxed{
 \Omega_{S,s}
 =\bigotimes_{p\in S}\Omega_{p,s}.}
\]

In the integer-labelled chart its coefficients obey

\[
 c_{mn}=c_mc_n
 \qquad((m,n)=1)
\]

and

\[
 c_{p^k}=c_p^k.
\]

Thus admissibility is a multiplicative Segre/Fock condition, not arbitrary
membership in a vector space.

## Finite detector nonvanishing

The finite Euler detector factorizes:

\[
 \mathcal Z_S(s)
 =\prod_{p\in S}\sum_{k\ge0}p^{-ks}
 =\prod_{p\in S}{1\over1-p^{-s}}.
\]

Every factor is nonzero wherever it is finite. Therefore

\[
 \boxed{
 \mathcal Z_S(s)\ne0
 \quad\text{for every finite }S}
\]

away from the declared local pole lattice.

The scalar detector is unfaithful on the ambient coefficient module but has
no zero on the distinguished finite Fock-state variety.

## Why the two-label witness is unauthorized

An isolated two-label packet

\[
 c=ae_m+be_n,
 \qquad ab\ne0,
\]

with all other occupation coefficients zero is generally not closed under
Fock multiplication.  If `m` and `n` contain coprime occupied prime content,
multiplicativity forces the `mn` coefficient `ab`; repeated occupation forces
the associated prime-power tower as well.

Hence the two-label cancellation in packet 183 is a valid detector-kernel
witness but not a source-admissible finite Euler state.  It disproves a theorem
on the whole coefficient module, not a theorem restricted to the distinguished
Fock variety.

## Tangent directions versus states

Linear coefficient differences remain legitimate tangent vectors, response
directions, and hostile perturbations.  Their detector kernels matter for
stability and for any claimed linear determinant--kernel bridge.  But a
vanishing tangent readout is not itself a vanishing physical state.

The typing distinction is:

\[
 \boxed{
 \text{ambient linear kernel}
 \ne
 \text{intersection of the kernel with the source-state variety}.}
\]

## Completion is again the only possible crossing

Every finite Fock state avoids the scalar kernel.  A nontrivial zero can enter
only if the restricted-product/Poisson completion of these nonvanishing states
meets the detector-null divisor.

The exact object is therefore the completed image

\[
 \overline{\{\Omega_{S,s}:S\text{ finite}\}}^{\rm source}
\]

inside the boundary-bearing two-sector carrier.  RH asks whether its
off-seam part remains disjoint from the distinguished detector-null divisor.

This is stronger and better typed than asking for injectivity on the whole
coefficient Hilbert space.

## Deutsch--Popperian target

Construct, using only authorized Fock formation and Poisson sewing, an
off-seam limit point

\[
 \Omega_s\in\ker\ell_s.
\]

The conjecture is that this task is impossible.  Its smallest falsifier is a
completion-compatible finite-prime net whose full boundary-bearing states
converge while their distinguished detector values tend to zero at one fixed
off-seam `s`.

Scalar partial Euler products in a changing trivialization do not constitute
such a net.

## Scope

This packet proves finite-prime nonvanishing and rejects generic sparse
coefficient kernels as source-state witnesses.  It does not prove that the
completed Fock variety remains disjoint from the detector divisor; that is the
remaining RH-equivalent transversality problem.
