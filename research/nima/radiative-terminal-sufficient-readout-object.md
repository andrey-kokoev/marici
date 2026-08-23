# The radiative carrier is the terminal sufficient three-corner readout object

The source and boundary packet exports three operations on the scalar memory
field \(N(z,\bar z)\):

\[
N\xmapsto{D_z^2}\Delta C_{zz},
\qquad
N\xmapsto{\mathcal O}Q_f^{\rm soft},
\qquad
N\xmapsto{D_z^2}\text{soft zero-frequency insertion},
\]

with

\[
\mathcal O=\tfrac14D^2(D^2+2).
\]

On scalar harmonics,

\[
\mathcal O\big|_{\mathcal H_l}
=\tfrac14(l-1)l(l+1)(l+2).
\]

Hence the complete three-corner family has joint kernel

\[
K=\mathcal H_0\oplus\mathcal H_1,
\]

the four-dimensional translation sector. The canonical quotient

\[
\boxed{
\mathcal N_{\rm rad}
=
C^\infty(S^2)/(\mathcal H_0\oplus\mathcal H_1)
}

is therefore terminal among quotients through which all three readouts
factor. On \(\mathcal N_{\rm rad}\), \(\mathcal O\) is invertible and
\(D_z^2\) is faithful modulo its declared spin-2 target.

## Why this is more than a vector-space quotient

The kernel is selected by a source differential operator and the spherical
harmonic decomposition, not by a fitted complement. It is invariant under
the rotation action and compatible with the elliptic operator calculus on
\(S^2\). The quotient participates in the exact soft--charge--memory
naturality squares with their corner orientation, antipodal matching,
zero-frequency prescription, and momentum-conservation obstruction retained.

Thus radiative gravity supplies the first established sector lift of the
minimal-sufficient theorem into a source-supported differential-operator
category.

## Boundary

This is not yet a universal derived-sector theorem. The result uses the
specific elliptic harmonic decomposition of the sphere. It does not construct
effective kernel-pair quotients for cosmological relative chains or string
twisted cycles, and it does not identify the quotient with conscious
experience. It establishes a terminal sufficient physical carrier for a
complete declared readout family.

## Verification

- `research/strominger/soft-bms-memory-source-boundary.md`
- `research/strominger/checkers/leading_triangle_exact_checks.py`
- `research/nima/checkers/check_radiative_terminal_sufficient_readout.py`
- `research/nima/results/radiative_terminal_sufficient_readout.json`
