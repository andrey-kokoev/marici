import { createHash } from 'node:crypto';
import { createModelChecker } from './model-evaluation.mjs';

export { modelVersion, predicateReadContract } from './model-evaluation.mjs';
const checker = createModelChecker(data => createHash('sha256').update(data).digest('hex'));
export const { verifyModel, verifyModelSelectively } = checker;
