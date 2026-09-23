# Seven-point fibre coverage must count closed cells on shared walls

The first extension of the fibre test beyond a single positive source gauge found an important correction to the candidate coverage question. A STRICTLY positive seven-column source may project to a target on a wall shared by two candidate image cells. In that case neither **open** cell contains the target, but both CLOSED images do. Counting only exact interior zero patterns produces a false coverage failure.

In 360 deterministic exact rational tests spanning one, two and three initial negative source columns (all 21 ordered source minors are checked strictly positive), the membership histogram is:

- 358: one open member, one closed member;
- 2: no open member, two closed members;
- 0: no closed member or more than one open member.

Both boundary exceptions have independently checked coincident candidate fibre vertices:

1. cells 0 and 5 meet at `(-2/15,-18/5)`, where column 5 vanishes and minor 23 also vanishes;
2. cells 4 and 5 meet at `(-7/15,-28/5)`, where column 5 vanishes and minor 71 also vanishes.

The checker lists ALL active ordered minors, not just the nominal constraints, and verifies the coincident inverse coordinates and absence of negative minors. The first wall was already supported by an exact source-residue equality and opposite local image sides. The second (4/5) wall is a NEW adjacency obligation: neither its target orientation nor its symbolic source-form residues have yet been checked.

This finite census does not prove global closed-cell coverage or uniqueness of the open chamber. It shows what a correctly stated universal theorem must distinguish: exactly one OPEN sector at generic targets, at least one CLOSED sector at all targets, and coherent multiple closed memberships along common walls. The next exact geometric step is the 4/5 wall calculation, followed by a complete active-set classification of the fibre halfspaces.

Run `python research/nima/checkers/check_seven_point_multichamber_stress.py`. Evidence: `research/nima/results/seven-point-multichamber-stress.json`.
