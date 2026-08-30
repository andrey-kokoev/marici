# Detector-confusion kernels for domain-resolved flavor (WP99)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## CP-covariant detector channel

Order true and observed routes as `(-,0,+)`. The smallest symmetric confusion
channel with sign-flip probability `e`, broken-to-zero loss `l`, and
zero-to-broken false-positive probability `b` is

\[
K=\begin{pmatrix}
1-e-l&b/2&e\\
l&1-b&l\\
e&b/2&1-e-l
\end{pmatrix}.
\]

Each column sums to one and CP exchanges the first and third rows and columns.
Its exact determinant factorizes as

\[
\det K=(1-l-2e)(1-b-l).
\]

Thus calibrated deconvolution is faithful on the labelled route simplex iff
both factors are nonzero.

The two kernels have different meanings. At `1-l-2e=0`, the odd orientation
mode `(1,0,-1)` is erased. At `1-b-l=0`, the even contrast between broken
support and the symmetric route is erased. Algebraic inversion cannot repair
either surface, and near either surface its condition number diverges.

## Pipeline classification

The source moment family of WP97 is jointly faithful before detection. The
first nonfaithful arrow can therefore be the physical detector channel `K`,
not the source selector or quotient map. Off the two kernel surfaces, `K`
changes neither selection nor chart rigidity; it is an invertible noisy
readout. On a kernel surface it coarsens the contextual partition.

Smallest exact falsifiers: `l=0,e=1/2` erases sign, while `l=0,b=1` makes a
symmetric route observationally identical in its even contrast to broken
support. Remaining instrument gate: calibrate `(e,l,b)`, bound drift away from
both singular surfaces, propagate finite-sample errors through `K^{-1}`, and
retain the WP93 canonical matching/domain-reset requirements.

Verification: `uv run --with sympy python research/flavor/checkers/wp99_domain_detector_confusion.py`.
