---
name: certificate-of-origin
description: Validates a VIN then fills a Manufacturer's Certificate of Origin (MCO) PDF with vehicle details. Accepts Issue Date, Invoice #, VIN, Model Year, Model, and Manufacturer as inputs. Validates the VIN before generating the certificate — if validation fails, the certificate is not created. Returns a completed, print-ready PDF. Use when the user wants to generate or fill out a Certificate of Origin or MCO document.
---

# Certificate of Origin PDF Filler

## Purpose
This skill validates a VIN and then populates a Manufacturer's Certificate of
Origin PDF template with vehicle information supplied by the user, returning
the completed document as a downloadable PDF named `MCO-<last5VIN>.pdf`.

## Inputs

Collect ALL six values from the user before running the script.

| Argument            | User Label   | Example             |
|---------------------|--------------|---------------------|
| `--issue-date`      | Issue Date   | `2026-07-25`        |
| `--invoice-number`  | Invoice #    | `INV-001234`        |
| `--vin`             | VIN          | `1HGCM82633A123456` |
| `--model-year`      | Model Year   | `2026`              |
| `--model`           | Model        | `Civic`             |
| `--manufacturer`    | Manufacturer | `Honda`             |

If any value is missing, ask the user for it before proceeding.

## Workflow

### Step 1 — Validate the VIN

Always run VIN validation first, before filling the certificate.

```bash
python /app/skills/certificate-of-origin/scripts/validate_vin.py \
  --vin "<vin>"
```

Always display the validation result to the user before proceeding.

- If the output starts with `SUCCESS:`, continue to Step 2.
- If the output starts with `FAILURE:`, stop. Do not run the fill script.
  Inform the user the certificate was not generated and ask them to provide
  a corrected VIN.

### Step 2 — Fill the Certificate (only on validation success)

```bash
python /app/skills/certificate-of-origin/scripts/fill_certificate.py \
  --issue-date "<issue_date>" \
  --invoice-number "<invoice_number>" \
  --vin "<vin>" \
  --model-year "<model_year>" \
  --model "<model>" \
  --manufacturer "<manufacturer>"
```

The script prints `SUCCESS: Certificate written to /app/created/MCO-<last5VIN>.pdf`
on completion. Present that path to the user as their downloadable file.

## Error Handling

- If VIN validation fails, do not generate the certificate. Show the full
  validation failure message to the user and ask them to correct the VIN.
- If the fill script exits non-zero, show the full stderr output to the user
  and ask them to correct the input values.
- Do not guess or substitute missing input values — always ask the user.
