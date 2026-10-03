from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    app_name: str = "Ecommerce API"
    debug: bool = False
    app_env: str = "development"

    db_connection: str = "mysql+pymysql"
    db_host: str = ""
    db_port: int = 3306
    db_database: str = ""
    db_username: str = ""
    db_password: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def database_url(self) -> URL:
        return URL.create(
            drivername=self.db_connection,
            host=self.db_host,
            port=self.db_port,
            database=self.db_database,
            username=self.db_username,
            password=self.db_password,
            query=(
                {"charset": "utf8mb4"} if self.db_connection.startswith("mysql") else {}
            ),
        )


settings = Settings()
