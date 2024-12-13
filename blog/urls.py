from django.urls import path
from .views import home_view, register_view, login_view, profile_view, logout_view, edit_profile_view, user_blogs_view, \
    create_blog_view, blog_detail_view, edit_blog_view, edit_comment_view, delete_comment_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('profile/edit/', edit_profile_view, name='edit-profile'),
    path('user-blogs/', user_blogs_view, name='user-blogs'),
    path('create-blog/', create_blog_view, name='create-blog'),
    path('edit-blog/<int:id>', edit_blog_view, name='edit-blog'),
    path('blog/<int:id>/', blog_detail_view, name='blog-detail'),
    path('edit-comment/<int:id>', edit_comment_view, name='edit-comment'),
    path('delete-comment/<int:id>', delete_comment_view, name='delete-comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)