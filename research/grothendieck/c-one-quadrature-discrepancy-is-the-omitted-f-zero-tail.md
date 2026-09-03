# The c=1 quadrature discrepancy is the omitted f-zero tail

## Diagnosis

Nima's independent checker integrates the archimedean kernel only through

`top=max(-min(M)A+4,1)`,

the endpoint beyond which the compact spline profile vanishes. But the integrand is

`[f(0)e^-x-f(x)e^(-x/4)]/(1-e^-x)`.

For `x>top`, only `f(x)` vanishes. The surviving term is

`f(0)e^-x/(1-e^-x)`.

Its omitted tail is exactly

`integral_top^infinity f(0)e^-x/(1-e^-x)dx`

`=-f(0) log(1-e^-top)`.

This term is positive. Omitting it lowers the reported baseline and shifts the cross value, matching the observed residual orientation.

## Repair

Either integrate to infinity, as the Grothendieck scout does, or add the exact tail above after the compact-support endpoint. Add a deliberate failure that truncates both numerator terms at spline support and requires a nonzero residual.

## Disposition

The value-level discrepancy is explained by a quadrature truncation defect, not a convention difference. Regenerate Nima's component table with the exact `f(0)` tail before choosing interval regression targets.
