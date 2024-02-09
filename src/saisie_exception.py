class SaisieException(Exception):
    def __init__(self, message):
        """
        Déclenche une Exception avec un nom et un message personnalisés
        """
        super().__init__(message)