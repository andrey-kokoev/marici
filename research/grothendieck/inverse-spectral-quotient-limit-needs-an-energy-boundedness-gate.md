# The inverse spectral-quotient limit needs an energy-boundedness gate

## Question

Does the correctly oriented inverse system of finite spectral quotients recover the completed Weil form domain automatically?

## Counterexample

Let `V=c_00`, the finitely supported sequences, and let

`R_N={x in c_00 : x_1=...=x_N=0}`.

Then `R_(N+1) subset R_N`, and

`V/R_N` is naturally the space of the first `N` coordinates. The canonical inverse maps forget the last coordinate. Consequently

`inverse_limit_N V/R_N = product_(n>=1) C`.

But

`intersection_N R_N=0`,

so

`V/(intersection_N R_N)=c_00`,

which is strictly smaller than the inverse limit. A compatible family of all-one prefixes belongs to the inverse limit but is not represented by any vector of `c_00`. It is also not in the Hilbert completion `ell^2`.

Thus inverse compatibility alone creates phantom families.

## Energy-bounded sublimit

Equip the finite quotient with the partial energy

`E_N(x)=sum_(n<=N) lambda_n |x_n|^2`,

where every `lambda_n>0`. Then the bounded-energy sublimit

`{(x^(N)) compatible : sup_N E_N(x^(N))<infinity}`

is canonically the weighted Hilbert space

`ell^2(lambda)={x : sum_n lambda_n |x_n|^2<infinity}`.

Monotone convergence proves both directions. The energy bound removes the all-one phantom when the weighted sum diverges.

## Weil implication

For spectral-cutoff quotients, the projective limit must be restricted by a completed form norm or graph norm. Bare compatibility of finite Gram classes is insufficient. A valid completion theorem needs:

1. monotone or otherwise coherent cutoff energies on one common core;
2. a uniform boundedness condition defining admissible compatible families;
3. proof that every bounded family is represented in the closure of the core;
4. identification of zero-energy families with the completed radical;
5. independence from the chosen cutoff exhaustion.

The current Gaussian rectangles provide finite energies but not a source-derived global positive norm, since positivity of the completed Weil form is the RH-bearing assertion. Therefore the boundedness gate cannot be filled by declaring the Weil energy positive.

## Contact with Voevodsky's completion theorem

Voevodsky's closed-form domain is exactly the missing boundedness structure. His common-core and closability requirements prevent replacement of a form completion by the unrestricted categorical inverse limit. The reduced-minimum-modulus and limiting-radical countermodels remain relevant after the quotient variance is corrected.

## Cheapest falsifier

Given a proposed inverse-limit realization, exhibit a compatible family whose finite energies diverge or whose norm depends on the cutoff exhaustion. Such a family disproves identification with the completed Hilbert quotient without challenging any finite-stage positivity.

## Disposition

The bare inverse quotient system is rejected as a completion. The surviving construction is its energy-bounded sublimit, conditional on a source-derived closable form norm. This returns the problem to the central arithmetic positivity gate rather than bypassing it categorically.
