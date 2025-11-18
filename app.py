import os
import psycopg2

print("🚀 بدء البرنامج...")

try:
    DATABASE_URL = os.getenv('DATABASE_URL')
    print("📊 تم الحصول على رابط قاعدة البيانات")
    
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    print("✅ تم الاتصال بقاعدة البيانات!")
    
    cur = conn.cursor()
    
    # إنشاء جدول
    cur.execute("CREATE TABLE IF NOT EXISTS ammar_table (id SERIAL PRIMARY KEY, name TEXT)")
    conn.commit()
    print("✅ تم إنشاء الجدول!")
    
    # إدخال الاسم
    cur.execute("INSERT INTO ammar_table (name) VALUES ('عمار عساف')")
    conn.commit()
    print("✅ تم إدخال 'عمار عساف'!")
    
    # عرض البيانات
    cur.execute("SELECT * FROM ammar_table")
    results = cur.fetchall()
    
    print("\n📋 النتائج:")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}")
    
    cur.close()
    conn.close()
    print("🎉 تم الانتهاء بنجاح!")
    
except Exception as e:
    print(f"❌ خطأ: {e}")
