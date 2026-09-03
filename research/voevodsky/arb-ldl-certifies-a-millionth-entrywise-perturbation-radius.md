# Arb LDL certifies a millionth entrywise perturbation radius

## Question

How much uniform interval uncertainty can the cutoff-\(250\), rank-\(25\) discrete Schur matrix tolerate while retaining the target margin \(0.001\)?

## Claim boundary

Arb interval elimination proves that every symmetric matrix whose entries lie within \(10^{-5}\) of the computed matrix satisfies \(S-0.001I>0\). Radius \(3\times10^{-5}\) fails at pivot \(23\), so the tested threshold lies between these values. This is a certificate for an entrywise perturbation model, not proof that the continuum Schur matrix lies in that model.

## Interval elimination

Each entry of

\[
S_{250}-0.001I
\]

was replaced by an Arb interval of radius \(r\). Manual interval \(LDL^*\) elimination was then performed without pivoting. Positivity follows when every interval diagonal pivot has positive lower endpoint.

All tested radii passed:

\[
r=10^{-14},10^{-12},10^{-10},10^{-8},10^{-6}.
\]

At \(r=10^{-6}\), the smallest pivot lower endpoint was

\[
0.0338646352>0.
\]

At \(r=10^{-14}\), it was approximately \(0.0348908623\). The stronger test \(r=10^{-5}\) also passed, with minimum pivot lower endpoint \(0.0241466931\). At \(r=3\times10^{-5}\), pivot \(23\) enclosed zero and the certificate failed.

## Meaning

The matrix-algebra stage no longer relies on floating Cholesky. If the continuum-derived rank-\(25\) Schur entries can each be enclosed within radius \(10^{-6}\) around the computed entries, Arb proves the target inequality

\[
S_{250}\geq0.001I.
\]

## Residual

No bound currently places the continuum entries inside those intervals. Required contributions include concentration-projector error, frequency quadrature error on \([-250,250]\), spatial Nyström error, and pseudoinverse/range error. The test used a uniform independent radius and therefore does not exploit correlated errors.

## Disposition

The interval linear-algebra backend is adequate and certifies at least a \(10^{-6}\) entrywise radius. The first missing object is now an analytic or interval quadrature enclosure of the matrix construction itself. Larger radii remain to be tested to determine the full available budget.

## Verification

- `research/voevodsky/checkers/check_interval_ldl_cutoff250.py`
- `research/voevodsky/results/interval_ldl_cutoff250.json`
