from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save()
            # Enviar email para o usuário
            send_mail(
                'Confirmação de Registro',
                f'Olá {registro.nome}, obrigado por se registrar no clube Guardiões Dourados!',
                'seu-email@dominio.com',
                [registro.email],
                fail_silently=False,
            )
            # Enviar email para o administrador
            send_mail(
                'Novo Registro no Clube',
                f'Nome: {registro.nome}\nEmail: {registro.email}\nTelefone: {registro.telefone}',
                'seu-email@dominio.com',
                ['email_admin@dominio.com'],
                fail_silently=False,
            )
            return redirect('registro_sucesso')
    else:
        form = RegistroForm()

    return render(request, 'registro/registro.html', {'form': form})

def registro_sucesso_view(request):
    return render(request, 'registro/sucesso.html')
