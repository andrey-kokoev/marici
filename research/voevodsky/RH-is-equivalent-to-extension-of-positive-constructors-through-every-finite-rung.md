# RH is equivalent to extension of positive constructors through every finite rung

## Positive rung constructor

Fix a Gaussian width and the source-derived Hermitian translate kernel \(K(a,b)\).

For a finite translate packet

\[
A=(a_1,\ldots,a_n),
\]

a positive constructor consists of a Hilbert space \(H_A\) and vectors

\[
v_{A,1},\ldots,v_{A,n}
\]

such that

\[
\langle v_{A,i},v_{A,j}\rangle
=K(a_i,a_j).
\]

Constructors are coherent when packet permutations act by the corresponding vector permutations and packet inclusions induce isometries carrying old vectors to old vectors.

## All-rung theorem

The following are equivalent:

1. every finite translate packet admits a coherent positive constructor;
2. every finite Gram matrix \([K(a_i,a_j)]\) is positive semidefinite;
3. the Gaussian translate kernel is positive definite.

A constructor makes its Gram matrix positive. Conversely, positive definiteness gives the canonical reproducing-kernel Hilbert space, whose finite vector spans provide all constructors and all coherence maps simultaneously.

Thus no separate higher coherence obstruction remains once the kernel is fixed: the obstruction at each rung is exactly positivity of that Gram packet.

## Least failing rung

Suppose the kernel is not positive definite. Some finite packet has a negative quadratic direction. The set of cardinalities of failing packets is a nonempty subset of the positive integers, so it has a least element \(N\).

Every packet of cardinality less than \(N\) has a positive constructor, while at least one \(N\)-point packet does not. All proper subpackets of a minimal failing packet are constructible, but they cannot be extended jointly to that next rung.

Therefore failure is witnessed by a finite first obstruction, although no universal bound on \(N\) follows.

## RH bridge

Gaussian translates have Schwartz-dense linear span. If the Weil form is not positive, continuity supplies a finite Gaussian combination with negative value. Its finite translate packet has no positive constructor.

Conversely, Weil positivity makes every Gaussian Gram packet positive. Under the standard source comparison and Weil criterion,

\[
\mathrm{RH}
\]

is therefore equivalent to coherent positive-constructor existence through every finite rung.

Equivalently,

\[
\neg\mathrm{RH}
\]

implies that some least finite next rung is impossible.

## Important limitation

This equivalence does not itself prove RH. Defining a constructor merely as an arbitrary Gram realization repackages positivity. A proof mechanism must construct the vectors and inner products from endpoint, gamma, and prime source data before assuming Gram positivity, and verify the kernel identity.

Numerical scouting is unnecessary for the logical equivalence. Its remaining uses are finite falsification, normalization checks, and locating conditioning barriers.

## Verification

```text
python research/voevodsky/checkers/check_positive_rung_constructor_obstruction.py
```

The checker gives an exact rank-three hostile whose every rank-two subpacket is positive but whose three-point all-ones direction is negative.

Artifacts:

- `research/voevodsky/checkers/check_positive_rung_constructor_obstruction.py`
- `research/voevodsky/results/positive_rung_constructor_obstruction.json`
