# Euler currents do not anchor long prime-power blocks

## Status

Research packet. It evaluates the source-derived primitive, square, and
connected Euler currents on the prime-power Følner hostile. It does not test
the independent seam-state norm or a stronger constructor topology.

## Source current on one prime orbit

Fix a prime (p). The connected (k)-th occupation has scale (k\log p)
and atomic weight

\[
w_{p,k}=\frac1k p^{-k/2}.
\]

For the normalized block

\[
v_N=\frac1{\sqrt N}\sum_{k=1}^{N}e_{p^k},
\]

the complete connected atomic current is

\[
I_p(v_N)
=
\frac1{\sqrt N}
\sum_{k=1}^{N}\frac1k p^{-k/2}\delta_{k\log p}.
\]

Its total variation satisfies

\[
\lVert I_p(v_N)\rVert_{\mathrm{TV}}
\le
\frac1{\sqrt N}
\sum_{k=1}^{\infty}\frac1k p^{-k/2}
=O(N^{-1/2}).
\]

Hence the entire connected Euler current tends to zero in total variation
and in every weaker current topology.

## Primitive and square ports

The primitive and square currents retain only the (k=1) and (k=2)
coordinates:

\[
I_{p,1}(v_N)
=
\frac{p^{-1/2}}{\sqrt N}\delta_{\log p},
\]

and

\[
I_{p,2}(v_N)
=
\frac{p^{-1}}{2\sqrt N}\delta_{2\log p}.
\]

Their linear amplitudes are (O(N^{-1/2})), and their associated quadratic
energies are (O(N^{-1})).

Thus neither port supplies a cutoff-independent boundary cost on long
normalized prime-power blocks.

## Undamped spectral readout

At finite cutoff, the odd character readout is a sum of the form

\[
\frac1{\sqrt N}\sum_{k=1}^{N}
\frac1k p^{-k/2}\sin(kt\log p).
\]

Its absolute value is bounded by the total mass above and therefore also
tends to zero uniformly in (t). Oscillation is not needed for the escape;
the source weights already make the current summable along one fixed prime
orbit.

## Meaning

The primitive and square currents remain essential typed data:

- they prevent illegal deletion of the first two divergent global prime
  grades;
- they distinguish distributional, non-trace-class, and trace-class
  completion behavior across primes;
- they reconstruct finite Euler cutoffs exactly.

But they do not act as a uniform coercive anchor on the coefficient module.
Along a fixed prime orbit, normalized mass can spread into higher powers while
all of these current readouts vanish.

## Scope qualification

This is a module-level no-go. It disproves a lower bound claimed for all
normalized arithmetic packets in a topology where (v_N) has unit norm. It
does not show that the distinguished theta/Fock state itself follows this
hostile family.

It also does not test the independent seam state. The retained seam component
may have a nonvanishing norm on (v_N), because translated seam atoms need
not decay with (k). Any such repair must be computed as seam energy, not
attributed to the Euler atomic currents.

## Next finite test

For the same (v_N), compute separately:

1. the full tail–seam Gram energy;
2. the Clark first-jet energy;
3. the mixed seam–bulk residual;
4. the archimedean boundary supply.

If their combined energy has a positive limit, identify the exact channel
that anchors the block. If it tends to zero, the entire local
boundary-current architecture has no uniform completion gap.

## Conclusion

Primitive, square, and connected Euler currents encode indispensable
arithmetic provenance, but they do not stop prime-power Følner escape. A
completion-stable orientation law must obtain its reserve from the retained
seam, an archimedean coupling, a nonlocal operator, or a stronger
source-authorized topology.
