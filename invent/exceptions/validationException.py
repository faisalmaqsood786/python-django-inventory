class validationException(Exception):
    def __init__(self, errors):
        self.errors = errors
