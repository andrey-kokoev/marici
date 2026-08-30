"""Function-valued FDT and independent-energy-scale calibration surrogate."""
import json, math, sys
from pathlib import Path

def run_fixture(contract, f):
    frequencies=[0.25*(i+1) for i in range(16)]
    k_b=contract["constants"]["boltzmann_j_per_k"]
    gamma=f["gamma"]; gain=f["gain"]; temp=f["bath_temperature_k"]
    susceptibility=[]; noise_psd=[]; ratios=[]
    for omega in frequencies:
        chi_im=gamma*omega/(gamma*gamma+omega*omega)
        color_factor=1.0+f["color"]*(omega/frequencies[-1])**2
        measured_chi=gain*chi_im
        measured_noise=gain*2.0*k_b*temp*chi_im*color_factor/omega
        susceptibility.append(measured_chi); noise_psd.append(measured_noise)
        ratios.append(omega*measured_noise/(2.0*k_b*measured_chi))
    mean=sum(ratios)/len(ratios)
    cv=math.sqrt(sum((x-mean)**2 for x in ratios)/len(ratios))/mean
    scale_error=abs(f["energy_scale_j"]-f["reference_scale_j"])/f["reference_scale_j"]
    t=contract["preregistered_thresholds"]
    gates={"independent_energy_scale":scale_error<=t["reference_scale_relative_error_max"],
           "function_valued_fdt":cv<=t["fdt_flatness_cv_max"],
           "frequency_support":len(frequencies)>=t["minimum_frequency_bins"]}
    return {"id":f["id"],"frequency_bins":frequencies,"susceptibility_im":susceptibility,
            "noise_psd":noise_psd,"temperature_ratio_k":ratios,
            "estimated_temperature_k":mean,"fdt_flatness_cv":cv,
            "reference_scale_relative_error":scale_error,"gates":gates,
            "admitted":all(gates.values()),"expected_admit":f["expect_admit"],
            "expectation_met":all(gates.values())==f["expect_admit"]}

def run(contract):
    fixtures=[run_fixture(contract,f) for f in contract["fixtures"]]
    a,b=fixtures[0],fixtures[1]
    gain_error=abs(a["estimated_temperature_k"]-b["estimated_temperature_k"])/a["estimated_temperature_k"]
    return {"schema":"marici.aspect.optical-bath-energy-calibration-result.v1",
            "claim_boundary":contract["claim_boundary"],"fixtures":fixtures,
            "gain_invariance_relative_error":gain_error,
            "all_expectations_met":all(x["expectation_met"] for x in fixtures),
            "material_room_temperature_claim":False}

def main(argv):
    if len(argv)!=3:
        print("usage: optical_bath_energy_calibration.py CONTRACT RESULT",file=sys.stderr); return 2
    contract=json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    result=run(contract); Path(argv[2]).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2)); return 0 if result["all_expectations_met"] else 1
if __name__=="__main__": raise SystemExit(main(sys.argv))
