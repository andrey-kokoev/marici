# Ramsey primitive and Golay cyclic-squaring test

Date: 2026-11-09. Finite exact certificate: `check_golay_from_cyclic_squaring.py` (standard-library Python).

## Question

Does the original seven-symbol `R G R G R 0 0`, using rotation, reflection, composition, and quotient, force the 23-position binary Golay code or the 11-bit syndrome field? In particular, does the proposed 2048-state quotient have a source-derived successor?

## Exact bridge: seven positions and 23 positions

For errors/marks of weight at most three, the Hamming sphere has size

\[V_3(n)=\sum_{j=0}^3\binom nj.\]

\[V_3(7)=1+7+21+35=64=2^6,\quad V_3(23)=1+23+253+1771=2048=2^{11}.\]

No integer length 8 through 22 satisfies `V_3(n)` is a power of two. Thus 23 is the first *possible* next perfect three-error-packing length after seven. **The premise that the Ramsey primitive must build a perfect binary three-error packing has not been derived.**

Take one specified binary projection of `R G R G R 0 0`: mark an `R` by 1 and `G` and empty by 0. The resulting seven-bit word has ones in slots 0,2,4. XOR-summing its seven cyclic rotations gives the all-ones word, since each slot is visited three times. That invariant word generates the `[7,1,7]` repetition code. The choice of binary projection is additional structure; it discards the original three-state distinction.

## Frobenius-doubling symmetry

Over F2, the cyclic polynomials split as

\[x^7+1=(x+1)(x^3+x+1)(x^3+x^2+1),\]

\[x^{23}+1=(x+1)f(x)f^*(x),\]

with

\[f(x)=x^{11}+x^9+x^7+x^6+x^5+x+1,\]

\[f^*(x)=x^{11}+x^{10}+x^6+x^5+x^4+x^2+1.\]

The doubling maps on nonzero residue classes have two inverse/reflection-paired orbits, of lengths 3 at modulus 7 and 11 at modulus 23. Therefore the binary cyclic modules decompose into sizes `1+3+3` and `1+11+11`. These decompositions are exact but do not constitute a map between the two carriers.

## Deriving the 23-bit Golay parity check without supplying its matrix

Factor `x^23+1` over F2 and choose either irreducible degree-11 factor `f`. In the field F2[x]/(f), let `zeta=x mod f`, of order 23. Generate 23 columns `h_j=zeta^j` for j=0,...,22. Their binary rank is 11.

For every index set A of size at most 3, compute the syndrome `s(A)=XOR_(j in A) h_j`. The checker obtains all 2048 possible 11-bit syndromes, each exactly once. Consequently the kernel is a `[23,12,7]` perfect binary code, equivalent to the binary Golay code. An explicit seven-coordinate kernel word is supported at `(0,1,2,3,9,12,21)`. The second irreducible factor yields an equivalent reversed-orientation construction.

The computation *assumes modulus 23 as an input*. Thus it proves Golay emerges from cyclic algebra at 23, not that the seven-position Ramsey primitive produces 23.

## Derived higher unique-completion laws

Enumerating all 4096 kernel codewords gives weight distribution:

`0:1, 7:253, 8:506, 11:1288, 12:1288, 15:506, 16:253, 23:1`.

The 253 weight-7 supports have pairwise intersections at most 3 (otherwise their difference would have weight less than 7). Each support contains 35 four-subsets, and `253*35=C(23,4)=8855`. Exact enumeration confirms every four-subset occurs once. Hence these supports form the Steiner system `S(4,7,23)`.

Extend each 23-bit word by one parity coordinate. The resulting `[24,12,8]` code has 759 weight-8 supports. Its minimum distance 8 ensures two distinct octads cannot share five positions. Since `759*C(8,5)=C(24,5)=42504`, these octads form `S(5,8,24)`. The classical automorphism group is Mathieu `M24`; the checker constructs the design, not the group automorphism classification.

The emerging sequence is: **cyclic positions → binary 11-dimensional syndrome → perfect three-mark packing → unique 4-to-7 completion → parity lift → unique 5-to-8 completion.**

## Interpretation and boundary for Ramsey

- Genuine structural link: 7 and 23 are perfect radius-3 binary packing lengths; 23 admits an exact `1+11+11` cyclic factorization; the higher Witt completion laws follow without supplying a Steiner design.
- Unproved transition: starting only with `R G R G R 0 0`, its geometric rotation/reflection histories do not yet force length 23, an 11-dimensional quotient, or one of the two conjugate degree-11 factors. Ordinary linear operations on seven coefficient positions cannot create 11 independent coordinates without a specified additional product/promotion operation.
- Ramsey caveat: the existence of a perfect Golay code at length 23 does not prove `R(3,7)=23`, or even imply that its code-derived adjacency meets Ramsey constraints. The same perfect-packing rule does not select `R(3,8)=28`.
- Next discriminating task: derive, from the original seven-symbol operation and retained composition records alone, a non-fitted promotion to a 23-position carrier with an 11-dimensional rank (or establish a no-go). Test the independent output incidence for red triangles and independent seven-sets before making any Ramsey assertion.

## External confirmation

Robert T. Curtis, *The Art of Working with the Mathieu Group M24*, chapter 4 (Cambridge University Press, 2024) describes the extended binary Golay code and `S(5,8,24)`. A. E. Brouwer's Octad Graph reference identifies the design automorphism group as `M24`.
