# v136: split-collar induced physical readout

A split collar now supplies an explicit candidate physical readout rather than
only an abstract nonannihilation argument. Compose the physical-to-endpoint
retraction with the existing endpoint detector.

Module 164 proves that this induced readout evaluated on any transported
endpoint class equals the original endpoint detector value, by applying the
detector to the split path. In particular the transported W value is preserved
exactly. Thus endpoint nonvanishing transfers automatically for this induced
readout.

The remaining identification is sharper: prove that the actual supported
physical residue/readout agrees with the retraction-induced detector on the W
sector. No independent W-survival proof is then needed.

`rzk/164-split-collar-induced-physical-readout.rzk.md` passes all six
declarations without assumptions.
