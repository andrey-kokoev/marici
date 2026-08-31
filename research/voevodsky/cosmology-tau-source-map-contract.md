# Source-map contract for the universal p-normal lift cell

## Question

After classifying the universal cell \(\tau_p\), what exact source map must be constructed before the relative Bockstein line can advance?

## Claim boundary

This packet defines an interface contract and checks whether current mutable packets satisfy it. It does not construct a resolved/Rees exceptional generator, logarithmic Čech--de Rham cone cell, Cayley--Menger face cone, Bockstein class, global contour, or physical period.

## Disposition

The universal target cell is

\[
d\tau_p=\Xi_{\log}+(-\sigma_{123}).
\]

A source construction must supply a degree-one generator or cone cell whose differential maps to the vector

\[
(1,1)
\]

in the rows \((\Xi_{\log},-\sigma_{123})\), with coefficient \(\pm1\) over \(\mathbb Z\). Nonunit multiples do not kill the primitive integral class. Reversing the normal or the ordered Čech face changes the sign but not the unit requirement.

The allowed source domains are now explicit:

- a resolved/Rees exceptional object for the ordered three-wall blow-up;
- a logarithmic Čech--de Rham cone cell with a chain map to the residue complex;
- a Cayley--Menger face cone with compensating residue and a chain map to the same target.

Current packets fail the contract at object existence. The frontier packet says the open route is the total chain-level lift of the source-ordered relative residue cocycle. The boundary-corner packet requires blowing up the coalescing three-vertex boundary corner and records Picard--Lefschetz variation as uncomputed. The post-candidate authority packet records the first failed gate as `total_Cech_de_Rham_chain_map_constructed`.

The checker represents current sourced generators by a zero-column matrix into rows \((\Xi_{\log},-\sigma_{123})\). Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), its coefficient rank is \(0\), while augmenting by the required vector \((1,1)\) gives rank \(1\). Thus current packets do not satisfy the source-map contract.

The next action is not another Laurent primitive search. It is to construct one allowed source domain and test whether its first differential column is the primitive vector \((1,1)\) up to sign.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_tau_source_map_contract.py`

Result:

- `research/voevodsky/results/cosmology_tau_source_map_contract.json`

Command:

- `python research/voevodsky/check_cosmology_tau_source_map_contract.py`
