# Optical Bath–Energy Calibration

Owner: marici.Aspect

This cell closes the measurement side of the optical analogue temperature
mapping. It does not map an optical simulator to a material transition
temperature.

The instrument measures two frequency-resolved packets on the same ports:
the dissipative susceptibility and the noise power spectrum. Their ratio
estimates the effective bath temperature bin by bin. Absolute detector gain
cancels. An independent spectroscopic reference supplies the energy unit.

Admission requires all of:

1. the independently measured energy scale agrees with its reference;
2. the fluctuation–dissipation temperature is flat across the preregistered
   frequency band;
3. the full frequency support is present.

The colored-bath hostile passes any scalar noise-strength test but fails the
function-valued flatness gate. The scale-alias hostile has an equilibrium
spectrum but fails the independent reference gate. Thus neither detector gain
nor a fitted noise amplitude can manufacture a Kelvin calibration.

Run:

python research/aspect/checkers/check_optical_bath_energy_calibration.py
