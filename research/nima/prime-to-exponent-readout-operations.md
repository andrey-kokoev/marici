# Finite deck selections retain only prime-to-exponent repetition operations

Let \(G\) be a finite abelian deck group and let the physical selection be the
identity idempotent

\[
\delta_0\in\operatorname{Fun}(G,\mathbb Q).
\]

The \(n\)-fold group map induces

\[
[n]^*\delta_0(d)=\delta_0(nd).
\]

This equals \(\delta_0(d)\) for every \(d\) precisely when \([n]\) has
trivial kernel.  For finite abelian \(G\), that is equivalent to

\[
\boxed{
\gcd(n,\exp G)=1.
}
\]

Hence the maximal selection-compatible index set is

\[
\mathbb N_{(\exp G)}^\times
=\{n\ge1:\gcd(n,\exp G)=1\}.
\]

It is closed under multiplication because

\[
[m]\circ[n]=[mn],
\]

but it is generally not closed under addition.  It therefore supplies a
prime-to-torsion multiplicative operation system—not the full conditional
semiring.

For five-site cosmology,

\[
G=(C_2)^5,
\qquad \exp G=2,
\]

so exactly the positive odd indices survive the physical delta selection.

## Cross-sector interpretation

The memory invariant ring admits every linear scaling as a graded pullback,
whereas the cosmological selection admits only indices prime to its deck
torsion.  The maximal common operation set is consequently the odd
multiplicative monoid, not \(\mathbb N\) as a semiring.

This resembles the indexing restriction of prime-to-torsion Adams-style
operations, but no Adams, Frobenius, or lambda structure is claimed.  Such a
structure would require independently derived operation laws and further
coherence.

## Verification

The exact checker verifies the criterion for every cyclic group
\(C_m\), \(2\le m\le30\), through \(n=60\), and for five product groups,
including \((C_2)^5\).  It also checks multiplicative closure of every
prime-to-exponent index set in the same range.

Evidence: `research/nima/check_prime_to_exponent_readout_operations.py` and
the preceding two-sector arithmetic naturality audit.
