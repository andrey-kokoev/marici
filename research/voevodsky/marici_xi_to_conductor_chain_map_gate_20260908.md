# First Xi-Koszul to Marici-conductor chain-map gate

Date: 2026-09-08

## Proposed comparison

The arithmetic source is

\[
K_\tau=[\mathcal L_\theta\xrightarrow{\xi}\mathcal O_U].
\]

The first proposed target was the parameter-independent closed Marici coordinate `lambda_v` and its conductor line. A degree-zero comparison square would satisfy

\[
d\Psi_1=\Psi_0\xi.
\]

Because `lambda_v` is closed, the left side is zero. Therefore

\[
\Psi_0\xi=0.
\]

## Exact obstruction

The local holomorphic parameter ring is a domain and the germ `xi` is nonzero, hence `xi` is a non-zero-divisor. The parameter-independent conductor target has no declared `xi`-torsion. It follows that

\[
\boxed{\Psi_0=0}.
\]

Thus a direct chain map from `K_tau` to the closed detector complex cannot transport the Xi cokernel residue nontrivially. This failure occurs before reflection, multiplicity, completion, or off-critical conservativity.

## Available repairs

Three typed repairs exist:

1. base-change the Marici detector to the Xi divisor `O_U/(xi)`;
2. tensor the detector complex with `K_tau`;
3. construct a parameter-dependent Marici differential whose torsion or determinant section is `xi`.

The first two produce valid supported objects, but simply importing `xi` into the target is tautological and cannot by itself prove RH. The third is the nontrivial route: `xi` must arise from the additive–multiplicative comparison or another source-derived parameter family.

Consequently the next useful object is not an arbitrary map from the Xi Koszul complex into a constant conductor line. It is a parameterized comparison complex whose differential already contains the theta/Euler comparison and whose endpoint specialization maps to `D35/D04`.

## Verification

```sh
python research/voevodsky/check_marici_xi_to_conductor_chain_map_gate_20260908.py \
  --root . \
  --output research/voevodsky/marici_xi_to_conductor_chain_map_gate_certificate_20260908.json
```

The checker performs six exact structural assertions and records the forced zero comparison.
