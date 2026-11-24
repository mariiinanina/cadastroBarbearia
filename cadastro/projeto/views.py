from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


@login_required
def barbearia(request):
    """Página da barbearia: só abre se o usuário estiver logado."""
    return render(request, 'projeto/barbearia.html')


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('barbearia')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)  # já entra logado depois de cadastrar
        return redirect('barbearia')
    return render(request, 'projeto/cadastro.html', {'form': form})
