# Copyright 2014-2023 The Open Source Company (www.tosc.nl).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "PS Account",
    "version": "14.0.1.0.0",
    "category": "accounts",
    "author": "The Open Source Company",
    "website": "http://www.tosc.nl",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_invoice_supplier_ref_unique",
        "report_qweb_operating_unit",
        "account_operating_unit",
        "operating_unit_report_layout",
        "ps_timesheet_invoicing",
        "report_qweb_pdf_watermark",
        "ps_calendar",
        "account_invoice_import",
        "account_move_tier_validation",
        "account_invoice_merge",
    ],
    "data": [
        "report/report_layout.xml",
        "report/report_invoice.xml",
        "views/account_move.xml",
        "views/project_view.xml",
        "report/account_invoice_report.xml",
    ],
    "demo": [
        "demo/operating_unit.xml",
        "demo/project_invoicing_properties.xml",
    ],
    "installable": True,
}
