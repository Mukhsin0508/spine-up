from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .yasg import schema_view
# from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Add this line for language switching



    # ================== Django Project API URLS ====================
    path('api/v1/', include("apps.amocrm.urls")),
    path('api/v1/', include("apps.chatbot.urls")),
    path('api/v1/', include("apps.vacancy.urls")),
    path('api/v1/', include("apps.web.urls")),
    path('api/v1/', include("apps.products.urls")),



    # ==================== Swagger and Redoc ====================
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Translated URL patterns
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    # Add other URL patterns that should be translated here
)

# # Debug toolbar URLs
# urlpatterns += debug_toolbar_urls()