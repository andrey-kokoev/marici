// Compatibility entrypoint for the straight edge-ray viewer procedure.
import {edgeProcedure,edgeProbe} from './edge-ray-model.mjs';
export const procedureState=edgeProcedure;
export function endingCell(k){return {...edgeProbe(k).end,outsideEnvelope:false};}
