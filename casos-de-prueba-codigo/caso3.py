#Verificar el comportamiento de la aplicación al ingresar un carácter especial. La automatización 
# deberá obtener el mensaje mostrado por la aplicación y validar que coincida con lo definido en las especificaciones funcionales.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


#Verificar el comportamiento de la aplicación al ingresar un número de siete cifras. La automatización deberá obtener
# el mensaje mostrado por la aplicación y validar que coincida con lo definido en las especificaciones funcionales.

class casoDePrueba2A(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.quit()
    
    def test_buscar(self):
        driver = self.driver
        driver.get("https://nahual.github.io/qc-celfar/?v=1")
        time.sleep(3)
        
        inputIngreso = driver.find_element(By.XPATH , "//*[@id='input']")
        btnConvertir = driver.find_element(By.XPATH , "//*[@id='converterform']/input[2]")
        resultadoSalida  = driver.find_element(By.XPATH , "//*[@id='output']")
        
        time.sleep(3)
        
        valor = "1*" #probamos ingresando 
        inputIngreso.send_keys(valor)
        btnConvertir.click()
        time.sleep(2)
        
        # Resultado emitido por celfar
        resultado_texto = resultadoSalida.text
        
        self.assertEqual
        ("El valor ingresado no es un número (recuerde que los decimales deben expresarse con '.' y no con ',')",
         resultado_texto)
        

if __name__ == '__main__':
    unittest.main()