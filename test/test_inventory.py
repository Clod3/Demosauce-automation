from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def test_inventory_title(driver_logged):
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "El titulo de la pagina a la que se accede no es correcto"

def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos) > 0

def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "El icono del menu no está presente en la pagina"
    assert filtro.is_displayed(), "El filtro del catalogo no está presente en la pagina"