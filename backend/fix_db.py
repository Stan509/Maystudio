import os
import sys

def get_connection_string():
    db_url = os.getenv('DATABASE_URL')
    if db_url and not db_url.startswith('${'):
        return db_url

    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT', '5432')
    dbname = os.getenv('POSTGRES_DB')

    if host and user and password and dbname:
        ssl = "?sslmode=require" if host not in ['localhost', '127.0.0.1', 'db'] else ""
        return f"postgresql://{user}:{password}@{host}:{port}/{dbname}{ssl}"
    return None

def prepare_database():
    conn_str = get_connection_string()
    if not conn_str:
        print("No PostgreSQL database configuration found in environment.")
        return

    print("=== STARTING DATABASE SCHEMA PERMISSION FIX ===")
    try:
        import psycopg
        conn = psycopg.connect(conn_str, autocommit=True)
        cur = conn.cursor()

        # 1. Transfer ownership of schema public to current user
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
            print("Executing: CREATE SCHEMA IF NOT EXISTS maystudio AUTHORIZATION CURRENT_USER;")
            cur.execute("CREATE SCHEMA IF NOT EXISTS maystudio AUTHORIZATION CURRENT_USER;")
            print("SUCCESS: Schema maystudio ensured!")
        except Exception as e:
            print("Notice: CREATE SCHEMA maystudio failed:", e)

        cur.close()
        conn.close()
        print("=== DATABASE PERMISSION SETUP COMPLETED ===")
    except Exception as e:
        print("CRITICAL ERROR in prepare_database:", e)

if __name__ == '__main__':
    prepare_database()
