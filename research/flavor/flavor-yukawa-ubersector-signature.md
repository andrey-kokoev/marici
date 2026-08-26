# Yukawa relational core and minimal Ubersector signature (WP421)

## Basis-free flavor object

Choose the convention

$$
Y_u:Q_L\longrightarrow u_R,
\qquad
Y_d:Q_L\longrightarrow d_R.
$$

This is a span with common source $Q_L$; reversing the arrows by adjunction gives
the equivalent cospan convention. The two positive operators

$$
A_u=Y_u^\dagger Y_u,
\qquad
A_d=Y_d^\dagger Y_d
$$

live on the shared port and transform by common conjugation under a weak-basis
change. Their individual spectra give the six quark masses. Their relative
eigenflag overlaps give the CKM matrix up to the admitted rephasings. The nine
moduli and signed Jarlskog coordinate are invariant readouts of that relation.

Flavor is therefore not the functor. The physical mixing relation is the
relative placement of the two eigenflag decompositions; flavors are its
distinguishable channel components.

`physical16` packages six masses, nine overlap moduli, and signed $J$. It is a
faithful redundant coordinate on the generic quotient, not a claim that the
physical flavor manifold has dimension sixteen.

## Exact hostile pair

WP421 constructs two exact three-generation pairs with identical singular
spectra on both Yukawa legs. One has aligned eigenflags; the other rotates the
first two down-sector eigenlines by the rational orthogonal matrix

$$
V=\begin{pmatrix}
3/5&4/5&0\\
-4/5&3/5&0\\
0&0&1
\end{pmatrix}.
$$

Their mass records agree while their overlap moduli differ. A simultaneous
weak-basis change of the shared port preserves $V$ exactly. This is the smallest
finite witness that separate leg spectra do not determine relational flavor.

## Minimal Ubersector signature

The current programme requires six typed objects:

1. normalized UV source;
2. selected vacuum;
3. Yukawa span;
4. `physical16` quotient coordinate;
5. calibrated detector record;
6. boundary preparation.

Its arrows are vacuum selection, covariant matching, RG transport, weak-basis
quotient, detector response, and boundary preparation. Numerical identity
across them requires five coherence cells: source-gauge equivariance of
matching; RG/matching scale-scheme compatibility with uncertainty; full
weak-basis descent; source-detector common-frame calibration; and compatibility
of boundary support with the source state.

The basis-free flavor core needs only an ordinary span in finite-dimensional
Hermitian spaces plus quotienting. A profunctor is optional bookkeeping for
channel decompositions; a larger multicategory is not forced until multiple
independently prepared inputs must be composed into one physical operation.

## Missing-arrow witnesses

WP232 places its first failure at the source-detector coherence cell: Standard
Model RG is source-derived and `physical16` is calibrated readout, but no
rank-two common-frame response joins them.

WP256 places its first failure at RG-to-detector transport: source-relative
scaling improves a shape residual but does not make it vanish and supplies no
uncertainty-authorized transport law. Coordinate compatibility cannot fill
either cell.

The Higgs-quartic instrument branch belongs outside the core as a possible
source intervention and detector constructor. It gains flavor authority only
if its output maps equivariantly into the Yukawa span and then through the same
calibrated quotient/readout diagram.

Run `uv run --with sympy python
research/flavor/checkers/wp421_yukawa_ubersector_signature.py` to regenerate the
JSON result.
