from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.LoginPage import login

#Login
# Test de login validación de login exitoso
def test_login_exitoso(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    titulo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert "Swag Labs" in titulo.text, "El título de la página no es correcto"
#Test de validación del titulo de la pagina
def test_titulo_inventario(login_in_driver):
    driver = login_in_driver
    titulo = driver.title
    assert titulo == "Swag Labs", "El título de la página no es correcto"
#Catalogo/Inventario
#Validamos que al menos se visualice un producto en el catalogo
def test_productos_visibles(login_in_driver):
    driver = login_in_driver
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos visibles en el inventario"
#Validamos que existe un nombre y precio para el primer producto
def test_primer_producto_nombre_precio(login_in_driver):
    driver = login_in_driver
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\nPrimer producto → Nombre: {primer_nombre} | Precio: {primer_precio}")
    assert primer_nombre, "El nombre del primer producto está vacío"
    assert primer_precio, "El precio del primer producto está vacío"
#Validamos que se visualice el menú y el filtro en la pagina de catalogo
def test_ui_elements(login_in_driver):
    driver = login_in_driver
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed(), "El menú no está presente en la página"
    assert filtro.is_displayed(), "El filtro no está presente en la página"
#Carrito
#Validamos que se agrega un producto al carrito y que se visualice en el mismo
def test_agregar_producto_al_carrito(login_in_driver):
    driver = login_in_driver
    # Agregar primer producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    # Verificar contador del carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se actualizó correctamente"
    # Obtener nombre del primer producto
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # Verificar que el producto aparezca en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item == product_name, "El producto en el carrito no coincide con el agregado"