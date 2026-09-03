# Polarization uniqueness and the nonlocal-kernel no-go

## Question

Can an unspecified positive nonlocal kernel reproduce the signed Weil quadratic form on a full test space while avoiding its negative local directions?

## Claim boundary

Polarization rules out that escape on any faithful linear form core. Positive compression on a proper restricted image remains possible and is the only surviving mechanism of this type.

## Polarization

A complex quadratic form \(Q(f)=B(f,f)\) determines its Hermitian sesquilinear form uniquely. With a fixed convention,

\[
B(f,g)
=
\frac14
\sum_{k=0}^3
i^kQ(f+i^kg),
\]

up to the corresponding conjugate orientation.

Therefore equality of two quadratic forms on every vector of a linear space implies equality of all cross pairings on that space.

## Kernel consequence

Suppose a continuous distributional kernel \(K\) and the local Weil form agree on every \(f\) in a linear form core:

\[
\iint\overline{f(u)}K(u,v)f(v)\,du\,dv
=
\langle W,|f|^2\rangle.
\]

Polarization forces

\[
\iint\overline{f(u)}K(u,v)g(v)\,du\,dv
=
\langle W,\overline f g\rangle
\]

for every \(f,g\) in that core. If the core is faithful for kernels, then

\[
K(u,v)=W(u)\delta(u-v)
\]

as a distribution on the represented domain.

Nonlocality cannot be inserted merely by choosing a different Gram representation. If the diagonal form has a negative direction on the full core, no positive kernel can equal it there.

## Proper compression is different

Let \(D\) be an indefinite form and let

\[
B:\mathcal C\to\mathcal X
\]

be a non-surjective feature map. The compressed form

\[
B^*DB
\]

can be positive even though \(D\) is indefinite, provided the image of \(B\) avoids every negative direction.

This is not a replacement of \(D\) by a positive kernel on \(\mathcal X\). It is positivity on a restricted source object.

The finite fixture

\[
D=\operatorname{diag}(1,-1,2)
\]

is negative on the middle coordinate. Restriction to the first and third coordinates gives

\[
B^*DB=\operatorname{diag}(1,2)>0.
\]

A restriction that still reaches the middle coordinate remains indefinite.

## Consequence for the Weil programme

An arbitrary positive nonlocal \(K_t\) cannot reproduce the Weil form on a faithful full test domain unless the Weil form is already positive there. Such a kernel would be another representation of the conclusion.

The surviving target must instead specify a proper source map

\[
B_t:\mathcal C_t\to\mathcal X
\]

and prove positivity of

\[
B_t^*W_tB_t
\]

from source structure. Required data are:

- the exact domain \(\mathcal C_t\);
- the image and its closure topology;
- the kernel of \(B_t\);
- which negative Weil directions are excluded and why;
- compatibility with heat-polynomial probes and mesh refinement;
- an identity proving positive compression before GNS.

## Relation to current source tests

The heat-polynomial map is a candidate \(B_t\), but its real-line image is large and its analytic form-core closure is unresolved. If that image is faithful for the full Weil kernel, polarization restores the original signed form and no nonlocal escape remains. If it is genuinely proper in the analytic graph topology, that precise failure of faithfulness must carry the mechanism.

## Disposition

Falsify the phrase “positive nonlocal kernel” as a mechanism without a named restriction. Polarization makes it identical to the original form on a faithful core. The only noncircular survivor is a positive compression along an explicit non-surjective source map or quotient.

## Verification

- `research/voevodsky/polarization-uniqueness-nonlocal-kernel-no-go-v1.json`
- `research/voevodsky/checkers/check_polarization_uniqueness_nonlocal_kernel_no_go.py`
- `research/voevodsky/results/polarization_uniqueness_nonlocal_kernel_no_go.json`
