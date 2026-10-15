from datetime import datetime

class LogMaster():
    def __init__(self, file):
        self.name = file

    def log(self, level, source, message,
            ident, user, add_info=""):
        self.dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.level = level
        self.source = source
        self.message = message
        self.ident = ident
        self.user = user
        self.add_info = add_info

        string = f"DATE AND TIME: {self.dt} | " \
                 f"LEVEL: {self.level} | " \
                 f"SOURCE: {self.source} | " \
                 f"MESSAGE: {self.message} | " \
                 f"IDENTIFIER: {self.ident} | " \
                 f"USER: {self.user} | " \
                 f"EXTRA INFO: {self.add_info}\n"

        with open(f"{self.name}.txt", "a", encoding='utf-8') as f:
            f.write(string)
