from selenium.webdriver.common.by import By

# ---------- Шапка сайта ----------
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет»
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка «Конструктор»
LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")  # Логотип Stellar Burgers

# ---------- Главная страница (конструктор) ----------
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт»
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» (видна после входа)
CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок «Соберите бургер»
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка «Булки»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка «Соусы»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка «Начинки»
ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")  # Название выбранной вкладки

# ---------- Общие поля форм ----------
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле «Email»
PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле «Пароль»

# ---------- Страница входа ----------
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок «Вход»
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти» в форме входа
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться»
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»

# ---------- Страницы регистрации и восстановления пароля ----------
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя»
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка «Некорректный пароль»
LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» (на страницах регистрации и восстановления пароля)

# ---------- Личный кабинет ----------
PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Ссылка «Профиль»
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход»
