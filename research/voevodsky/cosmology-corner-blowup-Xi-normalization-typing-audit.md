# Corner-blowup Xi normalization typing audit

## Result

The exceptional valuation calculation is correct: on the blow-up of `(u,v,p)=(0,0,0)`, `ord_E(p)=1`, so `Res_E(dlog p)=1`. It does not directly identify `Xi_log` with `dlog p`.

The two objects occupy different cochain degrees. `dlog p` is a degree-one logarithmic form, whereas `Xi_log` is a degree-two circuit/residue class in the formal horn. A degree-shifting connecting or Gysin morphism is required between them. Exceptional valuation fixes that morphism's coefficient to a unit if the morphism exists; it does not construct the morphism.

## Correction

The prior packet's claim that the corner blow-up itself supplies the missing `Xi_log` leg is withdrawn. Its valid residue is narrower: `ord_E(p)=1` is the forced normalization test for a future resolved/Rees or logarithmic Cech-de Rham comparison.

## Next gate

Construct an explicitly sourced degree-shifting map from the resolved blow-up cone cell to `Xi_log`, verify compatibility with the exceptional Cech face and total differential, and only then test the `(1,1)` column.

## Verification

- `research/voevodsky/check_cosmology_corner_blowup_Xi_normalization_typing.py`
- `research/voevodsky/results/cosmology_corner_blowup_Xi_normalization_typing.json`
