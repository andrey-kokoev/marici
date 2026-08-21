# Arbitrary finite-kernel monodromy spectrum

## Complete theorem

Let a finite group `H` act on an arbitrary finite group `K` through
`rho:H->Aut(K)`, let `M=im(rho)`, and form `K semidirect H -> H`.  The
`n`-th power correspondence commutes with every coefficient fiber sum and
basis-level fiber lift if and only if

`gcd(n,exp(K)*exp(M))=1`.

Neither the kernel nor the quotient action image is required to be abelian.

## Sufficiency

Fix a fiber whose action is `alpha in M`, of order `d`.  If `n` is coprime
to `exp(K)*exp(M)`, it is coprime to the exponent of
`K semidirect <alpha>` and to `d`.  The global `n`-th power map on this
cyclic semidirect product and the quotient power map on `<alpha>` are both
permutations.  Their restriction makes the twisted word map on the chosen
fiber bijective.  This argument depends only on the visible action, so
invisible factors in `H` are irrelevant.

## Necessity

If a prime `p` divides both `n` and `exp(K)`, the identity fiber fails by the
finite-group power-permutation theorem.

If `p` divides both `n` and `exp(M)`, choose a nontrivial action element
`alpha` of order `p`.  For any `x` moved by `alpha`, put

`k=x^{-1} alpha(x) != 1`.

Its twisted norm on the `alpha` fiber telescopes:

`k alpha(k) ... alpha^(n-1)(k) = x^{-1} alpha^n(x) = 1`,

because `p` divides `n`.  Thus `k` and the identity have the same image, so
that fiber is not bijective.

## Consequence

The conjecture left open in Ledgers 1275 and 1277 is proved.  The complete
survivor spectrum for arbitrary finite semidirect kernels is controlled by
the kernel exponent and the visible monodromy exponent.  For nonabelian total
groups this remains a basis-level power correspondence, not generally a ring
Adams operation.  No physical relative-chain pushforward follows.

## Verification basis

The proof is exact.  Existing hostile controls comprise the `S3`, `D8`, and
`Q8` complete automorphism sweep (71,664 checks), the quaternion `C3` action
(13,824 checks), and all earlier abelian-kernel spectra.
