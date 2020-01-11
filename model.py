class Notification:
    """
    Data class to describe data received from API.
    """

    def __init__(self):
        self.id = None
        self.title = None
        self.message = None
        self.start_time = None
        self.end_time = None
        self.source = None

    def __str__(self) -> str:
        props = ', '.join("{}={}".format(name, value) for name, value in vars(self).items())
        return f"{type(self).__name__}({props})"