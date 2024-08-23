import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://part1_cb2p_user:y3LtAjJX25q2DdXgP3HEbBUSMUDDYvc3@dpg-cr49u4o8fa8c73djoi5g-a.oregon-postgres.render.com/part1_cb2p")

settings = Settings()
