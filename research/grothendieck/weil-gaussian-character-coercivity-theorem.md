# The completed Gaussian Weil kernel is coercive in character

Fix `t>0`. In the explicit two-variable source formula, the gamma term is

```
K_gamma(t,xi)= -log(pi)/(4 sqrt(pi t))
 +1/(4pi) integral_R e^[-t(u-xi)^2]
             Re psi(1/4+iu/2) du.                     (1)
```

The classical digamma asymptotic in vertical strips gives

```
Re psi(1/4+iu/2)=log(|u|/2)+O(1/|u|)                  (2)
```

away from a fixed neighborhood of zero. Translating `u=xi+v` in (1) and
using Gaussian domination yields

```
K_gamma(t,xi)
 = [log(|xi|/(2pi))]/[4 sqrt(pi t)] + o_t(1)
                                      as |xi|->infinity. (3)
```

The endpoint term

```
e^(t/4-t xi^2)cos(t xi)
```

tends to zero. The log-Gaussian von Mangoldt series is absolutely convergent
for fixed `t`, so its cosine sum is bounded uniformly in `xi`. Consequently

```
Theta(t,xi) -> +infinity              as |xi|->infinity. (4)
```

## Attainment of the hostile character

The completed source kernel is continuous in `xi`: this follows from
dominated convergence for the shifted gamma integral and uniform absolute
convergence of the smoothed prime series. By (4), it therefore attains a
global minimum at some finite character for every fixed `t>0`.

This closes the character-escape caveat in the first-contact theorem. If a
finite positive smoothing threshold exists, its zero contact cannot disappear
to `|xi|=infinity`; subject to continuity in the smoothing parameter, it must
produce a finite solution of

```
Theta(t,xi)=partial_xi Theta(t,xi)=0.                  (5)
```

## Uniformity caveat

Equation (3) is for fixed `t`. Following minimizers while `t` tends to zero or
infinity requires estimates uniform in both variables. The theorem excludes
escape at a finite positive threshold but does not by itself establish a
broad-smoothing positive regime or rule out contact.

## Explanatory consequence

The large-character gamma growth acts as an archimedean confining potential.
The prime adjacency is an absolutely bounded oscillatory perturbation at each
positive smoothing scale. Any failure of completed positivity is therefore a
finite-character phenomenon, not an instability hidden at spectral infinity.
