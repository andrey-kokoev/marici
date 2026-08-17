---
id: 436
date: 2026-08-17
title: The Physical Derived Pullback Is One Primitive Integral Line
---

# The Physical Derived Pullback Is One Primitive Integral Line

Entry 435 supplies the normalization-sheet arrow whose absence previously
made the physical butterfly conditional. Keeping the established road
inclusion fixed, the derived pullback is now the unsplit conductor/road
homotopy-pullback complex
\[
C_3\longrightarrow C_2\longrightarrow C_1\longrightarrow C_0
\]
with ranks
\[
1\longrightarrow4\longrightarrow5\longrightarrow1
\]
and differential ranks \((1,3,1)\).

The integrated audit first reruns the completed mixed-variance transform and
both mandatory forgetting controls. It then computes the pullback matrices
over \(\mathbb Z\), verifies \(d^2=0\), and checks the ranks over
\(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and \(\mathbb F_{101}\). Unit minors
in every differential prove saturation of the image lattices. Therefore
\[
\boxed{H_1\cong\mathbb Z,qquad H_i=0\ (i\ne1),}
\]
with no integral torsion.

A primitive representative is
\[
z=(1,0,1,0,0)\in C_1,
\]
whose road augmentation is \(+1\). This integral verdict is obtained before
reading any physical shadow.

Afterward, the independent boundary data agree:

- the endpoint matrix of Entry 400 selects even loaded parity;
- the road-orientation and polarity reflection signs multiply to \(+1\);
- the generic \(Q\)-leg is primitive with coefficient \(+1\);
- the Cartier edge residue is \(+1\);
- both ordinary-forgetting images vanish.

Thus the favorable branch of the Entry-146 falsification trichotomy occurs:
the six-point positive-sheet physical derived pullback is neither zero nor of
higher rank. It is one unique primitive torsion-free line, fixed up to its
already chosen logarithmic orientation.

This statement remains scoped to the fs/Kato logarithmic realization. It does
not identify the class with a numerical amplitude or CHY formula, and it does
not prove factorization at higher multiplicity. The next decisive test is the
first eight-point Cut-naturality square: restrict the eight-point candidate to
a six-by-four factorization boundary and compare it with the external product
of this primitive six-point line and the four-point unit.

The executable audit is
`research/voevodsky/check_physical_derived_pullback_after_transform.py`.
