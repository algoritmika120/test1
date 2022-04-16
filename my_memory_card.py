#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какой овощ очень полезен для зрения?', 'морковь', 'капуста', 'помидор', 'яблоко'))
question_list.append(Question('Горело семь электрических лампочек.Две погасли сколько осталось?', '7', '3', '5', '0'))
question_list.append(Question('Горело 100 свечей, 100 погасло и 17 сгорело. Сколько отсалось?', '83', '15', '100', '73'))
#создание элементов интерфейса
app = QApplication([])


button = QPushButton('Ответить')
lb_Question = QLabel('Вопрос')

RadioGroupBox = QGroupBox("Варианты ответов")
AnsGroupBox = QGroupBox("Варианты ответов2")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignCenter))
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(RadioGroupBox)

AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)


layout_main = QVBoxLayout()


layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2)
layout_main.addLayout(layout_line3)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
    question_list.remove(q)

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n Всего вопросов:', main_win.total, '\n Правильных ответов', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    else:
        show_correct('Неверно!')
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')

def next_question():
    main_win.total += 1
    print('Статистика\n Всего вопросов:', main_win.total, '\n Правильных ответов', main_win.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)



def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
      #  if len(question_list) > 0:
        next_question()
       # else:
        #    end.answer()   




main_win = QWidget()

main_win.score = 0
main_win.total = 0
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 400)

next_question()

main_win.setLayout(layout_main)

button.clicked.connect(click_OK)

main_win.show()
app.exec()