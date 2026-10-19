# Frozen-rule lithium discrimination probe

## Protocol fixed before running the sweep

Targets: neutral Li-5, Li-6, Li-7, Li-8 (3 protons, respectively 2/3/4/5
neutrons, and 3 electron carriers). Empirical comparison: Li-6/Li-7 stable;
Li-5 unbound and Li-8 radioactive. Empirical labels are not search inputs.

Use the unchanged 343-cell domain, root proton 0, MMCC roles, PN/MCM,
NN/MCC with the existing reference assumption enabled, and terminal NE/MCC.
Every neutron must have a native proton reader. The same three-electron
port budget applies in all cases. Only the supported target-count range of
the enumerator is widened; no interfaces, phase laws or acceptance tests change.

Enumerate all bounded geometry candidates and every PN reader assignment.
Use `compilePhaseAssembly` and `auditPhaseAssembly` without changing their
acceptance rules. Do NOT filter to retention of a selected earlier isotope:
that would compare different search scopes. The viewer's retained-Li-6 Li-7
selection is therefore not the sampling rule for this experiment.

Report search prefix counts, typed nuclei, geometry candidates, tested reader
assignments, rejection reasons, admitted assignments and admitted geometries.
Keep one concrete accepted candidate per isotope as a reproducible witness.
No cutoff, timeout or untested remainder counts as rejection. Complete sweeps
are required for negative results. Do not add the controls to the viewer.

## Interpretation fixed in advance

An accepted unstable isotope refutes the proposition that these compatibility
rules alone are a sufficient criterion for stability. Rejection of a stable
isotope is a limitation of this bounded ansatz, not a physical impossibility.
A successful stable/unstable split would only be evidence in this small fixed
domain, not a derivation of binding energies or lifetimes.

Raw counts depend on representation, domain and enumeration multiplicities;
they are not probabilities, binding energies, or a fitted stability score.
Do not tune the grammar to the observed labels during this probe.
