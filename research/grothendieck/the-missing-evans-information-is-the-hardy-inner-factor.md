# The missing Evans information is the Hardy inner factor

## The observer mismatch revisited

The canonical adjoint completion produces a two-point source return or
autocorrelation. The physical Evans observer produces the one-point completed
transform. The recent reference-port and path-coherence results identify
exactly what the adjoint observer forgets.

Work first in the right half-plane of the centered coordinate `z`. For a
point `w` with positive real part, the half-plane Blaschke factor is

\[
b_w(z)=\frac{z-w}{z+\overline w}.
\]

On the boundary `z=it`,

\[
|b_w(it)|=1.
\]

Therefore replacing a boundary transform `F` by `b_w F` inserts an interior
zero at `w` while preserving its entire boundary modulus.

## Exact blindness theorem

Every boundary construction depending only on

\[
|F(it)|^2
\]

is invariant under multiplication by finite products of the factors `b_w`.
This includes the ordinary autocorrelation spectral density and every Gram
form obtained solely from that density.

Consequently source-adjoint positivity cannot distinguish a zero-free outer
factor from the same boundary magnitude carrying an interior Blaschke
divisor. This is the structural reason the canonical adjoint completion
realizes curvature and separation measures but not the Evans divisor.

The result is not limited to one inserted zero. Subject to the usual Hardy or
bounded-type hypotheses, canonical factorization separates a function into
outer, singular-inner, and Blaschke parts. Boundary magnitude determines the
outer part but does not determine the inner factor.

## Cross-sector transfer

Nima's phase-reference theorem now has a precise theta target. The missing
reference cannot be another real magnitude port. It must retain a primitive
phase character, hence at least a complex line or two real quadratures before
any independently proved Real reduction.

Strominger's pure-braid theorem identifies the corresponding global datum.
Endpoint labels and static period coordinates may be faithful while still
forgetting path winding. In the Hardy picture, the Blaschke factor is exactly
a path/winding record invisible to boundary magnitude.

Thus the observer bridge is not

```text
more positive moments -> Evans section.
```

It is

```text
boundary magnitude + source-authorized inner-factor record -> Evans section.
```

## Revised RH formulation

After placing the completed theta transform in the correct sectorwise Hardy
or bounded-type class and removing its known units, RH becomes the statement
that each open-sector transform has trivial Blaschke divisor. Equivalently,
the source filter is outer with respect to interior zeros in both open
half-planes. Reciprocal sewing relates the two sector factorizations on their
common boundary.

Calling the function outer without deriving it would merely rename RH. The
explanatory target is stronger:

1. construct a phase/path record from labelled theta/Tate operations;
2. prove it is compatible with the boundary magnitude supplied by the
   adjoint Gram object;
3. prove its interior winding is trivial in each open sector;
4. show that a hostile symmetric multiplier inserts a nontrivial record and
   is rejected before its zeros are inspected.

## Immediate falsifier

Any proposed proof using only boundary modulus, autocorrelation, positive
Gram matrices, or source separation measures is falsified by `F` versus
`b_wF`: the data are identical on the boundary while the interior divisors
differ.

Any proposed phase reference that transforms only by an even or higher-weight
character is also insufficient; it leaves a finite phase ambiguity. The
reference must carry primitive winding or be supplemented by an independently
derived Real structure and augmentation.

## Scope

This identifies the information missing from the adjoint completion and
connects it to a source-authorized path record. It does not construct that
record for theta, prove the required Hardy-class normalization, establish
outerness, or prove RH.
