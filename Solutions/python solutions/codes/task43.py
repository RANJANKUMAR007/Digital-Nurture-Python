import configparser

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.filename)

class DatabaseConfig(Config):
    def __init__(self, filename):
        super().__init__(filename)
        self.db_settings = {}

    def load_and_validate(self):
        self.load()
        if "database" not in self.config:
            raise KeyError("Section [database] is missing in configuration.")
        
        required_keys = ["host", "port", "user", "password", "dbname"]
        db_sec = self.config["database"]
        
        for key in required_keys:
            if key not in db_sec:
                raise KeyError(f"Required key '{key}' is missing in [database] section.")
            self.db_settings[key] = db_sec[key]

with open("db.ini", "w") as f:
    f.write("[database]\nhost = localhost\nport = 5432\nuser = admin\npassword = secret\ndbname = mydb\n")

try:
    db_cfg = DatabaseConfig("db.ini")
    db_cfg.load_and_validate()
    print("Database configuration loaded successfully:")
    print(db_cfg.db_settings)
except Exception as e:
    print(f"Configuration error: {e}")
