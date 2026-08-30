# The Blaschke model space is the rectangular defect carrier

Author: `marici.Nima`

## Correction

The diffuse Poisson current of an off-seam zero cannot be the spectral measure
of the defect projection itself. A projection has operator spectrum contained
in \(\{0,1\}\). The Poisson current instead appears when that projection is
read in the boundary-position representation.

## Hardy realization

Let \(B\) be the right-half-plane Blaschke inner factor and let \(M_B\) denote
multiplication by \(B\) on the corresponding Hardy space. Since \(B\) is
inner,

\[
 M_B^*M_B=I.
\]

Therefore

\[
 W=M_B^*
\]

is a coisometry, and its initial-space defect is

\[
 D=I-W^*W=I-M_BM_B^*=P_{K_B},
\]

where

\[
 K_B=H^2\ominus BH^2
\]

is the Hardy model space. For a finite Blaschke product, the rank of \(D\)
equals the total zero multiplicity of \(B\).

This is the operator realization missing from the divisor-budget statement:
the off-seam carrier is not an abstract unused dimension but the model-space
defect of a canonical coisometry.

## Boundary-position readout

For one right-sector zero \(\lambda=a+ib\), with \(a>0\), the normalized Hardy
kernel has boundary modulus

\[
 |k_\lambda(t)|^2
 =\frac1\pi\frac{a}{a^2+(t-b)^2}.
\]

It has total mass one. The reciprocal global packet contributes two such
units, giving

\[
 \frac1\pi\frac{2a}{a^2+(t-b)^2}\,dt.
\]

Thus Grothendieck's diffuse Blaschke current is exactly the boundary-position
diagonal density of the rectangular defect projection, with reciprocal
multiplicity included.

As \(a\) tends to zero from the right, this normalized kernel converges weakly
to a seam atom at \(b\). The atom/diffuse transition is therefore the boundary
degeneration of one defect state, not the creation or destruction of divisor
mass.

## What this proves

The rectangular operator language and the diffuse-measure language are two
representations of the same Hardy defect:

- operator view: \(D=P_{K_B}\);
- counting view: \(\operatorname{rank}D\) is off-seam multiplicity;
- boundary view: the diagonal density of \(D\) is the Blaschke Poisson
  current.

This also explains why the defect cannot be stored in the square trace-class
Schur return: it belongs to the inner-factor coisometry, while the relative
Fredholm determinant belongs to the coupled outer/boundary comparison.

## Circularity boundary

This theorem does not yet explain RH. The inner factor \(B\) is defined by the
off-seam divisor of the completed analytic object. Constructing \(M_B\) from
that factor faithfully repackages the zero data.

The missing source law must instead construct a coisometry

\[
 W_{\rm src}
\]

from labelled theta/Tate boundary operations before inner factorization, and
then prove that its defect agrees with \(P_{K_B}\). Only an independent source
law forcing

\[
 I-W_{\rm src}^*W_{\rm src}=0
\]

would exclude the diffuse component rather than redescribe it.

## Finite falsifier

Any proposed source comparison fails if one of the following occurs:

1. it is a coisometry but its initial defect is nonzero;
2. its defect rank disagrees with the Blaschke multiplicity;
3. its boundary diagonal disagrees with the normalized Poisson current;
4. it is constructed only after extracting the inner factor or locating its
   zeros.

The fourth failure is the current status of the canonical Hardy construction.

