# Descent of the physical period awaits the complete Cayley--Menger boundary audit

> **Superseded typing.** Entry 180 already supplies a canonical twisted
> relative Leray germ on the residue surface. The ordinary primitive-boundary
> audit below is not the correct next gate. See
> `cosmology-rank26-leray-pairing-typing-correction.md`; the remaining task is
> its explicit period covector on the stabilized rank-26 presentation and its
> global transport.

## Rank correction

The stabilized marked-relative bulk object has rank 26.  The earlier rank-21
value was a cutoff-five plateau.  Its literal source vector horizontally
saturates rank 26 at cutoff seven over three primes, in agreement with the
Euler-characteristic census.

## Variance is not the only missing gate

The physical integration chain \(\Gamma\) lies away from all five marked-pole
walls, but it has boundary on Cayley--Menger faces.  The rank-26 algebraic
reducer imposes integration-by-parts relations in the bulk.  For a primitive
\(\eta\), however, the physical chain obeys

\[
\int_\Gamma d\eta=\int_{\partial\Gamma}\eta.
\]

Therefore the bulk integral annihilates an exact relation only if the source
boundary condition makes the corresponding face trace vanish.

Several gates are already closed.  Entry 1067 proves vanishing at generic
smooth \(K=0\) points.  Entries 670 and 672 analyze \(K=q_i\) corners, but
those marked-wall tangencies do not lie on the literal positive chain because
every \(q_i\) is strictly positive there.  Their nonzero exceptional
functional is coefficient-boundary data, not a physical-contour obstruction.

The remaining physical gate is the unmarked Cayley--Menger boundary
stratification: face-line intersections and distance-zero vertices, together
with every source-labelled primitive used by the stabilized reducer.

The elementary exact control already proves the typing issue.  On
\(\Gamma=[0,1]\), \(dx=d(x)\) is zero in absolute de Rham cohomology but

\[
\int_0^1dx=1=x(1)-x(0).
\]

Thus bounded-chain integration does not factor through the absolute quotient;
the relative bulk--boundary pairing does.

## Correct target

It is consequently premature to assert a physical covector directly on the
bulk rank-26 quotient.  The provisional target is a mapping-cone pairing

\[
\left(\Omega^\bullet_{\rm bulk}
\longrightarrow
\Omega^\bullet_{\rm CM\ faces}\right)
\quad\times\quad
(\Gamma,\partial\Gamma)
\longrightarrow\mathbf C.
\]

If every remaining Cayley--Menger face trace vanishes, the bulk period does
descend to a covector on rank 26.  Otherwise the displayed relative complex is
mandatory, with the nonzero trace retained rather than discarded.
The marked-wall conductor cannot supply that contraction because the literal
positive chain does not meet it.

The next finite construction is therefore:

1. export the source-labelled primitives used by the stabilized rank-26
   integration-by-parts rows;
2. restrict them to the unmarked Cayley--Menger face-line and distance-zero
   strata of the literal chain;
3. compute the boundary-trace rank, excluding the marked \(q_i=0\) corners
   already proved disjoint from the chain;
4. form the minimal bulk--face mapping cone;
5. only then compute its transported physical readout quotient.

This replaces an unavailable covector with a geometrically derived relative
pairing and gives a direct falsifier: any nonzero face trace blocks descent to
the bulk quotient.

## Reproducibility

- `research/nima/checkers/check_physical_marked_rank26_geometry.py`
- `research/nima/results/physical_marked_rank26_geometry.json`
- `research/nima/checkers/check_bounded_chain_absolute_quotient_nondescent.py`
- `research/nima/results/bounded_chain_absolute_quotient_nondescent.json`
- ledger Entry 599 (file numbered 646): positive-chain wall support gate
