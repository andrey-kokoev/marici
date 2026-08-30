# Portal setting viability radius

Work package: WP583  
Owner: marici.Figueiredo

## Scope

WP580 compiles exact finite steps in the invariant portal coordinates

\[
(r,q)=\left(z,{\lambda_s z^2\over\lambda_H}\right).
\]

This packet determines the largest symmetric local step radius authorized by
the currently declared source and readout conditions. It does not promote the
compiler into a physical actuator and does not substitute a partial scalar
potential for a complete phenomenological viability analysis.

## Admitted domain

Use

\[
0<z<1,\qquad \lambda_s>0,\qquad \lambda_H>0.
\]

The lower mixing boundary is excluded because the quartic response vanishes
at \(z=0\). The upper boundary is excluded because the independently admitted
inclusive-Higgs relation \(\kappa_t^2=1-z\) has zero Standard Model production
coupling at \(z=1\). Strict positivity of \(\lambda_s\) is required by
boundedness of the declared isolated large-\(s\) quartic ray.

## Exact symmetric radius

The four compiled endpoints are

\[
S_r^\pm(h)=
\left(z\mathbin\pm h,\lambda_s{z^2\over(z\mathbin\pm h)^2}\right),
\]

and

\[
S_q^\pm(h)=
\left(z,\lambda_s\mathbin\pm{\lambda_Hh\over z^2}\right).
\]

They give the exact invariant responses \((\mathbin\pm h,0)\) and
\((0,\mathbin\pm h)\). All four endpoints remain in the admitted domain if

\[
0<h<\min\left(z,1-z,{\lambda_s z^2\over\lambda_H}\right).
\]

Every admitted base point therefore has a nonempty exact symmetric setting
neighborhood. This is a local source-coordinate theorem, not a claim that a
beam or detector can command the two settings.

## Exact boundary falsifiers

Each term in the minimum has a distinct typed failure:

- \(h=z\) sends the negative-\(r\) endpoint to the blind boundary \(z'=0\);
- \(h=1-z\) sends the positive-\(r\) endpoint to \(z'=1\), where
  \(\kappa_t^2=0\);
- \(h=q=\lambda_s z^2/\lambda_H\) sends the negative-\(q\) endpoint to
  \(\lambda_s'=0\), violating strict quartic stability.

At the rational point \(z=1/4\), \(\lambda_s=\lambda_H=1\), the common
radius is \(1/16\). The step \(h=1/32\) is admitted, while \(h=1/16\)
already reaches \(\lambda_s'=0\) on the negative-\(q\) branch.

## Classification and remaining gate

WP583 supplies an exact source-side local viability radius. It is neither a
selector nor a presentation rigidifier, and it has no detector instrument.
Full viability still requires a complete source potential, threshold and
decoupling support, experimental reach, and a publication-bound mixed-scalar
detector transport on the same domain. Those missing objects cannot be
inferred from the coordinate compiler.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp583_portal_setting_viability_radius.py

The generated result is
research/flavor/results/wp583_portal_setting_viability_radius.json.
