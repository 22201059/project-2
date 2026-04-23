from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # <-- add include
from users import views as userviews
from myapp import views as myviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home, name='home'),
    path('about/', myviews.about, name='about'),
    path('tickets/', myviews.ticket_list, name='all_tickets'),
    path('tickets_details/<str:id>', myviews.ticket_details, name='ticket_details'),
    path('upload/', myviews.upload_ticket, name='upload_ticket'),
    path('update/<str:id>', myviews.update_ticket, name='update_ticket'),
    path('delete/<str:id>', myviews.delete_ticket, name='delete'),
    path('login/', userviews.login_view, name='login'),
    path('signup/', userviews.register_view, name='signup'),
    path('welcome/', userviews.welcome_view, name='welcome'),
    path('users/', include('users.urls')),
    path('help/', myviews.help, name='help'),
    path('purchase/<int:ticket_id>/', myviews.purchase_ticket, name='purchase_ticket'),
    path('contact/', myviews.contact, name='contact'),
   
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

