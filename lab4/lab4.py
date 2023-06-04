
class FlowersVisitor(object):
    """Посетитель"""
    def draw(self, flowers):
        methods = {
            Rose: self.draw_Rose,
            Hriza: self.draw_Hriza,
        }
        draw = methods.get(type(flowers), self.draw_unknown)
        draw(flowers)
 
    def draw_Rose(self, flowers):
        print ('Роза')
 
    def draw_Hriza(self, flowers):
        print ('Хризантема')
 
    def draw_unknown(self, flowers):
        print ('Пион')
 
 
class flowers(object):
    def draw(self, visitor):
        visitor.draw(self)
 
 
class Rose(flowers):
    """Роза"""
 
 
class Hriza(flowers):
    """Хризантема"""
 
 
class Сurrant(flowers):
    """Пион"""
 
 
visitor = FlowersVisitor()
 
Rose = Rose()
Rose.draw(visitor)
 
Hriza = Hriza()
Hriza.draw(visitor)
 
currant = Сurrant()
currant.draw(visitor)
