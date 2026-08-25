# Source-generated observer hierarchy

The current cross-sector results approach one architecture, but at two
different evidential levels.  Benincasa and Strominger have explicit
reconstruction maps.  Kitaev has proved algebraic generation; turning that
control statement into physical observer faithfulness still requires an
authorized trace pairing and executable instruments.

\[
\begin{array}{c|c|c}
\text{sector}&\text{transform}&\text{faithful completion}\\
\hline
\text{Boolean deletion routes}&\text{zeta transform}&\text{Möbius score tower}\\
\text{magnetic reflection pair}&\mathbb Z_2\text{ character transform}&(E,M)\\
D(S_3)\text{ endpoints}&\text{flux-resolved generation}&
\text{full block algebra (control level)}
\end{array}
\]

For the reflection pair the transform is literally

\[
\binom{E}{M}
=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\binom{A}{B},
\qquad
\binom{A}{B}
=\frac12
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\binom{E}{M}.
\]

Thus the complete parity observer is the Fourier transform on `Z_2`, just as
the complete deletion-score observer is inversion in the Boolean incidence
algebra.  Kitaev's result is the candidate nonabelian control analogue: the
two flux types generate every endpoint block rather than merely its center.
It must not yet be promoted to a physical reconstruction theorem.

## Reconstruction certificate

For any finite family of typed ports `O_i:V->W_i`, assemble

\[
O:V\longrightarrow\bigoplus_iW_i,
\qquad v\longmapsto(O_iv)_i.
\]

The family is jointly faithful exactly when `O` is a monomorphism.  Over the
present finite-dimensional coefficient fields, this is equivalent to the
existence of reconstruction maps `R_i:W_i->V` satisfying

\[
\boxed{\sum_iR_iO_i=\operatorname{id}_V.}
\]

This left-inverse identity is the invariant certificate.  Möbius inversion
supplies the `R_i` for deletion scores; the half-Hadamard transform supplies
them for `(E,M)`.  Full endpoint-algebra generation supplies possible
operations, not such an identity for physical measurement outcomes.

This yields a localization theorem for information loss.  Once the complete
source-generated transform is proved faithful, any surviving kernel must lie
at one of three distinct arrows:

1. **Before transport:** an unauthorized or unfaithful typing map has already
   identified labelled source states.
2. **At readout selection:** only a proper subset of complementary ports is
   retained.  Magnetic towers and exceptional circuits are aliases of the
   magnetic port alone, while `(E,M)` reconstructs their full sheet packet.
3. **After faithful reconstruction:** a deliberate semantic quotient forgets
   additional structure.  In the magnetic closed sector, rational de Rham
   reduction kills the depth-zero tower and both exceptional circuits, but
   retains one common unlabelled residue line when any positive admitted pole
   depth is present.  A depth-labelled associated grade retains one line per
   depth, but that is a different typed object.

The third loss is not an observer defect.  It is the definition of the
cohomological readout.  Conflating it with a parity kernel would incorrectly
identify rationally contractible collision circuits with noncontractible tower
classes.

The resulting magnetic factorization is

\[
\text{source}
\xrightarrow[\text{injective}]{(A,B)}
\text{sheet packet}
\xrightarrow[\text{invertible}]{\mathcal F_{\mathbb Z_2}}
(E,M)
\supset \ker M
\longrightarrow
\ker M/\ker M^{\mathrm{rat}}.
\]

Only the final arrow creates the ordinary residue quotient; its dimension is
one when at least one visible positive pole depth exists, and zero otherwise.
