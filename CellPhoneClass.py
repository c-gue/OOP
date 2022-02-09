class CellPhone:


    def __init__(self,m,mo,rp):
        self.__manufact = m
        self.__model = mo
        self.__retail_price = rp


    def set_manufact(self,manufacturer):
        self.set_manufact = manufacturer

    def set_model(self,model):
        self.set_model = model

    def set_retail_price(self,rp):
        self.set_retail_price = rp

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price