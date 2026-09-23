# Paired B/D slope-face boundary currents cancel before singular pushforward

Although B and D have rank-seven source-to-target maps along `t=u` and their individual normal target jets differ, their **complete source maps are identical on that face** for arbitrary external twistors and all fermionic variables. Their independently computed oriented intrinsic eight-form densities are exact opposites. In the common ordered coordinates, the boundary seven-form residues are

```
Res_(t−u=0) Ω_B = + d(w₂,w₄,w₅,w₆,w₇,w₈,u)/(w₂ w₄ w₅ w₆ w₇ w₈ u),
Res_(t−u=0) Ω_D = − d(w₂,w₄,w₅,w₆,w₇,w₈,u)/(w₂ w₄ w₅ w₆ w₇ w₈ u).
```

The sign uses `dt∧du=d(t−u)∧du` and the six preceding weight coordinates. Thus, with the **same compact cutoff inside the positive source face**, the fully supersymmetric paired boundary integrands cancel **pointwise**, before any integration along the collapsed fibre. In two exact positive controls, contracting each nonzero face seven-form with its target-kernel direction gives nonzero, equal-and-opposite six-form densities; rank loss does not obstruct this **regulated boundary-current** cancellation.

**This does not prove cancellation of the singular pushed eight-forms or their target-space pole residues.** Individual positive fibre integrals may diverge at endpoints; a paired cutoff is essential. Taking a source residue and taking a residue of a singularly pushed target form need not commute. Other cells, target multiplicities and the global nine-point canonical form remain open.

Checker: `research/nima/checkers/check_nine_point_singular_face_regulated_boundary_current.py`; certificate: `research/nima/results/nine-point-singular-face-regulated-boundary-current.json`.
