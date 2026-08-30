# General-spin, general-grade ladder-kernel theorem

Let \(s\geq1\) be an integer and let

\[
\mathcal A_{s,r}=\bar\eth\,\eth^r,\qquad r\geq0,
\]

act on a smooth spin-\(s\) spherical field. The spin-two magnetic theorem is
the specialization \(s=2\). The conjugate-helicity branch follows by complex
conjugation, with the operator word conjugated as well.

## Spectral multiplier

The standard ladder rules give

\[
|\lambda_{s,r,l}|^2=(l+s+r)(l-s-r+1)
\prod_{j=0}^{r-1}(l-s-j)(l+s+j+1).
\]

For admitted \(l\geq s\), and \(r\geq1\), this vanishes exactly at

\[
l\in\{s,s+1,\ldots,s+r-1\}.
\]

The final lowering factor also vanishes at \(l=s+r-1\), but supplies no extra
class: the last raising factor already vanishes there. Every factor is
positive for \(l\geq s+r\). At \(r=0\), lowering has no kernel on admitted
spin-\(s\) modes. Uniformly,

\[
\ker\mathcal A_{s,r}=\bigoplus_{l=s}^{s+r-1}\mathcal H_l^{(s)},
\]

with an empty sum at \(r=0\).

## Dimensions and index

Per helicity,

\[
\dim\ker\mathcal A_{s,r}=\sum_{l=s}^{s+r-1}(2l+1)=r(2s+r).
\]

The target has spin \(s+r-1\). Its lowest representation is absent from the
range, so

\[
\dim\operatorname{coker}\mathcal A_{s,r}=2s+2r-1,
\qquad
\operatorname{ind}\mathcal A_{s,r}=(r-1)(r+2s-1).
\]

At \(s=2,r=3\), these are \(21\), \(9\), and \(12\).

## What protects the kernel

The theorem uses four constructor assumptions:

1. the carrier is the complete \(SO(3)\) spin-\(s\) harmonic representation;
2. admitted degrees begin at \(l=s\);
3. the operator is exactly the ordered word \(\bar\eth\eth^r\);
4. no projection removes low harmonics before that word acts.

Under those assumptions, each raising step increases the supported spin
threshold and kills the representation at the old endpoint. The coefficients
are ladder norms, so their integer factors measure distances to representation
endpoints; they are not fitted matrix weights.

Changing the sphere, representation, operator order, source carrier, or adding
lower-order mixing can change the kernel. Thus \(21\) is forced only after the
spin-two spherical grade-three constructor is authorized, not by “grade
three” alone.

## Scalar edge case and source availability

The restriction \(s\geq1\) is substantive. At \(s=0,r=0\), \(\bar\eth\)
annihilates the constant harmonic. This is the smallest hostile counterexample
to erasing the input-spin type.

The spectral kernel and availability of its vectors remain distinct:

- finite point-supported distributions contain no nonzero smooth finite
  harmonic sum;
- weak-star smooth completion admits the harmonic densities and realizes the
  full endpoint kernel;
- later observation quotients may retain, identify, or exclude these vectors,
  but do not cause the ladder zero.

The causal chain is

\[
\text{authorized spin carrier and ladder word}
\longrightarrow\text{representation-endpoint kernel}
\longrightarrow\text{source-completion availability}
\longrightarrow\text{chosen readout quotient}.
\]

Neither the local characteristic lattice nor a numerical rank coincidence is
part of this derivation.
