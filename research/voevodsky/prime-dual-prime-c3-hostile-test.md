# Prime/dual-prime C3 rotor: hostile source-geometry test

## Problem

Can two source-derived prime operations \(p,p'\) generate the three coherence phases \(1,pp',(pp')^2\) with cyclic closure?

## Bold conjecture

For distinct prime loci, there are involutive reflection-like operations \(p,p'\) on the compact-log-support test space such that the adjoint action of \(pp'\) has order three and its orbit realizes the three coherence vertices.

## Named rivals

1. source prime operations are translations, whose adjoints compose trivially rather than cyclically;
2. reflection completion makes each generator involutive, but their product is a nonperiodic translation of infinite order;
3. order three appears only after imposing an unsupported periodic quotient;
4. a spinorial central sign is mistaken for closure although the observable action itself fails to close.

## Source-derived operations

The Weil prime term acts by translation at \(\ell=\log n\). Its adjoint is translation by \(-\ell\), so the direct/adjoint pair satisfies

\[
T_\ell T_{-\ell}=1.
\]

This gives a degenerate identity, not a nontrivial \(C_3\) rotor.

The strongest nontrivial involutive completion is reflection about the prime-log midpoint:

\[
(R_\ell f)(x)=f(\ell-x),
\qquad R_\ell^2=1.
\]

For two prime logs \(\ell,m\),

\[
(R_\ell R_m f)(x)=f(x+m-\ell).
\]

Thus

\[
(R_\ell R_m)^3f(x)=f(x+3(m-\ell)).
\]

On the separating probe \(f(x)=e^x\), with \(\ell=\log2\), \(m=\log3\), the ratio is

\[
\frac{(R_{\log2}R_{\log3})^3f(x)}{f(x)}
=e^{3\log(3/2)}=\frac{27}{8}\neq1.
\]

## Strongest falsification attempt

The checker verifies both involution identities exactly and computes the rational obstruction \(27/8-1=19/8\). A deliberate equal-prime control \(\ell=m\) closes trivially and is rejected as a three-phase realization.

## Disposition and scope correction

This falsifier applies only to the interpretation in which \(p'\) is the adjoint or reflected prime-translation operation. The operator subsequently clarified that \(p'\) means the prime-derived next level of the realization ladder, plausibly the spectral realization. Under that intended typing, \(p\) and \(p'\) are not two endomorphisms of one test space, so the reflection calculation does not test the proposal. It is retained as a conditional countermodel against the adjoint reading, not as a refutation of the realization-ladder conjecture.

For the intended reading, multiplication \(pp'\) must first be replaced by a typed composition through arithmetic and spectral objects; its square must be typed as a quadratic/Gram or coherence construction rather than assumed to be ordinary operator squaring.

## Verification

- `research/voevodsky/checkers/check_prime_dual_prime_c3.py`
- `research/voevodsky/results/prime_dual_prime_c3.json`
