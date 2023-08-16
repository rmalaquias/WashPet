from django.urls import path
from reserva.views import criar_reserva, contato


app_name = 'reserva'
app_name = 'contato'

urlpatterns = [
    path ('criar_reserva', criar_reserva, name = "criar_reserva"),
    path ('contato/', contato, name='contato')
]

