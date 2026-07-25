---
name: new-cnpj-validation
description: Use when implementing, reviewing, or testing Brazilian CNPJ validation that must support both legacy numeric CNPJ and the Receita Federal alphanumeric CNPJ format scheduled for July 2026.
---

# New CNPJ Validation

Use this skill for any CNPJ validation work in this repository, especially profile data, forms, schemas, imports, integrations, or tests that must accept both the legacy numeric format and the new alphanumeric format.

Do not use this skill for CPF validation unless CNPJ and CPF are being changed together.

## Official Rule Summary

Base validation on Receita Federal documentation, not third-party snippets.

- Existing numeric CNPJs remain valid and unchanged.
- The alphanumeric CNPJ applies to new registrations from July 2026.
- The identifier keeps 14 positions.
- Positions 1-12 are alphanumeric (`0-9`, `A-Z`).
- Positions 13-14 are numeric verification digits.
- Character values are `ASCII code - 48`, so digits keep values `0-9` and uppercase letters become `A=17` through `Z=42`.
- Verification digits use modulo 11, not modulo 97.
- First digit weights are `5,4,3,2,9,8,7,6,5,4,3,2`.
- Second digit weights are `6,5,4,3,2,9,8,7,6,5,4,3,2`.
- If `sum % 11` is `0` or `1`, the digit is `0`; otherwise the digit is `11 - (sum % 11)`.
- Official alphanumeric example: `12.ABC.345/01DE-35`.

Official references:

- Receita Federal CNPJ Alfanumerico project: https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/cnpj-alfanumerico
- Receita Federal technical DV page: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/cnpj
- Receita Federal DV manual PDF: https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/documentos-tecnicos/cnpj/manual-dv-cnpj.pdf

## Repository Integration Rules

- Prefer `apps/web/src/lib/utils/validate-cnpj.ts` for web-local validation.
- Move validation to `packages/contracts` only when another workspace consumes it.
- Supabase Edge Functions cannot import `@vistase/contracts`; duplicate only the minimal validator under `supabase/functions/_shared/` if an Edge Function needs it.
- `profile.cnpj` is currently display-only. Do not turn it into an editable field unless the user explicitly asks.
- Allow `null` at schema boundaries when CNPJ is optional; validate only non-empty strings.
- Keep user-facing hints in `apps/web/src/messages/en/pages.json` and `apps/web/src/messages/pt-BR/pages.json`.
- Do not add an input mask for read-only profile display.
- Do not store normalized values back to the database unless the task explicitly includes data migration or write behavior.

## TypeScript Implementation Template

Use this exact algorithm unless a newer official Receita Federal document changes the rule.

```ts
const firstDigitWeights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2] as const;
const secondDigitWeights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2] as const;

export function normalizeCnpj(value: string) {
  return value.trim().toUpperCase().replace(/[.\-/\s]/g, "");
}

function toCalculationValue(character: string) {
  if (!/^[0-9A-Z]$/.test(character)) {
    return Number.NaN;
  }

  return character.charCodeAt(0) - 48;
}

function calculateDigit(value: string, weights: readonly number[]) {
  const sum = weights.reduce((total, weight, index) => {
    return total + toCalculationValue(value[index]) * weight;
  }, 0);
  const remainder = sum % 11;

  return remainder === 0 || remainder === 1 ? 0 : 11 - remainder;
}

export function validateCnpj(value: string) {
  const normalized = normalizeCnpj(value);

  if (!/^[0-9A-Z]{12}[0-9]{2}$/.test(normalized)) {
    return false;
  }

  if (/^[0-9]{14}$/.test(normalized) && /^(\d)\1{13}$/.test(normalized)) {
    return false;
  }

  const body = normalized.slice(0, 12);
  const firstDigit = calculateDigit(body, firstDigitWeights);
  const secondDigit = calculateDigit(`${body}${firstDigit}`, secondDigitWeights);

  return normalized.endsWith(`${firstDigit}${secondDigit}`);
}
```

## Required Unit Cases

Always include these cases in the closest test file.

```ts
import { describe, expect, it } from "vitest";

import { normalizeCnpj, validateCnpj } from "./validate-cnpj";

describe("validateCnpj", () => {
  it("accepts valid legacy numeric CNPJ values", () => {
    expect(validateCnpj("11.222.333/0001-81")).toBe(true);
    expect(validateCnpj("11222333000181")).toBe(true);
  });

  it("accepts the official alphanumeric CNPJ example", () => {
    expect(validateCnpj("12.ABC.345/01DE-35")).toBe(true);
    expect(validateCnpj("12abc34501de35")).toBe(true);
  });

  it("rejects invalid verification digits", () => {
    expect(validateCnpj("11.222.333/0001-80")).toBe(false);
    expect(validateCnpj("12.ABC.345/01DE-34")).toBe(false);
  });

  it("rejects invalid shape and placeholder values", () => {
    expect(validateCnpj("00.000.000/0000-00")).toBe(false);
    expect(validateCnpj("12.ABC.345/01DE-AA")).toBe(false);
    expect(validateCnpj("12.ABC.345/01D@-35")).toBe(false);
    expect(validateCnpj("12ABC34501DE3")).toBe(false);
  });

  it("normalizes formatting without changing alphanumeric content", () => {
    expect(normalizeCnpj(" 12.ABC.345/01DE-35 ")).toBe("12ABC34501DE35");
  });
});
```

## Profile Schema Pattern

When validating stored profile data, allow `null` and refine only present values.

```ts
cnpj: z
  .string()
  .nullable()
  .refine((value) => value === null || validateCnpj(value), {
    message: "Invalid CNPJ.",
  }),
```

If the error can surface in UI, replace the hardcoded message with an existing translated path or map the Zod error to translated copy at the UI boundary.

## Verification Commands

Use the narrowest commands first, then workspace verification.

```bash
npm run test --workspace @vistase/web -- apps/web/src/lib/utils/validate-cnpj.test.ts
npm run test --workspace @vistase/web -- apps/web/src/lib/supabase/profile.test.ts
npm run lint --workspace @vistase/web
npm run typecheck --workspace @vistase/web
```

If validation moves into `packages/contracts`, also run:

```bash
npm run build --workspace @vistase/contracts
npm run test --workspace @vistase/contracts
npm run typecheck --workspace @vistase/contracts
```

## Review Checklist

- CNPJ body accepts `0-9A-Z`; final two characters accept digits only.
- Lowercase input is normalized to uppercase before validation.
- Formatted and unformatted values both work.
- Numeric legacy examples still validate.
- Official alphanumeric example validates.
- Invalid verification digits fail.
- Repeated numeric placeholder values fail.
- No modulo 97 implementation exists.
- Profile CNPJ remains read-only unless explicitly requested.
- New user-facing text is translated in both supported locales.
