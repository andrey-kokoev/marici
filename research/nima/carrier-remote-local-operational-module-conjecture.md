# Deutsch--Popperian remote/local operational-module conjecture

## Independently suggested architecture

Sonar separates an authoritative `RemoteEntityName` from a constructed
`LocalEntity`. A local entity is not a cached copy: it adds state, columns,
validation, controlled actions, operating mode, and readout behavior. Several
local entities may realize one remote relation. Its RPC boundary separately
types the operated-on object `T` and returned object `R`.

This suggests the Marici factorization

\[
\boxed{
\text{Carrier}
\longrightarrow
\text{sector source relation}
\longrightarrow
\text{local operational module}
\longrightarrow
\text{physical readout}.
}
\]

The analogy is structural, not an identification. The Carrier corresponds
more nearly to schema/composition machinery than to one remote table. A
sector source relation is already a realization of it.

## Cosmology specialization

For the five-mark residue packet, freeze:

- remote/source relation: the common numerator space, Cayley--Menger quartic,
  five marked divisors, and unsplit physical source
  \(q_{g_{23}}+q_{g_{31}}\);
- generic local module: quotient by \(R_5\);
- physical local module: quotient by \(R_{-1/2}\);
- constructor/adapter: dimensional specialization or limiting-lattice
  transport;
- readout: pairing with the canonical physical Leray germ.

The two local modules may have equal rank without sharing coordinate
identifications. Their operational histories, not array positions, must type
their comparison.

## Preregistered prediction

The five replaced relations should be generated entirely by the
\(\gamma\)-dependent twisted-de-Rham/IBP differential over the unchanged
source geometry. They may change degrees, parity, or filtration placement,
but must not require:

- a new carrier polynomial or marked divisor;
- a new source numerator;
- a post-hoc projection selected from the desired readout;
- identification by matching finite-field coordinate indices.

The same source was initially predicted to remain cyclic in both modules. A
valid adapter was therefore expected to send the source to itself and
intertwine the source-defined operations. The higher-pole audit below
falsifies the cyclicity clause while preserving the module-family clause.

## Falsifiers

The conjecture fails in this case if any of the following occurs:

1. physical specialization requires new geometric support;
2. the common source ceases to generate the physical module;
3. the changed relation packet cannot be expressed inside the frozen
   twisted-de-Rham presentation;
4. no source-preserving operation-intertwiner exists;
5. an intertwiner exists only after choosing a coordinate splitting or the
   desired period values.

Success requires more than an abstract rank-26 isomorphism. It requires a
natural constructor from shared source operations, followed by an independently
defined Leray readout.

## Immediate test order

1. classify the invariant degree/parity/support profile of
   \(R_5\cap R_{-1/2}\) and both five-dimensional replacement packets;
2. derive the common source-word comparison;
3. test source preservation and connection intertwining;
4. only then pull back the Leray period covector.

## First test result: survived

The relation classifier replicated over \(\mathbf F_{32003}\) and
\(\mathbf F_{32009}\). In the common 36-dimensional numerator space,

\[
\dim R_5=\dim R_{-1/2}=10,
\quad
\dim(R_5\cap R_{-1/2})=5.
\]

For each five-dimensional replacement packet, the intrinsic degree-filtration
profile is

\[
(0,0,0,0,0,0,1,5)
\]

through degrees zero to seven. Neither packet contains a nonzero class inside
any single \((\deg_a\bmod2,\deg_b\bmod2)\) coordinate-parity subspace. Thus
the marked arrangement mixes parity, but generic and physical specialization
have identical filtered shape.

No new polynomial, marked divisor, denominator, or source generator occurs.
The change is wholly internal to the top two grades of the frozen operational
relation lattice. This is precisely the preregistered local-module behavior,
not a Carrier mutation.

The result does not yet prove that a natural constructor exists. It authorizes
the next test: the source-preserving connection intertwiner.

## Constructor typing correction

A direct fixed-fiber intertwiner was initially proposed as

\[
T A_i^{(5)}=A_i^{(-1/2)}T.
\]

That equation is too restrictive unless \(T\) is known to be independent of
kinematics. The actual horizontality equation is

\[
\partial_iT+A_i^{(-1/2)}T-TA_i^{(5)}=0.
\]

More fundamentally, twists differing by the noninteger amount \(11/2\) need
not define isomorphic local systems: their monodromy characters may differ.
The Sonar analogy therefore points to a constructor over a parameter base,
not necessarily an RPC-style isomorphism between two already constructed
local entities.

The corrected object is a source-labelled module \(\mathcal H_\gamma\) over
an open subset of the \(\gamma\)-line, with base-change maps

\[
\mathcal H_\gamma\otimes_{\gamma=5}k,
\qquad
\mathcal H_\gamma\otimes_{\gamma=-1/2}k.
\]

The next finite gate is regularity of this family at \(\gamma=-1/2\): stable
rank, stable source cyclicity, and a pivot/Plücker chart that does not acquire
a pole there. If regular, the physical module is derived by base change even
though its relation lattice differs. If singular, a limiting or nearby-cycle
lattice is genuinely required.

## Plücker regularity result

The bounded family is regular at the physical twist over both tested primes.
The same ten numerator coordinates

\[
(3,2),(3,3),(3,4),(4,2),(4,3),
(5,1),(5,2),(6,0),(6,1),(7,0)
\]

give a full-rank projection of the relation space at both \(\gamma=5\) and
\(\gamma=-1/2\). The relation rank is ten and the quotient rank is 26 in
both fibers. Although elimination chooses different preferred pivot charts,
one common Plücker chart contains both tested fibers.

Because the unreduced twisted differential is polynomial in \(\gamma\), the
nonzero physical Plücker minor defines an ordinary Zariski-open neighborhood
of \(-1/2\) in this bounded presentation. Thus no limiting or nearby-cycle
lattice is required merely to reach the physical twist at pole depth two:

\[
\boxed{
\text{same bounded module family}
\xrightarrow{\gamma=-1/2\text{ base change}}
\text{physical rank-26 presentation}.
}
\]

This does not exclude additional resonant classes first appearing at higher
\(K\)-pole depth. The next hostile check is pole-depth stabilization at the
half twist. If it remains rank 26, the canonical Leray covector may be built
directly in the physical Plücker chart and compared to the generic family by
ordinary base change.

## Higher-pole result: regular module, codimension-one physical source orbit

Complete normal-form reduction was extended from common \(K\)-pole depth two
to depth three. At both tested primes,

\[
\begin{array}{c|cc}
&K\text{-depth }2&K\text{-depth }3\\
\hline
\dim H_{\gamma=5}&26&26\\
\dim H_{\gamma=-1/2}&26&26\\
\dim\langle\nabla^I s\rangle_{\gamma=5}&26&26\\
\dim\langle\nabla^I s\rangle_{\gamma=-1/2}&25&25
\end{array}
\]

Thus no higher-pole cohomology appears through depth three, and the physical
fiber remains an ordinary rank-26 base change. Nevertheless the literal
unsplit source loses exactly one cyclic direction at the physical twist.

The prior rank-26 physical source-orbit report used an incomplete quotient
normal form that stopped at the first free leader. Eliminating every pivot
before free-coordinate projection gives the replicated rank 25.

This is not a Carrier mutation and not a rank singularity. It is a
codimension-one operational residual inside the regular physical module:

\[
\boxed{H_{-1/2}/\langle\nabla^I s_{\rm phys}\rangle\simeq k.}
\]

It is not yet identified as a physical readout class. The next test must
construct its intrinsic annihilator line, classify its filtration/support,
and evaluate whether the canonical Leray covector detects it.

Evidence:

- `research/nima/checkers/check_rank26_gamma_plucker_chart.py`
- `research/nima/results/rank26_gamma_plucker_chart_p32003.json`
- `research/nima/results/rank26_gamma_plucker_chart_p32009.json`

Evidence:

- `research/nima/checkers/check_rank26_replaced_relation_profile.py`
- `research/nima/results/rank26_replaced_relation_profile_p32003.json`
- `research/nima/results/rank26_replaced_relation_profile_p32009.json`
