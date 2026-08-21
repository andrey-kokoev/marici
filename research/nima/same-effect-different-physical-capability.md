# Same effect, different physical capability

## Hostile comparison

The one-mode Unruh–DeWitt pilot could conceivably have made the distinction
between record and update look special to absorption. We therefore compare it
with a source-motivated quantum-nondemolition controlled-pointer coupling.

A QND measurement is designed so that the measured eigenstate is retained
while information is coherently mapped to an ancilla. This operational
criterion is realized experimentally in ancilla-coupled spin readout and in
ancilla mappings of stabilizer eigenspaces. Relevant primary sources are
Nakajima et al., arXiv:1904.11220, and Barreiro et al., arXiv:1104.1146.

Take

[
H_{m QND}=g,|1anglelangle1|otimessigma_x
]

with the pointer initialized in (|0angle_A), followed by an energy-basis
pointer readout. At the same exact coupling point

[
c=cos	heta=rac35,qquad s=sin	heta=rac45,
]

the induced system Kraus maps are

[
Q_0=|0anglelangle0|+c|1anglelangle1|,
qquad
Q_1=-is|1anglelangle1|.
]

Compare these with the absorptive UDW maps

[
A_0=|0anglelangle0|+c|1anglelangle1|,
qquad
A_1=-is|0anglelangle1|.
]

## Same public records

Both instruments have exactly the same effects:

[
A_x^dagger A_x=Q_x^dagger Q_x,
]

namely

[
E_0=|0anglelangle0|+c^2|1anglelangle1|,
qquad
E_1=s^2|1anglelangle1|.
]

Therefore every input state gives the same complete outcome distribution in
both experiments. No amount of single-use record statistics distinguishes the
two capabilities.

## Different write semantics

On a click,

[
A_1ho A_1^dagger=s^2ho_{11}|0anglelangle0|,
]

whereas

[
Q_1ho Q_1^dagger=s^2ho_{11}|1anglelangle1|.
]

The absorptive detector removes the excitation. The QND pointer records it
without demolishing the measured population. Even after the outcome is
forgotten, the channels differ:

[
mathcal A(ho)=
egin{pmatrix}
ho_{00}+s^2ho_{11}&cho_{01}\
cho_{10}&c^2ho_{11}
end{pmatrix},
]

[
mathcal Q(ho)=
egin{pmatrix}
ho_{00}&cho_{01}\
cho_{10}&ho_{11}
end{pmatrix}.
]

Sequential behavior is also different. Two absorptive clicks are impossible
in the single-excitation sector, (A_1^2=0), while (Q_1^2
eq0): the QND
measurement can report the retained excitation again.

## Result

[
oxed{
	ext{effect algebra + all single-use probabilities}
;
otRightarrow;
	ext{physical instrument}.
}
]

This is stronger than the earlier UDW-versus-formal-Lüders comparison because
both sides now arise from explicit interaction capabilities. The distinction
survives selective updates, forgotten outcomes, and sequential composition.

For Marici, the sector lens cannot be only a map to observables. It must either
contain or be accompanied by a typed interaction capability. If the shared
Carrier explains physics at this level, it must constrain which capabilities
are admissible—not merely which probability tables can be displayed.

Exact verification:

- `research/nima/checkers/check_same_effect_different_capability.py`
- `research/nima/results/same_effect_different_capability.json`
