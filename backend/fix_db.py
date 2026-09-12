import os
import sys

def prepare_database():
    db_url = os.getenv('DATABASE_URL')
    if not db_url and os.getenv('USE_POSTGRES', 'True').lower() == 'true':
        user = os.getenv('POSTGRES_USER', 'maystudio')
        password = os.getenv('POSTGRES_PASSWORD', 'maystudio_password')
        host = os.getenv('POSTGRES_HOST', 'localhost')
        port = os.getenv('POSTGRES_PORT', '5432')
        dbname = os.getenv('POSTGRES_DB', 'maystudio')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    if not db_url:
        print("No PostgreSQL database configured. Skipping database schema preparation.")
        return

    print("Preparing PostgreSQL schema permissions...")
    try:
        import psycopg
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                # Create custom schema where user has owner rights
                cur.execute("CREATE SCHEMA IF NOT EXISTS maystudio;")
                try:
                    cur.execute("GRANT ALL ON SCHEMA public TO CURRENT_USER;")
                except Exception as e:
                    print("Notice (public schema grant):", e)
                try:
                    cur.execute("GRANT ALL ON SCHEMA maystudio TO CURRENT_USER;")
                except Exception as e:
                    print("Notice (maystudio schema grant):", e)
                conn.commit()
        print("Schema 'maystudio' prepared successfully!")
    except Exception as e:
        print("Warning during schema setup (continuing):", e)

if __name__ == '__main__':
    prepare_database()
