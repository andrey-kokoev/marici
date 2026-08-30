# Passivity, a lossless seam, and reciprocity still permit inner zeros

## Strong physical candidate

The anisotropic two-sector picture suggests a familiar scattering law:

- the right half-plane is passive and contractive;
- the critical seam is lossless and unitary;
- reciprocal reflection supplies the inverse left-sector response.

This is physically meaningful, source-oriented, and stronger than static
coherence. It still does not imply zero exclusion.

## Exact Blaschke hostile

On the right half-plane, define

\[
B(s)=\frac{s-1}{s+1}.
\]

It is analytic on the open right half-plane because its only pole is at `-1`.
For `s=x+iy`,

\[
|s+1|^2-|s-1|^2=4x.
\]

Therefore, whenever `x>0`,

\[
|B(s)|<1.
\]

On the seam `x=0`,

\[
|B(iy)|=1.
\]

Reciprocal reflection gives

\[
B(-s)=B(s)^{-1}.
\]

Thus the right sector is strictly passive, the seam is exactly lossless, and
the left sector is the reciprocal inverse. Nevertheless,

\[
B(1)=0
\]

strictly inside the passive half-plane.

## Control-theoretic meaning

The hostile is an inner or all-pass factor. Boundary energy sees only its unit
modulus and cannot detect its interior zero. Passivity constrains gain; it does
not imply minimum phase.

This is the control-theoretic version of the central symmetric multiplier and
stable-bundle conjugation hostiles. A system may be stable, passive, reciprocal,
and lossless on its boundary while its input-output transfer has a zero in the
interior.

## Relative-frame consequence

If the Evans comparison is typed as a passive scattering coefficient, then
RH-strength nonvanishing requires exclusion of inner factors. The missing
property is some source-derived version of:

- outerness;
- minimum phase;
- invertibility in the appropriate Hardy algebra;
- cyclicity of the input or vacuum vector;
- absence of a hidden all-pass channel;
- a spectral factorization whose inner factor is forced to be constant.

But declaring the transfer outer is merely another form of declaring it
zero-free. The useful theorem must derive outerness from the labelled source
constructor, boundary incidence, and completion law.

## A second warning from total positivity

Pointwise positivity on a real parameter slice is also insufficient. The
polynomial

\[
p(t)=t^2+1
\]

is strictly positive for every real `t` but has the complex zeros `i` and
`-i`. A lower-triangular relative frame with off-diagonal entry `p(t)` is
pointwise totally nonnegative on the real slice and still has complex bundle
intersections after analytic continuation.

Only a much stronger all-orders kernel property, such as a genuinely
source-derived variation-diminishing or Pólya-frequency structure, could have
complex zero-location force. Finite matrix positivity on the seam cannot.

## DPC

For any passive-scattering proposal, require:

1. the source-derived input, output, and hidden-state ports;
2. the Hardy or transfer-function class after completion;
3. its canonical inner–outer factorization;
4. a source theorem forcing the inner factor to be constant;
5. proof that the source input is cyclic and no all-pass hidden channel is
   unobserved;
6. compatibility with reciprocal sewing and the fixed Evans observer;
7. rejection of the exact Blaschke hostile before scalar projection.

Reject:

- passivity alone;
- seam unitarity alone;
- reciprocity alone;
- stability of poles used as evidence about zeros;
- pointwise total positivity on the seam;
- an outer or minimum-phase assumption inferred from the desired zero-free
  conclusion.

## Verdict

The complete passive two-sector scattering picture still admits off-seam
zeros. The frontier has narrowed to a source-derived no-inner-factor theorem
for the relative transfer. That theorem would be decisive, but it is not yet
present and cannot be supplied by boundary energy alone.

