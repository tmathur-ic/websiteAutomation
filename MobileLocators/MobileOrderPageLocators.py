address= "xpath@@input[@id='addresstext']"
address_order = "xpath@@//input[@id='addresstext']"
address_select = f"xpath@@//div[@class='tt-menu']/div/div[contains(text(),'{address}')]"
delivery_btn ="xpath@@//*[@class='btn-store-override btn-store-delivery']"
pickup_btn = "xpath@@//div[contains(@class,'col-6 mt-0 mt-sm-1')]//button[contains(@class,'btn btn-primary btn-block btn-store btn-store-pickup')][contains(text(),'Pickup')]"
confirm_address_continue_btn="xpath@@//button[@id='address-confirmation-modal-continue-btn']"
date_picker_selector="xpath@@//div[@id='ui-datepicker-div']"
widget_form = "xpath@@//div[@id='ui-datepicker-div']/table/tbody"