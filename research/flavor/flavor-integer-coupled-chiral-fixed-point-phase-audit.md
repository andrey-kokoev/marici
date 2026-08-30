# Integer Coupled Chiral Fixed-Point Phase Audit

## Question

Does the generalized Georgi--Glashow theory with both scalar sectors combine
WP803's asymptotic safety and WP804's direct chiral incidence into a complete
orientation-sensitive portal selector?

## Closest positive source

The source contains three Yukawa structures:

\[
\begin{aligned}
y_H&: T\widetilde F_1H,\\
y_1&: \widetilde F_1MF,\\
y_M&: \widetilde F_{j\ne1}MF.
\end{aligned}
\]

The first directly contains the anomaly-essential chiral tensor; the latter
two supply the mesonic contribution that was responsible for safety in WP803.
The literature identifies integer safe packets including ((N,p)=(5,26)).

At this packet, solving the three nonzero Yukawa fixed-flow equations gives

\[
\frac{a_H}{a_g}=\frac{68364}{15815},
\qquad
\frac{a_M}{a_g}=\frac{1458}{3163},
\qquad
\frac{a_1}{a_g}=\frac{3492}{15815}.
\]

Substitution into the gauge equation yields the exact truncated fixed point

\[
a_g^*=\frac{3163}{2234},
\quad
a_H^*=\frac{34182}{5585},
\quad
a_M^*=\frac{729}{1117},
\quad
a_1^*=\frac{1746}{5585}.
\]

All four beta functions vanish exactly. This is the first tested source with
integer anomaly-complete chiral matter, direct chiral portal incidence, and an
algebraically interacting ultraviolet fixed point in the same action.

## Perturbative-control failure

The achievement is not yet physically trustworthy. The normalized gauge
coordinate exceeds one and the chiral-tensor Yukawa coordinate exceeds six.
The fixed point lies outside the weak-coupling domain in which the admitted
two-loop gauge and one-loop Yukawa truncation can establish quantitative
existence or critical exponents. The exact zero is a property of the truncated
polynomials, not proof of a continuum theory.

## Coupling is not an orientation cycle

The beta functions couple the three squared magnitudes, but algebraic mixing
does not imply a physical phase invariant. On field phases
((T,\widetilde F_1,\widetilde F_{j\ne1},H,M,F)), the Yukawa charge matrix is

\[
Q=\begin{pmatrix}
1&1&0&1&0&0\\
0&1&0&0&1&1\\
0&0&1&0&1&1
\end{pmatrix}.
\]

It has rank three. Its transpose has zero kernel, so every Yukawa phase can be
removed by field rephasing. There is no rephasing-invariant odd product of
(y_H,y_1,y_M). The published coordinates (a_i=y_i^2/(4\pi)^2) consequently
collapse every sign packet.

This corrects WP804's preliminary heuristic: multiple coupled hyperedges are
necessary but not sufficient. The coupling incidence must have nonzero cycle
rank after quotienting by every legal field rephasing.

## Threshold and instrument gates

Scalar mass terms remain relevant deformations. Distinct positive masses give
distinct symmetry-breaking thresholds while leaving the dimensionless
truncated fixed point unchanged. Neither vacuum selection nor decoupling
matching is supplied. The intrinsic beta-function probe also has no calibrated
map to physical16.

## Classification

- Integer anomaly-complete chiral source: present.
- Direct chiral portal incidence: present.
- Interacting fixed point: algebraically present, nonperturbatively unverified.
- Portal orientation: absent after the full rephasing quotient.
- Threshold scale and vacuum: unselected.
- Physical16 instrument: absent.

## Smallest exact falsifiers

- Control: (a_H^*=34182/5585>6).
- Orientation: (ker Q^T=0).
- Threshold: masses one and four give distinct thresholds one and two at the
  same dimensionless fixed point.

## Disposition

The coupled integer source is a genuine progressive problem shift, but not the
answer. The next constructor must add an incidence edge that creates a nonzero
left kernel of the Yukawa phase-charge matrix, and its invariant phase must
enter beta functions through an interference term rather than only squared
magnitudes. Quantitative authority additionally requires a controlled fixed
point or independent nonperturbative construction, followed by vacuum,
threshold, and physical16 instruments.

Verification:

- checker: research/flavor/checkers/wp805_integer_coupled_chiral_fixed_point_phase_audit.py
- generated result: research/flavor/results/wp805_integer_coupled_chiral_fixed_point_phase_audit.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp805_integer_coupled_chiral_fixed_point_phase_audit.py
- primary source: [Mølgaard and Sannino](https://arxiv.org/abs/1610.03130)
