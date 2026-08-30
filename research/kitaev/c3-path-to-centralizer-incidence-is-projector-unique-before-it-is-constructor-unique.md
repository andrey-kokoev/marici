# `C3` path-to-centralizer incidence is projector-unique before it is constructor-unique

Owner: `marici.Kitaev`

## Bounded question

What is the exact algebraic ambiguity in identifying a three-path control
register with the three-cycle centralizer module used by the localized
`D(S3)` character PVM?

For an oriented `C3` action, every unitary equivariant incidence differs from
the canonical one by three independent Fourier phases. All such incidences
transport the same character projectors. A source-unit anchor removes the
continuous phase torsor and makes the open linear map unique. If orientation
is not fixed, one residual inversion exchanges the `G` and `H` characters.

Thus the incidence is already unique for charge probabilities before it is
unique as a coherent constructor.

## Two regular modules

Let the path module be

\[
\mathcal P=\mathbb C[C_3]
\]

with basis

\[
|0\rangle_P,\qquad |1\rangle_P,\qquad |2\rangle_P.
\]

Let the local centralizer module be

\[
\mathcal Z=\mathbb C[C_3]
\]

with basis

\[
|e\rangle_Z,\qquad |r\rangle_Z,\qquad |r^2\rangle_Z.
\]

The oriented regular actions are

\[
S_P|j\rangle_P=|j+1\rangle_P
\]

and

\[
S_Z|r^j\rangle_Z=|r^{j+1}\rangle_Z.
\]

The canonical incidence is

\[
J_0|j\rangle_P=|r^j\rangle_Z.
\]

## Classification of oriented equivariant unitaries

An oriented incidence `J` must satisfy

\[
J S_P=S_ZJ.
\]

Use the character bases

\[
|\chi_k\rangle_P
=
{1\over\sqrt3}
\sum_{j=0}^2\omega^{-kj}|j\rangle_P
\]

and the corresponding basis in `Z`. The regular shifts have three distinct
eigenvalues. Therefore every intertwiner is diagonal between the matching
character lines:

\[
J
=
\sum_{k=0}^2
\lambda_k
|\chi_k\rangle_Z
\langle\chi_k|_P.
\]

Unitarity is equivalent to

\[
|\lambda_0|=|\lambda_1|=|\lambda_2|=1.
\]

Hence the oriented unitary incidence space is a `U(1)^3` torsor. After
quotienting one physically irrelevant common phase, the projective ambiguity
is `U(1)^2`.

In the group basis these maps are precisely the unitary circulant matrices.
Equivariance alone does not choose one open-port phase convention.

## The source-unit anchor

The path source has a distinguished zero label, and the group algebra has a
distinguished unit. Impose

\[
J|0\rangle_P=|e\rangle_Z.
\]

Because

\[
|0\rangle_P
=
{1\over\sqrt3}
\sum_{k=0}^2|\chi_k\rangle_P,
\]

the anchor forces

\[
\lambda_0=\lambda_1=\lambda_2=1.
\]

Thus strict oriented equivariance plus the unit anchor uniquely determines

\[
J=J_0.
\]

If the anchor is equality only up to a ray, the three phases must still be
equal. The remaining common phase is projectively irrelevant.

The unit does not create the coupling. It removes the ambiguity after an
equivariant coupling has been supplied.

## Unoriented incidence leaves one inversion bit

If only the abstract cyclic subgroup is fixed and its generator is not
oriented, also admit

\[
J S_P=S_Z^{-1}J.
\]

The unit-anchored solution is then

\[
J_-|j\rangle_P=|r^{-j}\rangle_Z.
\]

The two anchored maps are exchanged by the automorphism

\[
r\longmapsto r^{-1}.
\]

They agree on the unit and on the trivial character while exchanging the two
nonreal characters. An oriented generator anchor such as

\[
J|1\rangle_P=|r\rangle_Z
\]

selects `J_0` and removes this final `C2` torsor.

This is the same `G/H` ribbon-orientation ambiguity found in the twist packet.

## Projector incidence is already unique

Let

\[
P_k^P=|\chi_k\rangle_P\langle\chi_k|_P
\]

and

\[
P_k^Z=|\chi_k\rangle_Z\langle\chi_k|_Z.
\]

Every oriented equivariant unitary in the full `U(1)^3` family obeys

\[
J P_k^P J^\dagger=P_k^Z.
\]

The phases cancel. Therefore:

- character probabilities do not require a unit anchor;
- the binary accepted-versus-fault syndrome is insensitive to the Fourier
  phase torsor;
- coherent superpositions of different character ports do depend on the
  relative phases;
- transport of an open amplitude or later interference requires the stronger
  anchored incidence.

This gives three useful equivalence notions.

1. **Projector equivalence:** incidences transport the same character PVM.
2. **Oriented constructor equivalence:** incidences agree as linear maps after
   the declared source-unit and generator anchors.
3. **Physical implementation equivalence:** local couplings are related by an
   admitted finite-depth, fault-compatible transformation.

The first does not imply the second, and the second does not imply the third.

## Minimal coherent transfer target

To move an unknown path qutrit into the centralizer register cleanly, the
apparatus target is

\[
|\psi\rangle_P|e\rangle_Z
\longmapsto
|0\rangle_P J_0|\psi\rangle_Z.
\]

In labelled qutrit coordinates this is an oriented swap. It can be decomposed
abstractly into controlled modular additions and subtractions. That circuit
identity still assumes interactions coupling the external path register to
the encoded local centralizer degree.

The frozen quantum-double Hamiltonian contains no such path register and no
declared swap term. Local finite support of the centralizer projectors does not
make the transfer native.

For measurement alone, coherent transfer may be stronger than necessary. A
nondemolition coupling that correlates the path character projector with a
pointer label is sufficient, provided every group-basis, frame, and Fourier
workspace is uncomputed.

## Fault classification

### Fourier-phase incidence fault

Multiplying the three character lines by independent phases preserves
equivariance and every character probability. It is invisible to the binary
syndrome but changes later cross-character interference.

### Orientation fault

Group inversion exchanges the two nonreal character labels. It preserves an
unoriented clean-return verdict and reverses signed phase identification.

### Unit-anchor fault

The map is equivariant but sends the distinguished zero branch to a circulant
superposition rather than the centralizer unit. Character measurement remains
correct while open-port transfer is miscalibrated.

### Nonintertwining fault

The residual

\[
J S_P-S_ZJ
\]

is nonzero. Character sectors can mix, so even charge probabilities are no
longer transported faithfully.

### Hidden-garbage fault

The visible centralizer label is correct but the original path or an
intermediate group-basis register remains entangled. The effect statistics may
agree while the branch instrument has excess dephasing.

## Relation to source-level comparison cells

A comparison effect defined only after character transport inherits the
equivalence level of its target.

- If it uses only character projectors, equivariance fixes it without choosing
  the Fourier phases.
- If it compares coherent open routes, it needs the unit and orientation
  anchors as well.
- If it claims physical executability, it additionally needs a local coupling
  and fault-action theorem.

This prevents a pre-aggregated comparison cell from silently borrowing a
stronger incidence than its source has derived.

## Exact falsifiers

- Oriented equivariance claimed to select a unique unitary incidence without
  an anchor.
- The `U(1)^3` Fourier-phase family claimed to change character probabilities.
- A source-unit anchor claimed to remove an unoriented `C2` inversion.
- Character-projector transport promoted to coherent open-amplitude transport.
- The canonical algebraic incidence promoted to a local Hamiltonian coupling.
- A correct visible character label claimed to prove workspace erasure.
- Two implementations called physically equivalent solely because their
  abstract intertwiners coincide.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies incidence, source and target ports, anchor
objects, observable-equivalence levels, hidden workspaces, and the distinction
between an abstract map and a local implementation.

The quantum coefficient lens supplies the regular `C3` actions, character
decomposition, Fourier-phase torsor, inversion automorphism, and `F/G/H`
charge interpretation.

## Result

The path-to-centralizer incidence is uniquely determined at the character-PVM
level by oriented equivariance. It becomes unique as an open linear
constructor only after the source unit is anchored. Without ribbon
orientation, one conjugation bit remains. None of these algebraic uniqueness
statements constructs the required physical qutrit transfer or nondemolition
character coupling.

No build or checker was run for this research-only packet.
