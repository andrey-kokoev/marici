# A multi-kink five-dimensional wall cannot turn one bulk family into three generations: WP776

## Question

Can one anomaly-free \(SU(6)\) bulk family evade WP775's spectral cost by
producing three localized chiral zero modes from a multi-kink mass profile?

## First-order kernel

For one chiral component, the zero-mode equation is

\[
\left(\partial_y+M(y)\right)f(y)=0.
\]

Its general solution is

\[
f(y)=C\exp\left[-\int^y M(s)\,ds\right].
\]

There is one integration constant \(C\). Zeros and sign changes of \(M\)
alter the shape and localization peaks of this one solution; they do not
increase the kernel dimension.

The exact hostile profile

\[
M(y)=(y+1)y(y-1)
\]

has three sign crossings. Nevertheless,

\[
f(y)=
\exp\left(-\frac{y^4}{4}+\frac{y^2}{2}\right)
\]

spans only a one-dimensional scalar kernel.

For an \(r\)-component first-order linear system, initial data have dimension
\(r\). Three independent same-chirality families therefore require internal
rank at least three. That rank is physical matter multiplicity, not free
localization degeneracy.

## Spectral consequence

Each anomaly-free \(SU(6)\) family has degree \(27\). Rank three costs

\[
3(27)=81
\]

bulk degrees and reproduces WP775's result

\[
\kappa=2+35-81=-44.
\]

## Classification

A multi-kink wall can create several peaks in one wavefunction, but peaks are
not independent generations. Treating them as three states confuses a
presentation of one kernel vector with kernel multiplicity.

The five-dimensional local domain-wall escape is therefore closed on the
declared first-order domain. A progressive successor requires a genuinely
higher-dimensional topological index or another source operator with index
three. Its complete spectral measure must be recalculated; the positive
five-dimensional tower coefficient cannot be transported into that changed
experiment.

The generation-resolved WP770 ports still need an actual physical16
production and decay realization.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp776_five_dimensional_domain_wall_generation_rank_no_go.py

Generated result:
research/flavor/results/wp776_five_dimensional_domain_wall_generation_rank_no_go.json
