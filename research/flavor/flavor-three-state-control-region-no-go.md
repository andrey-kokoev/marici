# Three-state control-region no-go

Work package: WP992  
Owner: marici.Figueiredo

## Question

Can a finite preregistered additive-control schedule prepare all three WP991
configurations over the full admitted positive \((q,k)\) domain?

## Frozen control geometry

Allow two formal invariant controls that shift the effective coefficients:

\[
Q=q+u,\qquad R=k+v.
\]

On the commuting, rank-two, and full-rank configurations the energies are

\[
E_0=0,qquad
E_2=-2Q,qquad
E_3=-\frac29Q-\frac2{27783}R.
\]

Exact comparison gives the three open preparation regions:

\[
\begin{array}{c|l}
\text{unique minimum}&\text{conditions}\\
0&Q<0,\ R<-3087Q\\
2&Q>0,\ R<24696Q\\
3&R>-3087Q,\ R>24696Q.
\end{array}
\]

All regions are nonempty. For a known source point, the effective settings
\((-1,0),(1,0),(0,1)\) prepare states \(0,2,3\), respectively.

## Uniform finite-schedule obstruction

The controls are additive. For any finite schedule \((u_i,v_i)\), choose
\(q>\max_i(-u_i)\). Then every effective \(Q_i=q+u_i\) is positive, so no
setting lies in the commuting-baseline region. Thus no finite source-independent
schedule prepares all three configurations uniformly on the unbounded positive
quadrant admitted by WP990.

The same geometry shows why setting controls after learning \((q,k)\) is not
a preregistered open-loop instrument: the calibration target is being used to
choose the preparation that is supposed to identify it.

## Reopening conditions

Either of two new objects would reopen the branch:

1. an independently authorized compact domain
   \(0<q\le q_{\max}\), \(0<k\le k_{\max}\), permitting finite robust
   controls chosen before measurement;
2. an adaptive controller with independently calibrated state estimates,
   intervention costs, stopping rule, and proof that feedback does not reuse
   the desired answer as calibration.

Neither object is present in WP977--WP991. The formal knobs themselves are also
not admitted source operations.

## Classification and falsifier

This is a uniform preparation no-go on the current domain, not a failure of
the rank-two relative-energy algebra. It neither selects nor rigidifies.

The smallest falsifier is an independently derived finite upper bound on
\(q\) together with one admitted negative-enough \(u\) setting that prepares
the commuting baseline across that bound. A posterior fitted bound does not
qualify.

## Reproduction

Run:

    python research/flavor/checkers/wp992_three_state_control_region_no_go.py

The generated result is
research/flavor/results/wp992_three_state_control_region_no_go.json.
