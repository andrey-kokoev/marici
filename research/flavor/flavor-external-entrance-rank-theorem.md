# Externally distinguishable entrance rank theorem

## General tree constructor

Let (H) collect the row vectors of externally distinguishable entrance
preparations. For an invertible connector frame (S), the tree-level port map
and its positive Gram are

\[
P=HS,
\qquad
W_{\rm tree}=P^TP.
\]

Because (S) is invertible,

\[
\operatorname{rank}P=\operatorname{rank}H.
\]

Thus a faithful three-direction tree port exists exactly when (H) has rank
three. At least three externally distinguishable preparations are necessary.

## Exact determinant criterion

For exactly three channels,

\[
\det(P^TP)=\det(H)^2\det(S)^2.
\]

For any larger finite channel family, Cauchy-Binet gives

\[
\det(H^TH)=\sum_A\det(H_A)^2,
\]

where (A) runs over all three-row subsets. Faithfulness therefore holds if
and only if at least one three-preparation minor is nonzero.

One channel has rank at most one. Two channels have rank at most two and leave
an exact blind direction. The presently frozen up/down entrances are scalar
multiples of the same equal vector, so together they still have rank one.

## Minimal sufficient packet

Three orthonormal preparations give

\[
H=I_3,
\qquad P=sI_3,
\qquad W_{\rm tree}=s^2I_3
\]

at the isotropic connector vacuum. This is both faithful and isotropic.

Faithfulness and isotropy are distinct requirements. A generic full-rank
weighted frame (H=\operatorname{diag}(x,y,z)) has no kernel but produces
(s^2\operatorname{diag}(x^2,y^2,z^2)), which is not isotropic unless the
three magnitudes agree. Neither condition selects the common magnitude.

## Executability boundary

The theorem counts external channels, not internal messenger multiplicity.
Three hidden routes that are coherently summed before observation still form
one preparation. To carry identification authority, each row label must remain
distinguishable through preparation, propagation, and calibrated readout.

No presently admitted flavor experiment supplies this three-channel interface.
The result is therefore a constructor theorem, not an instrument claim. A
physical successor must name the three preparations, derive their
gauge-invariant renormalizable vertices, and show that detector mixing and
resolution preserve response rank three.
