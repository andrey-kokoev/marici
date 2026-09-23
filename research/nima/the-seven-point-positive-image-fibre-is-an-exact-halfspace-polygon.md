# The seven-point positive-image fibre is an exact halfspace polygon

This is the first **direct**, rather than analogical, transfer from the recent polyhedral-selector work to the seven-point NNMHV positive-cell problem.

For fixed positive external `Z` of size 7x6 and any target representative `Y`, choose one source representative `C0` with `C0 Z=Y`. The one-dimensional left kernel of `Z` has generator

    k=(1,-6,15,-20,15,-6,1).

Every other source representative with this same `Y` is

    C(a,b)=C0+[a,b]^T k.

Every ordered rank-two minor is **affine** in `(a,b)`: the apparently quadratic `ab*k_i*k_j` terms cancel. Thus positive lifts over a fixed target are exactly the intersection of 21 rational halfplanes in a two-dimensional fibre. A zero-column candidate is the intersection of two coordinate equations; a separated-pair candidate is the intersection of two minor-support lines. This is a genuine polyhedral section/fibre problem, although the base positive geometry is eight-dimensional and source canonical forms are differential forms rather than atom-valued selectors.

The new exact checker reconstructs all 21 inequalities. In 160 deterministic rational top-source trials in a monotone coordinate gauge, each fibre has precisely one of the six repaired candidate lifts (all in cell zero). Crucially, this gauge does NOT explore all positive chambers. To control that bias, the checker also starts from each of the six candidate source cells and makes a small nonzero rational left-kernel shift that renders **every one of the 21 ordered source minors strictly positive**, without changing `CZ`. Reclassification then finds one candidate lift in each corresponding sector: `[0],[1],[2],[3],[4],[5]`. This demonstrates all six cells have access to strictly positive full source fibres; they are not merely boundary artefacts of the positive image.

This is finite evidence, **not** a universal six-cell coverage theorem. The executable next gate is an exact polygon theorem: for every strictly positive source matrix, prove the halfspace fibre has exactly one vertex in the six prescribed candidate strata (and handle degenerate fibres and shared walls separately). This may be approached by enumerating feasible active-set types of the 21 affine minors and proving the resulting oriented-matroid sign implications. Such a theorem would be a real use of the new boundary-obligation and cover discipline, rather than transplanting its hexagon formula count. It still would not by itself prove the six source canonical forms match the physical generalized-R histories or derive the analytic `n^-2` cutoff law.

The source of the previously proposed triple-parallel failure is transparent in this language: two neighboring minor constraints can have dependent fibre normals. Their intersection is a line of positive lifts, not a vertex. The zero-middle-column branch supplies two independent coordinate constraints instead.

Run `python research/nima/checkers/check_seven_point_fibre_polygon_stress.py`. Exact result: `research/nima/results/seven-point-fibre-polygon-stress.json`.
