# Copyright 2014-2023 The Open Source Company (www.tosc.nl).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet and Invoicing",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "summary": """This module introduces an advanced professional services invoicing process,
        offering fixed price, time and material, licensing and several combinations
         thereof""",
    "author": "The Open Source Company",
    "website": "http://www.tosc.nl",
    "category": "module_category_specific_industry_applications",
    "depends": [
        "account",
        "account_move_name_sequence",
        "analytic",
        "uom",
        "hr",
        "fleet",
        "ps_hr",
        "ps_crm",
        "data_time_tracker",
        "ps_date_range_week",
        "uom_unece",
        "ps_project",
        "web_m2x_options",
        "hr_timesheet_sheet",
        "analytic_base_department",
        "account_fiscal_month",
        "account_fiscal_year",
        "web_domain_field",
        "invoice_line_revenue_distribution_operating_unit",
        "queue_job",
    ],
    "data": [
        "data/account_analytic_tag.xml",
        "data/cron_data.xml",
        "data/data.xml",
        "data/date_range_type.xml",
        "security/ps_security.xml",
        "security/ir.model.access.csv",
        "wizard/time_line_invoice_view.xml",
        "wizard/change_chargecode_view.xml",
        "wizard/hr_employee_wizard.xml",
        "report/hr_chargeability_report.xml",
        "report/report_invoice.xml",
        "report/status_time_report.xml",
        "report/overtime_balance_report.xml",
        "report/crm_pipeline_actuals_report.xml",
        "views/hr_timesheet_sheet_view.xml",
        "views/project_timesheet_view.xml",
        "views/project_view.xml",
        "views/task_user.xml",
        "views/hr_department.xml",
        "views/ps_time_line_view.xml",
        "views/hr_employee.xml",
        "views/fleet_view.xml",
        "views/ps_invoice.xml",
        "views/product_view.xml",
        "views/account_move_view.xml",
        "views/invoice_view.xml",
        # 'views/inter_ou_account_mapping_view.xml',
        "views/menu_item.xml",
        "views/res_company_view.xml",
    ],
    "installable": True,
    "demo": [
        "demo/product_product.xml",
        "demo/account_analytic_account.xml",
        "demo/account_analytic_line.xml",
        "demo/date_range.xml",
        "demo/hr_department.xml",
        "demo/hr_employee.xml",
        "demo/project_invoicing_properties.xml",
        "demo/project_project.xml",
        "demo/res_company.xml",
        "demo/task_user.xml",
        # needs to be on the bottom
        "demo/ps_time_line.xml",
    ],
}
