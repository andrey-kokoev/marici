import importlib.util, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MODULE=ROOT/"checkers"/"compile_apparatus_calendar.py"
EXAMPLE=ROOT/"contracts"/"apparatus-capacity-measurement.example.json"
RESULT=ROOT/"results"/"apparatus_calendar_phase_diagram.json"
spec=importlib.util.spec_from_file_location("calendar",MODULE); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def main():
    binding=json.loads(EXAMPLE.read_text()); base=m.compile_calendar(binding); assert base["accepted"]
    durations={k:F(v) for k,v in base["duration_seconds"].items()}; keys=sorted(durations)
    boundaries={F(1)}
    for mask in range(1,1<<len(keys)):
        boundaries.add(sum((durations[keys[i]] for i in range(len(keys)) if mask&(1<<i)),F(0)))
    phases=[]; previous=None
    for capacity in sorted(boundaries):
        trial=dict(binding); trial["available_optical_seconds"]=str(capacity); result=m.compile_calendar(trial); assert result["accepted"]
        selected=tuple(result["selected_optical_instruments"])
        if selected!=previous: phases.append({"capacity_seconds":str(capacity),"selected":list(selected)}); previous=selected
    expected=[
      {"capacity_seconds":"1","selected":[]},
      {"capacity_seconds":"2080","selected":["comb_referenced_flavor_comparison"]},
      {"capacity_seconds":"5200","selected":["environment_port_tomography"]},
      {"capacity_seconds":"6880","selected":["comb_referenced_flavor_comparison","sealed_controller_replay"]},
      {"capacity_seconds":"7280","selected":["comb_referenced_flavor_comparison","environment_port_tomography"]},
      {"capacity_seconds":"12080","selected":["comb_referenced_flavor_comparison","environment_port_tomography","sealed_controller_replay"]}]
    assert phases==expected
    out={"schema":"marici.aspect.apparatus-calendar-phase-diagram.v1","status":"pass","example_is_not_physical_authority":True,"phase_boundaries":phases,"surprise":"Compression creates a two-sector comb-plus-replay phase at 6880 seconds, but replay is displaced again at 7280 seconds because comb-plus-environment covers three gains at lower time.","all_three_threshold_seconds":"12080"}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
