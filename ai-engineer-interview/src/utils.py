import json
import os

def process_user_data_and_calculate_benefits_and_permissions(user_data, department_rules, salary_data, access_rules):
    result = {}
    
    if department_rules.get(user_data["department"], {}).get("level") == "senior":
        if salary_data["base"] > 100000:
            result["salary_band"] = "Executive"
            result["bonus_eligible"] = True
            result["stock_options"] = True
        else:
            result["salary_band"] = "Senior"
            result["bonus_eligible"] = True
            result["stock_options"] = False
    else:
        result["salary_band"] = "Junior"
        result["bonus_eligible"] = False
        result["stock_options"] = False
    
    if user_data["department"] == "Engineering":
        result["systems_access"] = ["github", "aws", "database"]
        result["admin_level"] = True
    elif user_data["department"] == "HR":
        result["systems_access"] = ["hr_system", "payroll"]
        result["admin_level"] = False
    elif user_data["department"] == "Marketing":
        result["systems_access"] = ["marketing_tools"]
        result["admin_level"] = False
    else:
        result["systems_access"] = ["basic_access"]
        result["admin_level"] = False
    
    years_experience = user_data.get("years_experience", 0)
    if years_experience > 10:
        result["vacation_days"] = 25
    elif years_experience > 5:
        result["vacation_days"] = 20
    else:
        result["vacation_days"] = 15
    
    if result["salary_band"] in ["Executive", "Senior"]:
        result["health_plan"] = "Premium"
        result["dental"] = True
        result["vision"] = True
    else:
        result["health_plan"] = "Basic"
        result["dental"] = False
        result["vision"] = False
    
    if user_data.get("remote_work", False):
        result["equipment_allowance"] = 1000
        result["internet_stipend"] = 50
    
    return result

def load_config_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_user_preferences(user_id, preferences):
    filepath = f"/tmp/user_{user_id}_prefs.json"
    with open(filepath, 'w') as f:
        json.dump(preferences, f)