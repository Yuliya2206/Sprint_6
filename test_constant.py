from locators.locator_order_page import OrderPageLocators


class OrderTestData:
    CASE_1 = {
        "name": "Юлия",
        "surname": "Дементьева",
        "address": "Улица Ленина, дом 11",
        "phone_number": "89009000000",
        "scooter_color": OrderPageLocators.BLACK_PEARLS_CHECKBOX,
        "comment": "Как можно быстрее"
    }

    CASE_2 = {
        "name": "Петр",
        "surname": "Петров",
        "address": "улица Ленина, дом 21",
        "phone_number": "89019011111",
        "scooter_color": OrderPageLocators.GRAY_HOPELESSNESS,
        "comment": "Как можно быстрее"
    }