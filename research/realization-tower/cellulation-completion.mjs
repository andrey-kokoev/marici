// Complete the missing edge, then resolve its two red endpoints, then the white faces.
export const completionTiming=Object.freeze({hold:900,edge:1600,vertices:350,faces:650,total:3500});
const clamp=x=>Math.max(0,Math.min(1,x));
export function cellulationCompletionAt(elapsed){
 const {hold,edge,vertices,faces,total}=completionTiming;
 const arrowProgress=clamp((elapsed-hold)/edge),vertexFillProgress=clamp((elapsed-hold-edge)/vertices),faceFillProgress=clamp((elapsed-hold-edge-vertices)/faces);
 return {phase:elapsed<hold?'candidates':arrowProgress<1?'connecting':vertexFillProgress<1?'filling-vertices':faceFillProgress<1?'filling-faces':'complete',arrowProgress,vertexFillProgress,faceFillProgress,active:elapsed<total};
}
