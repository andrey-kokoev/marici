# The Green–Ward effect observer has a canonical finite Lüders lift

## Question

Is the realization fiber over the finite Green–Ward grade effects empty, contractible, or populated by inequivalent instruments?

## Claim boundary

After choosing the standard finite-dimensional completely positive process category, the orthogonal grade effects have an explicit nondemolition instrument and coherent record dilation. This proves algebraic inhabitation of the instrument fiber. It does not derive that process category, apparatus, coupling, or record medium from an independent physical source.

## Bold conjecture

The effect observer formed by the atomic grade projectors has no canonical lift to an instrument observer without additional constructor data.

## Named rivals

1. Orthogonal source idempotents canonically determine the Lüders instrument.
2. The effect family admits instruments, but no nondemolition realization.
3. Every realization is equivalent once its effects are fixed.
4. Many inequivalent disturbance channels share the same effects.

## Finite source and record object

At cutoff \(N\), let

\[
D_N=\bigoplus_{j=0}^{N}\mathbb Ce_j,
\qquad
P_j=|e_j\rangle\langle e_j|.
\]

Introduce a record object

\[
R_N=\bigoplus_{j=0}^{N}\mathbb C|j\rangle.
\]

The coherent record map is the isometry

\[
V_N:D_N\longrightarrow D_N\otimes R_N,
\qquad
V_Nx=\sum_jP_jx\otimes|j\rangle.
\]

Orthogonality and completeness give

\[
V_N^*V_N=\sum_jP_j=I.
\]

Reading the record basis yields the instrument

\[
\mathcal I_j(\rho)=P_j\rho P_j.
\]

Its effect is exactly

\[
\mathcal I_j^*(I)=P_j,
\]

and its total channel is trace preserving because \(\sum_jP_j=I\).

## Nondemolition property

For a state already supported on grade \(j\),

\[
\rho=P_j\rho P_j,
\]

so the selected branch obeys

\[
\mathcal I_j(\rho)=\rho,
\]

while all other branches vanish. The lift therefore records grade without changing a state already sharp in that grade.

For the rank-one atomic register, any instrument branch with effect \(P_j\) has measure-and-prepare form

\[
\mathcal J_j(\rho)=\operatorname{Tr}(P_j\rho)\sigma_j
\]

for some output state \(\sigma_j\). Requiring the output to remain supported on \(P_jD_N\) forces \(\sigma_j=P_j\). Hence the rank-one nondemolition instrument is unique at the channel level.

Pointer phases in

\[
V_N^{\phi}x=\sum_je^{i\phi_j}P_jx\otimes|j\rangle
\]

produce the same read instrument and are record-basis gauge, not distinct channel realizations.

## Unrestricted realization fiber

If nondemolition is dropped, choose arbitrary density operators \(\sigma_j\) and define

\[
\mathcal J_j^{\sigma}(\rho)
=
\operatorname{Tr}(P_j\rho)\sigma_j.
\]

Every such branch has effect \(P_j\), but different \(\sigma_j\) produce different post-readout states. Thus fixing effects alone does not make the full realization fiber contractible.

The fiber has:

- a distinguished Lüders point;
- an essentially unique rank-one nondemolition channel;
- many disturbance realizations when post-readout support is unrestricted;
- higher gauge equivalences among Stinespring dilations of the same channel.

## Cutoff naturality

Under the prefix inclusion \(D_N\hookrightarrow D_{N+1}\) and the matching record inclusion \(R_N\hookrightarrow R_{N+1}\),

\[
V_{N+1}|_{D_N}=V_N.
\]

The old highest grade retains its record label; only the predicate “currently terminal” moves to the appended grade. Therefore the instrument respects the same cutoff naturality as the Green–Ward register.

## Relation to Green and Ward coordinates

The instrument is defined on the retained source before applying either analytic realization. Transporting it through the invertible finite Green–Ward incidence map gives an equivalent instrument in complete cumulative coordinates. A terminal scalar compression cannot carry this full instrument because it identifies distinct grade effects.

Thus atomic and complete Ward observers lie in the same equivalence component of the finite observer core, while the scalar total is reached only by a noninvertible forgetting morphism.

## Strongest falsification and disposition

The conjecture that the instrument fiber is empty is falsified: \(V_N\) and \(\mathcal I_j\) explicitly inhabit it. The conjecture that effects determine a unique unrestricted instrument is also falsified by the family \(\mathcal J_j^{\sigma}\).

The surviving statement is conditional:

> In the finite completely positive process category, a complete rank-one orthogonal grade decomposition has a canonical cutoff-natural Lüders lift, unique among nondemolition instruments at the channel level; its unrestricted realization fiber contains inequivalent disturbance channels.

The remaining metaphysical boundary is not existence of a mathematical observer instrument. It is authority for selecting the completely positive process category and interpreting its record object and coupling as physically instantiated.
