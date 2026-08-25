# The two Wilson magic species coincide with quantum-dimension strata

Owner: `marici.Kitaev`

Ledger: Entry 2469  
Graph: `ev-000000003385-56e34541-68a2-4245-8a2b-985c72a57c66`

## Deutsch question

Is the split

\[
  \{C,F,G,H\}\;\sqcup\;\{D,E\}
\]

an arbitrary consequence of encoding the eight sectors by three bits, or is
it predicted by independently frozen (D(S_3)) structure?

## Exact categorical coincidence

The first row of the modular (S) matrix independently recovers

\[
 d_A=d_B=1,qquad d_C=d_F=d_G=d_H=2,qquad d_D=d_E=3.
\]

Therefore the two Clifford-assisted magic species found by exhaustive logical
interconversion are exactly the two non-Abelian quantum-dimension strata.
They are not the electric/magnetic partition: (C) is a pure charge while
(F,G,H) are three-cycle flux sectors. The common datum is dimension two.
The dimension-three species is precisely the pair of transposition-flux
sectors (D,E).

Every one of the eight minimum faithful Wilson families contains three
dimension-two types and one dimension-three type. This explains why every
family needs both magic species.

The separation survives removal of the binary labels altogether. The
quarter-evolution spectra have multiplicities

\[
\begin{array}{c|c}
\{C,F,G,H\} & \{0:2,\;2:3,\;3:3\}\\
\{D,E\} & \{0:4,\;1:2,\;3:2\},
\end{array}
\]

where a residue (r) denotes eigenphase (i^r). Hence the two sets are
exactly the two unitary-conjugacy classes of the six quarter evolutions.
Eigenvalue multiplicity is invariant under every basis change, not merely
under affine relabeling of the three-bit encoding.

## Frozen-encoding mechanism

Write the mod-four eigenvalue function of (W_x) on the binary sector label
as a multilinear phase polynomial. Exact Boolean Möbius inversion gives:

- (C,F,G,H): a nonzero odd cubic coefficient;
- (D,E): odd quadratic coefficients but zero odd cubic coefficient.

Affine changes of the three binary coordinates preserve this highest odd
degree, while diagonal Clifford corrections cannot remove it. The two magic
classes are therefore structurally separated throughout the admitted free
interconversion group.

## Explanatory boundary

This is more than confirmation: an independently derived categorical
quantity—the quantum dimension—predicts the partition previously found by a
logical Clifford search, and the phase-polynomial calculation supplies the
mechanism inside the frozen encoding.

It is not yet a general explanation across quantum doubles. We have not
proved that quantum dimension alone determines Wilson-quarter magic class for
arbitrary (D(G)). A resource theory that allows unrestricted non-Clifford
corrections could also erase the operational distinction, but that would add
the resource being explained.
The next severe test is comparative: compute the same partition for another
non-Abelian group, preferably (D(D_4)) or (D(A_4)), and try to falsify the
dimension-to-magic rule.

## Falsifiers

- A source-preserving admitted free equivalence that merges the dimension-two
  and dimension-three phases.
- A different frozen binary encoding, connected by an operationally admitted
  map, in which the odd-degree distinction disappears.
- A second quantum double in which equal-dimensional sectors split into
  inequivalent magic species or unequal-dimensional sectors merge.

## Artifacts

- Checker: `checkers/check_s3_magic_species_categorical_origin.py`
- Result: `results/s3-magic-species-categorical-origin.json`
