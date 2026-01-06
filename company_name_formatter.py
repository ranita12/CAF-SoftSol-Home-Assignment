def normalize_company_name(company_name: str) -> str:
    """
    Normalize company name to:
    'CAF SoftSol India Pvt Ltd.'
    """

    if not company_name or not company_name.strip():
        return "Company Name Not Available"

    name = company_name.lower()

    base_name = "CAF SoftSol"

    # Check if India is present
    india_part = " India" if "india" in name else ""

    # Standard Pvt Ltd format
    pvt_ltd_part = " Pvt Ltd."

    return f"{base_name}{india_part}{pvt_ltd_part}"
