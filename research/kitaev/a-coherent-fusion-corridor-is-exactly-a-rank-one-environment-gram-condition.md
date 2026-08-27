# A coherent fusion corridor is exactly a rank-one environment Gram condition

## Bounded question

What exact condition distinguishes a coherent fusion–wait–unfusion phase gate
from a process that returns the anyons correctly but has measured or dephased
their fusion channel?

When the corridor preserves the three fusion channels without mixing, its
logical channel is a Schur multiplier by the Gram matrix of the branch-dependent
environment states. It is a unitary phase gate exactly when that Gram matrix
has rank one.

## Closed-corridor dilation

Use the protected qutrit basis

\[
|e_L\rangle,
\qquad
e\in\{A,B,C\}.
\]

Assume the complete physical corridor starts with one environment and
workspace state \(|0\rangle_E\), preserves the pair-channel label, and returns
the encoded anyons to their original positions and charge configuration. Its
most general isometric action under those assumptions is

\[
|e_L\rangle|0\rangle_E
\longmapsto
e^{i\phi_e}|e_L\rangle|\eta_e\rangle_E,
\]

with normalized environment states \(|\eta_e\rangle\).

The environment includes every unreturned degree of freedom:

- fusion workspace;
- transport controller;
- emitted radiation or phonons;
- position and timing records;
- charge-syndrome ancillas;
- and any macroscopic apparatus mode that can retain branch information.

Calling a register unobserved does not remove it from this dilation.

## Exact reduced logical channel

For logical density matrix

\[
\rho=\sum_{e,f}\rho_{ef}|e_L\rangle\langle f_L|,
\]

tracing the environment gives

\[
\mathcal C(\rho)_{ef}
=e^{i(\phi_e-\phi_f)}
G_{ef}\rho_{ef},
\]

where

\[
G_{ef}=\langle\eta_f|\eta_e\rangle.
\]

The matrix \(G\) is positive semidefinite and has unit diagonal. Therefore the
closed corridor is a completely positive trace-preserving Schur-multiplier
channel followed by the intended diagonal phases.

All charge populations are preserved for every \(G\). Correct final charges
and pair-channel probabilities do not test the off-diagonal coherence factors.

## Unitary phase criterion

The logical channel is unitary and diagonal precisely when

\[
G_{ef}=e^{i(\chi_e-\chi_f)}
\]

for some phases \(\chi_e\). Equivalently:

- every pair satisfies \(|G_{ef}|=1\);
- all environment vectors lie on one common ray;
- \(G\) has rank one;
- the Schur channel has Kraus rank one.

The environment phases \(\chi_e\) can be absorbed into the logical phases
\(\phi_e\). Thus the physical requirement is not literally equal vectors but
one branch-independent environment ray.

If any pair has

\[
|G_{ef}|<1,
\]

the corridor has irreversibly reduced coherence between those logical fusion
paths.

## Lüders and partial-dephasing limits

If the environment states are mutually orthogonal, then

\[
G=I_3,
\]

and

\[
\mathcal C(\rho)
=\sum_eP_e^{(12)}\rho P_e^{(12)}.
\]

This is exactly the nonselective Lüders measurement of the first-pair channel.
The anyons may be returned to their initial positions afterward; the external
which-channel record still destroys qutrit coherence.

Intermediate overlaps produce partial dephasing. For example, if only the
vacuum branch emits a distinguishable record, coherences involving \(A\) are
suppressed while the \(B,C\) coherence may survive.

The environment Gram matrix therefore gives the complete interpolation between
coherent phase actuation and destructive fusion measurement under the
channel-preserving assumption.

## Rank is the constructor test

The visible map on classical charge populations is the identity for every
allowed Gram matrix. The distinguishing test must access coherent input
superpositions and their off-diagonal outputs.

A complete finite corridor audit should report:

\[
G_{AB},
\qquad
G_{AC},
\qquad
G_{BC}.
\]

Rank one is the exact success condition. Merely observing nonzero overlaps is
insufficient for exact unitarity. A smallest singular value or determinant can
quantify departure from the rank-one manifold, but the physical error metric
must also include leakage and channel mixing.

## Channel-mixing boundary

The Gram theorem assumes the physical path does not mix \(A,B,C\) channels. A
more general closed corridor may act as

\[
|e_L\rangle|0\rangle_E
\longmapsto
\sum_f|f_L\rangle|\eta_{f|e}\rangle_E.
\]

Then one must reconstruct the full process matrix. A rank-one Gram test on the
diagonal branches alone does not exclude coherent or incoherent channel
transitions.

The source must separately prove pair-charge conservation along the path or
include all transition amplitudes in the audit. In the ideal topological model,
superselection can forbid some mixing; a microscopic time-dependent corridor
still needs a leakage and symmetry theorem.

## Gapped code-deformation model

A natural candidate corridor is a time-dependent local Hamiltonian \(H(s)\),
with \(s\in[0,1]\), that moves and fuses the first pair while maintaining an
isolated three-dimensional spectral band.

Let

\[
P(s)=P_A(s)+P_B(s)+P_C(s)
\]

be its spectral projector, with mutually orthogonal channel branches. Require:

- constant band rank three;
- a nonzero gap to unwanted excitations along the entire path;
- no channel mixing, or a fully known Berry connection;
- return of the endpoint projector to the storage code;
- and one common final environment ray.

In an adiabatic regime, each branch accumulates dynamical and geometric phases.
The closed logical action has the form

\[
U_{\mathrm{ad}}
=\sum_e
e^{i\gamma_e-i\int E_e(t)dt}
P_e^{(12)}
\]

when the Berry connection is channel diagonal.

The native vacuum split can make the \(A\) phase differ from the \(C\) phase,
supplying the bridge.

## Exact versus adiabatic claims

The Gram criterion is exact for the actual completed physical dilation. The
adiabatic construction is conditional and approximate at finite runtime unless
an exact counterdiabatic or solvable deformation is supplied.

A finite-time claim must give:

- the minimum gap;
- derivative norms of \(H(s)\);
- a runtime-dependent leakage bound;
- the non-Abelian Berry connection on the three-dimensional band;
- phase calibration error;
- and the final environment Gram matrix.

An open gap by itself does not prove a rank-one environment return. Slow
control can still emit a branch-dependent record through an uncontrolled
apparatus coupling.

## Workspace dimension is not the criterion

The \(A\) branch may contain no localized residual excitation while \(B,C\)
contain one. A unitary corridor can nevertheless remain coherent by placing
the branches in orthogonal system sectors during the middle of the path. The
environment need not be identical at intermediate times.

What matters is closure: after unfusion, every degree of freedom outside the
logical qutrit must return to a common ray. Branch distinguishability may be
temporarily internal to the controlled system and later erased coherently.

Conversely, matching the dimensions or energies of the final visible system
does not ensure closure if a radiation or controller mode retained the branch.

## Fault interpretation

The environment Gram matrix also classifies several corridor faults.

### Coherent overrotation

The environment remains rank one, but the phases \(\phi_e\) are wrong. This is
a unitary logical control error invisible to charge syndrome.

### Which-channel leakage

Some \(|G_{ef}|<1\). The corridor has created an external record and partially
dephased the qutrit.

### Full fusion measurement

The environment states are orthogonal and \(G=I\). The logical channel is
Lüders pinching.

### Channel transition

Amplitude appears in \(|\eta_{f|e}\rangle\) with \(f\ne e\). This is outside
the diagonal Gram model and requires the full process audit.

### Leakage from the qutrit band

The returned system is not wholly in \(V_{CCC}^{C}\). This is detected by the
code projector but must be bounded before output release.

These faults have different repairs. Charge-population checks distinguish only
some of them.

## Highest-information experiment

Prepare coherent superpositions of two fusion paths, run the closed corridor,
and interfere the outputs in a noncommuting fusion basis. For each pair
\(e,f\), the fringe visibility determines \(|G_{ef}|\), while its phase combines
the desired dynamical phase with the environment-ray phase.

Repeating only charge measurements after the corridor cannot estimate
\(G_{ef}\). The experiment must retain or reconstruct off-diagonal coherence.

This is an instrument test, not merely a spectral-energy test.

## Exact falsifiers

- Correct final anyon positions and charges used to infer coherent return.
- Pair-channel populations preserved while off-diagonal visibility is omitted.
- Mutually orthogonal environment records called reversible fusion.
- Rank greater than one called an exact unitary phase corridor.
- A rank-one diagonal Gram test used despite untested channel mixing.
- An open spectral gap claimed to imply branch-independent environment return.
- An adiabatic finite-time path called exact without a runtime error bound.
- Workspace equality checked while radiation or controller modes are excluded
  from the environment.
- Charge measurements alone claimed sufficient to reconstruct the corridor
  channel.

## Machine-readable corridor certificate

```json
{
  "code": "fusion_corridor_environment_gram",
  "logical_channels": ["A", "B", "C"],
  "channel_preserving_assumption": true,
  "gram_entries": ["G_AB", "G_AC", "G_BC"],
  "unitary_phase_condition": "rank(G)=1",
  "equivalent_condition": "all_environment_states_share_one_ray",
  "luders_condition": "G=identity",
  "partial_dephasing": "some_abs_G_ef_between_0_and_1",
  "population_preservation_sufficient": false,
  "channel_mixing_separately_audited": true,
  "gap_path_required_for_adiabatic_candidate": true,
  "finite_time_error_bound_required": true,
  "native_vacuum_phase_can_bridge": true,
  "microscopic_corridor_constructed": false
}
```

## Deutschian explanation

Fusion becomes a measurement only when some external system keeps the answer.
During a coherent gate, the pair channel may become locally visible and acquire
different energy, but every trace of that visibility must be gathered back
before the anyons separate.

The environment Gram matrix says whether this happened. Rank one means all
external histories recombined into the same physical ray, leaving only a
logical phase. Higher rank means the world outside the qutrit can still tell
which fusion history occurred.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier geometry is closure of a temporary exposure corridor: a
hidden relational variable may be made local during actuation only if every
external branch record is erased before the protected carrier is restored.

The quantum coefficient lens supplies environment overlaps, Schur channels,
Kraus rank, Berry phases, and coherent interference tests.

## Claim boundary

This packet proves the exact environment-Gram characterization for a
channel-preserving closed corridor and specifies a conditional gapped
code-deformation implementation. It does not construct a microscopic path,
prove channel conservation, compute a gap, or supply finite-time adiabatic
bounds.

## Process calibration

Excitement is 10/10 and confidence in the exact dilation theorem is 10/10. The
missing fusion constructor now has a decisive coherence certificate rather
than a qualitative cleanliness requirement.
