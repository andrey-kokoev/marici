# Dual-Pair Source Existence Audit

## Question

Does any currently admitted Marici source realize WP873's primitive
electric–dual flavor pairing, rather than merely sharing its algebraic shape?

## Admitted candidates

### Strominger's joint electric/magnetic observer

Strominger's latest theorem starts from two sheet records \(A,B\) and forms

\[
E=A+B,
\qquad
M=A-B.
\]

The recombination is invertible in characteristic zero. The unbarred sheet map
is injective; magnetic kernel classes arise only when reflection parity is
projected. This is a strong transferable theorem about contextual
faithfulness: the complementary magnetic readout restores information erased
by the electric projection.

Its type is readout, not source coupling. Both \(E\) and \(M\) are linear
records of the same gravitational sheet packet. There is no operation
constructing a second flavor coupling \(g_D\), no nondegenerate constraint
\(\Delta_Qgg_D=1\), and no flavor detector calibration. Transporting the words
"electric" and "magnetic" across sectors would confuse a parity-resolved
observer with a Dirac-dual source.

### Monodromic \(G_2\) gauge theory

WP799 contains a genuine physical electromagnetic charge lattice, root/coroot
pairing, magnetic weights, and BPS instruments. It therefore passes the
source-duality type that Strominger's observer does not.

It fails selection. The one-loop flow

\[
\dot g=-8g^3
\]

admits every positive boundary value and has the Gaussian endpoint \(g=0\).
The values \(g_0=1/4\) and \(g_0=1/3\) give distinct transmutation scales while
preserving the same group, charge lattice, monodromy, and beta coefficient.
The Coulomb branch adds a further threshold modulus. No admitted map sends its
BPS readout into the faithful 'physical16' flavor quotient.

### Rank-one unimodular Green–Schwarz lattice

WP782 provides an integral self-dual lattice with primitive pairing magnitude
one. This is not a kinetic normalization theorem. The continuous positive
metric modulus changes the physical mass/coupling normalization while leaving
the integral lattice untouched. Gram three is nonunimodular, and a vector
\(3e\) inserts the desired integer nonprimitively.

Thus an integral primitive pairing does not imply WP873's dimensionless
coupling product.

## Exact typing table

| Candidate | Genuine dual source | Excludes zero | Fixes kinetic magnitude | Threshold attachment | physical16 instrument |
|---|---:|---:|---:|---:|---:|
| Strominger joint observer | no | no | no | readout-faithful only | no |
| monodromic \(G_2\) | yes | no | no | Coulomb/transmutation fiber | no |
| rank-one unimodular lattice | lattice only | not a coupling claim | no | metric modulus | no |

No row satisfies the WP873 source contract.

## Transferable lesson from Strominger

The useful transfer is not a magnetic flavor coupling. It is the exact
factorization

\[
\text{faithful sheet source}
\longrightarrow
\text{electric/magnetic pair}
\longrightarrow
\text{parity projection}.
\]

The first nonfaithful arrow is the final projection. This supports the
WP855--WP870 insistence on retaining complementary detector ports. It provides
no reverse arrow from complementary readout to a primitive dual source pair.

## Smallest exact falsifiers

- The \(2\times2\) electric/magnetic recombination has nonzero determinant,
  proving it is only a change of readout coordinates on \((A,B)\).
- In \(G_2\), \(g_0=1/4\) and \(g_0=1/3\) produce distinct transmutation scales
  under the identical source beta coefficient.
- In the rank-one lattice, varying the positive kinetic metric preserves the
  primitive integral pairing while changing physical normalization.

## Disposition

Negative existence result. WP873 is an abstractly sufficient added-source
architecture, but no current Marici flavor source constructs its dual port.
Strominger supplies a faithful complementary observer, not a coupling
duality; \(G_2\) supplies real electromagnetic duality without magnitude
selection; the unimodular lattice supplies integral pairing without a kinetic
metric.

The branch should not be promoted as the answer to flavor. Its precise
reopening condition is a microscopic chiral flavor model that independently
contains:

1. a physical dual coupling;
2. a primitive normalized product excluding zero;
3. exact self-duality without an exactly marginal or transmutation fiber;
4. duality-intertwining threshold matching;
5. a calibrated 'physical16' instrument.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp874_dual_pair_source_existence_audit.py
~~~
