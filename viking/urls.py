from django.urls import path
from . import views
from viking.views import( 
AanmeldView ,
 activityPage ,
apiOverview, 
createRoom, deleteMessage, deleteRoom,
KluisPage,
erv_createRoom,
erv_deleteMessage,
erv_deleteRoom,
PloegPage,
erv_loginPage,
erv_room,
urv_updateKluis,
erv_updateUser,
erv_userProfile,
events, 
home,
taak_rooster,
gebruikerslijst,
loginPage, logoutUser,
personenlijst,
recurrent_event,
registerPage, room, 
topicsPage, updateRoom, updateUser, userProfile,
vote, kluis,
DetailView,
aantalregels,
ploeg_participants
)

urlpatterns = [
    path('', home, name='home'),
    path('viking', home, name='home'),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('topics/', topicsPage, name="topics"),
    path('update-user/', updateUser, name="update-user"),
    path('register/', registerPage, name="register"),    
    path('profile/<str:pk>/', userProfile, name='user-profile'),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', deleteMessage, name='delete-message'),
    path('activity/', activityPage, name="activity"),
    path('room/<str:pk>/', room, name='room'),    


    path('recurrent/', recurrent_event, name='recurrent'),
    path('<int:room_id>/aanmelden/',vote, name='vote'),  
    path('<int:kluis_id>/kluisjes/',kluis, name='kluis'),  
    path('<int:pk>/update-kluis/',urv_updateKluis, name='update-kluis'),  
    path('ploegbeheer/',PloegPage , name="ploegbeheer"),
    path('kluisbeheer/',KluisPage , name="kluisbeheer"),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('api/person/', personenlijst,name='api-person'),    
    path('api/gebruikers/', gebruikerslijst,name='api-gebruikers'),    
    path('api/', apiOverview,name='api-overview'),    
    path('api/aantalregels/', aantalregels,name='api-aantalregels'),    
    path('ploegparticipants/', ploeg_participants,name='ploegparticipants'),    
    path('taakrooster/', taak_rooster, name='taakrooster'),
    path('events/', events, name='events'),
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>/', views.getNote, name="note"),

    ]
# https://docs.djangoproject.com/en/3.1/topics/http/urls/