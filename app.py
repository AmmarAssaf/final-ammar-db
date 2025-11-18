import os
import subprocess
import sys

print("🚀 بدء البرنامج البسيط...")

# تثبيت psycopg2 إذا لم يكن مثبتاً
try:
    import psycopg2
    print("✅ psycopg2 مثبت بالفعل")
except ImportError:
    print("📦 جارٍ تثبيت psycopg2-binary...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psycopg2-binary==2.9.7"])
    import psycopg2

DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test_names (id SERIAL, name TEXT)")
cur.execute("INSERT INTO test_names (name) VALUES ('عمار عساف')")
conn.commit()

cur.execute("SELECT * FROM test_names")
results = cur.fetchall()

print("\n📊 النتائج:")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}")

cur.close()
conn.close()
print("🎉 تم الانتهاء!")
