#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup, QMessageBox
import random

class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    question.setText(q.text)
    random.shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)

questions = [
    Question('Первый вопрос','да','нет','что','где?'),
    Question('В каком году Петр 13 завоевал луну?','4324','я хочу питцы','что?','Знакомьтесь с клавиатурой Gboard! Здесь будет сохраняться текст, который вы копируете.'),
    Question('Да?','да','нет','незнаю','где?'),
    Question('сколько стоит сырная булка в пятёрочке?','49 рублей','342 рубля','59 рублей','79 рублей'),
    Question('Клонирование. Теперь тут все кнопки да, но только одна правильная.','да','да','да','да'),
    Question('2Первый вопрос','да','нет','что','где?'),
    Question('3Первый вопрос','да','нет','что','где?'),
    Question('4Первый вопрос','да','нет','что','где?'),
    Question('5Первый вопрос','да','нет','что','где?'),
    Question('6Первый вопрос','да','нет','что','где?'),
]

def show_answers():
    if button_group.checkedButton() == None:
        return
        
    btn.setText("Следующий вопрос")
    for rbtn in buttons:
        if rbtn.isChecked():
            if rbtn.text() == buttons[0].text():
                rbtn.setStyleSheet('color: green;')
                main_win.score += 1
            else:
                rbtn.setStyleSheet('color: red;')
                buttons[0].setStyleSheet('color: green;')

def show_question():
    btn.setText("Ответить")
    button_group.setExclusive(False)
    var1.setStyleSheet('')
    for rbtn in buttons:
        rbtn.setStyleSheet('')
        rbtn.setChecked(False)
    button_group.setExclusive(True)
    next_question()
    

def next_question():
    if main_win.q_index >= len(question):
        main_win.q_index = 0
    q = questions[main_win.q_index]
    main_win.q_index += 1
    ask(q)

def next_question():
    if main_win.q_index >= len(questions):
        main_win.q_index = 0
        random.shuffle(questions)
        show_score()
        main_win.score = 0
    q = questions[main_win.q_index]
    main_win.q_index += 1 
    ask(q)

def start_test():
    if btn.text() == 'Ответить':
        show_answers()
    else:
        show_question()

def show_score():
    percent = main_win.score / main_win.total * 100
    percent = round(percent, 1)
    text = 'Уважаемый пользователь!\n'
    text += f'Вы правильно ответили на {main_win.score} из {main_win.total} вопросов.\n'
    text += f'Процент правильных ответов: {percent}5.\n'
    text += f'Тест начнется заново!'

    msg = QMessageBox()
    msg.setWindowTitle('Результат тестирования')
    msg.setText(text)
    msg.exec()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Meme Card')
main_win.resize(640,360)
main_win.q_index = 0
main_win.total = len(questions)
main_win.score = 0

question = QLabel('Do you want to continue training from this card?')
grp_box = QGroupBox('Варианты ответов')
button_group = QButtonGroup()
var1 = QRadioButton('1 variant')
var2 = QRadioButton('2 variant')
var3 = QRadioButton('3 variant')
var4 = QRadioButton('4 variant')
btn = QPushButton('Ответить')
result_text = QLabel('Ваш результат: 5 из 5')
#добавление кнопок в gruppu

button_group.addButton(var1)
button_group.addButton(var2)
button_group.addButton(var3)
button_group.addButton(var4)

#создание направляющих для виджетов
main_layout = QVBoxLayout()
main_h1 = QHBoxLayout()
main_h2 = QHBoxLayout()
main_h3 = QHBoxLayout()
grp_main_layout = QHBoxLayout()
grp_v1 = QVBoxLayout()
grp_v2 = QVBoxLayout()
grp_v3 = QVBoxLayout()
grp_v4 = QVBoxLayout()

# Размещение виджетов в QGroupbox
grp_v1.addWidget(var1)
grp_v1.addWidget(var2)
grp_v2.addWidget(var3)
grp_v2.addWidget(var4)
grp_main_layout.addLayout(grp_v1)
grp_main_layout.addLayout(grp_v2)
grp_box.setLayout(grp_main_layout)

main_h1.addWidget(question)
main_h2.addWidget(grp_box)
main_h3.addStretch(1)
main_h3.addWidget(btn, stretch = 2)
main_h3.addStretch(1)
main_layout.addLayout(main_h1)
main_layout.addLayout(main_h2)
main_layout.addLayout(main_h3)
main_win.setLayout(main_layout)
# размещение виджетов на 1 устройстве

# привязка
btn.clicked.connect(start_test)

# Создание списка с радиокнопками
buttons = [var1, var2, var3, var4]
ask(questions[main_win.q_index])
main_win.q_index += 1

main_win.show()
app.exec_()