from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
import info
import os
#lembrando que voce precisa ter essas bibliotecas instaladas
#por enquanto eu so criei um modo de selecao por genero, voce escolhe seu genero de musica
#e vai comecar a toca 
class facebook:
    def __init__(self):
        #coloque seu email e sua senha do facebook aqui depois e so executar 
        self.mail = ""
        self.senha = ""
        self.link = "https://www.facebook.com/login"
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('lang=pt-br')
        self.browser = webdriver.Firefox(executable_path=r'./geckodriver')

    def login(self):
        self.browser.get(self.link)
        time.sleep(1)
        login_email = self.browser.find_element_by_xpath("//input[@id='email']")
        login_email.click()
        login_email.send_keys(self.mail)
        time.sleep(1)
        login_senha = self.browser.find_element_by_xpath("//input[@id='pass']")
        login_senha.click()
        login_senha.send_keys(self.senha)
        time.sleep(1)
        login_buton = self.browser.find_element_by_xpath("//button[@id='loginbutton']")
        login_buton.click()
    def Escolha_genero(self, value):
        gen = info.genero
        self.link = "https://business.facebook.com/creatorstudio/?tab=ct_sound_collection&mode=facebook&collection_id=all_pages&sound_collection_tab=sound_tracks"
        self.browser.get(self.link)
        time.sleep(5)
        c = self.browser.find_element_by_xpath("//div[@class='_1f']")
        c.click()
        time.sleep(3)
        ele2 = self.browser.find_element_by_xpath(gen[value])
        ele2.click()
    def play(self):
        p = info.musica
        pl = self.browser.find_element_by_xpath(p["play"])
        pl.click()
    def prox_(self):
        musi_ = info.musica
        proxima = self.browser.find_element_by_xpath(musi_["proxima"])
        proxima.click()
    def volta_(self):
        music_ = info.musica
        volta = self.browser.find_element_by_xpath(music_["volta"])
        volta.click()
    def tempo_(self):
        Time = info.musica
        html = self.browser.find_element_by_xpath(Time['TimeInit'])
        TimeInit = html.get_attribute("textContent")
        html2 = self.browser.find_element_by_xpath(Time['TimeFim'])
        TimeFim = html2.get_attribute("textContent")
        if TimeFim == TimeInit:
            self.prox_()
    def menu_(self):
        pass
    def sair(self):
        self.browser.quit()


valor = info.validar_input()    
chama = facebook()
chama.login()
time.sleep(1)
chama.Escolha_genero(valor)
time.sleep(5)
chama.play()

while True:
    time.sleep(4)
    chama.tempo_()
