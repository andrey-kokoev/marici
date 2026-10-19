# Pivot/normal covariance and physical contour — iteration 7

Freshly read pins v46 and the integral projective-lattice receipt/checker. This turn checks full triple-normal GL3 current covariance, transports the marked arrangement and full cycle lattice, and constructs the two P1 residue/tube maps.

## Normal/current covariance with independent constraint check

For w=A nu and h=(A*(r,s,1))_3, the induced projective coordinate Jacobian is det(A)/h³. The checker proves this identity with a generic symbolic3x3 matrix. Under the source normal reparametrization, the ordinary radial source two-form transforms as a two-form, while the actual eight-constraint Jacobian transforms as Jnew=Jold/det(A). The new current coefficient is therefore det(A)*F(inverse)*Jac_inverse. Combined with delta(w)=delta(nu)/det(A), the complete external codim3 current agrees, with source sign and full fermionic numerator unchanged.

Four frames include mixed normals, determinant-1 swap, anisotropic mixing and uniform scaling. Their eight-by-eight incidence derivatives are independently evaluated at an actual localized triple-center fixture, and satisfy the claimed determinant law. The actual normalized Berezin component is nonzero. Omitting the external normal determinant gives nonzero defects in every tested frame.

## Marked arrangement and full integral cycles

All five homogeneous line covectors are transported by A inverse. All six projective intersection incidences agree. The four normalized logarithmic-form basis elements are transported using their original marked canonical denominator, not redefined from the receiving coordinate axes. Their full four-cycle pairing is unchanged and remains unimodular; hence all integral cycle coordinates, including split-invisible directions, are preserved.

A receiving affine horizon is not necessarily the transported canonical infinity line. The explicit regular source point[1:-4:1] maps to a receiving last coordinate0 in a mixed frame, while none of the five arrangement equations vanishes. A projective cover is required; declaring that receiving horizon a new canonical boundary would fabricate a divisor and change the contour problem.

## Integral boundary/tube maps to both P1 centers

Radial-first residues of the projective logarithmic basis yield the following tube maps. Columns are positively oriented local direction loops0,-1; rows use the triple-center integral cycle basis (O_s_inner,O_r_inner,RD_double,LD_double).

For p36 center:

    [ 0,-1]
    [-1, 1]
    [ 0, 0]
    [ 0, 0].

For p58 center:

    [-1, 0]
    [ 0, 0]
    [ 0,-1]
    [ 0,-1].

Pairing these with the full projective forms gives the prior local direction residue matrices[-1,1;0,-1] and[0,-1;-1,1]. Thus boundary maps retain complete integral class data, not only the matching split coefficient differences. These are arrangement residue/tube maps. They do **not** identify external codim2 and codim3 constraint currents without a separate degree/normal prescription; that physical gluing gate stays explicit.

## Next executable continuation

Materialize a conditional contour-admission contract requiring the full lift class, an owning-source selection/word, external normal/constraint prescription and chart-compatible cycle transport. Evaluate the existing regular corner word and its possible completions, retaining invisible class differences. Do not promote a conditional flag, a receiving chart axis or a desired period cancellation into a physical contour.

Evidence: `checkers/check_history6_current_gl3_transport.py`, `results/history6_current_gl3_transport.json`. Fresh run passes. Scientific verdicts unchanged; successor pins v47 and structural net/SCC checks separate. Local covariance is supported on declared opens, but global physical contour/current gluing and weighted admission remain open.
