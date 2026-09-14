# v182: selected physical amplitude witness assembled

The corrected five-direction lift and point-supported detector law now assemble
into one selected physical amplitude witness. Its data are:

1. one road/group-corrected five-direction lift;
2. three supported detector functionals;
3. the calibrated residue equality on the Gysin class of that lift's physical
   point.

The witness exposes both the physical point and its residue value, and proves
that value equals the calibrated three-coordinate expression. This is the
pointwise inhabitance target actually needed for one amplitude; it avoids the
unnecessary global supported law in module 131.

The closure of `rzk/210-selected-physical-amplitude-witness.rzk.md` together
with its point-supported detector dependency passes with no assumptions.

No concrete physical inhabitant is claimed. The remaining data are explicit:

- raw physical Cech residual equals `Cech(v)`;
- primitive log road boundary equals `Cech(v)`;
- raw group defect equals the supported reflection-cell boundary;
- primary and reciprocal detector comparisons on the selected Gysin class;
- the single residue formula `-beta(a+(b+c))` on that class.
