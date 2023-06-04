Практическая работа 5
Розанцева Елизавета БИСО-03-20
Ссылка на гитхаб – https://github.com/rozanseva/TMP/tree/main/lab_6
Код файла proxy.py

class IMath:
    def add(self, x, y):
        raise NotImplementedError()

    def sub(self, x, y):
        raise NotImplementedError()

    def mul(self, x, y):
        raise NotImplementedError()

    def div(self, x, y):
        raise NotImplementedError()

class Math(IMath):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class Proxy(IMath):

    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return self.math.mul(x, y)

    def div(self, x, y):
        return float('inf') if y == 0 else self.math.div(x, y) 

p = Proxy()
x, y = 10, 5
print ('10 + 5 = ' + str(p.add(x, y)))
print ('10 - 5 = ' + str(p.sub(x, y)))
print ('10 * 5 = ' + str(p.mul(x, y)))
print ('10 / 5 = ' + str(p.div(x, y)))

Код файла composite.py
class Graphic(object):
    def draw(self):
        raise NotImplementedError()
 
    def add(self, obj):
        raise NotImplementedError()
 
    def remove(self, obj):
        raise NotImplementedError()
 
    def get_child(self, index):
        raise NotImplementedError()
 
 
class Line(Graphic):
    def draw(self):
        print ('Линия')
 
 
class Rectangle(Graphic):
    def draw(self):
        print ('Прямоугольник')
 
 
class Text(Graphic):
    def draw(self):
        print ('Текст')
 
 
class Picture(Graphic):
    def __init__(self):
        self._children = []
 
    def draw(self):
        print ('Изображение')
        for obj in self._children:
            obj.draw()
 
    def add(self, obj):
        if isinstance(obj, Graphic) and not obj in self._children:
            self._children.append(obj)
 
    def remove(self, obj):
        index = self._children.index(obj)
        del self._children[index]
 
    def get_child(self, index):
        return self._children[index]
 
 
pic = Picture()
pic.add(Line())
pic.add(Rectangle())
pic.add(Text())
pic.draw()
 
line = pic.get_child(0)
line.draw() 


