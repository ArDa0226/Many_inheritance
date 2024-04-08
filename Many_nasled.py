class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'{self.__class__.__name__} model {self.model}'

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print('Робот охраняет военный объект c помощью', self.gun)

class WarSubmarineRobot(WarRobot):

    def operate(self):
        super().operate()
        print('Охрана ведеться под водой')

rc_submarine = WarRobot(model='Orbiter', gun='Lizer')
print(rc_submarine)
rc_submarine.operate()

r2d2 = WarRobot(model='R2D2', gun='пулемет')
print(r2d2)
r2d2.operate()

# class VacuumCleaningRobot(Robot):
#
#     def __init__(self, model):
#         super().__init__(model=model)
#         self.dust_bug = 0
#     def operate(self):
#         print('Робот пылесосит пол, заполненность мешка для пыли', self.dust_bug)
#
#
#
# roomba = VacuumCleaningRobot(model='Roomba M505')
# print(roomba)
# roomba.operate()