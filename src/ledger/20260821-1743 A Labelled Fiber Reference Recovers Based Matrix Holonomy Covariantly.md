# 1743 — A Labelled Fiber Reference Recovers Based Matrix Holonomy Covariantly

## Matrix-interference datum

Let \(E\) be the transported rank-two amplitude fiber and let

\[
F:R\xrightarrow{\sim}E
\]

be a source-labelled reference frame.  Define the framed holonomy readout

\[
\boxed{M_F(H)=F^{-1}HF.}
\]

## Physical gauge invariance

Under a change of the physical fiber frame,

\[
H\longmapsto GHG^{-1},
\qquad
F\longmapsto GF.
\]

Then

\[
M_{GF}(GHG^{-1})=F^{-1}HF=M_F(H).
\]

Thus the matrix packet is independent of arbitrary physical gauge.

## Reference covariance

Relabelling the reference basis by \(S\) gives

\[
F\longmapsto FS,
\qquad
M_{FS}(H)=S^{-1}M_F(H)S.
\]

If the reference basis labels are part of the source occurrence data, its
matrix entries are fixed.  If only the reference subspace is supplied, the
canonical output is again a conjugacy class.

For Entry 1741's loops, every admissible frame satisfies

\[
\boxed{M_F(AB)\ne M_F(BA).}
\]

Hence the framed readout recovers the based ordering lost by Wilson traces.

## Narrow result

A labelled matrix interference reference upgrades frame-free Wilson character
data to the complete based holonomy matrix while preserving physical gauge
invariance.  The extra structure is a sector-specific readout/frame object,
not a new Cut carrier stratum.

## Durable artifacts

- `research/benincasa/checkers/framed_matrix_holonomy_readout.rs`
- `research/benincasa/results/framed-matrix-holonomy-readout.json`
- `research/benincasa/framed-matrix-holonomy-readout.md`

## Next falsifier

Let the reference frame itself become singular or only partially labelled.
Compute the resulting parabolic flag readout and test whether supported Rees
data recover the lost matrix rows without a post hoc splitting.
