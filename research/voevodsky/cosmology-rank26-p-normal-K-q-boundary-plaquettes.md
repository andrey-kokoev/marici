# Cutoff-face plaquette classification

## Result

The 30 boundary q-lift signatures at each K pole partition exactly into:

- five 2-by-2 plaquettes indexed by even first-coordinate anchors \(a=0,2,4,6,8\), each sharing one normalized signature across

\[
(a,8-a),\ (a,9-a),\ (a+1,8-a),\ (a+1,9-a);
\]

- four lower-edge singletons at odd degree-8 coordinates

\[
(1,7),(3,5),(5,3),(7,1);
\]

- six upper-edge singletons at even degree-10 coordinates

\[
(0,10),(2,8),(4,6),(6,4),(8,2),(10,0).
\]

Thus 15 templates per pole, 30 total, classify all 60 cutoff-boundary identities. Together with the two interior canonical templates, 32 presentation templates cover all 132 residual rows.

## Disposition

N3b3d2 and the boundary-classification branch are completed. N3b3 is completed at the finite presentation-template level: every residual identity is reconstructed and assigned to a bounded template.

This does not construct a source-natural homotopy. The signatures depend on pivot order, one prime, and the degree-14 cutoff geometry. The next active child of N3b is an ambient-degree/source-natural comparison: test whether the interior and boundary decomposition transports to another ambient degree without importing degree-14 row ordering.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_boundary_plaquettes.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_boundary_plaquettes.json`
