# Two-copy theta labels form a product--ratio parity cone with half-density

## 1. Label translation law

The positive theta summands obey

\[
  \phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

For a two-copy label pair \((n,m)\), introduce base variables

\[
  r=u+\log n,
  \qquad
  s=v+\log m.
\]

Then

\[
  u=r-\log n,
  \qquad
  v=s-\log m.
\]

In sum--difference coordinates,

\[
  S=u+v=(r+s)-\log(nm),
\]

and

\[
  D=u-v=(r-s)-\log(n/m).
\]

Thus the two-copy rotation separates arithmetic labels into:

\[
\boxed{
\text{product }nm\text{ transported along }S,
\qquad
\text{ratio }n/m\text{ transported along }D.}
\]

## 2. Primewise rotated lattice

At a prime \(p\), write

\[
  a=v_p(n),
  \qquad
  b=v_p(m),
  \qquad
  a,b\in\mathbb Z_{\ge0}.
\]

The rotated coordinates are

\[
  c=a+b,
  \qquad
  d=a-b.
\]

They satisfy the exact constraints

\[
  \boxed{
  c\ge|d|,
  \qquad
  c\equiv d\pmod2.}
\]

Conversely,

\[
  a=\frac{c+d}{2},
  \qquad
  b=\frac{c-d}{2},
\]

so these cone and parity conditions characterize the image of the labelled
two-copy system.

The product and ratio are

\[
  nm=\prod_pp^{c_p},
  \qquad
  \frac nm=\prod_pp^{d_p}.
\]

An arbitrary point in product--ratio space is therefore not source
admissible. It must lie in the restricted product of the primewise parity
cones.

## 3. Origin of the half offset

The two label amplitudes multiply to

\[
  n^{-1/2}m^{-1/2}
  =
  (nm)^{-1/2}
  =
  \prod_pp^{-c_p/2}.
\]

Hence the coefficient \(1/2\) is not an arbitrary horizontal displacement in
the scalar \(s\)-plane. It is the half-density normalization attached to
unitary multiplicative transport in the product coordinate.

\[
\boxed{
\Re s=\frac12
\text{ is the scalar shadow of the two-copy product half-density}.}
\]

The relative coordinate \(d\) carries phase, while the product coordinate
\(c\) carries decay. The critical line is where these two roles are balanced
by the source normalization.

## 4. Reflection and the two sectors

Swapping the two source copies sends

\[
  (a,b)\longmapsto(b,a),
\]

and therefore

\[
  (c,d)\longmapsto(c,-d).
\]

Product depth is fixed while relative orientation reverses. The two
reciprocal sectors are the two signs of \(d\), sewn along

\[
  d=0.
\]

The cone boundaries

\[
  d=\pm c
\]

are the one-copy rays where one of \(a,b\) vanishes. Thus the rotated
arithmetic geometry is a discrete light-cone-like lattice, not an
unconstrained plane.

## 5. Defect-current expansion

For each labelled pair, the two-copy defect current contains

\[
  S\sinh(yS)\cos(xD).
\]

After the source translation, its arithmetic displacement is

\[
  S\mapsto S-\log(nm),
  \qquad
  D\mapsto D-\log(n/m),
\]

with weight \((nm)^{-1/2}\). Primewise, radial decay depends on \(c\), while
the oscillatory phase shift depends on \(d\).

This is the first exact combinatorial organization of the cross-\(S\)
pairing problem:

\[
\boxed{
\text{positive depth }c
+\text{signed phase }d
+\text{parity/integrality constraint}.}
\]

## 6. Relation to the operator's integrality intuition

The scalar \((S,D)\)-plane permits points that do not lift to nonnegative
integer label pairs. Loss of the cone/parity packet is exactly loss of source
integrality after the two copies have acquired distinct orientations.

This does not mean that every scalar zero is caused by parity violation.
Rather, any explanation of zero exclusion that ignores the parity cone has
forgotten an exact source constraint before asking the analytic question.

## 7. Next theorem and falsifier

At each prime, sum the labelled defect current over the cone

\[
  \{(c,d):c\ge|d|,\ c\equiv d\pmod2\}
\]

before aggregating primes or integrating the base variables. Test whether the
resulting transfer in \(d\) is sign-regular after the half-density
\(p^{-c/2}\) is included.

The smallest falsifier is one prime and one finite cone depth \(c\) at which
the canonical \(d\leftrightarrow-d\) or adjacent-depth pairing has negative
or incoherent orientation. No a posteriori regrouping is allowed.

## 8. Scope

The product--ratio transformation, cone/parity characterization,
half-density weight, and reflection law are exact consequences of the
label-shift formula. Their interpretation explains the \(1/2\) normalization
geometrically but does not prove sign regularity, Hermite--Biehler
orientation, or RH.
