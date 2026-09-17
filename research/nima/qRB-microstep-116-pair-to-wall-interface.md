# qRB microstep 116: pair-to-wall interface

For each ordered pair response `rho_nm`, define the candidate wall interface by its retained boundary data:

$$
J_{nm}(\rho_{nm})
=\bigl(\gamma_0\rho_{nm},\eta_{nm}(\rho_{nm})\bigr).
$$

The interface must satisfy:

1. `gamma_0 rho_nm` reproduces the shell initial value;
2. `eta_nm` records the oriented Wronskian/flux datum;
3. the pair coefficient `alpha_nm` is preserved;
4. the map is continuous in the pair-response graph norm;
5. summation over `(n,m)` is controlled in the relative wall topology.

The existing scalar wall port provides the target two-coordinate shape, but does not yet define `eta_nm` or prove pairwise summability. Thus this is an interface contract, not an identification.

Status: pair-to-wall map typed; construction of the flux coordinate and its source estimate remains open.
