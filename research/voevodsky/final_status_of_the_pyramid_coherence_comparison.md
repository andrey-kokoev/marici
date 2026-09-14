# Final status of the pyramid coherence comparison

## Established

### Pyramid lattice

The four oriented split-fiber component differences have primitive closure

\[
L_b=A_1^3
=
\mathbb Z\alpha_{12}
\oplus\mathbb Z\alpha_{13}
\oplus\mathbb Z\alpha_{14}.
\]

### Absolute response

The moving-fiber normal jet and universal filtered residue identify

\[
q_{e_6}=(-1,0,0),
\qquad
L_b^{\rm route}=\ker q_{e_6}
=
\langle\alpha_{13},\alpha_{14}\rangle.
\]

The shared rational direction of the \(a\)- and \(b\)-pencil Picard lattices is exactly \(\mathbb Q\alpha_{12}\).

### Relative wall response

For the two source-labelled wall extensions,

\[
W=
\mathbb Z\langle w_{101},w_{110}\rangle,
\]

the universal tails give

\[
q_{v_{\rm alg}}^W=(-1,+1),
\qquad
K_W=
\mathbb Z\langle w_{101}+w_{110}\rangle.
\]

The image is saturated. Individual wall routes carry unit response; their odd difference carries twice the unit.

### Transport facts

- Global site exchange is integral and label-preserving between the \(b\)- and \(a\)-pencils.
- Its de Rham volume orientation is negative.
- Smooth Gauss--Manin return through the strict physical chamber is identity on the fixed-pencil Picard lattice.
- The two pencil lattices share only the \(e_6\) line; their route planes occupy different joint-reflection character sectors.

## Missing comparison

The coherence comparison is the integral relative-to-absolute Gysin interface

\[
\boxed{
J:W\longrightarrow L_b^{\rm route}.
}
\]

Its role is to convert source-relative wall transport into an absolute fixed-pencil route before period readout. It is not:

- site exchange alone;
- physical-chamber Picard monodromy;
- an ordinary boundary residue;
- the conductor \(A_2\) specialization.

The typed information flow is

\[
\{d_i\}
\to L_b
\to
\bigl(\mathbb Ze_6\oplus L_b^{\rm route}\bigr),
\]

\[
W\xrightarrow{J}L_b^{\rm route}
\to L_b/K_{\rm route}
\to\langle e_6,v_{\rm alg}\rangle
\to\text{physical period}.
\]

## Residual value

If \(J\) is an integral isometry on the primitive route frames, exactly two fixed-pencil kernels remain:

\[
K_{\rm route}
=
\mathbb Z\langle\alpha_{13}+\alpha_{14}\rangle
\]

or

\[
K_{\rm route}
=
\mathbb Z\langle\alpha_{13}-\alpha_{14}\rangle.
\]

One labelled signed column \(J(w_{110})\) decides between them.

Prior obstruction theory identifies this same datum as the \(v_{\rm alg}\) coordinate of a source-normalized integral Picard--Lefschetz thimble lifted through the primitive infinity-Gysin sequence. That thimble is not present in the repository.

## Superseded shortcuts

The following inferences are explicitly withdrawn:

1. direct identification of total-energy punctures with pyramid vertices;
2. importing site exchange as a fixed-pencil route swap;
3. deciding an absolute Picard period from ordinary boundary residue;
4. identifying the two cross-pencil wall routes directly with \(\alpha_{13},\alpha_{14}\);
5. importing the conductor \(A_2\) difference into the pyramid \(A_1^2\).

## Disposition

The objective of determining the role and information-flow path of the missing coherence comparison is complete. Its final arithmetic value remains a sharply isolated external geometric input: one integral thimble/Gysin column.

Verification:

- `research/voevodsky/checkers/check_final_pyramid_coherence_status.py`
- `research/voevodsky/results/final_pyramid_coherence_status.json`
