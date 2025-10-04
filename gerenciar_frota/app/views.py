from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import VeiculoForm, MotoristaForm, EntregaForm, ManutencaoForm
from .models import Veiculo, Motorista, Entrega, Manutencao, Abastecimento, Coordenada
def index(request):
    return render(request,'index.html')
# Sistema
def cadastrarVeiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            VeiculoForm.save()
            messages.success(request, 'Veículo cadastrado com sucesso')
            return redirect('listaVeiculos')
        else:
            messages.error(request, 'Erro ao cadastrar o veículo')
    else:
        form = VeiculoForm()

    return render(request, 'cadastrarVeiculo.html', {'form': form})

def cadastrarMotorista(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            MotoristaForm.save()
            messages.success(request, 'Motorista cadastrado com sucesso')
            return redirect('listaMotoristas')
        else:
            messages.error(request, 'Erro ao cadastrar o motorista')
    else:
        form = MotoristaForm()

    return render(request, 'cadastrarMotorista.html', {'form': form})

def cadastrarEntrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            EntregaForm.save()
            messages.success(request, 'Entrega cadastrada com sucesso')
            return redirect('listaEntregas')
        else:
            messages.error(request, 'Erro ao cadastrar a entrega')
    else:
        form = EntregaForm()
    return render(request, 'cadastrarEntrega.html', {'form': form})


def veiculosDisponiveis(request):
def motoristasDisponiveis(request):

# Veiculo
def atualizarKm(request):

# Manutenção
def realizarManutencao(request):
def proxManutencao(request):
def verificarManutencoes(request):
def agendarManutencao(request):
def alertaManutencao(request):

# Motorista
def abastecer(request):
def solicitarManutencao(request):

# Entrega
def iniciarEntrega(request):
def monitorarEntrega(request):
def atualizarStatus(request):
def atualizarCoordenada(request):
def concluirEntrega(request):
def alertaStatus(request): 