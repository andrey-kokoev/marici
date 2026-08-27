# The authorized renormalization problem localizes to exponentiating two typed boundary currents

## Question

Once arbitrary zero-free counterterms are rejected as circular, what
renormalization operations are actually selected by the frozen theta/Tate
source grammar?

The existing source results leave a small answer: the connected bulk is
already controlled, and all nonordinary completion data are concentrated in
the primitive and square boundary currents.

## Canonical three-level split

The logarithm of a local Euler/Tate transition has prime-power grades `k>=1`.
The prime-vacuum cocycle gives three exact summability levels near the seam:

1. `k=1` is distributional and not Hilbert;
2. `k=2` is Hilbert but its scalar amplitudes are not absolutely summable;
3. `k>=3` is the connected determinant interior and is absolutely summable
   in a nontrivial seam neighborhood.

This is the source-native meaning of the order-three regularized determinant.
It is not permission to discard the first two grades.  It factors the finite
Euler determinant into:

```text
primitive boundary current
  times square boundary current
  times connected order-three determinant.
```

The multiplicative anomaly of the connected determinant is the coboundary of
the two removed low-order terms.  Once those boundary objects are fixed, its
coherence cells contain no further adjustable counterterm.

## What already completes

The `k>=3` connected bulk has an ordinary locally convergent determinant in
the source-derived window.  It therefore supplies a genuine holomorphic unit
and is not the present obstruction.

The first-cumulant subtraction likewise identifies the exact divergent local
phase as the primitive channel.  After removing it, the local seam deviations
are square summable and admit a projective infinite-tensor implementation.
But projective implementability does not choose a scalar phase or exponentiate
the retained primitive current.

The square channel lies between these cases: it is a Hilbert boundary
excitation but not an ordinary absolutely convergent scalar determinant
coefficient.

## Minimal missing constructor

The authorized compact-open completion problem therefore localizes to a
boundary exponentiation functor

\[
\operatorname{Exp}_{\partial}:
(P,Q,H_\infty,H_{seam})
\longrightarrow
\operatorname{Fr}(L_+),
\]

where `P` and `Q` are the primitive and square currents and `Fr(L_+)` denotes
a framed sector determinant line.  The functor must:

1. retain the distributional topology of `P`;
2. retain the Hilbert but non-absolutely-summable topology of `Q`;
3. incorporate archimedean and seam incidence;
4. reproduce the exact finite Euler determinant when tensored with the
   connected order-three bulk;
5. transport naturally under cutoff inclusion;
6. fix the scalar frame before reciprocal sewing;
7. produce a locally bounded sector-unit family.

This is much narrower than finding a counterterm function.  The missing
object is a functor from two typed current coordinates into a determinant-line
frame.

## Odd-exponential gauge

Reflected scalar sewing does not select that frame.  If

\[
F(z)=u(z)D_+(z)D_+(-z),
\]

then every odd entire `g` gives the same product after

\[
D_+(z)\mapsto e^{g(z)}D_+(z).
\]

Centered base-point normalization also leaves this ambiguity untouched.
Hence scalar sewing, functional equation, and one vacuum value cannot define
`Exp_partial`.

The finite cutoff bonding law must fix the increment of the odd gauge.  In
operator terms, it must arise from a Schur complement or relative determinant
of the newly admitted labelled states.  In current terms, the primitive and
square boundary coordinates must determine the first two logarithmic jets of
the frame, while the connected determinant determines all higher grades.

## Parity/index compatibility

If the reverse incidence is odd and satisfies a contracting identity off the
seam, the completed even and odd modes must have zero index imbalance.  The
boundary exponentiation functor must preserve this grading.  A scalar frame
that cancels prime divergence while leaving an unpaired hidden boundary mode
is inadmissible even if its sewn determinant is exact.

Thus the minimal functor has both determinant and complex-level output:

```text
typed low-order currents
  -> framed determinant unit
  plus parity-balanced boundary complex.
```

## Finite reconstruction test

At cutoff inclusion `X subset Y`, compute the exact finite quotient

\[
\frac{D_{+,Y}}{D_{+,X}}.
\]

The candidate boundary exponentiation passes only if this quotient equals the
product of:

- the primitive-current exponential for the new labels;
- the square-current exponential for the new labels;
- the connected order-three Schur determinant;
- the declared archimedean/seam incidence correction.

The equality must hold as a framed section before reflected scalar sewing.
If it holds only after multiplication by the opposite sheet, the odd gauge
remains untyped.

## Falsifiers

- Treating the primitive current as a Hilbert vector.
- Treating the square current as an absolutely summable scalar coefficient.
- Deleting either current because the order-three determinant converges.
- Fixing the odd exponential gauge from the completed scalar product.
- A finite quotient law that closes only after reflected sewing.
- A scalar phase convention with no parity-balanced boundary complex.
- A cutoff frame requiring increasingly many untyped constructors.
- Archimedean incidence continuous only after weakening `P` or strengthening
  `Q`.

## Verdict

The authorized renormalization monoid is no longer amorphous.  Its connected
bulk is the order-three determinant, and its only exceptional finite-prime
coordinates are the primitive and square currents.  The missing constructor
is their source-derived exponentiation into a framed sector determinant line,
with archimedean/seam incidence and parity balance retained.

The next decisive question is:

> Does the exact finite Euler cutoff quotient factor through one fixed
> boundary exponentiation functor on `P` and `Q`, thereby fixing the odd gauge
> and producing a compact-open sector determinant family?

That is a finite reconstruction problem followed by a completion theorem.  It
does not require inventing any further scalar counterterm.
