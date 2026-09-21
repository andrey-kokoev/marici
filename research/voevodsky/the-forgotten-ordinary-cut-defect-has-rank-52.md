# The forgotten ordinary cut defect has rank 52

## Result

For the raw coarse derivative forms with orthogonal coarse-cut labels and unit vacuum/Omega, the full 90-dimensional forgotten ordinary sector has nonzero relative form Delta=Q_L-Q_R of rank 52 and inertia (26,26,38).

The exact spectrum is

- +8 sqrt(3) and -8 sqrt(3), each with multiplicity 10;
- +4 sqrt(15) and -4 sqrt(15), each with multiplicity 16;
- zero with multiplicity 38.

There are 720 nonzero ordered cross entries and no nonzero diagonal entries in this basis. Both Q_L and Q_R separately have rank 90. The nullity 38 is the radical of their DIFFERENCE, not a radical of either carrier or source image.

## Basis and computation

For every ordered partition into three pairs retain the vector

    r0(first) tensor [forgotten middle path] tensor r0(last).

The two forgotten middle routes agree in B2. The 90 partition labels give 90 independent ordinary common-cell vectors. Apply the actual coarse maps D(aw) tensor D(c) and D(a) tensor D(wc), preserving respectively the four-event and two-event coarse cut labels. Every contributing coordinate has vacuum memory and Omega seam letter, so its prescribed pairing is exactly one. No feature Gram surrogate or spectral sample enters the calculation.

The common uncompressed form on this sector is 16 times the identity. Therefore the separately source-computed differences from that form telescope to Delta. This is bookkeeping of actual forms, not a sewing theorem.

## Relation to prior analytical work

`../grothendieck/the-ordinary-middle-block-has-a-nonzero-cut-dependent-green-anomaly.md` already supplies the intended multiplication maps, an anomaly within one partition involving retained-grade redistribution, and analytical nonvanishing of its full cross-spectral packet. Its checker passes. The present calculation adds the complete forgotten cross-partition sector, not a replacement for that stronger spectral result.

Together they show that a proposed repair must handle both cross-partition overlaps and within-partition grade redistribution. Merely retaining the partition labels with an orthogonal metric misses the first, while examining only vacuum vectors misses the second.

## Necessary size of a factorized correction

Suppose a proposed finite-dimensional auxiliary carrier Z and linear map T realize this defect as T^* J_Z T. Then rank(J_Z) and dim(Z) must be at least 52. Its signed form must have at least 26 positive and 26 negative directions. The same bounds apply to -Delta. In particular a positive-only added self-pairing cannot represent the defect.

These are necessary bounds for a single factorized signed correction, not a construction of source-admitted ports and not a lower bound for arbitrary changes to the comparison problem. A spectral factorization of this finite matrix would fit a metric after observation; it would not establish the required source-admitted relative sewing.

## Next construction target

Retain the two source-induced maps into their independently prescribed coarse carriers and the relative packet, rather than replacing either form. Seek a source-level relative sewing whose polarization reproduces both this 90-channel matrix and the existing within-partition spectral residual, with the same fixed weights and normalized two-sheet ports. Its verification must include full cross-spectral indices. No completed topology or positivity claim follows from these finite checks.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_forgotten_ordinary_cut_defect.py`

Artifact: `results/forgotten-ordinary-cut-defect.json`.

The spectrum, ranks, and all entries are computed exactly in SymPy. Root factors are omitted identically; the result is for the coefficient sector with the unit root vacuum. The full 2160-coordinate feature-dependent defect remains unevaluated.
