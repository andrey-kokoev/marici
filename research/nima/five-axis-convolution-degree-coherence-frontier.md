# Five-axis convolution-degree coherence frontier

## Local five-dimensional object

Use the axes

\[
(H,V,D,q,L),
\]

where

- `H`: input-arity/rooted-substitution direction;
- `V`: output-arity/physical-cut direction;
- `D`: polarity dagger;
- `q`: chart/helix successor;
- `L`: convolution-degree successor.

A local before/after model has 32 vertices and 80 edges. Its Freudenthal triangulation has

\[
5!=120
\]

maximal ordered 5-simplices, one for each ordering of the five operations.

Globally, `D` is involutive, while `q` and `L` are directed graded operations. The binary coordinates are local cells in their respective directed towers.

## Constructed pairwise faces

Six of the ten pair types have sourced or canonical models.

| Pair | Comparison |
|---|---|
| `H x V` | strict transverse mixed Beck--Chevalley |
| `H x D` | dagger naturality on minimal generated carriers |
| `V x D` | dagger naturality on minimal generated carriers |
| `D x q` | successor--polarity interchange |
| `D x L` | left/right convolution-successor dagger interchange |
| `q x L` | Fourier sends convolution successor to multiplication successor in the canonical Pontryagin chart model |

The last face is distributive rather than naively commuting:

\[
\mathcal F\,L_a
=M_{\mathcal Fa}\,\mathcal F.
\]

The exact Mellin and endpoint realizations of `L` are

\[
\mathcal M_{r+s}L_a^{(r)}=M_{m_a}\mathcal M_r,
\]

\[
\beta_{r+s}L_a^{(r)}=D_a^\partial\beta_r.
\]

Successive degree changes compose strictly:

\[
L_b^{(r+s)}L_a^{(r)}=L_{b*a}^{(r)}.
\]

## Missing pairwise faces

Four pair types prevent promotion to a historical full 5-cell.

| Pair | Missing datum |
|---|---|
| `H x L` | one consolidated typed theorem that observer convolution is natural under rooted-subtree substitution |
| `V x L` | one consolidated typed theorem that observer convolution commutes with the physical cut/coaction square |
| `H x q` | chart-to-input-arity intertwiner |
| `V x q` | chart-to-output-arity intertwiner |

The last two are the previously identified absence of maps from Fourier/chart ports to semilocal arity presentations. Equal cycle length does not provide them.

## Five-cell law

Once all ten pairwise faces exist, the 40 cubical 3-faces express coherence among triples, the 10 four-faces express coherence among those cubes, and the unique 5-cell compares all 120 operation orders.

The full law is a higher distributive coherence: every route from the initial state to the state after `H,V,D,q,L` agrees after inserting

- Beck--Chevalley cells;
- dagger mates;
- successor interchanges;
- convolution-to-multiplication Fourier transport;
- Mellin and endpoint natural transformations.

## Result

Convolution degree is validated as a genuine fifth axis. It has independent grading and exact transformations with Mellin, endpoints, polarity, and composition. The canonical Tate/Pontryagin model realizes its chart-distributive face.

The historical semilocal five-simplex is not assembled. Its first missing layer consists of the four pairwise squares above; higher coherence should be attempted only after those squares are typed.

`check_five_axis_successor_coherence_frontier.py` materializes the 32 vertices, 80 edges, 80 square faces, 40 three-faces, 10 four-faces, one five-cell, the 120 ordered simplices, and the status of all ten pair types.
