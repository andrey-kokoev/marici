# Monodromic G2 Polarization and Scale Fiber

## Question

Does the physical \(Z_3\)-monodromic construction of \(G_2\) supply the action
and electric polarization missing from WP798, and thereby make the asymmetric
flavor portal unavoidable?

## What the physical source adds

The non-simply-laced \(N=2\) gauge construction folds a simply-laced parent by
outer-automorphism monodromy. For \(G_2\), the relevant orbit has degree three.
The construction supplies a Dirac-integral electromagnetic charge lattice,
unit electric vectors, magnetic weights, and a BPS category. Root and coroot
data are therefore tied together by a physical pairing rather than chosen as
unrelated quadratic forms.

This repairs WP797's bare-pairing ambiguity at the level of the \(N=2\) gauge
theory. It does not yet identify either electromagnetic coordinate with the
Standard Model flavor portal. Electric/magnetic duality also warns that an
electric weak-coupling coordinate is not an absolute observable.

## Dimensional-transmutation fiber

For pure \(N=2\) \(G_2\) super-Yang--Mills, use the normalized asymptotically
free flow

\[
\frac{dg}{dt}=-b g^3,
\qquad b=2h^\vee=8.
\]

Its exact one-loop trajectory is

\[
g^2(t)=\frac{g_0^2}{1+2bg_0^2t}.
\]

The group and matter packet fix \(b\), but every positive \(g_0\) is admitted.
Equivalently, the RG-invariant transmutation scale

\[
\Lambda=\mu\exp\left[-\frac{1}{2bg^2(\mu)}\right]
\]

is constant along a trajectory but is not selected by the beta function.
Dimensional transmutation replaces one boundary coordinate by another; it
does not turn a finite fiber into a singleton.

If representation data conditionally give

\[
g_n=g^2C_n,\qquad g_m=g^2C_m,
\]

then the ratio \(g_n/g_m=C_n/C_m\) and the sign for an ordered embedding are
fixed, while

\[
g_n-g_m=g^2(C_n-C_m)
\]

retains the transmutation-scale fiber. The two exact boundary values
\(g_0=1/4\) and \(g_0=1/3\) obey identical triality, charge, and beta data but
give distinct \(\Lambda\) and distinct finite-scale portal magnitudes.

## Vacuum, threshold, and readout gates

The \(N=2\) source also has a Coulomb branch. BPS central charges and masses
vary with the Coulomb moduli and \(\Lambda\). Hence the source-authorized
threshold spectrum is not a single state. The Gaussian ultraviolet endpoint
has \(g=0\) and therefore selects the zero portal, not the required nonzero
one.

BPS masses and Dirac pairings are genuine instruments for this supersymmetric
gauge theory. They are not instruments for the faithful physical16 flavor
quotient. No admitted map turns a BPS charge or Coulomb modulus into the
ordered real-triplet portal response, and no chiral supersymmetry-breaking
completion has been supplied.

## Classification

- Triality monodromy: source-derived orbit-three rigidifier.
- Dirac charge lattice: physical root/coroot parallelizer.
- Representation Clebsches: conditional sign and ratio selector.
- Asymptotically free flow: trajectory rigidifier, not a nonzero magnitude
  selector.
- BPS spectrum: physical \(N=2\) readout, not a physical16 flavor instrument.

The physical monodromic theory therefore closes the algebra-to-charge
interface but opens no unique portal point.

## Smallest exact falsifier

At fixed group, charge lattice, Clebsches, and beta coefficient,
\(g_0=1/4\) and \(g_0=1/3\) generate distinct RG-invariant scales and distinct
portal magnitudes. Separately, two Coulomb expectation values give different
BPS thresholds. These variations leave the triality explanation intact.

## Successor

The remaining source principle cannot be gauge monodromy alone. It must lift
both \(\Lambda\) and the Coulomb vacuum, derive a chiral
supersymmetry-breaking route and Standard Model species embedding, and
co-generate finite threshold matching plus a calibrated physical16 response.
An isolated conformal construction is a possible magnitude alternative only
if it has no exactly marginal coupling, contains the required chiral
operators, and supplies the full descent and instrument.

Verification:

- checker:
  research/flavor/checkers/wp799_monodromic_g2_polarization_scale_fiber.py
- generated result:
  research/flavor/results/wp799_monodromic_g2_polarization_scale_fiber.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp799_monodromic_g2_polarization_scale_fiber.py
- monodromic \(G_2\) charge construction:
  [Cecotti and Del Zotto](https://arxiv.org/abs/1207.7205)
- \(G_2\) Seiberg--Witten Coulomb data:
  [Masuda, Sasaki, and Suzuki](https://arxiv.org/abs/hep-th/9705166)
- physical \(Z_3\)-twisted \(D_4\) SCFTs:
  [Chacaltana, Distler, and Trimm](https://arxiv.org/abs/1601.02077)
