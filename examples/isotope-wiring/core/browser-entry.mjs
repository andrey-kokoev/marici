import { inspectDefinition, compareDefinitions, trialPairPlacement, trialWitnessPlacement, surveyPlacements } from './editor-research.mjs';

// One local runtime for both file:// and the website's srcdoc embed.
// The JSON boundary also keeps core inputs in this realm's ordinary object types.
globalThis.IsotopeWiringResearch = Object.freeze({
  inspect: json => inspectDefinition(JSON.parse(json)),
  surveyPlacements: (source, kind, record, offset) => surveyPlacements(JSON.parse(source), kind, record, { offset }),
  compare: (base, target) => compareDefinitions(JSON.parse(base), JSON.parse(target)),
  trialPlacement: (source, pair, cell) => trialPairPlacement(JSON.parse(source), pair, cell),
  trialWitnessPlacement: (source, witness, cell) => trialWitnessPlacement(JSON.parse(source), witness, cell),
});
