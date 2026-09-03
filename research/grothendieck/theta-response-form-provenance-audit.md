# Provenance audit for theta Green response forms

## Decision

No approved packet supplies instantiated finite-cutoff Green response forms
`A_X=S_X^*S_X` and `Q_X` on a common theta state module. Their generalized
eigenvalue and any comparison with `D_theta` are therefore undefined.

## Inventory

### Approved common-path extension

Around lines 2024--2079, the extension introduces `S_X`, `A_X`, and `Q_X` as
the exact operator form that a future source construction would need. It then
states explicitly that no response matrices, uniform gap, or completion
estimate are supplied. The forms are a conditional theorem target, not source
data.

### Poisson--Clark generalized-eigenvalue packet

`research/kitaev/theta-poisson-clark-generalized-eigenvalue-gate.md` proves the
abstract matrix criterion for a typed decomposition `E_X=Q_X+R_X`. Its theta
status section says that the common-module `E_X`, typed `R_X`, and cutoff
covariance have not been supplied, so the actual theta interval is undefined.
This packet cannot instantiate the Green response pair.

### Clark--seam pro-Gram packet

`research/kitaev/theta-clark-seam-pro-gram-instantiation.md` reaches an earlier
typing obstruction. Only three of five proposed feature rows are admitted;
primitive and prime-square incidence maps, the archimedean row, and the full
mixed Green matrix are missing. Consequently the full feature Gramian and
finite dynamics cannot be assembled, and no generalized eigenvalue exists.

### Canonical theta diffusion

`research/grothendieck/theta-source-diffusion-canonical-compression.md`
constructs a valid scalar source operator `A_Phi` and canonical spectral
projections. It explicitly does not construct the comparison `T_s`, its Green
identity, or an RH Fredholm pair. This `A_Phi` is not the forced-response form
`A_X=S_X^*S_X`; symbol similarity gives no bridge.

Other repository hits reuse `A_X`, `Q_X`, or `rho_X` for unrelated anomaly,
incidence, determinant, arithmetic-renormalization, and observability objects.
None has the required common domain and Green semantics.

## Minimal construction request

The first executable bridge packet must provide, on one labelled cutoff module
`U_X` and with cutoff transition maps:

1. a source-derived forced-response map `S_X(z): U_X -> H_X+H_X`;
2. `A_X(z)=S_X(z)^*S_X(z)`;
3. a Hermitian residual form `Q_X(z):U_X->U_X` derived from the same Green
   identity;
4. the theta parameter/readout map connecting `(q,y)` to `(X,z,a)` on the
   selected state;
5. a proved inequality relating `D_theta(q,y)` to the Rayleigh quotient of
   `(Q_X,A_X)`; and
6. descent and cutoff-uniform bounds in the declared completion.

Only after items 1--4 are typed is the generalized-eigenvalue computation
meaningful. Item 5 is the actual `D_theta` bridge. Even a successful bound below
one settles residual absorption only; endpoint-current and constraint closure
remain independent gates.
