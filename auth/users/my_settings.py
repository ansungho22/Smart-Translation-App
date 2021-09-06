MY_DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'test',
        'USER':'root',
        'PASSWORD':'1234',
        'HOST':'localhost',
        'PORT':'3306',
         'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4', # 테이블 생성 자동으로 해줄때 쓸 인코딩,, 이거안하면 밑에꺼해도 효과 엑스
            'use_unicode': True,
        },
    }
}
MY_SECRET_KEY = 'django-insecure-=_zn)-q8nt@wqdoj7_s$x8^0pu!mb**p=c72a^kfs#ugr9le+7'