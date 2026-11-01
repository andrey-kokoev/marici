// Step 4 witnesses the dot only. Step 5 colours both adjacent faces after its return closes.
export const witnessTiming=Object.freeze({proposal:900,edge:1600,fill:650,total:4750});
const clamp=x=>Math.max(0,Math.min(1,x));
export function cellulationWitnessAt(elapsed,stage=4){
 const {proposal,edge,fill}=witnessTiming,colourFaces=stage===5,total=proposal+2*edge+(colourFaces?fill:0);
 const first=clamp((elapsed-proposal)/edge),second=clamp((elapsed-proposal-edge)/edge);
 const witnessed=second===1,fillProgress=colourFaces?clamp((elapsed-proposal-2*edge)/fill):0;
 return {phase:elapsed<proposal?(colourFaces?'ready':'proposition'):first<1?'first-return':second<1?'second-return':colourFaces&&fillProgress<1?'witnessed':'complete',first,second,witnessed,fillProgress,active:elapsed<total};
}
