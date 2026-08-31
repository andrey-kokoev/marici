# The Xi dual section defines a canonical Koszul complex with the correct divisor

## Source dual section

Let \(\mathcal L_\theta\) be the completed three-stratum theta determinant
line and let

\[
\tau\in H^0(U,\mathcal L_\theta^*)
\]

be the source-derived theta Mellin dual section.  In the source scalar frame,
its coordinate is \(\xi(s)\).

Because \(\tau\) is a line morphism rather than an everywhere-invertible
trivialization, it canonically defines a two-term Koszul complex.

## Theta Koszul complex

Define

\[
K_\tau:
0\longrightarrow
\mathcal L_\theta
\xrightarrow{\tau}
\mathcal O_U
\longrightarrow0.
\]

This complex is constructed from the theta line and its Mellin functional
before inspecting the zero set.  No inverse of \(\xi\), Blaschke factor, or
fitted kernel channel is used.

Its determinant-line section is exactly \(\tau\).  In a source frame,

\[
\det K_\tau(s)=\xi(s)
\]

up to the fixed sign convention for the two-term determinant functor.

## Fibre cohomology

At a parameter \(s_0\), the fibre differential is the linear map

\[
\tau_{s_0}:(\mathcal L_\theta)_{s_0}\to\mathbb C.
\]

If \(\xi(s_0)\ne0\), it is an isomorphism and the fibre complex is acyclic.
If \(\xi(s_0)=0\), then \(\tau_{s_0}=0\), so

\[
H^0(K_\tau|_{s_0})
=(\mathcal L_\theta)_{s_0},
\qquad
H^1(K_\tau|_{s_0})
=\mathbb C.
\]

Thus the Xi divisor has a canonical line-valued cohomology presentation.

## Local algebraic multiplicity

Choose a local nonvanishing frame \(e\) for \(\mathcal L_\theta\).  Then

\[
\tau(e)=f(s),
\]

where \(f\) is the local Xi coordinate.  The complex of local holomorphic
modules is

\[
\mathcal O_{s_0}
\xrightarrow{f}
\mathcal O_{s_0}.
\]

Since the local ring has no zero divisors, the module kernel is zero for a
nonzero germ, while the cokernel is

\[
\mathcal O_{s_0}/(f).
\]

Its length is

\[
\operatorname{length}_{s_0}
\mathcal O_{s_0}/(f)
=
\operatorname{ord}_{s_0}\xi.
\]

The Koszul complex therefore retains algebraic zero multiplicity, not merely
the dimension of the fibre kernel.

## Reciprocal structure

The Fourier--Poisson sewing identifies
\(\mathcal L_{\theta,s}\) with
\(\mathcal L_{\theta,1-s}\), and the theta functional obeys the reciprocal
law.  Hence reciprocal transport is a chain isomorphism

\[
K_\tau(s)\cong K_\tau(1-s).
\]

The two reciprocal divisor stalks are transported without identifying their
parameter support.

## What this construction does not prove

The Koszul complex is the section written as a source-line complex.  It gives
no independent open-sector contraction: such a contraction would be
multiplication by \(\xi^{-1}\), whose bounded existence is the zero-free
statement being sought.

It also does not identify its cohomology line with a state in the retained
history, seam, or Green domain.  The cohomology is initially a determinant-line
residue.

## Correct comparison target

The theta side of the G4 mapping-cone problem is now defined:

\[
K_\tau
\longrightarrow
C_{\rm FP}.
\]

The required chain map must send the determinant-line residue to the
forward-derived closed boundary state while preserving local module length.
An acyclic mapping cone would then prove the divisor-preserving comparison.

## Disposition

A completed theta complex with the exact Xi divisor and multiplicities exists
canonically as the Koszul complex of the source Mellin dual section.  This
closes the object-definition part of G4 but not its RH-bearing comparison to
the maximal-isotropic Green pencil.  No RH conclusion is authorized.
