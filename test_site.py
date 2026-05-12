import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = './chromedriver.exe'

def create_driver():
    """Создание драйвера браузера"""
    service = Service(executable_path=DRIVER_PATH)
    return webdriver.Chrome(service=service)


def test_checkbox():
    """Тест-кейс 1: Отметка чекбокса."""
    driver = create_driver()
    try:
        # Открываем страницу с чекбоксами
        driver.get('https://the-internet.herokuapp.com/checkboxes')
        time.sleep(1)
        
        # Находим все чекбоксы
        checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        
        # Отмечаем первый чекбокс (если не отмечен)
        if not checkboxes[0].is_selected():
            checkboxes[0].click()
            print('   Чекбокс 1 отмечен')
        
        # Проверяем, что первый чекбокс отмечен
        assert checkboxes[0].is_selected(), 'Первый чекбокс не отмечен'
        
        print('Test 1 PASSED: Чекбокс успешно отмечен.')
    except Exception as e:
        print(f'Test 1 FAILED: {e}')
    finally:
        driver.quit()


def test_dropdown():
    """Тест-кейс 2: Выбор опции из выпадающего списка."""
    driver = create_driver()
    try:
        # Открываем страницу с выпадающим списком
        driver.get('https://the-internet.herokuapp.com/dropdown')
        time.sleep(1)
        
        # Находим выпадающий список
        dropdown = driver.find_element(By.ID, 'dropdown')
        
        # Выбираем опцию "Option 2"
        from selenium.webdriver.support.ui import Select
        select = Select(dropdown)
        select.select_by_visible_text('Option 2')
        time.sleep(1)
        
        # Проверяем, что выбрана правильная опция
        selected_option = select.first_selected_option.text
        assert selected_option == 'Option 2', f'Выбрана опция "{selected_option}", ожидалась "Option 2"'
        
        print('Test 2 PASSED: Опция успешно выбрана из списка.')
    except Exception as e:
        print(f'Test 2 FAILED: {e}')
    finally:
        driver.quit()


def test_form_submit():
    """Тест-кейс 3: Заполнение и отправка формы."""
    driver = create_driver()
    try:
        # Открываем страницу с формой входа
        driver.get('https://the-internet.herokuapp.com/login')
        time.sleep(1)
        
        # Заполняем поле username
        username = driver.find_element(By.ID, 'username')
        username.send_keys('tomsmith')
        
        # Заполняем поле password
        password = driver.find_element(By.ID, 'password')
        password.send_keys('SuperSecretPassword!')
        
        # Нажимаем кнопку Login
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        
        # Проверяем успешный вход
        success_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'success'))
        )
        assert 'You logged into a secure area' in success_message.text, 'Сообщение об успешном входе не найдено'
        
        # Нажимаем кнопку Logout
        logout_button = driver.find_element(By.CSS_SELECTOR, 'a.button')
        logout_button.click()
        
        # Проверяем выход из системы
        logout_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'success'))
        )
        assert 'You logged out' in logout_message.text, 'Сообщение о выходе не найдено'
        
        print('Test 3 PASSED: Форма успешно заполнена и отправлена.')
    except Exception as e:
        print(f'Test 3 FAILED: {e}')
    finally:
        driver.quit()


if __name__ == '__main__':
    print("="*50)
    print("ЗАПУСК АВТОТЕСТОВ ДЛЯ САЙТА THE-INTERNET")
    print("="*50)
    
    test_checkbox()
    time.sleep(2)
    test_dropdown()
    time.sleep(2)
    test_form_submit()
    
    print("="*50)
    print("ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
    print("="*50)