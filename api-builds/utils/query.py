def prompt_template_cyber(large_text=None):

    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a cyber insurance PDF
        using a mix of digital text, OCR text, Rows and tables.

        ### Extraction Rules
        - **Search through the ENTIRE document for every required field**.
        - Dates must always be in MM/DD/YYYY format.
        - Do NOT stop at the first heading of “Forms and Endorsements” or “Endorsements”.
        Continue scanning to the **very end of the document**.
        - Merge multi-line form numbers/titles into a **single entry** if they are split
        across lines or pages.
        -socialengineering,businessinterruption,privacybreachresponseservices ( do not extract these values in additional coverages)these data should be extracted under individual datapoints
        - Preserve all numbers, dates, symbols, and formatting exactly as they appear.
        - Deduplicate only when text is truly identical.
        - If a field is missing, set it to `null`; if an array is empty, return `null`.
        - Output must be **only** a valid JSON object. No explanations or commentary.

        ### Datapoints to Extract ###
            1. Name Insured: 
            2. Other Named Insured: (Can also be called as DBA)
            3. Additional Insured: (retunr as array of objects with name and address)
            4. Mailing Address:
            5. Policy Number: (return only policy number not any other text around it)
            6. Policy Period: (MM/DD/YYYY to MM/DD/YYYY)
            7. Issuing Company:
            8. Premium: (include details)
            9. Paid In Full Discount
            10. Miscellaneous Premium
            11. Additional Coverage(s): (get all the possible information of coverages and sublimits of liability, return only value is present otherwise keep it has null)
            12. Forms and Endorsements: 
                Forms And Endorsements
                    - **Collect every form across the entire document**, including Property,
                        General Liability, Auto, Umbrella, Notices, and any state filings.
                    - Do NOT stop at the first “Forms and Endorsements” heading.
                    - Merge split lines into one entry.
                    - Normalize each entry strictly in this format:
                        "FormNumber | MM/YY   Form Title"
                    - Return **all forms** as a single JSON array.
            13. Endorsements: (don't include limits or Retention, and show when any of this is mentioned modified/changed/deleted/added details)
            14. Location (Extract only if it is present location address otherwise keep it has null)
            15. Exclusions: (return null value for this datapoint)
            16. Limits of Liability: (must list oliy liability limits with amounts which are not extracted in additional coverages section)
            17. Privacy Breach Response Services: (Limit value not premium)
            18. Business Interruption: (Limit value not premium)
            19. Media: (Limit value not premium)
            20. Social Engineering: (Limit value not premium)
            21. Terrorism: (return only if premium exist else keep it has null dont mention like "Waived")
            22. Deductible or Retention: 
            23. Retroactive Date[s]: (Extract only date)
            24. Prior and Pending Date: 
            25. Continuity Date[s]:
            26. Underlying Insurance: (list of insurance with details)

            {f'Text: {large_text}' if large_text else ''}

            Return only a pure JSON object, assigning null to any key without a corresponding value.
            """

def prompt_template_general(large_text=None):
    return f"""You are an expert insurance data extractor.
            The following text is extracted from a General insurance PDF
            using a mix of digital text, OCR text, Rows and tables.

            ### Extraction Rules
            - **Search through the ENTIRE document for every required field**.
            - **If a value is not explicitly present in the text, do NOT guess or invent it.**
            - Only extract values that are clearly present in the document.
            - If a field is missing, set it to `null`; if an array is empty, return `[]`.
            - Do NOT stop at the first heading of “Forms and Endorsements” or “Endorsements”.
            Continue scanning to the **very end of the document**.
            - Merge multi-line form numbers/titles into a **single entry** if they are split
            across lines or pages.
            - Preserve all numbers, dates, symbols, and formatting exactly as they appear.
            - Deduplicate only when text is truly identical.
            - Output must be **only** a valid JSON object. No explanations or commentary.
            - **Never fabricate, infer, or assume values. Only copy what is present.**

            ### Datapoints to Extract ###
            1. Name Insured (primary insured)
            2. Other Named Insured  (other named insureds)
            3. Additional Insured
            4. Mailing Address
            5. Policy Number
            6. Policy Period
            7. Issuing Company
            8. Premium
                - include all coverage premiums and total premium
            9. Paid In Full Discount
            10. Miscellaneous Premium
            11. Location (example:PREM 1 - 600 HARRISON ST FLOORS 3&4 - SAN FRANCISCO - CA - 94107)
            12. General Liability: (need to extract text along with value, example: "Medical expenses": "$10,000 any one person")
            - General Aggregate
            - Products or Completed Operations Aggregate
            - Personal And Advt Injury
            - Medical expenses
            - Damage to rented premises
            - Each Occurrence
            - Deductible
            - Hired Or Non Owned Auto
            - Schedule of Hazards Rating Info (extract *every* row/column, search entire document to get all data, return all rows and columns)
                - Loc/BLDG No
                - TERR
                - Classification Code
                - Coverage description
                - Description
                - Rating Basis
                - Exposure
                - Final Rate
                - Advance Premium
            - Additional Interest
            13. Employee Benefits Liability 
                Examle: "employeebenefitsliability": [
                    "Each Claim Limit": "$ 1,000,000",
                    "Aggregate Limit": "$ 1,000,000",
                    "Deductible": "$ 2,500 Each Claim",
                    "Retroactive Date": "06/30/2023"
                ]
            14. Directors and Officers
            15. Cyber
            16. Professional Liability
            17. EPLI on Policy
            18. Errors and Omissions on Policy
            19. Terrorism
            20. Work Exclusion
            21. Liability locations match property locations if applicable
            22. Property
                    -Building Value
                    -Business Personal Property Limit
                    -Business Income Limit
                    -Improvements and Betterments
                    -Wind And Hail
                    -Property Deductible
                    -Co Insurance
                    -Valuation
                    -Is Equipment Breakdown Listed
                    -Building Ordinance Or Law Listed Cov A
                    -Building Ordinance Demolition Cost Cov B
                    -Building Ordinance Inc Cost Of Construction Cov C
                    -Additional Interests
            23. Property Terrorism (data which is present in buidling prperty values under property declarations)
            24. Inland Marine Details
            25. Equipment Schedule
            26. Deductibles (extract only deductibles mentioned undder this section, not extract from other sections)
            27. Loss Payee (loss payee/ mortgage)
            28. Rental equipment from others
            29. Rental equipment to others
            30. Installation floater
            31. Inland Marine Terrorism (terrosion present under the inland marine page should be extracted)
            32. Umbrella Limits (Limits present under umbrella coverages)
            33. Underlying Policies(Extract only data ubder this section and return full details)
            34. Policy Exclusions (Note: Only mention Policy Exclusions not Exclusions)
            35. Additional Coverage(s)(Extract on coverages and their values)

            36. Forms And Endorsements
                - Extraction only forms from "Forms And Endorsements" section.
                - Normalize each entry strictly in this format:
                "FormNumber | MM/YY   Form Title" (if coverage also exist return as BOP BP0159 |  08/08  WATER EXCLUSION ENDORSEMENT )
                - Return **all forms** as a single JSON array.

            37. EndorsementsEndorsements (Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
                - Extract only from particular endorsement declaration page

            ### Output Rules
            - Return **only** the structured JSON object with the keys above in the exact order.
            - Dates → MM/DD/YYYY
            - Currency → keep "$" and commas as shown.
            - Missing values → null.

            {f'Text: {large_text}' if large_text else ''}
            """

def prompt_template_commercial_auto(large_text=None):
    return f"""You are an expert insurance data extractor.
        The following text is extracted from a Property insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Extraction Rules ###
            - Extract datapoints exactly as they appear (preserve numbers, punctuation, symbols and wording).  
            - All symbols used in the document (e.g., $, %, commas) must be preserved as-is in the JSON.  
            - Dates must always be in MM/DD/YYYY format.  
            - The Policy Period must be split into start and end.  
            - For Policy Period End, check alternative labels: "PROPOSED EXP DATE", "Expiration Date", "End date".  
            - End date should not be null if present anywhere in the document.  
            - Premiums must be extracted in the format:
                "Coverage Name": "$1,147.49"
            - Symbols must be extracted in the format:
                Example: "Category": 1, 2, 7, 8, 9
            - Vehicles Info must be extracted in the format:
                "Unit : 1. - VIN : 1FTNX21F93EB04329 - Year : 2003 - Make : FORD - Model : F250 - PREMIUM : $1,612.57"

            - Scheduled Drivers must be extracted in the format:
                {{NameLast, FirstName, DOB or Age, State, License Number, Premium}}
                - Include all available fields exactly as in the document
                - Return as an array of objects
                - Multiple values (Limits, Vehicles, Endorsements, Additional Interests, etc.) must always be returned in arrays.  
                - If a datapoint is missing, explicitly set it to null (or null for arrays).  
                - Do not assume or invent values — only return if present.  
                - Output must be a pure JSON object with no extra commentary.
            ### Datapoints to Extract ###
            1. Name Insured  
            2. Other Named Insured 
            3. Additional Insured → [{{Name, Address}}]  
            4. Mailing Address (extract only mailing address not any other address like location address etc) 
            5. Policy Number  
            6. Policy Period → (MM/DD/YYYY to MM/DD/YYYY) 
            7. Issuing Company  
            8. Premium (extract only coverage premiums and total premium, not vehicles, taxes or fees or limits) 
            9. Paid In Full Discount  
            10. Miscellaneous Premium (extract only if present, else keep it has null) 
            11. Location (Extract location under declaration page only, if multiple locations return all locations in array otherwise null)
            12. Symbol (extract only which was selected by crossmark)
                - Example:"symbol": [
                        "Combined Liability": "7, 8, 9, 19",
                        "Uninsured Motorist": "6",
                        "Underinsured Motorist": "6",
                        "Personal Injury Protection": "7",
                        "Comprehensive": "7",
                        "Collision": "7",
                        "Road Trouble Service": "7",
                        "Additional Expense": "7"]
            13. Limits (return only coverage limits with values, when there is no value dont extract the label)
                - Extract only from declaration page only, not from hired and non owned auto pages
                - Example: [LIABILITY- BI EACH ACCIDENT : $1000000
                            MEDICAL PAYMENTS -EACH PERSON : $5000]
            14. Vehicles Info 
                - Must capture all vehicles listed with full details
                - Return each vehicle in the specified format
                - Example: "Unit : 1. - VIN : 1FTNX21F93EB04329 - Year : 2003 - Make : FORD - Model : F250 - PREMIUM : $1,612.57"  
                - If model is null then output should be like this: "Unit : 1. - VIN : 1FTNX21F93EB04329 - Year : 2003 - Make : FORD - PREMIUM : $1,612.57"
                - Return costnew values also if and if it is present under this section only
            15. Scheduled Drivers → [{{NameLast, FirstName, DOB or Age, State, License Number, Premium}}]  
            16. Hired Or Non-Owned Auto Limits → {{Hired Autos Liability, Non-Owned Autos Liability}}  
            17. Drive Other Car Coverage   (Extract only if data present at declaration page, else keep it has null)
            18. Terrorism (Extrcat only if data present at premiums or schedule of terrorism act page, Only return if it has numerical value else return null)  
            19. Exclusions (Extrcat only if data present at this particular section)  
            20. Additional Interest → [{{Name, Address, Role if specified}}]  
            21. Additional Coverage(s) (include coverage which are not extracted in previous datapoints only, and return label which consists values only) 
            22. Forms and Endorsements: 
                Forms And Endorsements
                    - **Collect every form across the entire document**, including Property,
                    General Liability, Auto, Umbrella, Notices, and any state filings.
                    - Do NOT stop at the first “Forms and Endorsements” heading.
                    - Merge split lines into one entry.
                    - Normalize each entry strictly in this format:
                    "FormNumber | MM/YY   Form Title"
                    - Return **all forms** as a single JSON array.
            23. EndorsementsEndorsements (Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
                    - Extract only from particular endorsement declaration page
            ### Final Output Rules ###
            - Must return a single valid JSON object only.  
            - Missing datapoints must be null.  
            ### Special Priority ###
            Ensure **all datapoints** are extracted if present.  
            Pay particular attention to **Vehicles Info** and **Scheduled Drivers**, as these often appear in structured tables.  
            Do not skip or truncate them.  

            ### DOCUMENT CONTENT ###
            {f'Text: {large_text}' if large_text else ''}
            """

def prompt_template_general_liability(large_text=None):
    return f"""
            The following text is extracted from a insurance PDF
            using a mix of digital text, OCR text, Rows and tables.
            ### Extraction Rules
            -for following datapoints the data should be extracted which is present under the that particular declaration page only :
                1.Employee Benefits Liability
                2.Directors and Officers
                3.Cyber
                4.Professional Liability
                5.EPLI on Policy
                6.Inland Marine Details
                7.Equipment Schedule
            - **Search through the ENTIRE document for every required field**.
            - Do NOT stop at the first heading of “Forms and Endorsements” or “Endorsements”.
            Continue scanning to the **very end of the document**.
            - Merge multi-line form numbers/titles into a **single entry** if they are split
            across lines or pages.
            - Preserve all numbers, dates, symbols, and formatting exactly as they appear.
            - Deduplicate only when text is truly identical.
            - If a field is missing, set it to `null`; if an array is empty, return `null`.
            - Output must be **only** a valid JSON object. No explanations or commentary.

            ### Datapoints to Extract ###
            1. Name Insured (name primary insured)
            2. Other Named Insured - (DBA, alternate names, or any entity listed as an additional named insured, including "doing business as", "DBA", "Also Known As", "a/k/a", "t/a", "f/k/a", or similar labels. Extract all such names and return as an array. If none, return null.)
            3. Additional Insured: Includes any party listed as an additional insured under the same entity name, a separate named insured, or a 'doing business as' (DBA) designation.
            4. Mailing Address
            5. Policy Number (extract only policy number not any other text around it or any other number like reactivation number, renewal no etc)
            6. Policy Period (MM/DD/YYYY to MM/DD/YYYY)
            7. Issuing Company
            8. Premium
                - include all coverage premiums and total premium
            9. Paid In Full Discount
            10. Miscellaneous Premium
            11. Location (Extract Full location details icluding premises number, building number, suite, city, state, zip etc if and they exist in lacation section only)
                -Example: [ "PREM": "001","BLDG": "001", "Address": "3690 NW Adriatic Lane #107","City": "Jensen Beach","State": "FL","Zip": "34957"]
            -12. The datapoints mentioned from 13 to 18 should follows below description and each datapoint should treated as individual primary key
            - Extract the value **only from the "General Liability declaration page or section"**. Do not extract from other sections, schedules, or tables execpt for Schedule of Hazards Rating Info.
            - *Schedule of Hazards Rating Info* if these details are present in this section, then extract data from other section or table which consists the Class code, Description, Rating Basis, Exposure, Final Rate, Advance Premium etc. 
            - For each, include both the value (e.g., "$5,000") and any descriptive text that appears after the value (e.g., "Per Occurrence", "Any One Premise", etc.).
            - Output format for each: "<value> <descriptive text after value>" , not like "Medical expenses": "$10,000 Medical Expenses Limit",
            - Example: 
                - "Medical expenses": "$5,000 Per Occurrence"
                - "Personal And Advt Injury": "$1,000,000 Per Occurrence"
                - "Damage to rented premises": "$50,000 Any One Premise"
            13. General Aggregate Limit
            14. Products or Completed Operations Aggregate
            15. Personal And Advertising Injury Limit
            16. Damage to Rented Premises Limit
            17. Medical Payments Limit
            18. Hazards Rating info (extract class code, Classification, Exposure, Premium Basis, Rate)
            19. Employee Benefit Liability Coverage
            20. Hired And Non owned Coverage (don't extract from auto liability page)
            21. Directors and Officers
            22. Cyber(data should be extracted only which is present under the that particular "cyber" declaration page only)
            23. Professional Liability
            24. EPLI on Policy
            25. Errors and Omissions on Policy (Extract only from the "Errors and Omissions" declaration page or section)
            26. Terrorism (Extract only if it has a numerical value otherwise keep it has null)
            27. Work Exclusion (Extract only if it has a numerical value otherwise donot extract, if no data extected keep it as null)
            28. Additional Interest
            29. Additional Coverage (return all coverages with values,when there is no value dont extract the label)
            30. Forms And Endorsements
                - Extraction only forms from "Forms And Endorsements" section.
                - Normalize each entry strictly in this format:
                "FormNumber | MM/YY   Form Title" (if coverage also exist return as BOP BP0159 |  08/08  WATER EXCLUSION ENDORSEMENT )
                - Return **all forms** as a single JSON array
            31. EndorsementsEndorsements (Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
                - Extract only from particular endorsement declaration page otherwise keep it null

            ### Retrieved Sections
            {f'Text: {large_text}' if large_text else ''}

            ### Final Output
            ### Output Rules
            - Return **only** the structured JSON object with the keys above in the exact order.
            - Dates → MM/DD/YYYY
            - Currency → keep "$" and commas as shown.
            - Missing values → null.
            """

def prompt_template_property(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Property insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null` (or `[]` for arrays).
  
 
    ### Datapoints to Extract ###
    1. Name Insured (primary insured only, do not include any other named insureds here like DBA etc) 
    2. Other Named Insured  (it may have like DBA, do not extract from additional named insureds section)
    3. Additional Insured ( extract from Additional Named Insureds section and extract only name not address) 
    4. Mailing Address  
    5. Policy Number ( do not extract qoute number or qoutation number)
    6. Policy Period → {{"Start": "MM/DD/YYYY", "End": "MM/DD/YYYY"}}  
    7. Issuing Company  
    8. Premium → include all coverage-level premiums and the total premium  
    9. Paid In Full Discount  
    10. Miscellaneous Premium  

    11. Location  
        - Must capture all risk location details (address, suite, city, state, ZIP).  
        - If labeled as "Location", "Premises", "Risk Address", "Schedule of Locations", or "Description of Premises", extract it.  
        - If multiple locations exist, return all of them in an array.  
        - If no separate location is listed, but the insured premises address matches the mailing address, return that under Location as well.  

    12. Property (look across declarations, schedules, endorsements, and forms)  
        - Building Value:  
            * Search for "DESCRIPTION OF PREMISES:", "Building Value", "Building Limit", "Limit of Insurance", "Coverage A - Building", "Building Coverage", "Building Amount".  
            * Always include PREM and BLDG identifiers if available.  
            * Format: "PREM x - BLDG y - Building - $<amount> - <coverage description>".  
            * Example: "PREM 2 - BLDG 1 - Building - $1,007,000 - Special Form Including Theft".  
            * Return multiple buildings in an array.  
        - Business Income Limit  
        - Improvements and Betterments  
        - Wind and Hail (if included or excluded)  
        - Property Deductible (search for all deductibles, including general and peril-specific).  
        - Co-Insurance:  
            * Always capture with PREM and BLDG context.  
            * Example: "PREM 1 - BLDG 1 - 80%".  
        - Valuation:  
            * Extract basis per building (RC = Replacement Cost, ACV = Actual Cost Value, etc.).  
            * Format: "PREM x - BLDG y - <valuation text>".  
        - Is Equipment Breakdown Listed?  
        - Building Ordinance or Law Coverage A  
        - Building Ordinance Demolition Cost Coverage B  
        - Building Ordinance Increased Cost of Construction Coverage C  
        - Additional Interests (e.g., Mortgage Holders)  

    13. Terrorism → {{"Coverage": "string", "Premium": "string", "Exclusions": ["string"], "Inclusion_Status": "string"}}  
    14. Exclusions → all exclusions explicitly listed in the policy  
    15. Additional Interest → [{{"Name": "string", "Address": "string", "Role": "string"}}]  
    16. Additional Coverage → include all additional coverages  

    17. Forms And Endorsements  
        - **Collect every form across the entire document**, including but not limited to
          Property, General Liability, Auto, Umbrella, Notices, and State filings.  
        - Do NOT stop at the first "Forms and Endorsements" heading—scan to the end of
          the document.  
        - Merge lines if a form number or title is split.  
        - Normalize strictly into this format:  
          "FormNumber (MM-YY) | MM/YY   Form Title"  
        - Return **all forms** as a single JSON array, even if they belong to different
          coverage parts.

    18. Endorsements  
        - Extract every endorsement with Title, Effective Date, and any available details.  
        - Merge multi-line descriptions into one string.

    ### Output Rules
    - Return **only a valid JSON object** with the above keys.
    - Dates → MM/DD/YYYY
    - Currency → preserve `$` and commas
    - Arrays → [] if not found
    - Missing values → null

    {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_business_owner(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Business Owner’s Policy (BOP) insurance PDF
    using a mix of digital text, OCR text, Rows and tables.

    ### Extraction Rules
    -for following datapoints the data should be extracted which is present under the that particular declaration page only 
        1.Employee Benefits Liability
        2.Directors and Officers
        3.Cyber
        4.Professional Liability
        5.EPLI on Policy
        6.Inland Marine Details
        7.Equipment Schedule
    -NO data for these datapoints, pass them as null:
        Policy Exclusions
        Rental equipment from others
        Rental equipment to others
        Work Exclusion
        Liability locations match property locations if applicable
        Miscellaneous Premium 
    - **Search through the ENTIRE document for every required field**.
    - Do NOT stop at the first heading of “Forms and Endorsements” or “Endorsements”.
      Continue scanning to the **very end of the document**.
    - Merge multi-line form numbers/titles into a **single entry** if they are split
      across lines or pages.
    - Preserve all numbers, dates, symbols, and formatting exactly as they appear.
    - Deduplicate only when text is truly identical.
    - If a field is missing, set it to `null`; if an array is empty, return `null`.
    - Output must be **only** a valid JSON object. No explanations or commentary.

    ### Datapoints to Extract ###
    1. Name Insured (primary insured only, do not include any other named insureds here like DBA etc) 
    2. Other Named Insured  (it may have like DBA, do not extract from additional named insureds section)
    3. Additional Insured (it will be with same name or other named insured or DBA and should be extracted from additional named insureds section only)
    4. Mailing Address
    5. Policy Number
    6. Policy Period
    7. Issuing Company
    8. Premium 
    9. Paid In Full Discount (Present in premium( need to extract the data which is present under discounted premium))
    10. Miscellaneous Premium(like taxes, fees, surcharges etc, if amount not found return null)
    11. Location
        - Extract location details **only from the "declaration of location" page or section**.
        - Do not extract location data from other sections, schedules, or tables.
        - If multiple locations are listed in the declaration of location, return all as an array.
        - If no location is found in the declaration of location, set this field to null.
    
    -12. The datapoints mentioned from 13 to 22 should follows below description and each datapoint should treated as individual primary key
    - Extract the value **only from the "General Liability declaration page or section"**. Do not extract from other sections, schedules, or tables execpt for Schedule of Hazards Rating Info.
    - *Schedule of Hazards Rating Info* if these details are present in this section, then extract data from other section or table which consists the Class code, Description, Rating Basis, Exposure, Final Rate, Advance Premium etc. 
    - For each, include both the value (e.g., "$5,000") and any descriptive text that appears after the value (e.g., "Per Occurrence", "Any One Premise", etc.).
    - Output format for each: "<value> <descriptive text after value>" , not like "Medical expenses": "$10,000 Medical Expenses Limit",
    - Example: 
        - "Medical expenses": "$5,000 Per Occurrence"
        - "Personal And Advt Injury": "$1,000,000 Per Occurrence"
        - "Damage to rented premises": "$50,000 Any One Premise"
    13. General Aggregate
    14. Products or Completed Operations Aggregate
    15. Personal And Advt Injury
    16. Medical expenses
    17. Damage to rented premises
    18. Each Occurrence
    19. Deductible
    20. Hired Or Non Owned Auto
    21. "Schedule of Hazards Rating Info". Return as an array of dictionaries, each with:
            -Loc/BLDG No
            -TERR
            -Classification Code
            -Coverage description
            -Description
            -Rating Basis
            -Expoure
            -Final Rate
    22. Additional Interest
    23. Employee Benefits Liability
    24. Directors and Officers
    25. Cyber(data should be extracted only which is present under the that particular "cyber" declaration page only)
    26. Professional Liability
    27. EPLI on Policy
    28. Errors and Omissions on Policy
    29. Terrorism (Extrcat only if data present at premiums or schedule of terrorism act page)
    30. Work Exclusion
    31. Liability locations match property locations if applicable
    32. The datapoints mentioned from 33 to 45 should follows below description and each datapoint should treated as individual primary key
    - (Need to extract the datapoints in individual dictionary but not under the general liability dictionary, And this data should be extracted which is present under the property declaration page only)
    33. Building Value
    34. Business Personal Property Limit - (need to extract prem.no,bldg.no labels and its values along with limit data)
    35. Business Income Limit - (must and should extract complete value of it and if value consists "INCLUDED" then "included" comes in last index of value)
    36. Improvements and Betterments
    37. Wind And Hail
    38. Property Deductible - (need to extract prem.no,bldg.no labels and its values along with limit data and all deductible under this section only)
    39. Co Insurance
    40. Valuation
    41. Is Equipment Breakdown Listed
    42. Building Ordinance Or Law Listed Cov A
    43. Building Ordinance Demolition Cost Cov B
    44. Building Ordinance Inc Cost Of Construction Cov C
    45. Additional Interests (extract only from property declaration page only)
    46. Property Terrorism (data which is present in buidling prperty values under property declarations)
    47. Inland Marine Details
    48. Equipment Schedule
    49. Deductibles (extract only deductibles mentioned under this section, not extract from other sections)
    50. Loss Payee (loss payee/ mortgage)
    51. Rental equipment from others
    52. Rental equipment to others
    53. Installation floater
    54. Inland Marine Terrorism (terrosion present under the inland marine page should be extracted)
    55. Umbrella Limits (Limits present under umbrella coverages)
    56. Underlying Policies(Extract only data ubder this section and return full details)
    57. Policy Exclusions (Note: Only mention Policy Exclusions not Exclusions)
    58. Additional Coverage (Extract on coverages and their values)
    59. Forms And Endorsements
        - Extraction only forms from "Forms And Endorsements" section.
        - Normalize each entry strictly in this format:
          "FormNumber | MM/YY   Form Title" (if coverage also exist return as BOP BP0159 |  08/08  WATER EXCLUSION ENDORSEMENT )
        - Return **all forms** as a single JSON array.

    60. EndorsementsEndorsements (Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page

    ### Output Rules
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.

    {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_package(large_text=None):
    return f"""You are an expert insurance data extractor. Extract data from the Package insurance PDF text below with ABSOLUTE CONSISTENCY.

            ### CRITICAL CONSISTENCY RULES
            1. Extract EXACTLY what is written - no interpretation, no inference
            2. Use IDENTICAL formatting patterns for similar data types
            3. When multiple valid options exist, ALWAYS choose the FIRST occurrence
            4. If uncertain between multiple values, return ALL as comma-separated string
            5. Preserve original spacing, punctuation, and case EXACTLY as shown
            6. **FOR PROPERTY FIELDS: NEVER extract just the value - ALWAYS include the complete location/building identifiers in the EXACT format shown in the document**
            - WRONG: "Co Insurance": "80%"
            - CORRECT: "Co Insurance": ["LOCATION : # 1 - BUILDING # 1 - Building : 80%"]
            - WRONG: "Valuation": "RC"
            - CORRECT: "Valuation": ["Location Number : 0001 - Building Number : 001 - Building - Replacement Cost"]

            ### SCOPE RULES (CRITICAL - READ CAREFULLY)
            Extract data ONLY from these specific declaration pages/sections:
            - Employee Benefits Liability → Only from its declaration page
            - Directors and Officers → Only from its declaration page  
            - Cyber → Only from "Cyber" declaration page
            - Professional Liability → Only from its declaration page
            - EPLI on Policy → Only from its declaration page
            - Inland Marine Details → Only from its declaration page
            - Equipment Schedule → Only from its declaration page
            - Property → Only from Property declaration page
            - General Liability → Only from General Liability declaration page (EXCEPTION: Schedule of Hazards may reference other sections)

            ### NULL VALUES (Set these to null - do NOT search for them)
            - Policy Exclusions
            - Work Exclusion
            - Liability locations match property locations if applicable
            - Miscellaneous Premium

            ### EXTRACTION DATAPOINTS

            **1. Name Insured**
            - Extract: Full legal name as shown on declaration page
            - Format: Exact text as written

            **2. Other Named Insured**
            - Extract: Any DBA or alternate business names
            - Format: Exact text, or null if absent

            **3. Additional Insured**
            - Extract: Names listed as additional insured
            - Format: If multiple, return as array; otherwise single string

            **4. Mailing Address**
            - Extract: Complete mailing address
            - Format: Single line with commas: "Street, City, ST Zip"

            **5. Policy Number**
            - Extract: Policy/contract number
            - Format: Exact alphanumeric as shown

            **6. Policy Period**
            - Extract: Start and end dates
            - Format: "MM/DD/YYYY to MM/DD/YYYY" (must have only this format, do not mention start and end keys)

            **7. Issuing Company**
            - Extract: Insurance company name
            - Format: Exact text as written

            **8. Premium**
            - Extract: ALL premium line items from premium section up to "Total Premium"
            - Format: Object with keys as premium labels, values as amounts
            - Example: {{"General Liability Premium": "$5,000", "Property Premium": "$3,000", "Total Premium": "$8,000"}}
            - Include currency symbol and commas

            **9. Paid In Full Discount**
            - Extract: Discount amount from discounted premium section
            - Format: "$X,XXX" or null

            **10. Miscellaneous Premium**
            - Status: ALWAYS return null (per scope rules)

            **11. Location**
            - Extract: ONLY from "Declaration of Location" page/section
            - Format: "LocNum Address, City, ST Zip"
            - Example: "1 1731 W Business U.S. 60, Dexter, MO 63841"
            - If multiple: return as array
            - If none in Declaration of Location: null

            12. The datapoints mentioned from 13 to 23 should follows below description and each datapoint should treated as individual primary key
            - Extract the value **only from the "General Liability declaration page or section"**. Do not extract from other sections, schedules, or tables execpt for Schedule of Hazards Rating Info.
            - *Schedule of Hazards Rating Info* if these details are present in this section, then extract data from other section or table which consists the Class code, Description, Rating Basis, Exposure, Final Rate, Advance Premium etc. 
            - For each, include both the value (e.g., "$5,000") and any descriptive text that appears after the value (e.g., "Per Occurrence", "Any One Premise", etc.).
            - Output format for each: "<value> <descriptive text after value>" , not like "Medical expenses": "$10,000 Medical Expenses Limit",
            - Example: 
                - "Medical expenses": "$5,000 Per Occurrence"
                - "Personal And Advt Injury": "$1,000,000 Per Occurrence"
                - "Damage to rented premises": "$50,000 Any One Premise"
            13. General Aggregate
            14. Products or Completed Operations Aggregate
            15. Personal And Advt Injury
            16. Medical expenses
            17. Damage to rented premises
            18. Each Occurrence
            19. Deductible
            20. Hired Or Non Owned Auto
            21. Additional Interest
            22. "Schedule of Hazards Rating Info". Return as an array of dictionaries, each with:
                    -Loc/BLDG No
                    -TERR
                    -Classification Code
                    -Coverage description
                    -Description
                    -Rating Basis
                    -Expoure
                    -Final Rate
                    -Advance Premium

            **23. Employee Benefits Liability**
            - Extract: ONLY from its declaration page
            - Format: Object with coverage details or null

            **24. Directors and Officers**
            - Extract: ONLY from its declaration page
            - Format: Object with coverage details or null

            **25. Cyber**
            - Extract: ONLY from Cyber declaration page
            - Format: Object with coverage details or null

            **26. Professional Liability**
            - Extract: ONLY from its declaration page
            - Format: Object with coverage details or null

            **27. EPLI on Policy**
            - Extract: ONLY from its declaration page
            - Format: Object with coverage details or null

            **28. Errors and Omissions on Policy**
            - Extract: Coverage details if present
            - Format: Object with details or null

            **29. Terrorism**
            - Extract: ONLY if present in premiums or "Schedule of Terrorism Act" page
            - Format: Object with details or null

            **30. Work Exclusion**
            - Status: ALWAYS return null (per scope rules)

            **31. Liability locations match property locations if applicable**
            - Status: ALWAYS return null (per scope rules)

            **32. The datapoints mentioned from 35 to 46 should follows below description and each datapoint should treated as individual primary key
            - (Need to extract the datapoints in individual dictionary but not under the general liability dictionary, And this data should be extracted which is present under the property declaration page only)

            **IMPORTANT: For fields marked as ARRAY, must extract ALL occurrences with format mentioned and return as array of strings**

            33. "Building Value": ARRAY - Extract ALL buildings
            * Format per entry: "Location Number : XXXX - Building Number : XXX - $X,XXX,XXX - Cause Of Loss : [type] - Premium : $X,XXX.XX"
            * Example: ["Location Number : 0001 - Building Number : 001 - $4,722,000 - Cause Of Loss : Special Including Theft - Premium : $6,324.00"]

            34. "Business Personal Property Limit": ARRAY - Extract ALL occurrences
            * Format per entry: "Location Number : XXXX - Occupancy Number : XXX - $XXX,XXX - Cause Of Loss : [type] - Premium : $X,XXX.XX"
            * Example: ["Location Number : 0001 - Occupancy Number : 001 - $472,200 - Cause Of Loss : Special Including Theft - Premium : $1,283.00"]

            35. "Business Income Limit": ARRAY - Extract ALL occurrences
            * Format per entry: "Location Number : XXXX - Building Number : XXX - $XXX,XXX - Cause Of Loss : [type] - Premium : $X,XXX.XX"

            36. "Improvements and Betterments": ARRAY - Extract ALL occurrences
            * Format per entry: "Location Number : XXXX - Building Number : XXX - $XXX,XXX - Cause Of Loss : [type] - Premium : $X,XXX.XX"

            37. "Wind And Hail": ARRAY - Extract ALL occurrences
            * Format per entry: "Location Number : XXXX - Building Number : XXX - Building - Wind Or Hail Deductible : X%"
            * Example: ["Location Number : 0001 - Building Number : 001 - Building - Wind Or Hail Deductible : 2%"]

            38. "Property Deductible": ARRAY - Extract ALL deductibles under this section
            * Format per entry: "Location Number : XXXX - Building Number : XXX - Building - $X,XXX"
            * Example: ["Location Number : 0001 - Building Number : 001 - Building - $5,000", "Location Number : 0002 - Building Number : 001 - Building - $7,500"]

            39. "Co Insurance": ARRAY - Extract ALL occurrences with COMPLETE location and building identifiers
            * **CRITICAL**: DO NOT extract just "80%" - MUST include Co insurance of all locations and buildings with their numbers
            * Format per entry: "LOCATION : # X - BUILDING # X - Building : XX%"
            * Example: ["LOCATION : # 1 - BUILDING # 1 - Building : 80%", "LOCATION : # 2 - BUILDING # 1 - Building : 80%"]
            * If document uses "Location Number" format, use: "Location Number : XXXX - Building Number : XXX - Building - XX%"
            * Extract the ENTIRE row/line including all location identifiers, not just the percentage

            40. "Valuation": ARRAY - Extract ALL occurrences with COMPLETE location and building identifiers
            * **CRITICAL**: DO NOT extract just "RC" or "Replacement Cost" - MUST include location and building numbers
            * Format per entry: "Location Number : XXXX - Building Number : XXX - Building - [valuation type]"
            * Example: ["Location Number : 0001 - Building Number : 001 - Building - Replacement Cost", "Location Number : 0002 - Building Number : 001 - Building - Actual Cash Value"]
            * If document uses "LOCATION : #" format, adapt accordingly
            * Extract the ENTIRE row/line including all location identifiers, not just the valuation type

            41. "Is Equipment Breakdown Listed": "Yes" or "No" or null

            42. "Building Ordinance Or Law Listed Cov A": ARRAY or null - Extract ALL if multiple
            * Format per entry: "Location Number : XXXX - Building Number : XXX - $XXX,XXX" or just amount

            43. "Building Ordinance Demolition Cost Cov B": ARRAY or null - Extract ALL if multiple
            * Format per entry: "Location Number : XXXX - Building Number : XXX - $XXX,XXX" or just amount

            44. "Building Ordinance Inc Cost Of Construction Cov C": ARRAY or null - Extract ALL if multiple
            * Format per entry: "Location Number : XXXX - Building Number : XXX - $XXX,XXX" or just amount

            45. "Additional Interests": ARRAY of objects or null
            - Extract: ALL additional interests (from property section only)

            **46. Property Terrorism**
            - Extract: Terrorism values within building property values under Property declarations
            - Format: Object or null

            **47. Inland Marine Details**
            - Extract: ONLY from Inland Marine declaration page
            - Format: Object with details or null

            **48. Equipment Schedule**
            - Extract: ONLY from Equipment Schedule section
            - Format: Array of equipment items or null

            **49. Deductibles**
            - Extract: ONLY from section labeled "Deductibles"
            - Do NOT extract deductibles from other sections
            - Format: Object with deductible types and amounts

            **50. Loss Payee**
            - Extract: Loss payee or mortgage information page only
            - Format: Array of names/addresses or null

            **51. Rental equipment from others**
            - Extract: EXACT text and amount as written on the declaration page or Inland Marine section (whichever explicitly lists it)
            - Format: "$X,XXX" or exact value shown
            - If multiple values appear, return ALL as a comma-separated string in the exact order of appearance
            - If not present: null

            **52. Rental equipment to others**
            - Extract: EXACT text and amount as written on the declaration page or Inland Marine section (whichever explicitly lists it)
            - Format: "$X,XXX" or exact value shown
            - If multiple values appear, return ALL as a comma-separated string in the exact order of appearance
            - If not present: null

            **53. Installation floater**
            - Extract: Coverage details if present
            - Format: Object or null

            **54. Inland Marine Terrorism**
            - Extract: Terrorism section under Inland Marine page only
            - Format: Object or null

            **55. Umbrella Limits**
            - Extract: Limits from Umbrella coverages section
            - Format: Object with limit types and amounts

            **56. Underlying Policies**
            - Extract: ONLY from "Underlying Policies" section
            - Return COMPLETE details as shown
            - Format: Array of policy objects with all fields

            **57. Policy Exclusions**
            - Status: ALWAYS return null (per scope rules)

            **58. Additional Coverage**
            - Extract: Coverage names and values
            - Format: Object with coverage names as keys, values as amounts

            **59. Forms And Endorsements**
            - Extract: ONLY from "Forms And Endorsements" section
            - Scan to END of document
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title"
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only)

            **60. Endorsements**
            - Extract: ONLY from endorsement declaration page
            - Include: Description of changes (changed, added, deleted, estimated total premium, paid in full discount)
            - Format: Object with change details

            ### FINAL INSTRUCTIONS
            - Return ONLY valid JSON - no explanations, no markdown code blocks, no preamble
            - All dates: MM/DD/YYYY format
            - All currency: Keep $ symbol and commas
            - Missing data: null
            - Empty arrays: null (not [])
            - When in doubt: Extract exactly as written, no assumptions

            {f'Text: {large_text}' if large_text else ''}
            """

def prompt_template_workers_compensation(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Workers Compensation insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null`

    ### Datapoints to Extract ###
    1. Name Insured
    2. Other Named Insured ----- sometimes it given as DBA and in some cases it is present below the name insured 
    3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
    4. Mailing Address --- below the name insured , sometimes it is mentioned as POBOX and mailing address we can consider that one also 
    5. Policy Number
    6. Policy Period
    7. Issuing Company 
    8. Premium (include all coverage-level premiums and the total premium) ---- we have to extract all the premium mentioned in the decleration page 
    9. Paid In Full Discount ---- in premium it mentioned as discounted premium then we have to extract in this data point 
    10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
    11. Location
        - Extract location details **only from the "declaration of location" page or section**.
        - Do not extract location data from other sections, schedules, or tables.
        - need to extract loc label and its value along with address
        - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
        - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
        - if one or more location is present we have to extract like this --- 
            - If multiple locations are listed in the declaration of location, return all as an array 
            Example 2 -- 
                "Location": [
                    {{
                    "Loc No : 1 - 1 Embarcadero Ctr, San Francisco, CA 94111",
                    }},
                    {{
                    "Loc No : 2 - 799 Battery St, San Francisco, CA 94111",
                    }}
                    ],
        - If no location is found in the declaration of location, set this field to null. -- yes 
    12. Fein
    13. Coverage States
    14. Other States
    15. Employers Limits  --------------------- Employers Liability Insurance: this is the label to identify the employee limits in that we have to extract all the limits present in that section 
        - Extract: ALL employer limits listed
        - example : "Employers Limits": [
                        {{
                        "Bodily Injury by Accident  $100,000 each accident",
                        }},
                        {{
                        "Bodily Injury by Disease  $100,000 policy limit",
                        }},
                        {{
                        "Bodily Injury by Disease  $100,000 each employee",
                        }}
                    ], 
    - from 16 to 20 all data points must should comes in one label Rating Info and in that section premium and other lables also lisited we have to extract those also 
        example -- 

            "Rating Info": [
            {{
                "value": "8391 - AUTOMOBILE REPAIR SHOP & PARTS DEPARTMENT EMPLOYEES, DRIVERS - Estimated Payroll : 348,835 - Rate : 2.465- Premium : 20,352",
            }},
            {{
                "value": "8810 - CLERICAL OFFICE EMPLOYEES NOC - Estimated Payroll : 4,820 - Rate : 0.125 - Premium : 103",
            }}
                ], 

            example 2 --- 
                    "Rating Info": [
                    {{
                    "value": "State: CA - Loc No : 1 - 8078 - SANDWICH SHOPS - N.O.C. - not restaurants, bars or taverns - Estimated Payroll  $48,000 - Rate : - 1.79 - Net Rate : 1.67 - Manual Premium : $859",
                    "type": "string"
                    }},
                    {{
                    "value": "State: CA - Loc No : 2 - 8078 - SANDWICH SHOPS - N.O.C. - not restaurants, bars or taverns - Estimated Payroll  $24,000 - Rate : - 1.79 - Net Rate : 1.67 - Manual Premium : $430",
                    "type": "string"
                    }}
                    ],
    16. Class code
    17. Classification
    18. Estimated Payroll
    19. Rate
    20. No Of Employees
    21. Experience Mod --- it is mentioned as same name no other alternative 
    22. Changes in Credits --- it is mentioned as same name no other alternative 
    23. Members Excluded--- it is mentioned as same name no other alternative 
    24. Terrorism -------  sometimes it is present in the premiums or it has a sapreate page 
    25. Exclusions -- it is mentioned as same name no other alternative  
    26. Additional Interest ---- mortgagee or loss pay it is mentioned with those two names it can be present anywhere in the document 
    27. Additional Coverage ---- need to extract the remaining values and lables present in the document rather than the main datapoints  
    28. Forms And Endorsements
        - Extract: ONLY from "Forms And Endorsements" section
            - Scan to END of document
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title"
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only) --- yes 
    29. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page  ---- it mentioned as Endorsements and whatever you mentioned that only we have to extract 

    ### Output Rules
    - Return complete details for all datapoints with their exact labels with values.
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.

     {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_builder_risk(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Workers Compensation insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null`

    ### Datapoints to Extract ###
    1. Name Insured
    2. Other Named Insured ----- sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
    3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
    4. Mailing Address 
    5. Policy Number
    6. Policy Period
    7. Issuing Company 
    8. Premium
    9. Paid in Full Discount
    10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
    11. Location Address
        - no need to extract Property Location 
        - Extract location details **only from the "declaration of location" page or section**.
        - Do not extract location data from other sections, schedules, or tables.
        - need to extract loc label and its value along with address
        - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
        - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
        - if one or more location is present we have to extract like this ---
    12. Family Dwelling ----  if boolean present, then we need to extract the "true" value label  with the value along with its limit.
    13. Single structure policy ----  this data point that contains a boolean value, but we should not extract direct the boolean itself. Instead, we need to extract the true value label  with the value along with its limit.
    14. Commercial Structure ----it was shown as null because it was a false val no need to shown label also 
    15. New Construction ---- this data point is not in check box so should not extract boolean val , we need to extract limits which are present below  of the New Construction 
    16. Remodeling 
    17. Limits
    18. Deductible ---- need to extract check box value 
    19. Amount of loss or damage
    20. Terrorism -------  sometimes it is present in the premiums or it has a sapreate page
    21. Exclusions --- Donot extract this datapoint, pass it has null value
    22. Additional Coverage --- must extract value with their labels from Additional Coverage section only, no coverages should extract from other sections
    23. Additional Interests
    24. Forms And Endorsements — extraction rules
        -Extract ONLY from the "Forms And Endorsements" section.
        -Scan to END of document.
        -Merge multi-line entries into a single entry.
        -Format EXACTLY as:
            FormNumber | MM/YY Form Title
        -If a coverage code exists, format as:
            CoverageCode FormNumber | MM/YY Form Title
        -Form Title Extraction Rule (STRICT)
        -Extract a Form Title ONLY if it appears on the SAME LINE and IMMEDIATELY to the right of the Form Number and Date.
        -If no title appears beside the form number and date on the same line, DO NOT extract a title.
        -Do not extract titles from any other position (different line, different column, separated by layout, etc.).

        --Return Requirements
            -Return a single array of all extracted forms.
            -Deduplicate exact duplicates only.
            -If a form has no title, return it as:
            -FormNumber | MM/YY
    25. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page  ---- it mentioned as Endorsements and whatever you mentioned that only we have to extract
    ### Output Rules
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.
     {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_commercial_earthquake(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Commercial Earthquake insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null`

    ### Datapoints to Extract ###
    1. Name Insured
    2. Other Named Insured
        - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
        - No need extract "DBA" in value
    3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
    4. Mailing Address 
    5. Policy Number
    6. Policy Period
    7. Issuing Company 
    8. Premium
        - Need to extract all premiums under the Premium declaration section only not from other sections(need to extract with their labels)
    9. Paid in Full Discount
    10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
    11. Location
        - Extract location details **only from the "declaration of location" page or section**.
        - Do not extract location data from other sections, schedules, or tables.
        - need to extract loc label and its value along with address
        - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
        - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
        - if one or more location is present we have to extract like this ---
    12. Building Value
        - SCHEDULE OF COVERAGES , PROPERTY COVERAGES in those pages the building value is presnt.
        - If there are more than one location or  builidng values are present then along with lacation and bulding value has to bee extract along with lables like mention below
    13. Improvements And Betterments
    14. Business Personal Property Limit
    15. Business Income Limit
    16. Earthquake Limits
        - extract the limits under earthquake declaration page  
        - extract from  Limit of Insurance, any one "loss occurrence" 
    18. Earthquake Deductible
    19. Wind and Hail
    20. Deductible
    21. Co Insurance
        - most of the cases the data present , in where the bulding value is present , otherwsie it is present in the limits page 
        - If there are more than one location or  builidng values are present then along with lacation and bulding value has to bee extract along with lables like mention below
    22. Valuation
        - most of the cases the data present , in where the bulding value is present , otherwsie it is present in the limits page 
        - If more than one bulding values are present, then extract all of them as individual along with their labels
    22. Is Equipment Breakdown Listed
    23. Building Ordinance Or Law Listed Cov A
    24. Building Ordinance Demolition Cost Cov B
    25. Building Ordinance Inc Cost Of Construction Cov C
    26. Terrorism
    27. Exclusions
        - Pass this datapoint as null
    28. Additional Coverage
    29. Forms And Endorsements
        - Extract: ONLY from "Forms And Endorsements" section
            - Scan to END of document
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title"
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only) --- yes 
    30. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page  ---- it mentioned as Endorsements and whatever you mentioned that only we have to extract 

    ### Output Rules
    - Return complete details for all datapoints with their exact labels with values.
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.

     {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_commercial_fire(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Commercial Fire insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null`

    ### Datapoints to Extract ###
    1. Name Insured
    2. Other Named Insured ----- sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
    3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
    4. Mailing Address 
    5. Policy Number
    6. Policy Period
    7. Issuing Company 
    8. Premium
        - Need to extract all premiums under the Premium declaration section only not from other sections(need to extract with their labels)
    9. Paid in Full Discount
    10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
    11. Location
        - Extract location details **only from the "declaration of location" page or section**.
        - Do not extract location data from other sections, schedules, or tables.
        - need to extract loc label and its value along with address
        - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
        - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
        - if one or more location is present we have to extract like this ---
    12. Building Value
        - SCHEDULE OF COVERAGES , PROPERTY COVERAGES in those pages the building value is presnt.
        - If there are more than one location or  builidng values are present then along with lacation and bulding value has to bee extract along with lables like mention below
        - "Location#  : 1 - Building# :1 - Building : $ 200,000"
    13. Improvements And Betterments
    14. Business Personal Property Limit
    15. Business Income Limit
    16. Cause of Loss
        - most of the cases the data present , in where the bulding value is present , otherwsie it is present in the limits page 
        - If more than one bulding values are present, then extract all of them as individual along with their labels
        - Do not treat Premiums as cause of loss, the value will be present in builidng value section
    17. Wind and Hail
    18. Deductible
    19. Co Insurance
        - most of the cases the data present , in where the bulding value is present , otherwsie it is present in the limits page 
        - If there are more than one location or  builidng values are present then along with lacation and bulding value has to bee extract along with lables like mention below
        - "Location# : 1 - Building# : 1 - Coinsurance: 80%",
    20. Valuation
        - most of the cases the data present , in where the bulding value is present , otherwsie it is present in the limits page 
        - If more than one bulding values are present, then extract all of them as individual along with their labels
    21. Is Equipment Breakdown Listed
    22. Building Ordinance Or Law Listed Cov A
    23. Building Ordinance Demolition Cost Cov B
    24. Building Ordinance Inc Cost Of Construction Cov C
    25. Terrorism
    26. Exclusions
        - Pass this datapoint as null
    27. Additional Interest
    28. Additional Coverage
        - Only the remaining limits after extracting every required data point are considered as additional limits.
        - Premium values are not treated as additional limits.

    29. Forms And Endorsements
        - Extract: ONLY from "Forms And Endorsements" section
            - Scan to END of document
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title", if total year is present then format should be like : "FormNumber | MM/YYYY   Form Title"
            
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only) --- yes 
    30. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page  ---- it mentioned as Endorsements and whatever you mentioned that only we have to extract 

    ### Output Rules
    - Return complete details for all datapoints with their exact labels with values.
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.

     {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_commercial_flood(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Commercial Flood insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null`

    ### Datapoints to Extract ###
    1. Name Insured
    2. Other Named Insured (in some cases it is present below the name insured and do not extract from additional named insured section and DBA )
    3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
    4. Mailing Address 
    5. Policy Number
    6. Policy Period
    7. Issuing Company 
    8. Premium
        - Need to extract all premiums under the Premium declaration section(need to extract with their labels)
    9. Paid in Full Discount
    10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
    11. Location
        - Extract location details **only from the "declaration of location" page or section**.
        - No need to extract to Property Location like this : (Property Location: 1318 MAIN ST, SCOTT CITY MO 63780), it should be like : (Location: 1318 MAIN ST, SCOTT CITY MO 63780)
        - Do not extract location data from other sections, schedules, or tables.
        - need to extract loc label and its value along with address
        - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
        - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
        - if one or more location is present we have to extract like this ---
    12. Building Value
    13. Improvements And Betterments
    14. Business Personal Property Limit --- need to extract with contents label
    15. Business Income Limit
    16. Flood Limits
        - Extract limits and coverages that present under "flood declaration" section only
        - Donot include "Limit of Liability" for every datapoint like "Building Property A. Limit of Liability $750,000",
    17. Wind and Hail
    18. Deductible
    19. Co Insurance
    20. Valuation ----need to extract replacement cost with label and limit under valuation datapoint
    21. Is Equipment Breakdown Listed
    22. Building Ordinance Or Law Listed Cov A
    23. Building Ordinance Demolition Cost Cov B
    24. Building Ordinance Inc Cost Of Construction Cov C
    25. Terrorism
    26. Exclusions
        - Pass this datapoint as null
    27. Additional Interest
    28. Additional Coverage 
        - Extract only from Additional Coverage section
    29. Forms And Endorsements
        - Extract: ONLY from "Forms And Endorsements" section
            - Scan to END of document
            - Should return unique from number and date and return only which have form number and date
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title"
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only) --- yes 
    30. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page  ---- it mentioned as Endorsements and whatever you mentioned that only we have to extract 

    ### Output Rules
    - Return complete details for all datapoints with their exact labels with values.
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.

     {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_crime(large_text=None):
    return f"""
    You are an expert insurance data extractor.
    The following text is extracted from a Crime insurance PDF using a mix of
    digital text, OCR text, and tables.  
    Some forms or endorsements may be spread across multiple pages or split into separate
    lines. Your task is to search the **ENTIRE** document and extract every required
    datapoint listed below.  

    ### Rules for Extraction
    - **Never stop** at the first occurrence of any section.  
      Continue scanning until the **very end of the document** to ensure nothing is missed.
    - Merge multi-line form numbers/titles into a **single entry** if they are split.
    - Deduplicate only when the text is **identical**.
    - Preserve all numbers, dates, symbols, and formatting exactly as shown.
    - If no value exists for a field, set it to `null`

    ### Datapoints to Extract ###
    - The following datapoints should extract from only "Crime" section, not from other sections like cyber, property etc.
    1. Name Insured (primary insured only, do not include district orany other named insureds here like DBA etc) 
    2. Other Named Insured  (extract all other names except primary name, it may have like DBA, do not extract from additional named insureds section)
    3. Mailing Address 
    4. Policy Number
    5. Policy Period
    6. Issuing Company 
    7. Premium
        - Extract premium of crime declaration section
        - Extraction should be like example metioned below
        - Example : "Premium": [
                {{
                "value": "Crime - EMC -  Expiring Annual Premium : $723.00 - Renewal Annual Premiums: $638.00",
                "type": "string"
                }}
            ]
    8. Paid in Full Discount
    9. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
    10. Location
        - Extract location details **only from the "declaration of location" page or section**.
        - Do not extract location data from other sections, schedules, or tables.
        - need to extract loc label and its value along with address
        - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
        - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
        - if one or more location is present we have to extract like this ---
    11. Limts of Insurance 
        only extract from crime section not from other sections
        Extraction should be like example metioned below
        Example : Limts of Insurance": [
                    {{
                    "value": "Employee Theft ---- Per Loss Coverage  : PER SCHED",
                    "type": "string"
                    }},
                    {{
                    "value": "Employee Theft ---- Per Employee Coverage  : NOT COVERED ",
                    "type": "string"
                    }}]
    12. Retention
        Extraction should be like example metioned below
        Example :"Retention": [
                {{
                "value": "1. Employee Theft - Deductible Amount Per Occurrence : $ 1,000",
                "type": "string"
                }}
            ]
    13. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured)
    14. Additional Interest
    15. Additional Coverage 
        - Extract all coverages values which only under "crime" section not from other sections like cyber, property etc.
        - The extraction should be formatted like under the example metioned below
        - Example : "Additional Coverage": [
            {{
            "value": "Item Number : 1 - Names Of Covered Employees : BOB HEMBROCK - Limit Of Insurance On Each Employee : $100,000 - Deductible Amount On Each Employee : $1,000",
            "type": "string"
            }},
            {{
            "value": "Item Number : 2 - Names Of Covered Employees : KAREN JACKSON - Limit Of Insurance On Each Employee : $100,000 - Deductible Amount On Each Employee : $1,000",
            "type": "string"
            }}]
    16. Terrorism
    17. Exclusions 
        - keep this datapoint as null
    18. Forms And Endorsements
        - Extract: ONLY from "Forms And Endorsements" section not from other sections like POLICYWRITING INDEX  or  COMPUTER PRODUCED FORMS  etc.
            - Scan to END of document
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title"
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only) --- yes 
    19. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page  ---- it mentioned as Endorsements and whatever you mentioned that only we have to extract 

    ### Output Rules
    - Return complete details for all datapoints with their exact labels with values.
    - Return **only** the structured JSON object with the keys above in the exact order.
    - Dates → MM/DD/YYYY
    - Currency → keep "$" and commas as shown.
    - Missing values → null.

     {f'Text: {large_text}' if large_text else ''}
    """

def prompt_template_directors_and_officers(large_text=None):
    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a Directors and Officers insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Rules for Extraction
        - **Never stop** at the first occurrence of any section.  
        Continue scanning until the **very end of the document** to ensure nothing is missed.
        - Merge multi-line form numbers/titles into a **single entry** if they are split.
        - Deduplicate only when the text is **identical**.
        - Preserve all numbers, dates, symbols, and formatting exactly as shown.
        - If no value exists for a field, set it to `null`

        ### Datapoints to Extract ###
        1. Name Insured (primary insured only, do not include any other named insureds here like DBA etc) 
        2. Other Named Insured
            - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
            - No need extract "DBA" in value
        3. Additional Insured (it will be with same name or other named insured or DBA and should be extracted from additional named insureds section only)
        4. Mailing Address 
        5. Policy Number
        6. Policy Period
        7. Issuing Company 
        8. Premium
        9. Paid in Full Discount
        10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names) -- yes 
        11. Location
            - Extract location details **only from the "declaration of location" page or section**.
            - Do not extract location data from other sections, schedules, or tables.
            - need to extract loc label and its value along with address
            - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
            - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
            - Do not extract property location
        12. Business Classification
        13. Limits of Liability
        14. Deductible or Retention
        15. Retro Date
        16. Prior and Pending Date
        17. Continuity Date
        18. Underlying Insurance
        19. Terrorism
        20. Exclusions - do not extract, pass null to this datapoint
        21. Additional Coverage
        22. Forms And Endorsements
            - Extract: ONLY from "Forms And Endorsements" section
            - Scan to END of document
            - Merge multi-line entries into single entry
            - Format EXACTLY: "FormNumber | MM/YY   Form Title" 
            - If coverage code exists: "BOP BP0159 | 08/08  WATER EXCLUSION ENDORSEMENT"
            - Return: Single array of ALL forms (deduplicate exact duplicates only) --- yes 
        23. Endorsements
            - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
            - Extract only from particular "endorsement" declaration page

        ### Output Rules
        - Return complete details for all datapoints with their exact labels with values.
        - Return **only** the structured JSON object with the keys above in the exact order.
        - Dates → MM/DD/YYYY
        - Currency → keep "$" and commas as shown.
        - Missing values → null.

        {f'Text: {large_text}' if large_text else ''}
        """

def prompt_template_dwelling_fire(large_text=None):
    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a Dwelling Fire insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Rules for Extraction
        - **Never stop** at the first occurrence of any section.  
        Continue scanning until the **very end of the document** to ensure nothing is missed.
        - Merge multi-line form numbers/titles into a **single entry** if they are split.
        - Deduplicate only when the text is **identical**.
        - Preserve all numbers, dates, symbols, and formatting exactly as shown.
        - If no value exists for a field, set it to `null`

        ### Datapoints to Extract ###
        1. Name Insured (primary insured only, do not include any other named insureds here like DBA etc) 
        2. Other Named Insured
            - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
            - No need extract "DBA" in value
        3. Additional Insured (it will be with same name or other named insured or DBA and should be extracted from additional named insureds section only)
        4. Mailing Address
        5. Physical Address 
        6. Policy Number
        7. Policy Period
        8. Issuing Company
        9. Premium
            - Need to values with labels
        10. Paid in Full Discount
        11. Miscellaneous Premium
        12. Dwelling Limit
            - Need extract full value with their labels like mentioned below
            - "$ 566,277 - ANNUAL PREMIUM : 883.00"
        13. Other Structures
            - Include complete details
        14. Fair Rental Value
        15. Loss of use
            - Need extract full value with their labels
        16. Personal Property
            - Need extract full value with their labels
        17. Personal Liability
            - Need extract full value with their labels
            - Annual premium should extracted if present
        18. Additional Living Expense
        19. Medical Payments
        20. Deductibles
        21. Windhail
        22. Water Backup
        23. Property Info
        24. Terrorism
        25. Exclusions
        26. Additional Interest
        27. Additional Coverage
        28. Forms And Endorsements — extraction rules
            -Extract ONLY from the "Forms And Endorsements" section.
            -Scan to END of document.
            -Merge multi-line entries into a single entry.
            -Format EXACTLY as:
                FormNumber | MM/YY Form Title
            -If a coverage code exists, format as:
                CoverageCode FormNumber | MM/YY Form Title
            -Form Title Extraction Rule (STRICT)
            -Extract a Form Title ONLY if it appears on the SAME LINE and IMMEDIATELY to the right of the Form Number and Date.
            -If no title appears beside the form number and date on the same line, DO NOT extract a title.
            -Do not extract titles from any other position (different line, different column, separated by layout, etc.).

            --Return Requirements
                -Return a single array of all extracted forms.
                -Deduplicate exact duplicates only.
                -If a form has no title, return it as:
                -FormNumber | MM/YY
        29. Endorsements
        - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
        - Extract only from particular endorsement declaration page
        ### Output Rules
        - Return **only** the structured JSON object with the keys above in the exact order.
        - Dates → MM/DD/YYYY
        - Currency → keep "$" and commas as shown.
        - Missing values → null.
        {f'Text: {large_text}' if large_text else ''}
        """
    
def prompt_template_epli(large_text=None):
    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a EPLI insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Rules for Extraction
        - **Never stop** at the first occurrence of any section.  
        Continue scanning until the **very end of the document** to ensure nothing is missed.
        - Merge multi-line form numbers/titles into a **single entry** if they are split.
        - Deduplicate only when the text is **identical**.
        - Preserve all numbers, dates, symbols, and formatting exactly as shown.
        - If no value exists for a field, set it to `null`

        ### Datapoints to Extract ###
        1. Name Insured (primary insured only, do not include any other named insureds here like DBA etc) 
        2. Other Named Insured
            - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
            - No need extract "DBA" in value
        3. Additional Insured (it will be with same name or other named insured or DBA and should be extracted from additional named insureds section only)
        4. Mailing Address
        5. Policy Number
        6. Policy Period
        7. Issuing Company  
        8. Premium	
        9. Paid In Full Discount	
        10. Miscellaneous Premium	
        11. Location	
        12. Limits of Liability	
            - Extract limits which are present declaration section only, donot include other coverges limits
        13. Deductible or Retention	
        14. Retro Date	
        15. Prior and Pending Date	
        16. Continuity Date	
        17. Underlying Insurance	
        18. Terrorism -------  sometimes it is present in the premiums or it has a sapreate page
        19. Exclusions --- Donot extract this datapoint, pass it has null value
        20. Additional Coverage
            - Extract coverages with values along with their labels
        21. Additional Interests
        22. Forms And Endorsements — extraction rules
            -Extract ONLY from the "Forms And Endorsements" section.
            -Scan to END of document.
            -Merge multi-line entries into a single entry.
            -Format EXACTLY as:
                FormNumber | MM/YY Form Title
            -If a coverage code exists, format as:
                CoverageCode FormNumber | MM/YY Form Title
            -Form Title Extraction Rule (STRICT)
            -Extract a Form Title ONLY if it appears on the SAME LINE and IMMEDIATELY to the right of the Form Number and Date.
            -If no title appears beside the form number and date on the same line, DO NOT extract a title.
            -Do not extract titles from any other position (different line, different column, separated by layout, etc.).

            --Return Requirements
                -Return a single array of all extracted forms.
                -Deduplicate exact duplicates only.
                -If a form has no title, return it as:
                -FormNumber | MM/YY
        23. Endorsements
            - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
            - Extract only from particular endorsement declaration page
            
        ### Output Rules
        - Return **only** the structured JSON object with the keys above in the exact order.
        - Dates → MM/DD/YYYY
        - Currency → keep "$" and commas as shown.
        - Missing values → null.
        {f'Text: {large_text}' if large_text else ''}
        """

def prompt_template_errors_omissions(large_text=None):
    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a Errors and Omissions insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Rules for Extraction
        - **Never stop** at the first occurrence of any section.  
        Continue scanning until the **very end of the document** to ensure nothing is missed.
        - Merge multi-line form numbers/titles into a **single entry** if they are split.
        - Deduplicate only when the text is **identical**.
        - Preserve all numbers, dates, symbols, and formatting exactly as shown.
        - If no value exists for a field, set it to `null`

        ### Datapoints to Extract ###
        1. Name Insured (primary insured only, do not include any other named insureds here like DBA etc) 
        2. Other Named Insured
            - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
            - No need extract "DBA" in value
        3. Additional Insured (it will be with same name or other named insured or DBA and should be extracted from additional named insureds section only)
        4. Mailing Address
        5. Policy Number
        6. Policy Period
        7. Issuing Company  
        8. Premium
            - Need to extract with values with their labels for Premium datapoint
        9. Paid In Full Discount	
        10. Miscellaneous Premium	
        11. Location	
        12. Limits of Liability	
        13. Deductible or Retention	
            - Extract value with label as they mentioned in document
        14. Retro Date	
            - Extract value with label as they mentioned in document
        15. Prior and Pending Date	
        16. Continuity Date	
        17. Underlying Insurance	
        18. Terrorism -------  sometimes it is present in the premiums or it has a sapreate page
        19. Exclusions --- Donot extract this datapoint, pass it has null value
        20. Additional Coverage --- must extract value with their labels from Additional Coverage section only, no coverages should extract from other sections
        21. Forms And Endorsements — extraction rules
            -Extract ONLY from the "Forms And Endorsements" section.
            -Scan to END of document.
            -Merge multi-line entries into a single entry.
            -Format EXACTLY as:
                FormNumber | MM/YY Form Title
            -If a coverage code exists, format as:
                CoverageCode FormNumber | MM/YY Form Title
            -Form Title Extraction Rule (STRICT)
            -Extract a Form Title ONLY if it appears on the SAME LINE and IMMEDIATELY to the right of the Form Number and Date.
            -If no title appears beside the form number and date on the same line, DO NOT extract a title.
            -Do not extract titles from any other position (different line, different column, separated by layout, etc.).

            --Return Requirements
                -Return a single array of all extracted forms.
                -Deduplicate exact duplicates only.
                -If a form has no title, return it as:
                -FormNumber | MM/YY
        22. Endorsements
            - Include: Data under Description of changes should be extracted(changed, added, deleted, estimated total premium, paid in full discount))
            - Extract only from particular endorsement declaration page
            
        ### Output Rules
        - Return **only** the structured JSON object with the keys above in the exact order.
        - Dates → MM/DD/YYYY
        - Currency → keep "$" and commas as shown.
        - Missing values → null.
        {f'Text: {large_text}' if large_text else ''}
        """

def prompt_umbrella(large_text=None):
    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a Umbrella or Excess Liability insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Rules for Extraction
        - **Never stop** at the first occurrence of any section.  
        - Continue scanning until the **very end of the document** to ensure nothing is missed.
        - Merge multi-line form numbers/titles into a **single entry** if they are split.
        - Deduplicate only when the text is **identical**.
        - Preserve all numbers, dates, symbols, and formatting exactly as shown.
        - If no value exists for a field, set it to `null`

        ### Datapoints to Extract ###
        1. Name Insured
        2. Other Named Insured
            - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
            - No need extract "DBA" in value
        3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
        4. Mailing Address 
        5. Policy Number
        6. Policy Period
        7. Issuing Company 
        8. Premium
            - Need to extract all premiums under the Premium declaration section
            - Extract with combination of labels and values
        9. Paid in Full Discount
        10. Miscellaneous Premium (the miscellaneouspremium is mentioned as miscellaneouspremium only there is no other alternatives names)
        11. Umbrella Limits
            - Extract the numerical value for the 'Umbrella limit' (or 'Excess Liability limit') from the insurance document section that specifies the maximum aggregate coverage amount.
        12. Underlying Policies
            -Extract following datapoints
            1.Underlying Carrier
            2.Underlying Coverage
            3.Underlying Policy
            4.Underlying Term
            5.Underlying Limits
        13. Retention
        14. Terrorism
        15. Exclusions
            - Pass this datapoint as null
        21. Forms And Endorsements — extraction rules
            -Extract ONLY from the "Forms And Endorsements" section.
            -Scan to END of document.
            -Merge multi-line entries into a single entry.
            -Format EXACTLY as:
                FormNumber | MM/YY Form Title
            -If a coverage code exists, format as:
                CoverageCode FormNumber | MM/YY Form Title
            -Form Title Extraction Rule (STRICT)
            -Extract a Form Title ONLY if it appears on the SAME LINE and IMMEDIATELY to the right of the Form Number and Date.
            -If no title appears beside the form number and date on the same line, DO NOT extract a title.
            -Do not extract titles from any other position (different line, different column, separated by layout, etc.).

            --Return Requirements
                -Return a single array of all extracted forms.
                -Deduplicate exact duplicates only.
                -If a form has no title, return it as:
                -FormNumber | MM/YY
        22. Endorsements
            - Extract only from particular endorsement declaration section
            - Donot extract from other than this section, do not include when value have endoresement which is not under this section
            
        ### Output Rules
        - Return **only** the structured JSON object with the keys above in the exact order.
        - Dates → MM/DD/YYYY
        - Currency → keep "$" and commas as shown.
        - Missing values → null.
        {f'Text: {large_text}' if large_text else ''}
        """

def prompt_master_bop(large_text=None):
    return f"""
        You are an expert insurance data extractor.
        The following text is extracted from a Master BOP insurance PDF using a mix of
        digital text, OCR text, and tables.  
        Some forms or endorsements may be spread across multiple pages or split into separate
        lines. Your task is to search the **ENTIRE** document and extract every required
        datapoint listed below.  

        ### Rules for Extraction
        - **Never stop** at the first occurrence of any section.  
        - Continue scanning until the **very end of the document** to ensure nothing is missed.
        - Merge multi-line form numbers/titles into a **single entry** if they are split.
        - Deduplicate only when the text is **identical**.
        - Preserve all numbers, dates, symbols, and formatting exactly as shown.
        - If no value exists for a field, set it to `null`

        ### Datapoints to Extract ###
        1. Name Insured
            -(primary insured only, do not include any other named insureds here like DBA etc) 
        2. Other Named Insured
            - sometimes it given as DBA and in some cases it is present below the name insured and do not extract from additional named insured section 
            - No need extract "DBA" in value
        3. Additional Insured (it will be with same name or other named insured or DBA ) --- for this data point ,  it has a sapreate page mentioned as Name insured schedule page or Additional insured 
        4. Mailing Address
           - it will be starts with number , PO BOX ,text below named or other named insured
        5. Policy Number
        6. Policy Period
        7. Issuing Company
            - Extract the company issuing or underwritting
        8. Premium
            - Need to extract all premiums under the Premium declaration section
            - Extract with combination of labels and values
        9. Paid in Full Discount
            - Extract Paid in Full discount if present.
        10. Miscellaneous Premium
            - Extract only if field explicitly labeled 'miscellaneous premium'
        11. Location
            - no need to extract Property Location 
            - Extract location details **only from the "declaration of location" page or section**.
            - Do not extract location data from other sections, schedules, or tables.
            - need to extract loc label and its value along with address
            - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
            - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60
        12. The datapoints mentioned from 13 to 22 should follows below description and each datapoint should treated as individual primary key
            - Extract the value **only from the "Business Liability declaration page or section"**. Do not extract from other sections, schedules, or tables execpt.
            - For each, include both the value (e.g., "$5,000") and any descriptive text that appears after the value (e.g., "Per Occurrence", "Any One Premise", etc.).
            - Output format for each: "<value> <descriptive text after value>" , not like "Medical expenses": "$10,000 Medical Expenses Limit",
            - Example: 
                - "Medical expenses": "$5,000 Per Occurrence"
                - "Personal And Advt Injury": "$1,000,000 Per Occurrence"
                - "Damage to rented premises": "$50,000 Any One Premise"
        13. General Aggregate (Extract  only if field  General Aggregate)
        14. Products or Completed Operations Aggregate (Extract  only if field Products or Completed Operations Aggregate)
        15. Personal And Advt Injury (Extract  only if field Personal And Advt Injury)
        16. Medical expenses (Extract if field Medical expenses)
        17. Damage to rented premises (Extract  if field Damage to rented premises)
        18. Each Occurrence (Extract  if field Each Occurrence)
        19. Deductible (extract if field as  deductible with labels if label not present then limit is enough  from General Liability)
        20. Hired Or Non Owned Auto ("extract if field as hired and non owned auto with labels from General Liability)
        21. "Schedule of Hazards Rating Info". Return as an array of dictionaries, each with:
                -Class Code
                -Classification
                -Premium Basis
                -Exposure
                -Rate
                -Premium
        22. Additional interest
        - From 23 to 36 extract only if field is present
        23. Employee Benefits Liability
        24. Directors and Officers
        25. Cyber
        26. Professional Liability
        27. EPLI on Policy
        28. Errors and Omissions on Policy
        29. Garage Liability
        30. Crime
        31. Pollution Liability
        32. Liquor Liability
        33. Fiduciary Liability
        34. Commercial Flood
        35. Commercial Earthquake
        36. Terrorism
            - Extract terrorism coverage information with labels
        37. The datapoints mentioned from 38 to 51 should follows below description and each datapoint should treated as individual primary key
        - (Need to extract the datapoints in individual dictionary but not under the general liability dictionary, And this data should be extracted which is present under the property declaration page only)
        38. Building Value
        39. Business Personal Property Limit - (need to extract prem.no,bldg.no labels and its values along with limit data)
        40. Business Income Limit - (must and should extract complete value of it and if value consists "INCLUDED" then "included" comes in last index of value)
        41. Improvements and Betterments
        42. Wind And Hail
        43. Property Deductible - (need to extract prem.no,bldg.no labels and its values along with limit data and all deductible under this section only)
        44. Co Insurance
        45. Valuation
        46. Is Equipment Breakdown Listed
        47. Building Ordinance Or Law Listed Cov A
        48. Building Ordinance Demolition Cost Cov B
        49. Building Ordinance Inc Cost Of Construction Cov C
        50. Additional Interests (extract only from property declaration page only)
        51. Property Terrorism (data which is present in buidling prperty values under property declarations)
        52 From 53 to 60 extract datapoints from "Commercial Auto" section only, if datapoints mentioned below are not present in this section then pass them null
        53. Symbol (extract only which was selected by crossmark and extract all of them as individual)
                - Example:"symbol": [
                        "Combined Liability": "7, 8, 9, 19",
                        "Uninsured Motorist": "6",
                        "Underinsured Motorist": "6",
                        "Personal Injury Protection": "7",
                        "Comprehensive": "7",
                        "Collision": "7",
                        "Road Trouble Service": "7",
                        "Additional Expense": "7"]
        54. Limits (return only coverage limits with values, when there is no value dont extract the label)
                - Extract only from declaration page only, not from hired and non owned auto pages
                - Example: [LIABILITY- BI EACH ACCIDENT : $1000000
                        MEDICAL PAYMENTS -EACH PERSON : $5000]
        55. Vehicles Info (extract following datapoints)
                1. VIN
                2. Year
                3. Make
                4. Model
                5. Cost New
                6. Premium
                - Must capture all vehicles listed with full details
                - Return costnew values also if and if it is present under this section only
        56. Scheduled Drivers → [{{NameLast, FirstName, DOB or Age, State, License Number, Premium}}]  
        57. Hired Or Non-Owned Auto Limits → (extract all the data  if field as Hired Or Non owned Auto Limits with labels  from auto lob)
        58. Drive Other Car Coverage   (extract all the data  if field as Drive Other Car Coverage Auto Limits with labels  from auto lob )
        59. Lein Holder or Loss Payee (extract all the data  if field as Lein Holder or Loss Payee with labels  from auto lob)
        60. Auto Terrorism (extract all the data  if field as Auto Terrorism with labels  from auto lob )
        61. From 62 to 75 extract them from only "Workers Compensation" declaration section
        62. Locations
            - Extract location details **only from the "declaration of location" page or section**.
            - Do not extract location data from other sections, schedules, or tables.
            - need to extract loc label and its value along with address
            - Example:"Loc 1  1731 W Business U.S. 60, ---- if any one those are lisited in the document we have to extract in location                                                                                                   
            - sometimes BLDG label is also present in some document , in that case the output should be like -- "Loc 1 - BLDG 1 - 1731 W Business U.S. 60  
            - if one or more location is present we have to extract like this --- 
                - If multiple locations are listed in the declaration of location, return all as an array 
                Example 2 -- 
                    "Location": [
                        {{
                        "Loc No : 1 - 1 Embarcadero Ctr, San Francisco, CA 94111",
                        }},
                        {{
                        "Loc No : 2 - 799 Battery St, San Francisco, CA 94111",
                        }}
                        ],
            - If no location is found in the declaration of location, set this field to null. -- yes 
        63. Fein
        64. Coverage States
        65. Other States
        66. Employers Limits  --------------------- Employers Liability Insurance: this is the label to identify the employee limits in that we have to extract all the limits present in that section 
            - Extract: ALL employer limits listed
            - example : "Employers Limits": [
                            {{
                            "Bodily Injury by Accident  $100,000 each accident",
                            }},
                            {{
                            "Bodily Injury by Disease  $100,000 policy limit",
                            }},
                            {{
                            "Bodily Injury by Disease  $100,000 each employee",
                            }}
                        ], 
        - from 67 to 71 all data points must should comes in one label Rating Info and in that section premium and other lables also lisited we have to extract those also 
            -- Must and should extract in format mentioned below example
            example -- 
                "Rating Info": [
                {{
                    "value": "8391 - AUTOMOBILE REPAIR SHOP & PARTS DEPARTMENT EMPLOYEES, DRIVERS - Estimated Payroll : 348,835 - Rate : 2.465- Premium : 20,352",
                }},
                {{
                    "value": "8810 - CLERICAL OFFICE EMPLOYEES NOC - Estimated Payroll : 4,820 - Rate : 0.125 - Premium : 103",
                }}
                    ], 

                example 2 --- 
                        "Rating Info": [
                        {{
                        "value": "State: CA - Loc No : 1 - 8078 - SANDWICH SHOPS - N.O.C. - not restaurants, bars or taverns - Estimated Payroll  $48,000 - Rate : - 1.79 - Net Rate : 1.67 - Manual Premium : $859",
                        "type": "string"
                        }},
                        {{
                        "value": "State: CA - Loc No : 2 - 8078 - SANDWICH SHOPS - N.O.C. - not restaurants, bars or taverns - Estimated Payroll  $24,000 - Rate : - 1.79 - Net Rate : 1.67 - Manual Premium : $430",
                        "type": "string"
                        }}
                        ],
        67. Class code
        68. Classification
        69. Estimated Payroll
        70. Rate
        71. No Of Employees
        72. Experience Mod --- it is mentioned as same name no other alternative 
        73. Changes in Credits --- it is mentioned as same name no other alternative 
        74. Members Excluded--- it is mentioned as same name no other alternative 
        75. WC Terrorism -------  sometimes it is present in the premiums or it has a sapreate page 
        76. From 77 to 84, extract datapoints from "Inland Marine" section only
        77. Inland Marine Details
        78. Equipment Shedule
        79. Deductibles
        80. Loss Payee (extract all the data  if field as Loss Payee/mortgagee from inland marine lob)
        81. Rental equipment from others
        82. Rental equipment to others
        83. Installation floater
        84. Inland Marine Terrorism
        85. From 86 to 87, extract datapoints from "Commercial Umbrella" section only
        86. Umbrella Limits
            - Extract the numerical value for the 'Umbrella limit' (or 'Excess Liability limit') from the insurance document section that specifies the maximum aggregate coverage amount.
        87. Underlying Policies
            -Extract following datapoints
                1.Underlying Carrier
                2.Underlying Coverage
                3.Underlying Policy
                4.Underlying Term
                5.Underlying Limits
        88. Policy Exclusions
            -extract all the data  if field as Policy Exclusions
        89. Additional Coverage
            -extract all the limits with labels which are not included in main datapoints anther named as coverages/limit of insurance /sublimits/additional coverages
        90. Forms And Endorsements
            -Extract ONLY from the "Forms And Endorsements" section.
            -Scan to END of document.
            -Merge multi-line entries into a single entry.
            -Format EXACTLY as:
                FormNumber | MM/YY Form Title
            -If a coverage code exists, format as:
                CoverageCode FormNumber | MM/YY Form Title
            -Form Title Extraction Rule (STRICT)
            -Extract a Form Title ONLY if it appears on the SAME LINE and IMMEDIATELY to the right of the Form Number and Date.
            -If no title appears beside the form number and date on the same line, DO NOT extract a title.
            -Do not extract titles from any other position (different line, different column, separated by layout, etc.).

            --Return Requirements
                -Return a single array of all extracted forms.
                -Deduplicate exact duplicates only.
                -If a form has no title, return it as:
                -FormNumber | MM/YY
        91. Endorsements
            - Extract only from particular endorsement declaration
            - Extract Description of Changes (changed, added, deleted, premium changes) from endorsement declaration page.
        
        ### Output Rules
        - Return **only** the structured JSON object with the keys above in the exact order.
        - Dates → MM/DD/YYYY
        - Currency → keep "$" and commas as shown.
        - Missing values → null.
        {f'Text: {large_text}' if large_text else ''}
        """
