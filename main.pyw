import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase


from Calk import Ui_MainWindow

operations = {
	'+': add,
	'-': sub,
	'x': mul,
	'/': truediv
}


class Calculator(QMainWindow):
	def __init__(self):
		super(Calculator, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

		# digits
		self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
		self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
		self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
		self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
		self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
		self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
		self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
		self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
		self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
		self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

		# actions
		self.ui.btn_clear.clicked.connect(self.clear_all)
		self.ui.btn_ce.clicked.connect(self.clear_entry)
		self.ui.btn_point.clicked.connect(self.add_point)
		self.ui.btn_neg.clicked.connect(self.negate)
		self.ui.btn_backspace.clicked.connect(self.backspace)

		# math
		self.ui.btn_r.clicked.connect(self.calculate)
		self.ui.btn_plus.clicked.connect(lambda: self.math_operation('+'))
		self.ui.btn_min.clicked.connect(lambda: self.math_operation('-'))
		self.ui.btn_x.clicked.connect(lambda: self.math_operation('x'))
		self.ui.btn_.clicked.connect(lambda: self.math_operation('/'))
		

	def add_digit(self, bnt_text: str) -> None:
		self.clear_temp_if_equality()
		if self.ui.lb_t.text() == '0':
			self.ui.lb_t.setText(bnt_text)
		else:
			self.ui.lb_t.setText(self.ui.lb_t.text() + bnt_text)
	def add_point(self) -> None:
		self.clear_temp_if_equality()
		if '.' not in self.ui.lb_t.text():
			self.ui.lb_t.setText(self.ui.lb_t.text() + '.')

	def negate(self):
		self.clear_temp_if_equality()
		entry = self.ui.lb_t.text()

		if '-' not in entry:
			if entry != '0':
				entry = '-' + entry
		else:
			entry = entry[1:]

		self.ui.lb_t.setText(entry)	

	def backspace(self) -> None:
		self.clear_temp_if_equality()
		entry = self.ui.lb_t.text()

		if len(entry) != 1:
			if len(entry) == 2 and '-' in entry:
				self.ui.lb_t.setText('0')
			else:
				self.ui.lb_t.setText(entry[:-1])
		else:
			self.ui.lb_t.setText('0')

	def clear_all(self) -> None:
		self.ui.lb_t.setText('0')
		self.ui.lbl_temp.clear()

	def clear_entry(self) -> None:
		self.clear_temp_if_equality()
		self.ui.lb_t.setText('0')

	def clear_temp_if_equality(self) -> None:
		if self.get_math_sign() == '=':
			self.ui.lbl_temp.clear()
			

	@staticmethod
	def remove_trailing_zeros(num: str) -> str:
                n = str(float(num))
                return n[:-2] if n[-2:] == '.0' else n

 
	def add_temp(self, math_sign: str):
		if not self.ui.lbl_temp.text() or self.get_math_sign() == '=':
			self.ui.lbl_temp.setText(self.remove_trailing_zeros(self.ui.lb_t.text()) + f' {math_sign} ')
			self.ui.lb_t.setText('0')

	def get_entry_num(self) -> Union[int, float]:
		entry = self.ui.lb_t.text().strip('.')

		return float(entry) if '.' in entry else int(entry)

	def get_temp_num(self) -> Union[int, float, None]:
		if self.ui.lbl_temp.text():
			temp = self.ui.lbl_temp.text().strip('.').split()[0]
			return float(temp) if '.' in temp else int(temp)

	def get_math_sign(self) -> Optional[str]:
		if self.ui.lbl_temp.text():
			return self.ui.lbl_temp.text().strip('.').split()[-1]

	
	def calculate(self) -> Optional[str]:
		entry = self.ui.lb_t.text()
		temp = self.ui.lbl_temp.text()

		if temp:
			result = self.remove_trailing_zeros(
				str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num())))

			self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
			self.ui.lb_t.setText(result)
			return result

	def math_operation(self, math_sign: str):
		temp = self.ui.lbl_temp.text()

		if not temp:
			self.add_temp(math_sign)
		else:
			if self.get_math_sign() != math_sign:
				if self.get_math_sign() == '=':
					self.add_temp(math_sign)
				else:
					self.ui.lbl_temp.setText(temp[:-2] + f'{math_sign} ')

			else:
				self.ui.lbl_temp.setText(self.calculate() + f' {math_sign}')

		
if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = Calculator()
	window.show()

	sys.exit(app.exec())
