# Lead-208 nucleus schematic

Question: show proton/neutron packing in the heaviest stable atom.
Interpretation: heaviest observationally stable isotope, lead-208, Z=82 and
N=126; not largest atomic radius. Both nuclear shell numbers are magic.
Bismuth-209 is radioactive. A neutral lead atom has 82 electrons, omitted here.

**Claim boundary:** the FCC marker layout is purely illustrative, not a nuclear
crystal, measured nucleon positions, quantum wavefunction, literal shell layering,
physical radius calculation or P/N/E-loom-derived packing. No nuclear force,
binding or stability law has been computed. Finite marker spacing is not a
physical coherence or size bound.

Open `index.html` directly in a browser: no server, CDN, network, package install
or publication is needed. Drag either canvas to rotate both, use arrow keys,
filter protons/neutrons, or reset. The second view removes a display wedge to
reveal interior markers without changing the isotope. Cutaway counts refer only
to markers being drawn, not changed constituent counts. Full view includes all
208 markers although front markers obscure some interior ones.

The deterministic FCC site selection and seeded color assignment are display
choices. Both views share the original unique marker IDs. Neither displayed
marker sizes nor sites should be read as a microscopic nuclear arrangement.

Verification and execution disposition:

    python research/aspect/scc/scc.py check lead-208-nucleus-v1 --verbose

The checker uses existing Playwright, offline file loading and real headless
Chromium. It verifies exact counts/IDs, center separation, scope labels, cutaway,
filtering, mouse/keyboard controls, reset and responsive sizing. It writes
`research/strominger/results/lead-208-nucleus/verification.json`, desktop image
`lead-208.png` and `lead-208-mobile.png`. Harness success verifies only the display.
No native assembly or nuclear-packing admission is gained.
