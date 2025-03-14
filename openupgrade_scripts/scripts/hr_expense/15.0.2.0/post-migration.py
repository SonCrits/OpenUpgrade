from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "hr_expense", "15.0.2.0/noupdate_changes.xml")
    openupgrade.delete_record_translations(
        env.cr,
        "hr_expense",
        [
            "hr_expense_template_register",
        ],
    )
