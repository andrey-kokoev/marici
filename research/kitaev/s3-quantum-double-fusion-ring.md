# The exact fusion ring of `D(S3)`

Owner: `marici.Kitaev`

## Bounded question

Can the non-Abelian ribbon programme move beyond the anyon census without
silently assuming associators or braid matrices?

Yes.  The Grothendieck fusion ring follows from the Hopf-algebra coproduct and
the exact irreducible characters of `D(S3)`.  This determines fusion
multiplicities but not bases of fusion spaces or their coherence maps.

## Frozen labels

The eight simple sectors are labelled

| label | conjugacy sector | centralizer irrep | dimension |
|---|---|---|---:|
| `A` | identity | trivial | 1 |
| `B` | identity | sign | 1 |
| `C` | identity | standard | 2 |
| `D` | transposition | plus | 3 |
| `E` | transposition | minus | 3 |
| `F` | three-cycle | trivial | 2 |
| `G` | three-cycle | `omega` | 2 |
| `H` | three-cycle | `omega^2` | 2 |

This is the same ordered dimension census `1,1,2,3,3,2,2,2` established in
the predecessor packet.

## Exact construction

Characters are functions on commuting pairs `(g,x)`.  For a sector
`(C,rho)`, the character vanishes unless `g in C` and `x` centralizes
`g`.  Choose `q` with `g=q r q^-1`; the nonzero value is

\[
\chi_{C,\rho}(g,x)=\operatorname{tr}\rho(q^{-1}xq).
\]

The checker uses the exact cyclotomic ring
`Q[omega]/(omega^2+omega+1)`; no floating point enters.  The inner product

\[
\langle\chi,\psi\rangle={1\over |S_3|}
\sum_{gx=xg}\overline{\chi(g,x)}\psi(g,x)
\]

gives the `8 x 8` identity matrix.  The coproduct gives the tensor character

\[
\chi_{i\otimes j}(g,x)=\sum_{ab=g}\chi_i(a,x)\chi_j(b,x),
\]

and projection against the eight irreducible characters produces every
fusion coefficient.

## Fusion result

All coefficients are zero or one, the ring is commutative, `A` is the
identity, and every rule preserves quantum dimension.  The nontrivial
unordered rules are stored exactly in
`research/kitaev/results/s3-fusion-ring.json`.  Structural witnesses include

\[
C\otimes C=A\oplus B\oplus C,
\]

\[
D\otimes D=A\oplus C\oplus F\oplus G\oplus H,
\]

\[
D\otimes E=B\oplus C\oplus F\oplus G\oplus H,
\]

\[
F\otimes F=A\oplus B\oplus F,
\qquad F\otimes G=C\oplus H.
\]

The sign charge exchanges `D <-> E` and fixes the three-cycle sectors.
The standard charge mixes each three-cycle sector into the other two.

## Verification

`python research/kitaev/checkers/check_s3_fusion_ring.py` checks all eight
characters, all 64 ordered products, integrality and nonnegativity of all 512
candidate multiplicities, vacuum identity, commutativity, and quantum-
dimension conservation.  Seven aggregate gates pass.

## Exact remaining boundary

The fusion ring records only isomorphism classes and multiplicities.  It does
not choose intertwiners, bases of fusion spaces, associators, `F` symbols,
braid maps, `R` symbols, topological spins, or verify pentagon/hexagon
coherence.  Multiplicity-free fusion reduces basis ambiguity but does not
remove phase/gauge choices.  Therefore this packet does not promote the
programme to a braided fusion category.

The construction is the finite-group specialization of the representation
theory underlying [Kitaev's quantum double](https://arxiv.org/abs/quant-ph/9707021)
and the open-ribbon `D(G)` bimodule treatment of
[Cowtan and Majid](https://arxiv.org/abs/2107.04411).  The orientation-sensitive
operator multiplication remains governed by
[Jia et al.](https://arxiv.org/abs/2105.08202).

## Falsifiers

The result fails if the characters are not orthonormal, any multiplicity is
nonintegral or negative, `A` fails to act as the identity, a rule violates
dimension conservation, or an independently frozen `D(S3)` convention gives
a different rule after the explicit label dictionary is applied.
