from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("case/<int:id>/", views.caseprofile, name="case"),
    path("allcases/", views.allcases, name="allcases"),
    path("admin/", views.adminPanel, name="login"),
    path("admin/ufqaregister/", views.register, name="adminPanel"),
    path("admin/casos/", views.casos, name="casos"),
    path("admin/casos/vercaso/<int:id>/", views.vercaso, name="vercaso"),
    path("admin/casos/editarcaso/<int:id>/", views.editcase, name="editcase"),
    path("admin/casos/updateCase/<int:id>/", views.createUpdate, name="createUpdate"),
    path("admin/casos/addDonator/<int:id>/", views.addDonator, name="addDonator"),
    path("admin/casos/deleteDonator/<int:id>/", views.deleteDonator, name="deleteDonator"),
    path("admin/casos/subirimg/<int:id>/", views.uploadImg, name="uploadImg"),
    path("admin/casos/borrarimg/<int:id>/", views.deleteImg, name="deleteImg"),
    path("admin/casos/crearcaso/", views.createcase, name="createcase"),
    path("admin/casos/crearcaso/caseUpload/", views.uploadCase, name="uploadCase"),
    path("admin/casos/deleteCase/<int:id>/", views.deleteCase, name="uploadCase"),
    path("admin/contenido/", views.contenido, name="contenido"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)