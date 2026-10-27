from abc import ABC,abstractmethod
class base(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    def display_value(self):
        print("22")
class value(base):
    def abstract_method(self):
        print("44")
v=value()
v.display_value()
v.abstract_method()
