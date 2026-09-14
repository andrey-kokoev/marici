# v198: normalization-to-endpoint-Q compatibility preflight

The target endpoint connector is concrete, but its coefficient object is the integer Laurent ring on 18 labelled Rees generators used by the 215-cell K6 support flag. The ramified qg2 source instead lives over the localized quadratic algebra `Q[p^+-1,(kappa^2-1)^+-1,x,d]/(d^2-Delta)` and has odd generator `d/(16p^4)`.

No current packet defines a labelled coefficient-ring map between these objects, or a cell map sending the endpoint/conductor branch pair to the target `VPLUS/VMINUS` cells. Therefore their matching odd characters and primitive detector values cannot identify them.

The first reopening datum is a labelled ring map from the 18 Rees generators to the ramified physical parameters. It must be accompanied by the endpoint cell map and a commuting square for the source differential, target restriction `rho`, and endpoint connector `kV`.

This supersedes the broader claim that the target endpoint connector was absent. The connector exists; its normalization-source comparison does not.
