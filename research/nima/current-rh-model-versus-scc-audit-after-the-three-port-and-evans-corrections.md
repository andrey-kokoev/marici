# Current RH model versus SCC audit after the three-port and Evans corrections

## Question

Does the current RH constructor state agree with the checked SCC interaction-net
contract, and does an SCC pass certify the current model?

## Executed SCC checks

The canonical contract is

`research/aspect/contracts/theta-rh-interaction-net-state.v1.json`.

Executed through structured-command MCP:

```text
python research/aspect/scc/scc.py doctor
python research/aspect/scc/scc.py rh-state research/aspect/contracts/theta-rh-interaction-net-state.v1.json
```

Results:

- SCC doctor: healthy;
- Python: CPython 3.14.6;
- discovered models: 38;
- manifest errors: none;
- path issues: none;
- RH state compiler exit code: 0;
- contract result: `passed: true`;
- terminal remains `open` with `rh_proved: false`.

This pass certifies the frozen contract topology and hostile basis. It does not
certify that the contract represents every later RH result.

## Agreements

The current model and SCC agree on these structural points:

1. RH remains unproved and the terminal must remain open.
2. Coercivity and Xi spectral identification are independent witnesses.
3. A global positive margin is forbidden because the seam must retain the
   possible divisor defect.
4. A strict zero-free diagonal carrier cannot itself carry Xi zeros.
5. Scalar determinant equality cannot replace source spectral identification.
6. Arithmetic-to-analytic incidence, transport, completion, determinant line,
   and kernel exclusion remain separately typed.
7. Algebraic/passive realizations cannot be promoted to source realizations
   without an explicit intertwiner.

## Contract drift

### Determinant ideal classes

The SCC contract is organized around

- `det2_higher_prime_power_packet`;
- `finite_det_det2_trace_comparison`;
- `det2_anomaly_identification`.

The current G4 audit distinguishes instead:

- bare Euler loop: \(\det_3\), with primitive and square anomaly lines;
- reciprocal relative return: \(\det_2\);
- centered seam return through \(B_\Sigma\): trace-class ordinary Fredholm
  factor where the bounded chart exists.

SCC currently lacks separate nodes for these three determinant objects and can
therefore miss double counting or a det2/det3 variance substitution.

### Theta divisor versus conservative pencil

The current model has three distinct objects:

1. the theta Koszul complex
   \[
   K_\tau:\mathcal L_\theta\xrightarrow{\tau}\mathcal O;
   \]
2. the exact two-sided Evans matching complex;
3. the conservative maximal-isotropic Green pencil.

The SCC contract contains only the downstream slot
`xi_boundary_pencil_spectral_identification`. It does not represent the
triangular divisor compiler separately from the RH-bearing chain map into the
conservative pencil.

### Three-port source typing

The source carrier is

\[
H\oplus\mathbb C_\theta\oplus U_{\rm ar},
\qquad
D_\theta=0,
\qquad
R_{\theta U}=0
\]

before propagated history returns. SCC lacks explicit nodes enforcing:

- theta forcing and arithmetic incidence are different ports;
- no primitive direct theta--arithmetic dynamic arrow exists;
- \(V^\dagger B_\Sigma\) is a Gram/readout compression, not source dynamics.

### Same-sign passive no-go

For a strict same-sign Cayley complement, every seam kernel has arithmetic
coordinate zero. Such a complement can control nondivisor directions but
cannot create an arithmetic-dressed Xi zero. The current hostile
`strict_diagonal_carrier_claims_zeros` is related but weaker: it does not test
the full three-port kernel implication.

### Centered incidence range

The centered seam incidence obeys

\[
\ker B_\Sigma=0,
\qquad
\Phi\in
\overline{\operatorname{ran}B_\Sigma}
\setminus
\operatorname{ran}B_\Sigma.
\]

SCC has no fields distinguishing exact range, closure of range, injectivity,
and source-energy cost. Consequently a contract revision could accidentally
promote closure membership to an exact forcing lift.

### RH-bearing adjoint residual

For the unchanged Evans state, the arithmetic source coordinate is forced to
zero and Green promotion reduces to

\[
B_\Sigma^\dagger u_z=0.
\]

Because \(\Phi\in\overline{\operatorname{ran}B_\Sigma}\), this implies
\(V^\dagger u_z=0\). Together with the Green identity it proves critical-seam
confinement. This residual is therefore the RH-bearing theorem itself.

SCC currently hides it inside `xi_boundary_pencil_spectral_identification` and
`off_seam_kernel_exclusion`; it does not expose the cutoff-natural
prime-shell residuals as hostile witnesses.

## New hostile fixtures required

A current SCC contract should reject:

1. bare Euler \(\det_3\) replaced by relative \(\det_2\);
2. relative \(\det_2\) counted again as a bare Euler factor;
3. theta Koszul stabilization claimed as an independent Green spectral
   realization;
4. strict same-sign arithmetic feedback claimed to create a seam zero;
5. \(\Phi\in\overline{\operatorname{ran}B_\Sigma}\) promoted to
   \(\Phi\in\operatorname{ran}B_\Sigma\);
6. \(V^\dagger B_\Sigma\) promoted from Gram compression to primitive dynamic
   coupling;
7. scalar Evans mismatch claimed to imply
   \(B_\Sigma^\dagger u_z=0\);
8. full adjoint cancellation claimed without every prime-shell Green residual;
9. seam scalar continuation substituted for a maximal-isotropic history
   state;
10. pointwise kernel inclusion substituted for local module-length
    preservation.

## Revised SCC topology

A future owner-reviewed contract should insert these nodes before the terminal:

- `theta_koszul_divisor_complex`;
- `two_sided_evans_matching_lift`;
- `bare_euler_det3_with_two_anomaly_lines`;
- `relative_reciprocal_det2_return`;
- `centered_trace_class_seam_return`;
- `three_port_source_separation`;
- `zero_free_arithmetic_complement`;
- `prime_shell_adjoint_residual_family`;
- `seam_limiting_absorption_domain`;
- `evans_to_conservative_green_chain_map`;
- `holomorphic_mapping_cone_complement`;
- `local_module_length_preservation`.

The terminal must depend on the chain map and Green confinement, not merely on
having both a coercivity packet and a scalar determinant section.

## Verdict

The existing SCC contract passes and remains conservative, so it does not
conflict with the current RH status. It is nevertheless stale as a model of
the current G4 frontier. Its pass is a valid consistency certificate for the
older interaction net, not a validation of the corrected three-port,
determinant-line, Evans, or prime-shell architecture.

The current RH model fails SCC completion at the source chain map

\[
K_\tau\longrightarrow C_{\rm FP},
\]

whose unchanged-Evans component is the RH-bearing vector identity

\[
B_\Sigma^\dagger u_z=0
\]

on the Xi divisor. No RH conclusion is authorized.
