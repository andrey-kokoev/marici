# Domain-wall localization magnitude fiber: WP757

## Question

Can a source-derived domain wall remove the anomaly-neutral localization
kernel and make the asymmetric flavor portal unavoidable?

## Claim boundary

The admitted model has a scalar kink, one anomaly-neutral vectorlike fermion
pair, and an interval of length \(L\). The kink-induced mass has magnitude
\(M>0\), and

\[
x=ML.
\]

Opposite mass signs give normalized chiral zero-mode profiles proportional to
\(e^{-My}\) and \(e^{My}\). Domain-wall trapping of chiral fermion modes is a
source-derived mechanism; analytic kink localization and its parameter
dependence are treated explicitly by
[George and Volkas](https://arxiv.org/abs/hep-ph/0612270).

## Exact overlap map

At the boundary \(y=0\), the dimensionless normalized densities are

\[
D_+(x)=\frac{2x}{1-e^{-2x}},
\qquad
D_-(x)=\frac{2x}{e^{2x}-1}.
\]

They obey

\[
\frac{D_+(x)}{D_-(x)}=e^{2x},
\qquad
D_+(x)-D_-(x)=2x.
\]

Thus the wall creates a genuine relative localization and can rigidify which
profile couples more strongly to a specified boundary. It is sensitive to the
anomaly-neutral relocation that defeated WP756.

But the domain-wall index is constant for every \(x>0\). Normalizability fixes
chirality and the sign class, not \(x\). For example, \(x=1/2\) and \(x=3/2\)
have the same chiral index but boundary-density contrasts \(1\) and \(3\).
More generally every positive desired contrast \(\Delta\) is reproduced by

\[
x=\frac{\Delta}{2}.
\]

Reversing the wall orientation exchanges the profiles and reverses the
labelled contrast. Therefore even its sign has authority only after the source
fixes both wall orientation and the assignment of kink charges to the labelled
flavor channels.

## Disposition

The domain wall is progressive relative to anomaly inflow: it is an admitted
operation that detects anomaly-neutral matter placement. It conditionally
selects a localization side and rigidifies a boundary readout. It does not
select the numerical portal.

The continuous fiber is now concentrated in \(x=ML\), whose factors include
the kink Yukawa coupling, wall scale, and interval length. The topological
index does not fix their magnitude, RG evolution, finite-width corrections,
KK thresholds, or radion stabilization. Nor is a normalized profile overlap
itself a detector instrument.

The next viable source principle must quantize or dynamically attract \(x\),
fix the labelled wall orientation, and provide threshold and detector maps in
the same source frame. Without those arrows, the kink is a localization
selector but not a Deutschian explanation of the portal.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp757_domain_wall_localization_magnitude_fiber.py

Generated result:
research/flavor/results/wp757_domain_wall_localization_magnitude_fiber.json
