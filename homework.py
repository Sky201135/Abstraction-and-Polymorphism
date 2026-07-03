class BMW:
    def drive(self):
        return "BMW is driving fast"

    def stop(self):
        return "BMW has stopped"


class Ferrari:
    def drive(self):
        return "Ferrari is driving fast"

    def stop(self):
        return "Ferrari has stopped"


def test_drive(vehicle):
    print(vehicle.drive())
    print(vehicle.stop())


bmw = BMW()
ferrari = Ferrari()

test_drive(bmw)
test_drive(ferrari)
