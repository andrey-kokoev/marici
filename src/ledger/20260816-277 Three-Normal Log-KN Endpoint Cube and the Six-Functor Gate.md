# Three-Normal Log--KN Endpoint Cube and the Six-Functor Gate

Date: 2026-08-16  
Status: proved in the finite labelled log/Kato--Nakayama model. The literal
mixed-variance six-functor realization remains open. No graph admission is
claimed.

Entry 315 constructs one branch-selected log interval. At the positive
endpoint the three labelled branches are ordered \((1,3,5)\). Their tensor
product is the full Boolean cube

\[
C_{\log,+}=C(I_1,\partial_{x_1}I_1)\otimes
C(I_3,\partial_{x_3}I_3)\otimes
C(I_5,\partial_{x_5}I_5).
\]

It contains a canonical simultaneous top generator \(\eta_+\). Its boundary
is

\[
d\eta_+
=e_{\{3,5\}}-e_{\{1,5\}}+e_{\{1,3\}},
\]

which is exactly the coefficient pattern of the literal entry143
normal-removal row from
\([v_+,\{1,3,5\}]\). The polarity-conjugate cube uses \((0,2,4)\) and gives
the corresponding \(v_-\) row. Thus the three local odd counits are not
merely juxtaposed: their product canonically supplies the previously absent
three-normal source cell.

The executable checks all eight states on both endpoints, duplicates them
over two spectator conductor Tor-grade copies, verifies the Cech complement
label census, proves \(d^2=0\), and verifies cyclic and labelled sheet
exchange transport with the exterior signs. The three admitted one-branch
maps each carry sign \(-1\), so their product is odd before the once-relative
polarity twist. No integer or base function is inverted. This finite checker
does not construct the Tor or Cech differentials beyond the displayed Boolean
normal cube.

This closes the finite simultaneous-normal endpoint gap. It does not yet
construct the functor

\[
\operatorname{Sp}^{\log,!}(\mathcal S^{\rm norm,reg})
\longrightarrow E_{\partial,Q}^{\rm BM,\check C}
\]

that must identify these labelled cube states with the literal entry143
costalks while also carrying the hemisphere top to based \(q_\Sigma\).
Consequently the spatial endpoint comparison cells, pointed mapping fibre,
physical parity, and Bockstein remain undefined.

## Certificate

- `research/voevodsky/check_three_normal_log_kn_endpoint_cube.rs`

~~~json
{
  "claim": "The three labelled one-normal log/KN intervals tensor canonically to the full simultaneous endpoint Boolean cube, including the top (+,-,+) boundary and both spectator Tor grades.",
  "status": "proved_scoped_finite_three_normal_log_KN_endpoint_cube",
  "endpoint_labels": {"plus": [1,3,5], "minus": [0,2,4]},
  "states_per_endpoint": 8,
  "spectator_Tor_grade_copies": 2,
  "state_Tor_census_rows": 32,
  "top_boundary_coefficients": [1,-1,1],
  "D3": true,
  "polarity_top_character_before_twist": -1,
  "integer_inverted": false,
  "literal_six_functor_realization": "unconstructed",
  "based_qSigma_connector": "unconstructed",
  "physical_p_partial_Q": "undefined"
}
~~~
