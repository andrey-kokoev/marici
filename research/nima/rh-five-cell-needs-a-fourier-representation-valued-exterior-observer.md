# RH five-cell needs a Fourier-representation-valued exterior observer

## Instantiating the boundary quotient

The linear Fourier tail cell has one interior Gaussian bulk line and four
boundary directions:

\[
W=\operatorname{span}\{1,\delta_0,K,V\}.
\]

Here (K=H-1/2) is the centered tail and (V=\mathcal FK) is its
principal-value partner. Thus, relative to the Gaussian interior, the actual
five-cell boundary quotient has dimension four.

Fourier transport acts by

\[
1\leftrightarrow\delta_0,
\qquad
K\mapsto V,
\qquad
V\mapsto-K.
\]

These are not relations that reduce dimension. They are the transport law on
the quotient.

## Character decomposition

Over the complex numbers, the quotient splits into four one-dimensional
Fourier character sectors:

\[
W=W_1\oplus W_{-1}\oplus W_i\oplus W_{-i}.
\]

Dual character covectors can be chosen as

\[
(1,1,0,0),
\quad
(1,-1,0,0),
\quad
(0,0,1,i),
\quad
(0,0,1,-i).
\]

They are linearly independent and separate the entire boundary quotient.

## Scalar equivariance no-go

An equivariant scalar observer has one Fourier character. It can therefore
see only the matching isotypic line. On the four-dimensional boundary
quotient it has rank one and leaves a three-dimensional extension torsor.

Demanding scalar Fourier invariance is worse: it selects only the character
one overlap combination and annihilates both odd orientation characters.
That would remove the principal-value information whose boundary
differential produces the positive interval density.

The canonical exterior observer must consequently be representation-valued
before scalar projection. Its target must retain all four character ports, or
an equivalent typed object carrying their transport. The completed Riemann
section can be a later matrix coefficient of this packet; it cannot serve as
the packet itself.

## Refined DPC

The abstract extension torsor now has a concrete finite gate.

1. Construct one observer component in each Fourier character sector.
2. Verify its value on the corresponding boundary generator.
3. Check Clark-before-tail precedence so no unauthorized delta jet enters.
4. Assemble the four rows and prove full rank on the quotient.
5. Verify reciprocal and archimedean transport of the complete packet.
6. Only then apply the source-authorized scalar matrix coefficient.

The verdicts become:

- rank four: finite boundary descent is separated;
- rank below four: a residual observer torsor remains;
- incompatible transported rows: the proposed observer packet is
  inconsistent;
- rank four only after scalar-dependent fitting: authority failure.

## Immediate falsifiers

One scalar continuation row has rank one, regardless of how accurately it is
known. Two scalar rows with the same character remain confined to one
isotypic sector. A Fourier-invariant observer that reports a nonzero odd port
violates equivariance. Reversing tail and Clark operations creates a delta
jet outside this four-dimensional quotient and invalidates the finite model.

Aspect's moment result supplies the parallel warning: full rank certifies only
the declared support object. Here the support object is source-authorized by
the five-cell closure itself, so the remaining audit is whether the proposed
observer rows genuinely come from source constructors rather than being
chosen as a convenient dual basis.

## Scope

Full character rank would prove canonical finite boundary descent. It would
still not prove RH. The next cross-tower theorem must show that output nullity
of the eventual scalar matrix coefficient is transported by the control
Green cell into vanishing of the faithful input Ward packet.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_five_cell_observer_characters.py
```
