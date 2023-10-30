class InvalidTaxiName(Exception):
    def __init__(self, message="Bu id lik taxi mavjut"):
        self._message=message
        super().__init__(message)