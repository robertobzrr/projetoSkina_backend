from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Produto, Categoria_Produto
from .serializers import CategoriaSerializer, ProdutosSerializer, Categoria_ProdutoSerializer
from django.http import HttpResponse
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoriaFilter, ProdutoFilter, Categoria_ProdutoFilter


def home(request):
    return HttpResponse("<h1> OF THE KING OF THE POWER</h1>")


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoriaFilter



class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProdutoFilter



class Categoria_ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria_Produto.objects.all()
    serializer_class = Categoria_ProdutoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = Categoria_ProdutoFilter




# class ListaViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Lista.objects.all()
#     serializer_class = ListaSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = ListaFilter





# class Lista_ProdutosViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Lista_Produtos.objects.all()
#     serializer_class = Lista_ProdutosSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = Lista_ProdutosFilter

