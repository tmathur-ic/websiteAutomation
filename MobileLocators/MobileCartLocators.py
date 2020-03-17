delete_btn = "xpath@@//button[@class='btn btn-clear p-0 pull-left']"
edit_icn = "xpath@@//i[@class='ml-2 fa fa-pencil']"
apply_btn = "xpath@@//button/span[contains(text(),'Apply')]"
input_apply_coupon= "xpath@@//button/span[contains(text(),'Apply')]/ancestor::div/input"
checkout_btn = "xpath@@//button[contains(text(),'Checkout')]"
edit_product = "xpath@@//div[@class='card clickable']"
address_input= "xpath@@//div[@class='input-group d-flex']"
import Static.Constants as const
from datetime import date
today = date.today().strftime("%d")
address_select = f"xpath@@//div[@class='tt-menu']/div/div[contains(text(),'{const.order_address}')]"


date_picker_selector="xpath@@//div[@id='ui-datepicker-div']"
time_selector = "xpath@@//div[@id='delivery-time-container']"
time_selector_dropdown = "xpath@@//select[@class='delivery-timepicker-dropdown custom-select']"
before_12_date =f"xpath@@//td[not(contains(@class,'ui-datepicker-other-month'))]/span[text()='{today}']"
after_12_date=f"xpath@@//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{today}']"