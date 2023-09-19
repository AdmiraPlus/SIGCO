from django.urls import path

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

from views import registrar_usuario, iniciar_sesion, cerrar_sesion

urlpatterns = [
	path('registrar/', registrar_usuario, name='registrar_usuario'),
	path('sesion/iniciar/', iniciar_sesion, name='iniciar_sesion'),
	path('sesion/cerrar/', cerrar_sesion, name='cerrar_sesion'),
	
	path('password/reset/', PasswordResetView.as_view(
		template_name='password-reset.html'),
		name='password_reset'),
	path('password/reset/done/', PasswordResetDoneView.as_view(
		template_name="password-reset-done.html"),
		name='password_reset_done'),
	path('password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
		template_name='password-confirm.html'),
		name='password_reset_confirm'),
	path('password/reset/complete/', PasswordResetCompleteView.as_view(
		template_name="password-reset-complete.html"),
		name='password_reset_complete'),
]
