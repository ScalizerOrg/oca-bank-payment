# Copyright 2026 Engenere - Felipe Motter Pereira
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # Moved here from account_payment_partner (2026-08-24): account_payment_partner
    # is not installed in this project (no manifest depends on it, only on
    # account_payment_mode), so this flag - and the guard that makes it effective in
    # _compute_partner_bank_id below - must live in account_payment_mode itself to
    # have any effect.
    keep_partner_bank_without_payment_mode = fields.Boolean(
        string="Keep Bank Account Without Payment Mode",
        default=True,
        help="When enabled, invoices without a payment mode will keep "
        "the bank account auto-selected by Odoo. When disabled, "
        "the bank account will be cleared if no payment mode is set.",
    )
