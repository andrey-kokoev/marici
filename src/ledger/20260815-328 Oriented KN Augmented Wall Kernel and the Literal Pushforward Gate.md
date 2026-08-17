# Oriented KN Augmented Wall Kernel and the Literal Pushforward Gate

## Record

Date: 2026-08-15

Status: constructed the missing third wall as a canonical oriented
Kato--Nakayama/constructible augmented-interval kernel. This derives the
complete three-term vertex boundary and its reflection signs. A proper
six-functor pushforward into the literal entry143 costalk sheaves remains
unconstructed. No graph admission is claimed.

## Geometric wall object

For the ordered product-branch log map
\[
\mathbb N\longrightarrow\mathbb N^2,\qquad 1\longmapsto(1,1),
\]
the relative characteristic lattice is the anti-diagonal orientation line
\(\mathbb Z_{\rm or}\). Its Kato--Nakayama fibre is an oriented circle.

Entry105's positive-real radial basepoint marks that circle canonically.
Cutting there gives an oriented interval \(I\) whose two endpoint germs
are labelled by the two Rees charts. If \(e\) is its oriented one-cell,
\[
\partial e=v_1-v_0.
\]
The normalized Borel--Moore cap of the relative circle is
\[
\int_{\rm KN}e=+1.
\]
Combining the interval boundary and the cap gives the augmented
correspondence
\[
\boxed{
e\longmapsto w-v_0+v_1,
}
\]
where \(w\) is the conductor-Tor wall output.

Under the entry324 axis dictionary this is exactly
\[
\boxed{
D=\iota_\tau+\iota_{n_0}-\iota_{n_1}.
}
\]
Thus the third primitive wall is not an ordinary boundary divisor. It is
the proper BM integral of the oriented relative KN fibre.

## Integral matrix and symmetry

The augmented row has Smith factor one. Tensoring it with the complete
three-axis Boolean packet gives, across six ordered pairs:

- 72 total boundary rows;
- 48 chart rows;
- 24 wall rows; and
- 72 two-step cancellations, hence \(D^2=0\).

Reflection reverses the interval orientation and the anti-diagonal wall
orientation and exchanges the two cut germs:
\[
r(e)=-e,\qquad r(w)=-w,\qquad r(v_0)=v_1.
\]
Therefore
\[
\partial_{\rm aug}r(e)=r\partial_{\rm aug}(e)
\]
integrally. The two odd signs multiply to the loaded wall sign \(+1\),
matching entry324. Rotation only relabels the six ordered pairs.

The principal occurrence-line factors from entry325 remain compatible:
each section and its dual rescale inversely, so every radial evaluation
stays primitive without localization.

## Exact remaining gate

This constructs the previously missing oriented wall object and explains
geometrically why an ordinary two-boundary or fs-log-divisor model fails.
It is still a theorem in the local constructible KN-link category.

The remaining spatial arrow is the proper pushforward/Beck--Chevalley
comparison
\[
\Gamma_{\rm KN}^{!,\log}
\longrightarrow
\operatorname{Star}_{143}(v)
\]
that identifies:

1. the two cut germs with the two literal Rees-chart edge costalks;
2. the BM integral \(w\) with the literal third-edge/Tor costalk;
3. every normal-circle and Čech lower state with the corresponding
   entry143 \([S,H]\) generator; and
4. the three matching principal-line evaluations with the actual radial
   corestrictions.

The source geometry and all finite coefficients are now forced. What
remains is the sheaf-level proper base-change theorem proving that this
labelled KN correspondence pushes forward to the already fixed literal
target diagram. Endpoint odd counits and the based \(q_\Sigma\) row must
then be attached to that pushforward before the endpoint/\(Q\) mapping
fibre can be formed.

## Executable evidence

Checker:
research/voevodsky/check_dp6_oriented_kn_augmented_wall.rs

SHA-256:
e1242684f4cb078df1813704fb3594e5a3a20703d77c368f237cbb1928f0cc07

Fresh rustfmt --check, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used because no
repository-scoped structured-command MCP capable of invoking Rust is
exposed.

## Outcome contract

~~~json
{
  "claim": "The positive-real cut of the oriented anti-diagonal Kato-Nakayama circle gives a canonical augmented interval kernel e to w-v0+v1. Its interval boundary supplies the two Rees-chart terms and its primitive BM integral supplies the conductor-Tor wall, yielding D=i_tau+i_n0-i_n1 with integral reflection covariance.",
  "status": "proved_scoped_oriented_KN_augmented_wall_kernel",
  "scope": "local constructible KN-link and line-valued bivariant kernel; literal entry143 sheaf-level proper pushforward excluded",
  "geometry": {
    "relative_KN_fiber": "oriented circle",
    "basepoint": "entry105 positive-real radial basepoint",
    "cut_interval_boundary": ["-chart0", "+chart1"],
    "BM_integral_wall": "+tau",
    "augmented_boundary": ["+tau", "+n0", "-n1"],
    "primitive_smith_factor": 1,
    "ordinary_fs_log_divisor_used": false
  },
  "matrix": {
    "ordered_pairs": 6,
    "total_boundary_rows": 72,
    "chart_rows": 48,
    "wall_rows": 24,
    "total_d_squared": 0
  },
  "symmetry": {
    "reflection_interval_sign": -1,
    "reflection_wall_orientation_sign": -1,
    "loaded_wall_sign": 1,
    "D3_covariant": true,
    "principal_line_rescaling_invariant": true
  },
  "unconstructed": [
    "literal entry143 six-functor pushforward and Beck-Chevalley comparison",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_oriented_kn_augmented_wall.rs",
  "checker_sha256": "e1242684f4cb078df1813704fb3594e5a3a20703d77c368f237cbb1928f0cc07"
}
~~~
