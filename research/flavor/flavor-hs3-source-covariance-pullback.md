# HS3 source-covariance pullback

Work package: WP561  
Owner: marici.Figueiredo

## Released likelihood authority

HEPData record `ins2845789`, DOI `10.17182/hepdata.157024`, releases the ATLAS
triple-Higgs signal-plus-background likelihood suite in HS3 format. Resource
`r1` is a 6,616,140-byte archive with SHA-256 digest
`30954c386e381f943bbbb430ecf4d263f5d9279b3e91e721ff9ce09de4314036`.
It contains 118 JSON workspaces: 90 heavy-resonant, 14 nonresonant TRSM, 13
resonant TRSM, and one Standard Model workspace.

The bounded audit inspects
`Likelihood_TRSM_X400_S275.json`, whose SHA-256 digest is
`f3eacf5d38c82dbb2e86d08b7849bc525dcba993f22634682cde997bd096eb04`.
It has two analyses, three distributions, four data objects, and 139 named
nuisance parameters. Its modifier grammar includes normalization, histogram,
shape, and statistical uncertainties. Thus an actual detector likelihood and
nuisance model exist; WP560's broad statement that covariance was simply
absent is too coarse.

## Exact remaining mismatch

The inspected workspace has one physics parameter of interest,
`SigXsecOverSM6j`. It is a normalization of a fixed TRSM signal template. The
workspace contains neither the WP559 coefficient \(\lambda_s\), the
trace-adjoint/Higgs mixing coordinate \(z=\sin^2\theta\), nor an interpolation
map from those source coordinates to bin yields.

Let the profiled detector coordinate be \(\mu\). Even if a completed model made
it depend only on the induced light-Higgs quartic contribution,

\[
q={\lambda_s z^2\over\lambda_H},
\qquad \mu=F(q),
\]

the Jacobian from \((\lambda_s,z)\) to one detector coordinate has rank at most
one. Any positive scalar detector information \(w\) pulls back to

\[
G=J^T wJ,
\qquad \det G=0.
\]

The exact hostile pair

\[
(\lambda_s,z)=(1,1/4),
\qquad (\lambda_s,z)=(16,1/16)
\]

has the same \(\lambda_s z^2=1/16\) but different source quartics and mixing.
Nuisance completeness cannot remove a kernel already present before the
detector likelihood.

## Complementary physical probe

The smallest rank repair is not another triple-Higgs normalization. It is an
independent mixing readout. On the leading universal-mixing domain used by
WP472, a single-Higgs rate measures

\[
r=1-z.
\]

Together with \(q=\lambda_s z^2/\lambda_H\), the source response is

\[
J_{rq}=
\begin{pmatrix}
0&-1\\
z^2/\lambda_H&2\lambda_s z/\lambda_H
\end{pmatrix},
\qquad
\det J_{rq}={z^2\over\lambda_H}.
\]

It has rank two for \(z>0\) and \(\lambda_H>0\). This complementary probe is
source-derived: mixing simultaneously controls ordinary Higgs rates and the
projection of the source quartic into the light-Higgs vertex.

## Instrument boundary

WP472 supplies an experimentally typed single-Higgs signal-strength readout,
and the HS3 suite supplies a covariance-bearing triple-Higgs detector
likelihood. They are not yet one common statistical experiment. Their datasets
and systematic sources can overlap, and no admitted cross-analysis covariance
or joint likelihood transports both records to \((\lambda_s,z)\).

Therefore WP561 establishes:

- detector covariance exists inside each fixed HS3 signal model;
- it cannot be pulled back without a source-to-template map;
- one HHH normalization remains rank one on the two-dimensional portal source;
- the single-Higgs plus HHH pair is algebraically rank restoring;
- uncertainty-stable physical identification still requires a joint or
  demonstrably independent covariance and portal-complete templates.

The smallest exact falsifier is \(z=0\), where both quartic transport and the
rank-two determinant vanish. The smallest covariance falsifier is an unknown
cross-analysis block large enough to make the combined weighted Gram singular
or statistically unresolved.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp561_hs3_source_covariance_pullback.py

The generated result is
research/flavor/results/wp561_hs3_source_covariance_pullback.json.
