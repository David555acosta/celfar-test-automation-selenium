from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class casoDePrueba1(unittest.TestCase):
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
        
        valor = 0 #variable para modificar en cada ejecucion y no hacer validaciones desde el inputIngreso
        inputIngreso.send_keys(valor)
        btnConvertir.click()
        
        time.sleep(2)
        
        # Resultado emitido por celfar
        resultado_texto = resultadoSalida.text
        resultado = float(resultado_texto)
        
        #Valor esperado
        esperado = (valor * 9 / 5) + 32
        
        print("Esperado:", esperado)
        print("Resultado:", resultado)
        
        self.assertEqual(esperado, resultado)
        
if __name__ == '__main__':
    unittest.main()
        
        


