# Polarity is the third axis of the dagger-duoidal cube

## Cube

Use coordinates

\[
(a_{in},a_{out},\epsilon)\in\{0,1\}^3,
\]

where `epsilon` is polarity. The eight vertices are

\[
V_1^+,V_2^+,V_3^+,V_4^+,
\qquad
V_1^-,V_2^-,V_3^-,V_4^-.
\]

```text
             negative polarity

       V2- -------- V3-
        |            |
        |            |
       V1- -------- V4-
        |            |
        | dagger     | dagger
        |            |
       V2+ -------- V3+
        |            |
        |            |
       V1+ -------- V4+

             positive polarity
```

The top and bottom faces are the two arity squares. The four vertical faces express dagger compatibility with each arity edge.

## Source-derived vertical operation

Source star is

\[
\iota(p)=p^*,
\qquad
(p*q)^*=q^**p^*.
\]

On every minimal source-generated feature carrier it induces an antiunitary

\[
D_{q,r}:\overline{\operatorname{ran}A_{q,r}^+}
\xrightarrow{\sim}
\overline{\operatorname{ran}A_{q,r}^-}.
\]

Endpoint exchange is its boundary mate. Existing source results prove that:

- edge maps reverse by adjoint conjugation;
- face homotopies transport under dagger;
- tetrahedral modifications transport under dagger;
- left and right successors are exchanged;
- aperture and graph completions are preserved.

These statements provide the four vertical edges and four side faces of the cube on minimal generated carriers.

## Three-cell law

Let `beta+` be the mixed Beck--Chevalley cell on the positive sheet. The negative-sheet cell is its dagger mate with reversed orientation:

\[
\beta^-
=D\,(\beta^+)^\dagger D^{-1}.
\]

Equivalently, dagger carries the positive arity-square filler to the oppositely oriented negative filler. This is the cube's three-dimensional coherence law.

The interchange-order parameter is therefore retained in the correct place: it labels the `beta` filler on each polarity sheet rather than becoming a third object coordinate.

## Exact status

### Minimal source-generated carriers

The cube is complete:

- 8 vertices;
- 12 edges;
- 6 faces;
- 1 dagger/Beck--Chevalley compatibility cell.

The vertical arrows are antiunitaries, and the cube is a dagger-duoidal cube.

### Independently completed physical carriers

The source determines dagger only on the generated closures. Ambient carriers may contain source-orthogonal summands. Filling the ambient physical cube requires:

1. specified antiunitaries on those summands;
2. compatibility with independently fixed physical symmetries;
3. the common-positive-bulk condition needed for positive quotient descent.

Absent those data, the ambient cube is represented by source-labelled closed relations rather than everywhere-defined antiunitaries.

`check_dagger_duoidal_polarity_cube.py` materializes the eight vertices, twelve edges, six faces, and the minimal-versus-ambient status boundary.
