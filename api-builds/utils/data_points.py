
def cyber_data_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Additional Coverage',
        'Forms and Endorsements',
        'Endorsements',
        'Location',
        'Exclusions',
        'Limits of Liability',
        'Privacy Breach Response Services',
        'Business Interruption',
        'Media',
        'Social Engineering',
        'Terrorism',
        'Deductible or Retention',
        'Retroactive Date',
        'Prior and Pending Date',
        'Continuity Date',
        'Underlying Insurance'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict  # <-- no comma

def general_liability_data_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Each Occurrence Limit',
        'General Aggregate Limit',
        'Products or Completed Operations Aggregate',
        'Personal And Advertising Injury Limit',
        'Damage to Rented Premises Limit',
        'Medical Payments Limit',
        'Deductible',
        'Hazards Rating info',
        'Employee Benefit Liability Coverage',
        'Hired And Non owned Coverage',
        'Directors and Officers',
        'Cyber',
        'Professional Liability',
        'EPLI on Policy',
        'Errors and Omissions on Policy',
        'Terrorism',
        'Work Exclusion',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    # Convert list to dict with default regex (catch-all)
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict  # <-- no comma

def comercial_auto_data_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Symbol',
        'Limits',
        'vehiclesinfo',
        'scheduleddrivers',
        'hiredornon-ownedautolimits',
        'driveothercarcoverage',
        'terrorism',
        'exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms and Endorsements',
        'Endorsements',
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict  # <-- no comma

# utils/data_points.py
def business_owner_data_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'General Aggregate',
        'Products or Completed Operations Aggregate',
        'Personal And Advt Injury',
        'Medical expenses',
        'Damage to rented premises',
        'Each Occurrence',
        'Hired Or Non Owned Auto',
        'Deductible',
        "Schedule of Hazards Rating Info",
        'Additional Interest',
        'Employee Benefits Liability',
        'Directors and Officers',
        'Cyber',
        'Professional Liability',
        'EPLI on Policy',
        'Errors and Omissions on Policy',
        'Terrorism',
        'Work Exclusion',
        'Liability locations match property locations if applicable',
        'Building Value',
        'Business Personal Property Limit',
        'Business Income Limit',
        'Improvements and Betterments',
        'Wind And Hail',
        'Property Deductible',
        'Co Insurance',
        'Valuation',
        'Is Equipment Breakdown Listed',
        'Building Ordinance Or Law Listed Cov A',
        'Building Ordinance Demolition Cost Cov B',
        'Building Ordinance Inc Cost Of Construction Cov C',
        'Additional Interests',
        'Property Terrorism',
        'Inland Marine Details',
        'Equipment Schedule',
        'Deductibles',
        'Loss Payee',
        'Rental equipment from others',
        'Rental equipment to others',
        'Installation floater',
        'Inland Marine Terrorism',
        'Umbrella Limits',
        'Underlying Policies',
        'Policy Exclusions',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]

    # Convert list to dict with default regex (catch-all)
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def forms_hunting_points():
    return [
        "Forms and Endorsements complete list",
        "All form numbers, titles, and dates",
        "Endorsements list",
        "All insurance forms, notices, state filings",
        "Any text matching pattern like AA-123 (MM-YY)"
    ]

def property_data_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Building Value',
        'Improvements And Betterments',
        'Business Personal Property Limit',
        'Business Income Limit',
        'Wind and Hail',
        'Deductible',
        'Co Insurance',
        'Valuation',
        'Is Equipment Breakdown Listed',
        'Building Ordinance Or Law Listed Cov A',
        'Building Ordinance Demolition Cost Cov B',
        'Building Ordinance Inc Cost Of Construction Cov C',
        'Terrorism',
        'Exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict
    
def workers_compensation_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'FEIN',
        'Coverage States',
        'Other States',
        'Employers Limits',
        'Rating Info',
        'Experience Mod',
        'Changes in Credits',
        'Members Excluded',
        'Terrorism',
        'Exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def builder_risk_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid in Full Discount',
        'Miscellaneous Premium',
        'Location Address',
        'Family Dwelling',
        'Single structure policy',
        'Commercial Structure',
        'New Construction',
        'Remodeling',
        'Limits',
        'Deductible',
        'Amount of loss or damage',
        'Terrorism',
        'Exclusions',
        'Additional Coverage',
        'Additional Interests',
        'Forms and Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def commercial_earthquake_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Building Value',
        'Improvements And Betterments',
        'Business Personal Property Limit',
        'Business Income Limit',
        'Earthquake Limits',
        'Earthquake Deductible',
        'Wind and Hail',
        'Deductible',
        'Co Insurance',
        'Valuation',
        'Is Equipment Breakdown Listed',
        'Building Ordinance Or Law Listed Cov A',
        'Building Ordinance Demolition Cost Cov B',
        'Building Ordinance Inc Cost Of Construction Cov C',
        'Terrorism',
        'Exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements',
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def commercial_fire_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Building Value',
        'Improvements And Betterments',
        'Business Personal Property Limit',
        'Business Income Limit',
        'Cause of Loss',
        'Wind and Hail',
        'Deductible',
        'Co Insurance',
        'Valuation',
        'Is Equipment Breakdown Listed',
        'Building Ordinance Or Law Listed Cov A',
        'Building Ordinance Demolition Cost Cov B',
        'Building Ordinance Inc Cost Of Construction Cov C',
        'Terrorism',
        'Exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def commercial_flood_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Building Value',
        'Improvements And Betterments',
        'Business Personal Property Limit',
        'Business Income Limit',
        'Flood Limits',
        'Wind and Hail',
        'Deductible',
        'Co Insurance',
        'Valuation',
        'Is Equipment Breakdown Listed',
        'Building Ordinance Or Law Listed Cov A',
        'Building Ordinance Demolition Cost Cov B',
        'Building Ordinance Inc Cost Of Construction Cov C',
        'Terrorism',
        'Exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def crime_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Limts of Insurance',
        'Retention',
        'Additional Insured',
        'Additional Interest',
        'Additional Coverage',
        'Terrorism',
        'Exclusions',
        'Forms and Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def directors_and_officers_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Business Classification',
        'Limits of Liability',
        'Deductible or Retention',
        'Retro Date',
        'Prior and Pending Date',
        'Continuity Date',
        'Underlying Insurance',
        'Terrorism',
        'Exclusions',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def dwelling_fire_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Physical Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Dwelling Limit',
        'Other Structures',
        'Fair Rental Value',
        'Loss of use',
        'Personal Property',
        'Personal Liability',
        'Additional Living Expense',
        'Medical Payments',
        'Deductibles',
        'Windhail',
        'Water Backup',
        'Property Info',
        'Terrorism',
        'Exclusions',
        'Additional Interest',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def epli_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Limits of Liability',
        'Deductible or Retention',
        'Retro Date',
        'Prior and Pending Date',
        'Continuity Date',
        'Underlying Insurance',
        'Terrorism',
        'Exclusions',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def errors_omissions_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'Limits of Liability',
        'Deductible Or Retention',
        'Retro Date',
        'Prior and Pending Date',
        'Continuity Date',
        'Underlying Insurance',
        'Terrorism',
        'Exclusions',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def umbrella_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Underlying Policies ',
        'Retention',
        'Terrorism',
        'Exclusions',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

def master_business_owners_points():
    fields = [
        'Name Insured',
        'Other Named Insured',
        'Additional Insured',
        'Mailing Address',
        'Policy Number',
        'Policy Period',
        'Issuing Company',
        'Premium',
        'Paid In Full Discount',
        'Miscellaneous Premium',
        'Location',
        'General Aggregate',
        'Products or Completed Operations Aggregate',
        'Personal And Advt Injury',
        'Each Occurrence',
        'Damage to rented premises',
        'Medical expenses',
        'Hired Or Non Owned Auto',
        'Deductible',
        'Schedule of Hazards Rating Info',
        'Additional Interest',
        'Employee Benefits Liability',
        'Directors and Officers',
        'Cyber',
        'Professional Liability',
        'EPLI on Policy',
        'Errors and Omissions on Policy',
        'Garage Liability',
        'Crime',
        'Pollution Liability',
        'Liquor Liability',
        'Fiduciary Liability',
        'Commercial Flood',
        'Commercial Earthquake',
        'Terrorism',
        'Building Value',
        'Business Personal Property Limit',
        'Business Income Limit',
        'Improvements and Betterments',
        'Wind And Hail',
        'Earthquake',
        'Flood',
        'Property Deductible',
        'Co Insurance',
        'Valuation',
        'Is Equipment Breakdown Listed',
        'Building Ordinance Or Law Listed Cov A',
        'Building Ordinance Demolition Cost Cov B',
        'Building Ordinance Inc Cost Of Construction Cov C',
        'Additional Interests',
        'Property Terrorism',
        'Symbol',
        'Limits',
        'Vehicles Info',
        'Scheduled Drivers',
        'Hired Or Non owned Auto Limits',
        'Drive Other Car Coverage',
        'Lein Holder or Loss Payee',
        'Auto Terrorism',
        'Locations',
        'FEIN',
        'Coverage States',
        'Other States',
        'Employers Limits',
        'Rating Info',
        'Experience Mod',
        'Changes in Credits',
        'Members Excluded',
        'WC Terrorsim',
        'Inland Marine Details',
        'Equipment Schedule',
        'Deductibles',
        'Loss Payee',
        'Rental equipment from others',
        'Rental equipment to others',
        'Installation floater',
        'Inland Marine Terrorism',
        'Umbrella Limits',
        'Underlying Policies',
        'Policy Exclusions',
        'Additional Coverage',
        'Forms And Endorsements',
        'Endorsements'
    ]
    data_points_dict = {field: r"([\s\S]*?)" for field in fields}
    return data_points_dict

