from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FORM = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FORM = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FORM = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_SELECTOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER_FORM = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[(@class ='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее')]")
    DELIVERY_SCOOTER_DAY_FORM = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FORM = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    BLACK_PEARLS_CHECKBOX = (By.XPATH, "//input[@id='black']")
    GRAY_HOPELESSNESS = (By.XPATH, "//input[@id='grey']")
    COURIER_COMMENTS_FORM = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                               "div.Order_Buttons__1xGrp > "
                                               "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")
    CONFIRMATION_ORDER_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                             "div.Order_NextButton__1_rCA > "
                                             "button.Button_Button__ra12g.Button_Middle__1CSJM")
    CREATED_ORDER_WINDOW = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    GET_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    CHERKIZOVSKAYA_METRO_STATION = (By.XPATH, "//div[text()='Черкизовская']")
    DATE_29_OCTOBER = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--029']")
    RENT_DAYS_3 = (By.XPATH, "//div[text()='трое суток']")
    SOKOLNIKI_METRO_STATION = (By.XPATH, "//div[text()='Сокольники']")
    DATE_30_OCTOBER = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--030']")
    RENT_DAYS_4 = (By.XPATH, "//div[text()='четверо суток']")