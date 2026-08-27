# Fourier–Poisson Sewing Rotates the Augmentation Line into the Control Port

## Smallest exact sewing model

Let `F_N` be the unnormalized Fourier transform on the cyclic label space
`C[Z/N]`. For the augmentation vector

\[
\Omega=(1,\ldots,1),
\]

character orthogonality gives

\[
F_N\Omega=N e_0,
\]

where `e_0` is the zero-frequency control vector.

For every `N>1`, this is not proportional to the target augmentation vector.
Thus Fourier sewing does not preserve the augmentation line. It rotates the
common input mode into the distinguished vacuum/control port.

## Exterior incidence under sewing

Exterior naturality is exact:

\[
(\Lambda^2F_N)(\Omega\wedge g)
=(F_N\Omega)\wedge(F_Ng)
=N e_0\wedge(F_Ng).
\]

The transported edge current is therefore the control-relative coboundary,
not the ordinary target augmentation coboundary

\[
\Omega\wedge(F_Ng).
\]

This is not a failure of Fourier coherence. It is a typing correction: the
sewing functor exchanges which distinguished line defines the comparison.

## The 90-degree rotation

This gives a literal finite form of the previously suspected mental rotation:

- constant position mode becomes a zero-frequency point;
- augmentation comparison becomes control-port comparison;
- the pair-label bivector survives, but relative to a different anchor.

The input, output, and control towers are therefore not three parallel copies.
Fourier–Poisson sewing cyclically changes their roles.

## Architectural consequence

The `3` in `3+2+2+1` is load-bearing. A two-sector state model cannot make
Fourier sewing a chain map for one fixed augmentation incidence. The control
tower is required so that the transported incidence lands in

\[
e_0\wedge\mathcal H_{\mathrm{dual}}.
\]

The next coherence cell must compare the output augmentation line with the
dual control line. It cannot identify them directly, because they have
different support and operational meaning. Instead it must specify the
source-derived incidence by which the control point is expanded back into the
completed output boundary—Poisson summation's comb reconstruction.

This also explains why scalar aggregation was repeatedly misleading: Fourier
does not preserve the scalar port; it transports it into a different tower.

