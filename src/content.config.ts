import { defineCollection } from 'astro:content'
import { glob } from 'astro/loaders'
import { z } from 'astro/zod'

const ledger = defineCollection({
  loader: glob({
    base: './src/ledger',
    pattern: '**/*.md',
  }),
  schema: z.object({
    draft: z.boolean().optional(),
  }).passthrough(),
})

export const collections = { ledger }
