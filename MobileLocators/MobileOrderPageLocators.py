from datetime import date
today = date.today().strftime("%d")
import Static.Constants as const
address= "xpath@@input[@id='addresstext']"
address_select = f"xpath@@//div[@class='tt-menu']/div/div[contains(text(),'{const.order_address}')]"
delivery_btn ="xpath@@//*[@class='btn-store-override btn-store-delivery']"
pickup_btn = "xpath@@//div[contains(@class,'col-6 mt-0 mt-sm-1')]//button[contains(@class,'btn btn-primary btn-block btn-store btn-store-pickup')][contains(text(),'Pickup')]"
confirm_address_continue_btn="xpath@@//button[@id='address-confirmation-modal-continue-btn']"
date_picker_selector="xpath@@//div[@id='ui-datepicker-div']"
time_selector = "xpath@@//div[@id='delivery-time-container']"
time_selector_dropdown = "xpath@@//select[@class='delivery-timepicker-dropdown custom-select']"
rows = "xpath@@//div[@id='ui-datepicker-div']/table/tbody/tr"
columns = "xpath@@//div[@id='ui-datepicker-div']/table/tbody/tr[2]/td"
before_12_date =f"xpath@@//td[not(contains(@class,'ui-datepicker-other-month'))]/span[text()='{today}']"
after_12_date=f"xpath@@//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{today}']"