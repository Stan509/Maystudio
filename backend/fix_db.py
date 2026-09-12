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
        return

    print("=== STARTING DATABASE SCHEMA PERMISSION FIX ===")
    try:
        import psycopg
        conn = psycopg.connect(db_url, autocommit=True)
        cur = conn.cursor()

        # 1. Attempt to transfer ownership of schema public to current user
        try:
            print("Executing: ALTER SCHEMA public OWNER TO CURRENT_USER;")
            cur.execute("ALTER SCHEMA public OWNER TO CURRENT_USER;")
            print("SUCCESS: public schema owner changed to current user!")
        except Exception as e:
            print("Notice: ALTER SCHEMA public OWNER failed:", e)

        # 2. Grant all privileges on schema public to PUBLIC
        try:
            print("Executing: GRANT ALL ON SCHEMA public TO PUBLIC;")
            cur.execute("GRANT ALL ON SCHEMA public TO PUBLIC;")
            print("SUCCESS: Granted ALL on schema public!")
        except Exception as e:
            print("Notice: GRANT ALL ON SCHEMA public failed:", e)

        # 3. Create schema maystudio as additional fallback
        try:
            print("Executing: CREATE SCHEMA IF NOT EXISTS maystudio;")
            cur.execute("CREATE SCHEMA IF NOT EXISTS maystudio;")
            print("SUCCESS: Schema maystudio ensured!")
        except Exception as e:
            print("Notice: CREATE SCHEMA maystudio failed:", e)

        cur.close()
        conn.close()
        print("=== DATABASE PERMISSION FIX COMPLETED ===")
    except Exception as e:
        print("CRITICAL NOTICE during fix_db.py execution:", e)

if __name__ == '__main__':
    prepare_database()
