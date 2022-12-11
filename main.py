#подключаем библиотеку пайкюти
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#делаем окошко 
app = QApplication([])
ui = uic.loadUi("inter.html") #и подключаем файл интерфейса, который сделали в кютедизайнере
ui.show() #показываем интерфейс

def analize():
    text = ui.textEdit.toPlainText() #получаем текст из поля ввода
    text = text.split()  #делаем из текста отдельный скписок со словами
    len_text = len(text) #длина текста
    counter = 0 #счетчик сколько раз встретится слово св тексте
    ui.label_3.setText('Не заспамлен!')  #выводим в результат что изначально текст не заспамлен
    for i in text: #находим сколько раз встречается слово в тексте
        for ii in text:
            if i == ii:
                counter += 1
            if counter/len_text*100 > 60: 
                ui.label_3.setText('Заспамлен!')     
        counter = 0 #сбрасываем счетчик после проверки каждого слова

ui.pushButton.clicked.connect(analize) #привязываем к кнопке функцию анализа текста

app.exec_()