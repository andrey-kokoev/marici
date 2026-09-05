# Six-point NMHV primary-source audit

## Question

Do the retrieved primary sources authorize the local triangulation, boundary mechanism, and interpretation as a six-point NMHV amplitude identity?

## Retrieved sources

Operator-authorized shell retrieval materialized PDFs and TeX archives for:

- Arkani-Hamed and Trnka, *The Amplituhedron*, arXiv:1312.2007. PDF SHA-256 `553863867402aeb4a95d8ed0b8aac1f17fd7871304972517b09f7503f00eee4d`; TeX archive SHA-256 `6a87819def9bc8a8c2fc116484cc44f037ae5f2e7917ff2e89fbc59359c0175f`.
- Arkani-Hamed et al., *Scattering Amplitudes and the Positive Grassmannian*, arXiv:1212.5605. PDF SHA-256 `eff72d669a1c2ea45ec86f8f546050232e419883bad4250488af080f5f5899ed`; TeX archive SHA-256 `7f02ce67cfa9789b12b80b330053da61aa740959cb0f3ae98d14a78153674e8c`.

## Located claims

In `1312.2007/amplituhedron.tex` lines 479–520, the source states that the tree amplituhedron is the image of the positive Grassmannian under `Y=C·Z`; for `k=1,m=4`, four-dimensional cells are labelled by five nonzero coefficients; the triangulation is written as a sum over `(1,i,i+1,j,j+1)`; and interpreting those cells as R-invariants gives a canonical BCFW representation of NMHV tree amplitudes.

In `1212.5605/positive_grassmannian_update.tex` lines 1462–1475, the source states that the six-particle NMHV tree amplitude has two distinct three-term BCFW representations. The terms are encoded by included diagrams and permutation labels rather than by the textual five-brackets used in the local fixture.

At lines 1495 onward, the source states that identities among Yangian-invariant on-shell forms arise by taking boundaries of appropriate positive-Grassmannian cells. This supports the local-boundary explanation as a source claim.

## Comparison

The local chains

\[
[12345]+[12356]+[13456]
\]

and

\[
[12346]+[12456]+[23456]
\]

are now derived term by term from the textual source formula `(1,i,i+1,j,j+1)` at `n=6`: its three nondegenerate terms give the first chain, and one cyclic relabelling gives the second. The checker verifies both label lists exactly.

The five-bracket formula is source-located at `1008.2958/all_loop__v2_penult.tex` lines 269–273, equation `Rinv`. Its Grassmann delta and all five cyclic denominator brackets match the generic-super checker exactly. There is no normalization residual within this R-invariant convention.

The source also supports boundary-generated Yangian identities. The local suite proves the corresponding generic bosonic and super identities and detects orientation mutations.

## Full-amplitude normalization and physical poles

`1312.2007/amplituhedron.tex` lines 221–240 defines the color-stripped superamplitude component `M_{n,k}` and factors it into momentum conservation, supermomentum conservation, the Parke–Taylor denominator, and the momentum-twistor function `cal M_{n,k}`. This locates the exact boundary between the replicated R-invariant sum and the fully normalized color-stripped superamplitude.

`0907.5418/n4dual-7-31final.tex` lines 839–856 states that the six-term identity removes unphysical poles and lists the nine physical poles: six two-particle collinear poles `s12,...,s61` and three parity-invariant three-particle poles `t123,t234,t345`. The updated boundary checker verifies that the nine external four-bracket facets map bijectively to this set.

## Residual

The diagram permutation labels in the six-particle figure were not independently decoded; the textual triangulation formula supplies the local labels without using that figure. This does not affect the source-matched formula but remains an unverified alternative presentation.

## Disposition

The five-bracket formula, both three-term label sets, generic bosonic and super identities, triangulation origin, boundary mechanism, full-amplitude prefactor convention, and nine physical pole classes are source-matched. This is an independent replication of the six-point NMHV tree identity under the cited color-stripped superamplitude convention. It does not replicate the figure-level permutation presentation or extend beyond this finite tree benchmark.
