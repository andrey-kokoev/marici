import argparse, csv, json
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"contracts"/"sealed-controller-replay-acquisition.v2.json"
TREATMENTS=("L1","R2","L2","R1")

def cells():
    replay={("sealed_replay",b,p,t) for b in TREATMENTS for p in TREATMENTS for t in TREATMENTS}
    live={("live_controller",p,p,t) for p in TREATMENTS for t in TREATMENTS}
    return replay|live

def assess(rows,minimum_count):
    c=json.loads(CONTRACT.read_text()); required=set(c["required_columns"]); expected=cells()
    counts,outcomes=Counter(),Counter(); keys,epochs,schedules=set(),set(),set()
    blocks,positions,cell_positions=defaultdict(Counter),defaultdict(set),defaultdict(Counter)
    transcripts,commands,digests=defaultdict(set),defaultdict(set),defaultdict(set); manifests=set(); complete=True; failures=0
    for row in rows:
        complete &= required<=set(row) and all(row.get(k,"")!="" for k in required)
        if row.get("trial_key") in keys: complete=False
        keys.add(row.get("trial_key")); cell=tuple(row.get(k) for k in ("arm","transcript_bound_predecessor","actual_predecessor","target"))
        if cell not in expected: complete=False; continue
        try: pos=int(row["within_block_position"]); outcome=int(row["target_outcome"]); failure=int(row["reset_failure"])
        except ValueError: complete=False; continue
        block=row["acquisition_block"]; blocks[block][cell]+=1; positions[block].add(pos); cell_positions[cell][pos]+=1
        counts[cell]+=1; outcomes[cell]+=outcome; failures+=failure
        key=(row["arm"],row["transcript_bound_predecessor"],row["target"])
        transcripts[key].add(row["controller_transcript_key"]); commands[key].add(row["correction_command"]); digests[key].add(row["sealed_payload_digest"])
        manifests.add(row["controller_input_manifest"]); epochs.add(row["acquisition_epoch"]); schedules.add(row["sealed_schedule_key"])
    all_cells=set(counts)==expected; n=len(expected)
    full_blocks=bool(blocks) and all(set(v)==expected and set(v.values())=={1} and positions[k]==set(range(n)) for k,v in blocks.items())
    balanced=all_cells and all(set(v)==set(range(n)) and len(set(v.values()))==1 for v in cell_positions.values())
    enough=all_cells and all(counts[x]>=minimum_count for x in expected)
    deterministic=all(len(v)==1 for v in transcripts.values()) and all(len(v)==1 for v in commands.values()) and all(len(v)==1 for v in digests.values())
    def mean(cell): return F(outcomes[cell],counts[cell])
    replay_spread=max(max(mean(("sealed_replay",b,p,t)) for p in TREATMENTS)-min(mean(("sealed_replay",b,p,t)) for p in TREATMENTS) for b in TREATMENTS for t in TREATMENTS) if all_cells else None
    live_spread=max(max(mean(("live_controller",p,p,t)) for p in TREATMENTS)-min(mean(("live_controller",p,p,t)) for p in TREATMENTS) for t in TREATMENTS) if all_cells else None
    gates={"raw_records_complete_and_unique":complete,"one_epoch_and_schedule":len(epochs)==len(schedules)==1,"all_80_legal_cells_present":all_cells,"every_block_is_complete_80_cell_permutation":full_blocks,"every_cell_uniform_over_block_position":balanced,"minimum_attempted_counts_pass":enough,"transcripts_commands_and_digests_are_deterministic":deterministic,"actual_predecessor_absent_from_controller_inputs":manifests=={"transcript_bound_predecessor,target,calibration_epoch"},"live_controller_output_is_predecessor_invariant":live_spread is not None and live_spread<=F(1,20),"sealed_replay_output_is_predecessor_invariant":replay_spread is not None and replay_spread<=F(1,20)}
    return {"accepted":all(gates.values()),"gates":gates,"attempted_trial_count":sum(counts.values()),"live_predecessor_spread":str(live_spread) if live_spread is not None else None,"replay_predecessor_spread":str(replay_spread) if replay_spread is not None else None,"saturated_parameter_count":80,"cell_count_lower_bound":80,"recorded_reset_failures":failures}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input_csv",type=Path); p.add_argument("--output",type=Path,required=True); a=p.parse_args(); c=json.loads(CONTRACT.read_text())
    with a.input_csv.open(newline="",encoding="utf-8") as h: result=assess(csv.DictReader(h),c["minimum_attempted_trials_per_cell"])
    result["schema"]="marici.aspect.sealed-controller-replay-run-analysis.v2"; a.output.write_text(json.dumps(result,indent=2)+"\n"); print(json.dumps(result,sort_keys=True)); raise SystemExit(0 if result["accepted"] else 1)
if __name__=="__main__": main()
