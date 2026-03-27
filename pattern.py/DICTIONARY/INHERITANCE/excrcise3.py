class device:
    def power_on(self):
        print("device is powering")
class laptop(device):
    def coding(self):
        print("coding in laptop")
class mobile(device):
    def call(self):
        print("making a call")
l = laptop()
m = mobile()
l.power_on()
l.coding()
m.call()
