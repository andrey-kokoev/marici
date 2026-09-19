# The two square normalizations are distinct jet coordinates, not rival interface conventions

The primitive coefficient is already fixed:

\[
b_p^{(P)}=(\log p)p^{-1/2}.
\]

For the square grade, the twisted-moment source module contains both

\[
\frac12p^{-1}
\qquad\text{and}\qquad
(\log p)p^{-1}.
\]

Treating these as rival choices for one scalar square row creates an artificial
interface ambiguity.  They have different constructor roles:

- `p^(-1)/2` is the square endpoint/value coordinate, including its half-density
  normalization;
- `(log p)p^(-1)` is the logarithmic square-current coordinate obtained by
  differentiating the Euler/Tate character.

They are respectively a zero-jet and connection/first-jet coordinate of the
same square determinant-line stratum.  A jet-enhanced boundary package must
retain both rather than choose a polynomial `P` that conflates them.

This role separation is forced by the middle-facet typing.  The `SC`
characteristic interval carries both the determinant section and its
logarithmic connection, while the `SG` Green interval carries endpoint value
and ordered current as separate ports.  A `CG` map must compare like roles:

\[
\frac12p^{-1}
\longleftrightarrow
\text{square endpoint port},
\]

\[
(\log p)p^{-1}
\longleftrightarrow
\text{square current/connection port}.
\]

After this refinement, local square normalization is coefficientwise fixed by
source moments.  The remaining ambiguity is no longer which square
coefficient to select; it is whether the external comparison preserves the
value--connection pair, its archimedean mate, and reciprocal orientation.

This advances the labelled-current comparison from a scalar row problem to a
rank-two square-jet naturality square.  Collapsing the two coordinates before
comparison would recreate the underdetermination.
