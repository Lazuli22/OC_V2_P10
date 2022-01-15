"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import ProjectsViewset
from core.views import AdminUsersViewset
from contributor.views import ContributorDetailView, ContributorsViewset
from issue.views import IssuesList, IssueDetail

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘projects’ et notre view
router.register('projects', ProjectsViewset, basename='projects')
router.register('contributors', ContributorsViewset, basename='contributors')
router.register('admin/signup', AdminUsersViewset, basename='admin-users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/projects/<int:id>/contributors/<int:pk>/', ContributorDetailView.as_view()),
    path('api/projects/<int:id>/issues/', IssuesList.as_view()),
    path('api/projects/<int:id>/issues/<int:pk>/', IssueDetail.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
