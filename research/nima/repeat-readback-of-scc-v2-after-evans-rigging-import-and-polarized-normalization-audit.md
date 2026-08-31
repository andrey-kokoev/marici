# Repeat readback of SCC v2 after Evans-rigging import and polarized-normalization audit

## Mutable-state readback

The SCC v2 contract changed during this work. Its current digest is

```text
44d3fa22c7ad883b04bff130828e7bc852ac93c8edb27ad7caad3ae6fd593ddd
```

It now imports the Evans-rigging witness and replaces the old undifferentiated
limiting-absorption node by explicit history-domain, block-domain,
five-port-summability, maximal-isotropic Evans-domain, and global-response
nodes.

## Correct changes

The revised contract now records as constructed:

- exact Evans history domain;
- three-port block-domain membership;
- five-port arithmetic summability;
- maximal-isotropic Evans history domain.

It keeps open:

- prime-shell residual cancellation;
- global Fourier--Poisson response intertwining;
- Evans-to-conservative chain map;
- local module length;
- seam confinement;
- RH.

It also records the full residual-jet family rather than only the zeroth
residual.

## Remaining dependency defects

### Exact Evans domain has the wrong parent

The current node `exact_evans_history_domain` depends on
`conservative_green_complex`. Its proof instead uses the two-sided Evans source
integrals, theta decay, and exact mismatch. It should depend on
`two_sided_evans_matching_lift` and the theta source class. Conservative Green
promotion is downstream, not upstream.

### Prime-shell residual needs the Evans constructor in its ancestry

The shell family is evaluated on \(u_z\). Its current ancestry passes through
`five_port_arithmetic_summability`, but that node reaches an
`exact_evans_history_domain` which presently omits the two-sided lift. Repairing
the previous edge repairs this ancestry; alternatively add the two-sided lift
directly.

### Port summability is not final source normalization

The imported witness proves continuity and arithmetic summability for the
declared five proposed ports. Later audit separates this from construction of
one final source-normalized G4 adjoint. Two comparison gates remain:

1. completed polarized Stokes--Wronskian metric transport;
2. stratified contragredient Fourier--Poisson response transport.

The contract currently places the second under global response intertwining but
has no node for the first. Add
`polarized_stokes_wronskian_metric_comparison` between five-port summability and
the final prime-shell residual.

## Independently verified local blocker

The one-dimensional odd comparison gives only

\[
 \lambda_p=-\frac{\kappa_p}{2s_p}.
\]

The full retained quadratic comparison requires

\[
 G_S=T_p^*G_WT_p,
 \qquad
 T_p=\operatorname{diag}(\alpha_p,\lambda_p),
\]

including both diagonal entries, the real mixed tail, and the reciprocal-odd
entry. Repository search finds no completed theorem with this matrix identity;
the present occurrences are the newly stated open gate.

Thus the next computation cannot be performed without source definitions of
the G4 even coefficient \(\alpha_p\) and the complete source/target polarized
matrices. Reusing unrelated symbols named \(\alpha_p\) from auxiliary history
packets would smear types.

## Disposition

The SCC revision correctly imports the rigging progress but still omits the
polarized metric-comparison node and misorients one dependency. The bounded
quadratic-comparison objective is blocked at missing source matrix data, not at
analysis or completion. No RH conclusion is authorized.
