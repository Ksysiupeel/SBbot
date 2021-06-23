class Country_Info:
    def __init__(self, r):
        self.r = r

    @property
    def get_country_name(self):
        return self.r[0]["country"]

    @property
    def get_country_confirmed(self):
        return self.r[0]["confirmed"]

    @property
    def get_country_recovered(self):
        return self.r[0]["recovered"]

    @property
    def get_country_deaths(self):
        return self.r[0]["deaths"]