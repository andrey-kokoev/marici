# Prime-power thresholds are form-continuous but not operator-norm continuous

At the threshold `L=a/2`, where `a=log n`, the new arithmetic term is the
compressed translation

\[
T_{a,L}=\chi_{[-L,L]}T_a\chi_{[-L,L]}.
\]

For each fixed smooth test function, its overlap integral tends to zero as
`L downarrow a/2`, because the overlap interval has length `2L-a`. Hence the
family is continuous in the test-function form topology.

It is not continuous in operator norm. For every `L>a/2`, choose a unit vector
supported inside the overlap interval. Translation is isometric there, so

\[
\|T_{a,L}\|=1,
\]

whereas the overlap operator vanishes at and below the threshold. Thus a new
prime-power term appears with its full operator norm immediately, even though
all fixed smooth matrix elements vanish continuously.

This rules out a global continuation argument based only on operator-norm
Lipschitz bounds in `L`. It also explains the edge-concentrated near-null modes
seen numerically before successive thresholds. A valid threshold transfer must
split off the shrinking edge channel (or use a rescaled edge coordinate) and
prove positivity of its finite co-defect block; the bulk complement can retain
a uniform Loewner gap.
