# The relative equivariant eight-lattice tower admits a universal Waldhausen cone enhancement

## Input already constructed

Let \(\mathcal J_{rel}\) be the directed source category whose objects are admissible indices

\[
\iota=(L,n,F,N)
\]

and whose arrows are the source-authorized maps \(U_{\iota'\iota}\).

Let

\[
L_7=\operatorname{esd}_7(\Delta^3)
\]

and let \(C_4\) act by cyclic permutation of the four presentation labels and tetrahedral coordinates.

Prior work supplies, on the observer-generated relative system, a homotopy-coherent diagram

\[
\Phi_{rel}:
\mathcal J_{rel}\times(C_4\ltimes L_7)
\longrightarrow
N(\mathsf{Herm}_{rel}).
\]

Its restrictions contain:

- all lattice objects and conductor comparisons;
- triangular modifications and tetrahedral coherences;
- strict source composition;
- order-four chart rotation;
- source-successor naturality.

The identities are

\[
U_{\iota''\iota'}U_{\iota'\iota}=U_{\iota''\iota},
\]

\[
T_{j,\iota'\iota}C_{ij,\iota}
=
C_{ij,\iota'}T_{i,\iota'\iota},
\]

and

\[
T\tau=\tau T,
\qquad
\tau^4=I.
\]

## Stable envelope

The Hermitian presentation category is not assumed to be stable. Let

\[
\operatorname{St}(\mathsf{Herm}_{rel})
\]

be its universal stable envelope, formed by pointed presheaves, stabilization, and localization at the admitted analytic equivalences.

Write

\[
j:\mathsf{Herm}_{rel}
\longrightarrow
\operatorname{St}(\mathsf{Herm}_{rel})
\]

for the universal map.

The composite

\[
\Phi_{st}=j\Phi_{rel}
\]

is the canonical stable enhancement of the prior diagram. This construction is formal and does not assert that every resulting stable object already has a preferred realization by a closed operator.

## Conductor cone packages

For every oriented conductor edge

\[
C_{ab}:X_a\to X_b,
\]

define its compressed analytic symbol by

\[
K_{ab}=\operatorname{cofib}(jC_{ab}).
\]

For a composable pair

\[
X_a\xrightarrow{C_{ab}}X_b
\xrightarrow{C_{bc}}X_c,
\]

the stable octahedral law gives the canonical triangle

\[
K_{ab}
\longrightarrow
K_{ac}
\longrightarrow
K_{bc}.
\]

Consequently each triangular lattice cell maps to a quotient-of-quotients triangle, and each tetrahedral lattice cell maps to a compatible octahedron.

This is precisely the local data required by the Waldhausen construction.

## Waldhausen object

Apply the Waldhausen construction to the stable envelope:

\[
S_\bullet\operatorname{St}(\mathsf{Herm}_{rel}).
\]

The enhanced realization is

\[
\widehat\Phi_{rel}:
\mathcal J_{rel}\times(C_4\ltimes L_7)
\longrightarrow
S_\bullet\operatorname{St}(\mathsf{Herm}_{rel}),
\]

where a lattice simplex is sent to its system of interval composites and cofibers.

The 2-Segal comparison maps are equivalences because cofiber composition in a stable category satisfies the octahedral law. Different triangulations therefore yield canonically equivalent compressed quotient data.

## Successor compatibility

Successor naturality gives commutative squares

\[
\begin{matrix}
X_{a,\iota}&\xrightarrow{C_{ab,\iota}}&X_{b,\iota}\\
\downarrow T_a&&\downarrow T_b\\
X_{a,\iota'}&\xrightarrow{C_{ab,\iota'}}&X_{b,\iota'}.
\end{matrix}
\]

Functoriality of cofibers produces

\[
K_{ab,\iota}
\longrightarrow
K_{ab,\iota'}.
\]

Thus the already proved relative successor acts on every conductor cone, every octahedron, and the full Waldhausen object. No homological suspension is needed to manufacture this successor.

## Chart action

Because \(\tau^4=I\) and \(T\tau=\tau T\) before stabilization, the same identities hold after stabilization and after applying \(S_\bullet\):

\[
\widehat\tau^4=I,
\qquad
\widehat T\widehat\tau
=
\widehat\tau\widehat T.
\]

Stable suspension remains an independent operation commuting with exact functors.

## Reciprocal duality

The prior polarity has type

\[
\dagger:
\mathsf{Herm}_{rel}^{+}
\to
(\mathsf{Herm}_{rel}^{-})^{op}.
\]

It extends to an exact contravariant duality on the stable envelope. On a conductor cone it gives

\[
\mathbb D K_{ab}
\simeq
\Sigma^{-1}K_{ba}^{\dagger},
\]

with the shift determined by the cofiber/fiber convention. Hence

\[
\mathbb D\Sigma
\simeq
\Sigma^{-1}\mathbb D.
\]

This realizes the reversal between the two 2-Segal path spaces while retaining the prior positive/negative polarity typing.

## Physical obstruction as a mapping class

For the unreduced physical system, define

\[
\delta_{\iota'\iota}
=
T^{phys}_{\iota'\iota}\mathcal O^{phys}_{\iota}
-
\mathcal O^{phys}_{\iota'}U_{\iota'\iota}.
\]

After stabilization this determines a class

\[
[\delta_{\iota'\iota}]
\in
\pi_0\operatorname{Map}(A_{\iota},B_{\iota'}).
\]

A physical stable seam is not the assertion that the cone of \(\delta\) vanishes. It is a specified nullhomotopy of \(\delta\). Therefore the exact extension criterion is

\[
[\delta_{\iota'\iota}]=0
\]

together with coherent choices of nullhomotopies under composition.

The known relative subsystem has \(\delta=0\) strictly. The physical class is supported only in the previously isolated prolate-placement, prolate-to-Tate, Sonin, and endpoint channels.

## Closed-operator realization

Let \(\mathcal C_{cl}\) be the stable infinity-category of admitted closed cone packages, once constructed. A genuine analytic realization is an exact functor

\[
R_{cl}:
\operatorname{St}(\mathsf{Herm}_{rel})
\to
\mathcal C_{cl}
\]

whose value on each generating presentation agrees with its closed graph model.

The existing finite cone and octahedral checkers verify local instances of this lift. Uniform graph-domain and completion control are required to construct \(R_{cl}\) globally.

## Theorem and boundary

The prior relative equivariant tower has a canonical universal Waldhausen cone enhancement with:

- the full seventh edgewise subdivision;
- strict directed successor action;
- order-four chart symmetry;
- cone and octahedral quotient cells;
- 2-Segal reconstruction;
- reciprocal duality.

This theorem is formal after the prior analytic diagram is admitted. What remains unproved is the nonformal lift to the intended category of closed operators and the coherent nullhomotopy of the physical seam class.
