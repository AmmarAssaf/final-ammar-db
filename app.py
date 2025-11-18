import os
import psycopg2

print("=" * 50)
print("🚀 نظام تخزين اسم عمار عساف - بدء التشغيل")
print("=" * 50)

try:
    # الحصول على رابط قاعدة البيانات من Render
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    if not DATABASE_URL:
        print("❌ خطأ: لم يتم العثور على رابط قاعدة البيانات")
        exit()
    
    print("✅ تم العثور على رابط قاعدة البيانات")
    
    # تحويل الرابط ليكون متوافقاً مع PostgreSQL
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    # الاتصال بقاعدة البيانات
    print("🔗 جارٍ الاتصال بقاعدة البيانات...")
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    print("✅ تم الاتصال بقاعدة البيانات بنجاح!")
    
    # إنشاء مؤشر للتعامل مع قاعدة البيانات
    cursor = connection.cursor()
    
    # إنشاء الجدول إذا لم يكن موجوداً
    print("📊 جارٍ إنشاء الجدول...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ammar_names (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    print("✅ تم إنشاء الجدول 'ammar_names' بنجاح!")
    
    # إدخال اسم "عمار عساف"
    print("📝 جارٍ إدخال الاسم في قاعدة البيانات...")
    cursor.execute("INSERT INTO ammar_names (full_name) VALUES (%s)", ("عمار عساف",))
    connection.commit()
    print("✅ تم إدخال الاسم 'عمار عساف' بنجاح!")
    
    # استعراض جميع الأسماء في الجدول
    print("\n🔍 جارٍ استعراض البيانات...")
    cursor.execute("SELECT * FROM ammar_names ORDER BY created_at DESC")
    all_names = cursor.fetchall()
    
    print("\n" + "=" * 60)
    print("📋 جميع الأسماء المخزنة في قاعدة البيانات:")
    print("=" * 60)
    
    for name_record in all_names:
        record_id = name_record[0]
        name_value = name_record[1]
        created_time = name_record[2]
        print(f"🆔 الرقم: {record_id} | الاسم: {name_value} | الوقت: {created_time}")
    
    print("=" * 60)
    
    # عرض إحصائية
    cursor.execute("SELECT COUNT(*) FROM ammar_names")
    total_count = cursor.fetchone()[0]
    print(f"\n📊 إجمالي عدد الأسماء المسجلة: {total_count}")
    
    # تنظيف الموارد
    cursor.close()
    connection.close()
    
    print("\n" + "🎉" * 20)
    print("✅ تم تنفيذ البرنامج بنجاح!")
    print("✅ تم تخزين اسم 'عمار عساف' في قاعدة البيانات!")
    print("🎉" * 20)
    
except Exception as error:
    print(f"\n❌ حدث خطأ أثناء التنفيذ: {error}")
    print("🔧 يرجى التحقق من إعدادات قاعدة البيانات في Render")
