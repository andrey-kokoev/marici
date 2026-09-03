# Angular septic windows reduce the quadratic localization budget

## Construction

Let `s` be the septic smoothstep and set

`theta(t)=pi s(t)/2`,

`rho_1(t)=sin(theta(t))`,

`rho_2(t)=cos(theta(t))`.

Then `rho_1^2+rho_2^2=1` identically. Because the first three derivatives of `s` vanish at both endpoints, these windows extend by the appropriate constants as proper `C^3` windows. No denominator or post-normalization is required.

## Comparison with algebraic normalization

The earlier algebraically normalized pair

`s/sqrt(s^2+(1-s)^2), (1-s)/sqrt(s^2+(1-s)^2)`

has scout value `||rho_1'''||_1 approximately 70.15771`.

For the angular pair, high-precision root search and quadrature give

`||rho_1'''||_1 approximately 46.40882`.

Under the same two-window, two-transition Fourier estimate, the `h=1` budget falls from approximately `146.93796` to `97.19841`, a reduction of about 33.9 percent.

## Insertion into the normalized endpoint cover

Voevodsky's coordinate `theta=pi(x+L)/L` and physical overlap `h_x=L` give angular overlap `h_theta=pi`. Third-derivative scaling therefore divides the `h=1` budget by `pi^2`, yielding the scouted quadratic localization constant

`C_loc^quad approximately 9.84825790`.

The cancellation of `L` is a consequence of choosing overlap proportional to the full support scale. This number is larger than the linear-partition constant `224 sqrt(5)/(25 pi) approximately 6.378`, but unlike that linear constant it is admissible in the quadratic IMS identity.

## Claim boundary

The partition identity and endpoint regularity are exact. The derivative norm and comparison are numerical scouts, not directed interval certificates. Root scanning can miss a tangential zero of the third derivative; certification requires interval root counting and directed quadrature.

## Disposition

The angular profile dominates the algebraically normalized profile under the current commutator budget and should be the default quadratic candidate. It is not proved optimal among admissible profiles. The next gate is directed certification, followed by insertion of Voevodsky's physical overlap scale `h_x=L` and chart-coordinate factor.

## Verification

- `research/grothendieck/checkers/angular_septic_partition_scout.py`
- `research/grothendieck/results/angular-septic-partition-scout.json`
