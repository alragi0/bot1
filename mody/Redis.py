from redis import StrictRedis

# تعيين المعلمات الخاصة بالاتصال
host = "containers-us-west-143.railway.app"  # عنوان خادم Redis
port = 7622  # المنفذ الذي ترغب في استخدامه
password = "WktZRmP7Q7PmlT3sasBY"  # كلمة المرور إذا كانت مطلوبة

# إنشاء اتصال Redis
db = StrictRedis(host=host, port=port, password=password, decode_responses=True)

# الآن يمكنك استخدام الاتصال db للقيام بالعمليات على خادم Redis بالمنفذ المحدد
