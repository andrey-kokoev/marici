# Naturals carry a symmetric--exterior prime-index calculus

## Question

What algebra incorporates both arbitrary prime multiplicities and the exterior orientation of distinct shell directions?

## Claim boundary

Prime valuations form a bosonic symmetric algebra, while oriented sets of distinct shell moves form an exterior algebra. Their tensor product supports creation, annihilation, transfer, cubical boundary, and probe-induced Clifford operations. “Bosonic” and “fermionic” here name algebraic commutation laws; no physical particle interpretation is asserted.

## Symmetric prime-valuation algebra

Let \(F\) have basis \(f_i\) indexed by primes. The monomial algebra

\[
\operatorname{Sym}(F)=k[x_1,x_2,\ldots]
\]

has basis

\[
x^D=\prod_i x_i^{d_i}
\]

for finite effective divisors \(D=(d_i)\). Under

\[
N=\prod_i p_i^{d_i}
\longleftrightarrow x^D,
\]

multiplication of monomials is multiplication of natural numbers. Arbitrary powers of a prime are symmetric occupation multiplicities rather than additional exterior directions.

Define creation and annihilation operators

\[
a_i^\dagger(x^D)=x^{D+f_i},
\qquad
a_i(x^D)=d_i x^{D-f_i}.
\]

They satisfy the Weyl relations

\[
[a_i,a_j^\dagger]=\delta_{ij},
\qquad
[a_i,a_j]=[a_i^\dagger,a_j^\dagger]=0.
\]

## Prime-transfer operators

The multiplicity-weighted transfer from \(p_i\) to \(p_j\) is

\[
E_{ji}=a_j^\dagger a_i.
\]

These operators satisfy

\[
[E_{ab},E_{cd}]
=
\delta_{bc}E_{ad}-
\delta_{ad}E_{cb},
\]

the finitary \(\mathfrak{gl}\)-relations on prime-index modes.

Adjacent-shell transfers are

\[
E_i=E_{i+1,i}.
\]

Disjoint adjacent transfers commute. Neighboring transfers obey

\[
[E_i,E_{i+1}]=-E_{i+2,i},
\]

so their operator commutator detects the direct two-index transfer skipped by the adjacent presentation. This does not contradict commutative subset vertices when both partial moves are admissible: the weighted operators also record multiplicity and enabling changes.

## Exterior shell algebra

Let \(W\) have basis \(e_i\) indexed by adjacent shells. The exterior algebra

\[
\Lambda(W)
\]

records oriented families of distinct directions. Its creation and contraction operators satisfy

\[
\varepsilon_i\varepsilon_j+
\varepsilon_j\varepsilon_i=0,
\qquad
\iota_i\varepsilon_j+
\varepsilon_j\iota_i=
\delta_{ij}.
\]

The combined state-and-direction object is

\[
\mathcal K=
\operatorname{Sym}(F)\otimes\Lambda(W).
\]

On admissible divisor cells, the cubical differential is the partial Koszul operator

\[
\partial=
\sum_i(\tau_i-1)\iota_i,
\]

while the probe-induced Clifford action is

\[
c_i=
\varepsilon_i+
\sum_jQ_{ij}\iota_j.
\]

Thus symmetric degree counts prime multiplicity, exterior degree counts distinct oriented shell directions, and arithmetic height reads the symmetric monomial.

## Repeated same-shell moves

Two chips at prime site \(i\) permit two successive applications of the same shell transfer. Their direction label is a multiplicity-two symmetric operation, not

\[
e_i\wedge e_i,
\]

which vanishes. A labelled-chip cover separates the two moves into distinct coordinate directions; quotienting by label permutations returns divided-power multiplicity data. Therefore repeated shell motion belongs to the symmetric or divided-power part of the calculus, while Boolean cubes of distinct shell indices belong to the exterior part.

## Geometric meaning

The arithmetic geometry is not purely Clifford. It is a mixed symmetric--exterior calculus:

- \(\operatorname{Sym}(F)\) stores natural-number prime content;
- \(\Lambda(W)\) stores cubical direction and orientation;
- the type-\(A\) Cartan form compares adjacent transfers;
- the Hankel form measures probe distinguishability;
- the height covector assigns prime magnitude.

This resolves why natural numbers admit unbounded prime powers while each Boolean shell direction appears at most once in an oriented cube label.

## Strongest falsification attempt

On a bounded family of valuation monomials, verify all creation--annihilation commutators and the matrix-unit commutator formula. Check that disjoint adjacent transfers commute and neighboring ones produce the signed two-step transfer. Verify that two same-shell transfers act nontrivially on multiplicity-two states while the corresponding exterior square vanishes. Retain the coefficient difference between labelled and unlabelled chips rather than absorbing it.

## Disposition

The natural-number geometry is best modeled by \(\operatorname{Sym}(F)\otimes\Lambda(W)\), with a divided-power refinement for indistinguishable repeated moves. Clifford algebra governs the exterior probe geometry; the symmetric algebra carries the prime multiplicities on which those directions act.
