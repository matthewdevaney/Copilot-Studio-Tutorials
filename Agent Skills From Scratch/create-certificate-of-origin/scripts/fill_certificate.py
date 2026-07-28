#!/usr/bin/env python3
"""
Fill a Manufacturer's Certificate of Origin PDF with vehicle details.

Writes values directly into the PDF's interactive form fields using pypdf.
Output is written to /app/created/ as MCO-<last5VIN>.pdf.
"""

import argparse
import sys
from pathlib import Path

try:
    import pypdf
except ImportError as e:
    print(f"ERROR: Missing required library: {e}", file=sys.stderr)
    sys.exit(1)

TEMPLATE_PDF = Path(__file__).parent.parent / "assets" / "CertificateOfOrigin-13b2f006.pdf"
OUTPUT_DIR   = Path("/app/created")


def fill_certificate(issue_date, invoice_number, vin,
                     model_year, model, manufacturer):
    reader = pypdf.PdfReader(str(TEMPLATE_PDF))
    writer = pypdf.PdfWriter()
    writer.append(reader)

    writer.update_page_form_field_values(
        writer.pages[0],
        {
            "IssueDate":       issue_date,
            "InvoiceNumber":   invoice_number,
            "VehicleIDNumber": vin,
            "ModelYear":       model_year,
            "Model":           model,
            "Manufacturer":    manufacturer,
        },
        auto_regenerate=False,
    )

    last5 = vin[-5:] if len(vin) >= 5 else vin
    output_path = OUTPUT_DIR / f"MCO-{last5}.pdf"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"SUCCESS: Certificate written to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Fill a Manufacturer's Certificate of Origin PDF"
    )
    parser.add_argument("--issue-date",     required=True, help="Issue date (e.g. 2026-07-25)")
    parser.add_argument("--invoice-number", required=True, help="Invoice number")
    parser.add_argument("--vin",            required=True, help="Vehicle Identification Number")
    parser.add_argument("--model-year",     required=True, help="Model year (e.g. 2026)")
    parser.add_argument("--model",          required=True, help="Vehicle model name")
    parser.add_argument("--manufacturer",   required=True, help="Manufacturer name")
    args = parser.parse_args()

    if not TEMPLATE_PDF.exists():
        print(f"ERROR: Template PDF not found at {TEMPLATE_PDF}", file=sys.stderr)
        sys.exit(1)

    fill_certificate(
        issue_date=args.issue_date,
        invoice_number=args.invoice_number,
        vin=args.vin,
        model_year=args.model_year,
        model=args.model,
        manufacturer=args.manufacturer,
    )


if __name__ == "__main__":
    main()
