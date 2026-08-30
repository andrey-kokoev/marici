# The universal conductor closes the six mixed coefficient boundaries

Date: 2026-08-23

The eight octahedral comparison faces split intrinsically into six mixed
faces and two pure-sheet faces.  On a mixed face, write (a,b) for its two
same-sheet vertices and (c) for its opposite-sheet vertex.  Entry 627's
universal conductor differential supplies the two cross-sheet differences.
Their difference is

\[
(\epsilon_a-\epsilon_c)
-(\epsilon_b-\epsilon_c)
=\epsilon_a-\epsilon_b,
\]

which is exactly the conductor restriction of the independently present
same-sheet edge.  Hence the coefficient boundary cancels on all six mixed
faces with no fitted scalar, division, or cross-line identification.

The universal conductor kernel is silent on the two pure-sheet faces:
neither boundary contains a cross-sheet edge.  A joint constrained solve of
the full reflection homotopy shows, however, that no pure face is needed.
There is a unique integral representative with (H_1) supported only on
the six mixed faces and (H_2=0).  Consequently:

\[
\boxed{
\text{minimal reflection homotopy}
=
6\text{ conductor-compatible mixed gates}.
}
\]

The two pure faces and relative interior remain part of the ambient
octahedral completion, but are gauge data rather than required cells for
this comparison.  The remaining legitimate gate is geometric: promote the
six mixed coefficient identities to actual support-changing
Beck--Chevalley transformations.

Evidence:

- `research/nima/checkers/check_tate_conductor_kernel_mixed_face_identity.py`
- Entries 255--258 and 627.
