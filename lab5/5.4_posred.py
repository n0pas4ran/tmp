from abc import ABCMeta, abstractmethod
from weakref import proxy
import inspect
#ПОСРЕДНИК

class Mediator(metaclass=ABCMeta):
	@abstractmethod
	def send(self, message: str) -> None:
		pass


class Colleague(metaclass=ABCMeta):
	def __init__(self, mediator: Mediator) -> None:
		self._mediator = proxy(mediator)

	@abstractmethod
	def send(self, message: str) -> None:
		pass

	@abstractmethod
	def receive(self, message: str) -> None:
		pass


class TelegramBetweenTwoColleagues(Mediator):
	def __init__(self) -> None:
		self._first = None
		self._second = None

	def set_first(self, first: Colleague) -> None:
		self._first = first

	def set_second(self, second: Colleague) -> None:
		self._second = second

	def send(self, message: str) -> None:
		sender = inspect.currentframe().f_back.f_locals['self']
		receiver = self._first if sender == self._second else self._second
		receiver.receive(message)


class Max(Colleague):

	def send(self, message: str) -> None:
		self._mediator.send(message)

	def receive(self, message: str) -> None:
		print('Олег получил сообщение: {}'.format(message))


class Makar(Colleague):

	def send(self, message: str) -> None:
		self._mediator.send(message)

	def receive(self, message: str) -> None:
		print('Саша прочитал в телеграме сообщение: {}'.format(message))


if __name__ == '__main__':
	print('OUTPUT:')
	telegram = TelegramBetweenTwoColleagues()
	max = Max(telegram)
	makar = Makar(telegram)
	telegram.set_first(max)
	telegram.set_second(makar)
	max.send('Как дела?')
	makar.send('Нормально')
