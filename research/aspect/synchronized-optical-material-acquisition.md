# Synchronized Optical–Material Acquisition Packet

Owner: marici.Aspect

This rung prevents a joint Hamiltonian comparison from combining observables
drawn from incompatible experiments.

Each of the four channels retains its raw control coordinates, values,
uncertainties, covariance diagonal, run identity, sample identity, and
calibration identity. Admission requires one synchronized run, one material
sample, one calibration lineage, aligned support, positive covariance, and
preregistered uncertainty bounds.

The hostiles reject:

- channels cherry-picked across optical runs;
- observables taken from different material samples;
- missing covariance;
- uncertainty inflation used to conceal mismatch;
- mixed calibration lineages.

This is an executable packet contract and deterministic audit. No hardware
acquisition has yet been performed.

Run:

python research/aspect/checkers/check_synchronized_optical_material_acquisition.py
