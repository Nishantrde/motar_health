from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://www.acko.com/gi/auto-storefront/fresh-car/vehicle-prequote?proposal_ekey=1Z9tkdmxfrwT85o_jufmNA&current_node=previous_claim_confirmation_node&registration_number=JH10BK5078")

wait = WebDriverWait(driver, 1)

# Example: Extracting Car Model and Registration Number using their unique class names
car_model_elem = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-kvZOFW.sc-jwKygS.gYYlqM"))
)
car_model = car_model_elem.text

reg_number_elem = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-kvZOFW.sc-btzYZH.iCrpAX"))
)
registration_number = reg_number_elem.text

# Extract the detail values (Variant, Registration year, NCB, Policy expiry date)
# All these values are in <p> elements with the class "sc-kvZOFW sc-jtRfpW dRCNdl"
detail_elements = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "dRCNdl"))
)

pincode_elements = wait.until(
    EC.presence_of_all_elements_located((By.ID, "pincode"))
)

# Assuming the order based on the HTML snippet:
# detail_elements[0] -> Variant, [1] -> Registration year, [2] -> NCB, [3] -> Policy expiry date
variant = detail_elements[0].text
registration_year = detail_elements[1].text
ncb = detail_elements[2].text
policy_expiry_date = detail_elements[3].text
pincode = pincode_elements[0].get_attribute("value")

print("Car Model:", car_model)
print("Registration Number:", registration_number)
print("Variant:", variant)
print("Registration Year:", registration_year)
print("No Claim Bonus (NCB):", ncb)
print("Policy Expiry Date:", policy_expiry_date)
print("pincode", pincode)

driver.quit()
