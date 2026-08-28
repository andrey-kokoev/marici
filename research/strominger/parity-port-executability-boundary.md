# Magnetic parity closure has an executable partial observer

The completed magnetic source canonically carries the reflection-helicity
involution (Q) and its complementary projectors

[
Pi_E=(1+Q)/2,
qquad
Pi_M=(1-Q)/2.
]

Their joint algebraic readout is faithful because
(Pi_E+Pi_M=1). This proves invariant closure: no transported distinction is
lost when both components are retained.

There is also an executable partial observer. The existing low-kernel theorem
supplies 21 source-authorized finite-integral ports for the magnetic
(l=2,3,4) coefficients. They minimally repair the low-mode kernel of the
grade-three magnetic readout.

Those 21 ports do not implement the full joint parity observer. They observe
only the finite magnetic low block. They do not supply the complementary
electric record, nor prove that electric and magnetic records can be bound to
the same prepared packet without destructive or decohering interaction.

The smallest missing constructor is therefore a source-authorized
complementary electric observer

[
mathsf I_E:
	ext{prepared transported packet}
longrightarrow
	ext{electric observation record},
]

together with a coherence cell binding that record to the existing magnetic
record from the same prepared packet.

| Claim | Verdict |
|---|---|
| complementary parity decomposition exists | proved |
| joint algebraic readout is faithful | proved |
| 21 magnetic low-harmonic ports are executable | proved |
| complementary electric observation is executable | not authorized |
| coherent joint acquisition is executable | not authorized |
| the nine-mode state is actuable or controllable | not constructed |

The hostile implications rejected are:

1. algebraic projection implies an unwitnessed executable measurement;
2. invertible joint coordinates imply simultaneous accessibility;
3. executable observation implies constructor or actuator authority.

Thus we do not need to add arbitrary state control. We already possess a
restricted executable observer. The remaining arrow is the complementary
electric instrument and its same-packet coherence binding. If those are
source-derived, full parity faithfulness becomes operational; state actuation
would remain a separate question.

## Why the electric repair is not another 21-port packet

The number 21 belongs to the magnetic low kernel of the grade-three spectral
multiplier. The preceding magnetic parity projection discards every electric
harmonic, not only (l=2,3,4). At harmonic cutoff (L), the real electric
dimension is

[
d_E(L)=sum_{l=2}^{L}(2l+1)=(L+1)^2-4.
]

Already (d_E(5)=32>21), and (d_E(L)) grows without bound. Therefore no
fixed finite family of scalar ports can restore full parity faithfulness on
the completed source. The missing electric observer must be field-valued, or
an unbounded separating family of coefficient ports.

A possible escape would be to treat the complete shear field as one
field-valued record and obtain electric coefficients by postprocessing. The
existing source audit does not authorize that escape. Its complete local shear
tests are scoped to the magnetic (l=2,3,4) block; it explicitly leaves the
observer class, accessible field region, and instrument execution undeclared.
Contextual point separation therefore cannot be promoted to full electric
field acquisition.

This does not conflict with the degree-nine grade recurrence. Nine is the
minimal state dimension of one scalar determinant sequence under the grade
shift; it is not the dimension of the transported magnetic field.

## Same-packet coherence is a pullback, not a product

Even separately executable electric and magnetic instruments would not yet
supply a joint observer. Their records must retain a common preparation
identity. Categorically, the admissible joint records form the fiber product

[
R_E	imes_{mathcal P}R_M,
]

where (mathcal P) is the prepared-packet object. The ordinary product
(R_E	imes R_M) permits records drawn from different packets and therefore
manufactures joint states that the source never supplied.

For two packets with records (p_0mapsto(0,0)) and
(p_1mapsto(1,1)), the ordinary product also admits ((0,1)) and ((1,0)).
Neither is a valid source record. The pullback retains exactly the two valid
pairs.

Preparation identity is an incidence type, not a temporal label. The
coherence requirement says that both records factor through the same source
object; it does not invoke before, after, or simultaneity.

## The pullback is necessary but not sufficient

A shared preparation identity proves provenance compatibility. It does not prove
that both acquisitions may be executed on one preparation. If the prepared
packet is a linear resource, either individual port may be valid while the
first acquisition consumes the capability required by the other.

Thus executable joint closure requires a joint refinement instrument

[
mathsf J:mathcal Plongrightarrow R_E	imes_{mathcal P}R_M
]

whose marginals reproduce the electric and magnetic instruments. Neither the
pullback object nor the two marginal instruments constructs (mathsf J).
Equivalently, copying or nondestructive reuse of the preparation must be
separately authorized.

The hostile fixture admits either electric or magnetic acquisition on one
linear packet, but rejects both orders of sequential composition. Both records
would carry the same packet identifier if they existed, yet no joint execution
exists. This separates provenance coherence from acquisition compatibility.

## Finite hostile witness

On one reflection orbit use sheet coordinates. Compare

[
x_0=(0,0),
qquad
x_1=(1,1).
]

The second state is a nonzero pure electric direction. Every currently admitted
magnetic acquisition gives the same record on the pair because
(Pi_Mx_0=Pi_Mx_1=0). The algebraic joint observer separates them because
(Pi_Ex_1=x_1
eq0).

This is the smallest witness requested by the instrument contract: the missing
capability is observable as an actual equivalence class of the admitted
acquisition, not inferred merely from the absence of a declaration.

Replay:

`python research/strominger/checkers/parity_port_executability_boundary_checks.py`
