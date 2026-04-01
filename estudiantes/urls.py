from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # ── Autenticación ────────────────────────────────────────────────────────
    path('login/',  auth_views.LoginView.as_view(),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ── Páginas ──────────────────────────────────────────────────────────────
    path('',                              views.inicio,    name='inicio'),
    path('nosotros/',                     views.nosotros,  name='nosotros'),

    # ── Estudiantes CRUD ─────────────────────────────────────────────────────
    path('estudiantes/',                  views.estudiantes, name='estudiantes'),
    path('estudiantes/crear/',            views.crear,       name='crear'),
    path('estudiantes/editar/<int:id>',   views.editar,      name='editar'),
    path('estudiantes/detalle/<int:id>/', views.detalle,     name='detalle'),
    path('eliminar/<int:id>/',            views.eliminar,    name='eliminar'),

    # ── Asistencia / Almuerzo ────────────────────────────────────────────────
    path('estudiantes/almuerzo/',         views.almuerzo,    name='almuerzo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
