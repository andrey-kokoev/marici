# The Sonin residual splits into a vanishing inside atom and a stable outside carrier with an open Green map

## Objective

Resolve the typing and successor status of residual channel 3, previously called
“the Sonin intersection atom.”

## The phrase names two different atoms

For orthogonal projections \(P,Q\), set

\[
B^{\rm in}=PQP|_{\operatorname{Ran}P},
\qquad
B^{\rm out}=(I-P)(I-Q)(I-P)|_{\operatorname{Ran}(I-P)}.
\]

Then

\[
P_{\{1\}}(B^{\rm in})
=P_{\operatorname{Ran}P\cap\operatorname{Ran}Q}
=:P_{11},
\]

while

\[
P_{\{1\}}(B^{\rm out})
=P_{\ker P\cap\ker Q}
=:P_{00}.
\]

The standard Sonin space is \(H_{00}=\ker P\cap\ker Q\), not the
inside--inside space \(H_{11}\). Thus channel 3 must be split before asking for
seam naturality.

## Inside atom

In the ordinary finite time--band model, a vector in \(H_{11}\) is both
compactly supported and bandlimited. Paley--Wiener uncertainty forces it to
vanish:

\[
H_{11}=0,
\qquad
P_{\{1\}}(B^{\rm in})=0.
\]

The large-cutoff near-one prolate spectrum is not an exact atom. It is a
cutoff-dependent spectral cloud whose behavior depends on joint cutoff and
dyadic depth. Therefore no separate inside “Sonin leg” should be transported
through the seam.

For the exact semilocal one-sided carrier, the corresponding uncertainty
statement must still be supplied on that carrier. The ordinary model does not
by itself prove semilocal vanishing.

## Generic inside/outside transport

After removing all four exact Halmos intersections, the inside and outside
contractions are represented by the same angle operator \(B\). The sewing block

\[
S=(I-P)QP
\]

has polar decomposition \(S=V|S|\) and satisfies

\[
VB^{\rm in}=B^{\rm out}V
\]

on generic support. Hence

\[
Vf(B^{\rm in})=f(B^{\rm out})V
\]

for every bounded Borel function \(f\). This gives exact natural transport of
all dyadic generic-angle defect layers. It does not transport either exact
intersection atom, because the sewing operator vanishes there.

Thus the generic tower belongs to channel 2's absolute-Gram problem, while the
outside exact atom remains a separate channel-3 datum.

## Source-authorized outside Sonin dynamics

Connes--Consani--Moscovici construct semilocal Sonin spaces and maps

\[
\Sigma_S:\mathcal S(\mathbb R,e^\lambda)
\xrightarrow{\sim}\mathcal S(X_S,\lambda).
\]

In the weighted Hardy--Titchmarsh realization these maps are Hilbertian
isomorphisms, Fourier compatible, and stable under enlargement of the finite
place set. Characterwise they multiply by

\[
M_S(s)=
\prod_{p\in S\setminus\{\infty\}}
(1-p^{-1/2-is}).
\]

Consequently the outside Sonin carrier already has source-authorized
place-successor dynamics. For \(S\subset S'=S\cup\{p\}\), the transition is
multiplication by

\[
1-p^{-1/2-is}.
\]

After the prescribed weighted realization, this transition is isometric. This
closes carrier transport and place-set naturality for the Sonin space itself.

## Why this does not close the physical seam

The Weil/Tate contribution is governed by the logarithmic derivative

\[
-i\partial_s\log M_S(s),
\]

not by the norm square \(|M_S|^2\). The source-authorized Sonin isometry only
multiplies by local inverse Euler factors. Differentiating generates the full
prime-power current and is unbounded; it is not supplied by ordinary Hilbert
norm preservation.

What remains is a Green/commutator map assigning the outside Sonin atom its
signed boundary role. Schematically one needs

\[
W_S(f)
=
\operatorname{Tr}(\vartheta_S(f)P_{00,S})-E_S(f)
\]

or an equivalent identity, compatible under adding places and with a uniformly
controlled remainder. No recorded theorem identifies the negative spectral
sector of the semilocal prolate operator with the Suzuki Toeplitz cokernel or
with the completed endpoint channel.

## Correct seam inventory

Residual channel 3 should now be recorded as follows.

| component | successor status | seam status |
|---|---|---|
| inside exact atom \(H_{11}\) | zero in ordinary finite time--band model | semilocal uncertainty still required |
| inside/outside generic angle tower | exact polar intertwining | absorbed into absolute-Gram gate |
| outside Sonin atom \(H_{00}\) | source-authorized stable isometric carrier under adding places | signed Green/commutator image open |
| near-one clouds | joint cutoff/depth system required | not exact atoms |

## Status change

“The Sonin intersection atom is unconstructed” is inaccurate. The corrected
status is:

- the relevant intersection has been identified as outside--outside;
- its semilocal carrier and place-successor isometries are constructed;
- the previously proposed inside atom is mislabelled and vanishes in the
  ordinary model;
- the sole remaining seam datum is the signed Green/logarithmic-derivative map
  from the stable outside Sonin carrier.

## Verdict

Residual channel 3 is closed at the level of carrier typing and
source-authorized \(k\)-dynamics, but not at the level of physical signed
readout:

\[
\boxed{
\text{stable Sonin carrier and successor: constructed;
Green/endpoint seam map: open}.}
\]

## Repository dependencies

- `correction-the-eigenvalue-one-atom-of-pqp-is-the-inside-inside-intersection-not-the-sonin-space.md`
- `the-inside-and-outside-prolate-towers-share-one-halmos-angle-operator-and-differ-only-at-exact-intersection-atoms.md`
- `semilocal-sonin-amplification-is-isometric-but-only-multiplies-by-local-euler-factors.md`
- `connes-consani-moscovici-prolate-spaces-do-not-identify-the-suzuki-cokernel-endpoint.md`
