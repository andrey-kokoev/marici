# Scalar Li moments encode divisor mass, not operator multiplicity

## Obstruction

A positive scalar moment functional determines a cyclic GNS representation.
For a finite atomic measure

`mu=sum_j w_j delta_(u_j)`,

the multiplication operator on `L^2(mu)` has one-dimensional eigenspace at
each distinct atom `u_j`, regardless of the numerical weight `w_j`.

If a zero ordinate has divisor multiplicity `m`, the conditional Li increment
measure places mass

`w=m/(gamma^2+1/4)`

at its phase. The scalar moments record `m` through this mass, but the cyclic
GNS operator still has spectral multiplicity one at that phase.

Indeed, one atom of mass `m` and `m` identical scalar copies have identical
scalar moments. Their operators have different eigenspace dimensions. No
scalar moment sequence can distinguish those representations.

## Consequence

Positivity of the Li Toeplitz functional plus scalar GNS does not by itself
construct a Hilbert--Pólya operator with the zeta divisor multiplicities. It
constructs a cyclic spectral model whose atomic weights encode the
multiplicities numerically.

To obtain operator multiplicity, one needs an additional theorem:

1. prove the GNS measure is purely atomic at the required phases;
2. prove the renormalized masses
   `(gamma^2+1/4) mu({u_gamma})` are nonnegative integers;
3. canonically amplify the fibre at `u_gamma` to that integer dimension;
4. show this amplification is source-defined and compatible with the
   explicit formula.

Alternatively, a matrix-valued or correspondence-valued positive functional
could carry multiplicity before scalarization. That would be structurally
closer to the earlier coefficient--Betti/Mackey program, but it is strictly
more data than the scalar Li sequence.

## Falsifier

Any claim that scalar GNS alone recovers zero multiplicities is false. The
finite-atomic checker exhibits identical moments with scalar eigenspace
dimension one and an amplified eigenspace of arbitrary dimension `m`.

This obstruction does not damage Li positivity or the RH equivalence. It
separates those scalar statements from the stronger Hilbert--Pólya demand for
the exact divisor spectrum with multiplicities.
