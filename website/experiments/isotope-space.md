# Isotope and R-space viewer

[Open the interactive viewer](/experiments/particle-overlap-tetrahedron/tessellated-space.html)

Explore two **separate mathematical construction views**, not experimentally established nuclear geometry.

- **R-space tessellation** opens immediately and displays repeated proton/neutron/electron-labelled tetrahedra in the declared realization frame.
- **Isotope construction** displays the selected construction on its native tetrahedral grid. Choose an isotope to fetch its prepared geometry. Construction searches and source checks run during publication, not in your browser. Switching to R-space remains available while loading.

Drag to orbit; scroll or pinch to zoom. **Grid context** adds face-adjacent cell layers around the isotope. Returning to an already loaded isotope reuses its data for this session. Selecting another isotope cancels unfinished loading. If loading fails, use **Retry construction**.

[Open nitrogen-15 directly](/experiments/particle-overlap-tetrahedron/tessellated-space.html?view=isotope&isotope=nitrogen15)

## Scope and provenance

There is **no established placement map between the native isotope grid and the R-space tessellation**. Switching views does not identify their coordinates. Labels and constituent counts describe the supplied models; they do not establish nuclear binding, measured masses, or physical particle identity. Realization levels are not physical time.

The authoritative implementation is [the research demo source](https://github.com/andrey-kokoev/marici/tree/main/research/strominger/demos/particle-overlap-tetrahedron). The website publishes copies through `prepare_particle_overlap_viewer.mjs`; models are not independently maintained in the public directories. Each geometry asset is checked against the published manifest's SHA-256 digest before display. Export validates constituent counts and native cells for every isotope, and runs the phase-certificate audit for phase-assembly models; this is not a new physical verification claim.

See also [reader fields and their verification boundaries](/research/results/tessellated-reader-fields) and the [construction gallery](/experiments/).
