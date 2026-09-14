# v193: ramified branch difference reaches the selected rank-one line

For the exact conductor roots `xi_plus=(-B+d)/(2A)` and
`xi_minus=(-B-d)/(2A)`, their odd difference is exactly `d/A`. Multiplication
by the unit `A/d` normalizes it to one. The deck involution negates the
unnormalized difference and preserves the resulting choice of odd primitive
orientation.

This normalized generator maps generator-preservingly to the log primitive
gamma, and the existing selected L2 comparison maps gamma's coordinate one to
`v=a^3+a^3b`, characterized by `rho0(v)=1`. Hence the ramified conductor,
logarithmic, and selected L2 free rank-one lines now have an explicit composite
comparison respecting both primitive coordinate and odd character.

This is a local ramified-road comparison, not yet the physical Cech equality.
The remaining descent must retain occurrence and branch labels and prove that
the descended class equals the raw physical Cech defect.

Evidence is `results/qg2-branch-difference-primitive.json`.
`rzk/221-qg2-branch-difference-selected-line.rzk.md` passes all eight
declarations without assumptions.
