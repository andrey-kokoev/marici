# Nonboundary detector for the endpoint-translation P24 class

Date: 2026-09-08

## Closed primitive coordinate

The framed Branch B line map is a degree-zero chain detector. In each endpoint/channel frame it supplies a closed linear formal coordinate `lambda_v` dual to the strict cycle

\[
v=b_{\sigma,T},\qquad \lambda_v(v)=1.
\]

Thus

\[
Q\lambda_v=0.
\]

The ordinary constant function also satisfies `Q1=0`.

## Boundary detector

Bruce's derived product therefore obeys

\[
\lambda_v\star1=0,
\qquad
1\star\lambda_v=0.
\]

A Hochschild coboundary of a zero-cochain is assembled from evaluation on these products (with convention-dependent shifted signs). Consequently, for every zero-cochain `sigma`,

\[
(b\sigma)(\lambda_v,1)=0.
\]

By contrast, the constant-translation P24 cocycle has the already checked residue value

\[
\phi_v(\lambda_v,1)=-1.
\]

It follows immediately that no `sigma` can satisfy

\[
\phi_v=-b\sigma.
\]

Hence

\[
\boxed{[\phi_v]\ne0}
\]

in the degree-one derived cyclic cohomology of the algebraic continuous-formal model. The same detector works in all eight frames. Relative/Dorroh normalization cannot create a unit-degenerate primitive because both derived products involving the detector pair already vanish.

## Scope

The conclusion concerns the algebraic continuous-formal cyclic complex equipped with the GR distributional residue trace. It does not assert that the function space is a nuclear Frechet algebra of smooth functions on a compact supermanifold. That analytic realization remains a separate strengthening, not a prerequisite for the stated formal cyclic class.

## Verification

```sh
python research/voevodsky/check_marici_p24_nonboundary_detector_20260908.py \
  --root . \
  --output research/voevodsky/marici_p24_nonboundary_detector_certificate_20260908.json
```

The checker performs 56 integration checks across all eight frames.
