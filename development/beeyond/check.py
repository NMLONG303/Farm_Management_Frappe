import os, sys, json

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.getcwd(), "sites"))
sys.path.insert(0, os.path.join(os.getcwd(), "apps"))
sys.path.insert(0, os.path.join(os.getcwd(), "env", "lib", "python3.14", "site-packages"))

import frappe
frappe.init(site="bfarm.localhost", sites_path="sites")
frappe.connect()

data = {
    "location_exists": frappe.db.exists("DocType", "Location"),
    "installed_apps": frappe.get_installed_apps(),
}
print(json.dumps(data))
frappe.destroy()
