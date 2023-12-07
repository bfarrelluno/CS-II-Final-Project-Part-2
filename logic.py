from PyQt6.QtWidgets import *
from gui import *
import math
import random
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addButton.clicked.connect(lambda: self.add())
        self.subtractButton.clicked.connect(lambda: self.subtract())
        self.multiplyButton.clicked.connect(lambda: self.multiply())
        self.divideButton.clicked.connect(lambda: self.divide())
        self.randomButton.clicked.connect(lambda: self.choose())
        self.averageButton.clicked.connect(lambda: self.average())
        self.powerButton.clicked.connect(lambda: self.power())
        self.exitButton.clicked.connect(lambda: exit())

    def add(self) -> None:
        """
        This function adds a minimum of 3 numbers together
        through addition.  Numbers less than or equal to 0 are not used.
        if all numbers are less than or equal to 0,
        the function will answer with 0.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) < 3:
                raise TypeError
            else:
                final_answers = float(sum(x for x in list_answers if x > 0)) or 0.00
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Add\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Add', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
            self.numberInput.setText('')
        except TypeError:
            self.answerLabel.setText('Error: Need to provide at least 3 values')
            self.numberInput.setText('')

    def subtract(self) -> None:
        """
        This function subtracts a minimum of 3 negative numbers together
        through subtraction.  Numbers greater than or equal to 0 are not used.
        if all numbers are greater than or equal to 0,
        the function will answer with 0.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) < 3:
                raise TypeError
            else:
                final_answers = float(sum(x for x in list_answers if x < 0)) or 0.00
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Subtract\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Subtract', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
            self.numberInput.setText('')
        except TypeError:
            self.answerLabel.setText('Error: Need to provide at least 3 values')
            self.numberInput.setText('')

    def multiply(self) -> None:
        """
        This function multiplies a minimum of 3 numbers together
        through multiplication.  If the number 0 is used
        the function will answer with 0.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) < 3:
                raise TypeError
            else:
                if sum(list_answers) != 0:
                    final_answers = math.prod(x for x in list_answers if x != 0)
                else:
                    final_answers = 0
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Multiply\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Multiply', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
            self.numberInput.setText('')
        except TypeError:
            self.answerLabel.setText('Error: Need to provide at least 3 values')
            self.numberInput.setText('')

    def divide(self) -> None:
        """
        This function takes at least 3 numbers and divides the first one
        by the rest of them.  The first number can be a 0, but it will always make the
        answer a 0.  If any number but the first is a 0, there will be a ZeroDivisionError
        and a new set of numbers will need to be entered.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) < 3:
                raise TypeError
            elif 0 in list_answers[1:]:
                raise ZeroDivisionError
            else:
                if list_answers[0] == 0:
                    final_answers = 0
                else:
                    final_answers = list_answers[0]
                    for item in list_answers:
                        print('3')
                        final_answers = final_answers / item
                    final_answers = final_answers
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Divide\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Divide', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
        except TypeError:
            self.answerLabel.setText('Error: Need to provide at least 3 values')
            self.numberInput.setText('')
        except ZeroDivisionError:
            self.answerLabel.setText('Error: Cannot Divide by 0')
            self.numberInput.setText('')


    def choose(self) -> None:
        """
        This function randomly selects a number from a
        minimum of 3 numbers.  All types of numbers are usable unlike previous ones.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) < 3:
                raise TypeError
            else:
                final_answers = random.choice(list_answers)
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Random Choice\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Random Choice', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
            self.numberInput.setText('')
        except TypeError:
            self.answerLabel.setText('Error: Need to provide at least 3 values')
            self.numberInput.setText('')

    def average(self) -> None:
        """
        This function takes the average of a minimum of 3 numbers.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) < 3:
                raise TypeError
            else:
                final_answers = sum(list_answers)/len(answers)
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Average\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Average', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
            self.numberInput.setText('')
        except TypeError:
            self.answerLabel.setText('Error: Need to provide at least 3 values')
            self.numberInput.setText('')


    def power(self) -> None:
        """
        This function inputs 2 numbers and multiplies the first number by
        itself to the power of the second number.
        The function finishes a successful run by logging the answer into a csv file.
        :param self: Parameter that refers to itself.
        """
        try:
            answers = self.numberInput.text().split()
            list_answers = [float(i) for i in answers]
            if len(answers) < 1:
                raise ValueError
            elif len(answers) >= 3:
                raise TypeError
            else:
                final_answers = list_answers[0]**list_answers[1]
                x = str(list_answers)
                x = x.replace("[", "")
                x = x.replace("]", "")
                self.answerLabel.setText(f'Problem Type: Power\nNumbers used: {x}\nFinal Answer = {final_answers:.2f}')
                info = [f'Problem Type: Power', f'Numbers used: {x}', f'Final Answer = {final_answers:.2f}']
                with open('data.csv', 'a') as f:
                    data = csv.writer(f)
                    data.writerow([info])
                f.close()
                self.numberInput.setText('')
        except ValueError:
            self.answerLabel.setText('Error: Need to provide operator/Need to provide numbers')
            self.numberInput.setText('')
        except TypeError:
            self.answerLabel.setText('Error: Only provide 2 values')
            self.numberInput.setText('')
