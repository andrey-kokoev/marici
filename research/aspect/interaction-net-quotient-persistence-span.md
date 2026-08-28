# The quotient instrument is a persistence span

Benincasa's depth transition is noninjective in both charts.

The depth-three quotient has dimension 53. Its image at depth four has
dimension 33, leaving a 20-dimensional kernel. The depth-four quotient has
dimension 1386, so its cokernel relative to the old image has dimension 1353.

The first transition has three sectors:

- 33 channels transported from depth three to depth four;
- 20 depth-three channels that do not lift;
- 1353 genuinely new depth-four channels.

Deeper transitions refine this into a barcode. Of the original 53 classes, 20
die by depth four, another 6 die by depth five, and 27 survive through both
depth five and depth six. Survival beyond depth six is unknown.

There is no lossless restriction that turns this into the earlier inverse
pro-instrument tower. Dually, the map from depth-four observables to
depth-three observables has rank 33. Twenty low-level observables are not
restrictions of high-level observables, and 1353 high-level observables vanish
on the transported old image.

This is experimentally useful. A quotient-aware optical design should split
into barcode banks: 20 first-death channels, 6 second-death channels, 27
through-depth-six transport channels, and 1353 depth-four emergence channels.
Calling all 33 first-step survivors persistent would be false.

Ranks do not synthesize optics. Physical construction still needs coefficient
rows for image, kernel, and cokernel bases in the source-labelled carrier,
together with chart transition data. Those rows would compile into coherent
mode-transform networks followed by calibrated homodyne or intensity readout.
