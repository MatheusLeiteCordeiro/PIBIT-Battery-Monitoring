from multiprocessing import parent_process
from pickle import FALSE
from turtle import color
from django.shortcuts import render
from .models import Thing
from django.http import Http404
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as x
from plotly.offline import plot
from .forms import MyForm
from datetime import datetime



def home(request):
    return render(request, 'template/index.html')


def current_dashboard(request):
    # Dashboard Carga
    def dash():
        fig = make_subplots(
            vertical_spacing=0.5,
            horizontal_spacing=1,
            subplot_titles=(),
            rows=2, cols=2 )
        
        fig.add_trace(x.Bar(
            name='CARGA DA CÉLULA',
            y=[100, 90, 80, 70, 50, 75, 10, 20, 95, 40, 30, 60],
            x=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23]
            ), row=1, col=1 )

        fig.add_trace(x.Scatter(
            name='TENSÃO',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[400, 290, 220, 300, 366, 270, 200], ),
            row=2, col=2
        )

        fig.add_trace(x.Indicator(
            mode="gauge+number",
            value=5,
            title={'text': "Temperatura (C°)"},
            domain={'x': [0, 0.5], 'y': [0, 0.95]}
        ))

        fig.update_layout(
            showlegend=False,
            # template= 'plotly_dark', #modelo
            width=750,  # dimencionamento horizontal da área de plotagem (paper)
            height=1300,  # dimensionamento vertical do paper
            title_xanchor='left',  # posição do título
            # title='Monitoramento de Baterias',
            titlefont={'family': "Arial", 'size': 40, 'color': 'white'},  # dados do título
            legend_orientation="v", legend=dict(x=1, y=1),   # orientação, posição da legenda (séries)
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)', # cor da área do gráfico
            modebar_orientation='h', modebar_bgcolor='steelblue',  # orientação  e cor da modbarra
        )

        # expressura e cor da borda dos gráficos:

        fig.data[0].marker.line.width = 3
        fig.data[0].marker.line.color = 'white'
        fig.data[1].marker.line.width = 3
        fig.data[1].marker.line.color = 'yellow'

        plotar = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
        return plotar

    context = {'plot': dash}

    return render(request, 'template/Battery_Dashboards.html', context)

def tabela (request, id):
    key = request.GET.get('key')
    value = request.GET.get('value')
    #get = Thing.get(data="15/11/2021", hora="15:23")
    context = {'key': key}
    return render(request, 'template/tabela.html', context)


def mvp(request):
    get = Thing.get(chaveP="chave1", chaveC="chave2")
    context = {'item': get}
    return render(request, 'template/item.html', context)


def testecss(request):
    return render(request, 'template/imagemIF.html')


def sla(request):
    def bar():
        get = Thing.get(chaveP="chave1", chaveC="chave2")
        eixo = get.to_dict()
        v0 = eixo["coluna"][0]  # 10
        v1 = eixo["coluna"][1]  # 20
        v2 = eixo["coluna"][2]  # 30
        v3 = eixo["coluna"][3]  # 40
        v4 = eixo["coluna"][4]  # 50

        fig = make_subplots(
            vertical_spacing=0.15,
            horizontal_spacing=0.05,
            rows=1, cols=1
        )
        fig.add_trace(x.Bar(
            name='Tensão',
            x=[1, 2, 3, 4, 5],
            y=[v0, v1, v2, v3, v4]
        ),
            row=1, col=1)

        plotar = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
        return plotar

    context = {'plot1': bar}

    return render(request, 'template/plot.html', context)


def monitoramento_baterias(request):
    def dashboard():
        # get = Thing.get(hash="key1", sort="key2")
        # eixo = get.to_dict()
        # v0 = eixo["coluna"][0]
        # v1 = eixo["coluna"][1]
        # v2 = eixo["coluna"][2]
        # v3 = eixo["coluna"][3]
        # v4 = eixo["coluna"][4]

        fig = make_subplots(
            vertical_spacing=0.15,
            horizontal_spacing=0.05,
            subplot_titles=('', 'CARGA DA CÉLULA', 'CARGA DO BANCO', '', 'CORRENTE', 'TENSÃO'),
            rows=2, cols=3

        )

        fig.add_trace(x.Bar(
            name='CARGA DA CÉLULA',
            x=[50, 40, 30, 20, 15, 10, 5, 100, 90, 80, 70, 60],
            y=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]),
            row=1, col=2
        )

        fig.add_trace(x.Bar(
            name='CARGA DO BANCO',
            x=[5, 100, 90, 80, 70, 60, 50, 40, 30, 20, 15, 10],
            y=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]),
            row=1, col=3
        )

        # noinspection PyTypeChecker
        fig.add_trace(x.Scatter(
            name="CORRENTE",
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[150, 246, 320, 402, 315, 200, 180],
            marker_color='rgba(203, 254, 0, 0.8)',
            hovertemplate='célula3 - %{x} horas - %{y}% de carga'),
            row=2, col=2
        )

        fig.add_trace(x.Scatter(
            name='TENSÃO',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[400, 290, 220, 300, 366, 270, 200], ),
            row=2, col=3
        )

        fig.add_trace(x.Indicator(
            mode="gauge+number",
            value=5,
            title={'text': "temperatura(C°)"},
            domain={'x': [0, 0.2], 'y': [0.4, 1]}
        ))

        fig.update_layout(
            # template= 'plotly_dark', #modelo
            width=1520,  # dimencionamento horizontal da área de plotagem (paper)
            height=700,  # dimensionamento vertical do paper
            title_xanchor='left',  # posição do título
            # title='Monitoramento de Baterias',
            titlefont={'family': "Arial", 'size': 40, 'color': 'white'},  # dados do título
            legend_orientation="v", legend=dict(x=1, y=1),  # orientação, posição da legenda (séries)
            plot_bgcolor='powderblue',  # cor da área do gráfico
            paper_bgcolor='lightgreen',
            modebar_orientation='h', modebar_bgcolor='steelblue',  # orientação  e cor da modbarra
        )

        # expressura e cor da borda dos gráficos:

        fig.data[0].marker.line.width = 3
        fig.data[0].marker.line.color = 'white'

        fig.data[1].marker.line.width = 3
        fig.data[1].marker.line.color = 'white'

        fig.data[2].marker.line.width = 3
        fig.data[2].marker.line.color = 'white'

        fig.data[3].marker.line.width = 3
        fig.data[3].marker.line.color = 'white'

        plotar1 = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)
        return plotar1

    context = {'plotbaterias': dashboard}

    return render(request, 'template/monitoramento-baterias.html', context)


def monitoramento_trafos(request):
    def dashboard():
        # get = Thing.get(hash="key1", sort="key2")
        # eixo = get.to_dict()
        # v0 = eixo["coluna"][0]
        # v1 = eixo["coluna"][1]
        # v2 = eixo["coluna"][2]
        # v3 = eixo["coluna"][3]
        # v4 = eixo["coluna"][4]
        # v5 = v4 + v3
        # v6 = v1 + v2
        # v7 = v5 + v6
        # v8 = v7 - v1

        fig = make_subplots(
            vertical_spacing=0.15,
            horizontal_spacing=0.05,
            subplot_titles=('HARMÔNICO DE TENSÃO', '', 'TENSÃO', 'CORRENTE', '', 'HARMÔNICO DE CORRENTE'),
            rows=2, cols=3
        )

        fig.add_trace(x.Bar(
            name='HARMÔNICOS-T',
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            y=[100, 0, 8, 0, 5, 0, 2, 0, 0]),
            row=1, col=1
        )

        fig.add_trace(x.Bar(
            name='HARMÔNICOS-C',
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            y=[100, 0, 27, 0, 18, 0, 9, 0, 5, 0, 0]),
            row=2, col=3
        )

        fig.add_trace(x.Scatter(
            name='TENSÃO-F1',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[400, 290, 220, 300, 366, 270, 200],
            hovertemplate='FASE1'),
            row=1, col=3
        )

        fig.add_trace(x.Scatter(
            name='TENSÃO-F2',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[233, 345, 382, 250, 97, 157, 270],
            hovertemplate='FASE2'),
            row=1, col=3
        )

        fig.add_trace(x.Scatter(
            name='TENSÃO-F3',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[150, 246, 320, 402, 315, 200, 180],
            hovertemplate='FASE3'),
            row=1, col=3
        )

        fig.add_trace(x.Scatter(
            name='CORRENTE-F1',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[15, 38, 44, 59, 45, 31, 17],
            hovertemplate='FASE1'),
            row=2, col=1
        )

        fig.add_trace(x.Scatter(
            name='CORRENTE-F2',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[30, 46, 62, 42, 35, 18, 10],
            hovertemplate='FASE2'),
            row=2, col=1
        )

        fig.add_trace(x.Scatter(
            name='CORRENTE-F3',
            x=[8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6],
            y=[60, 41, 36, 15, 34, 43, 50],
            hovertemplate='FASE3'),
            row=2, col=1
        )

        fig.add_trace(x.Indicator(
            mode="gauge+number",
            value=50,
            title={'text': "temperatura(C°)"},
            domain={'x': [0.5, 0.3], 'y': [0, 0.3]}
        ))

        fig.add_trace(x.Indicator(
            mode="gauge+number",
            value=0.94,
            title={'text': "FATOR DE POTÊNCIA"},
            domain={'x': [0.5, 0.3], 'y': [0.6, 0.9]}
        ))

        fig.update_layout(
            template='plotly_dark',  # modelo
            width=1520,  # dimencionamento horizontal da área de plotagem (paper)
            height=700,  # dimensionamento vertical do paper
            title_xanchor='left',  # posição do título
            # title='Monitoramento de Baterias',
            titlefont={'family': "Arial", 'size': 40, 'color': 'white'},  # dados do título
            legend_orientation="v", legend=dict(x=1, y=1),  # orientação, posição da legenda (séries)
            plot_bgcolor='#b3093f',  # cor da área do gráfico
            paper_bgcolor='#b3093f',
            modebar_orientation='h', modebar_bgcolor='steelblue',  # orientação  e cor da modbarra
        )

        # expressura e cor da borda dos gráficos:

        fig.data[0].marker.line.width = 3
        fig.data[0].marker.line.color = 'white'

        fig.data[1].marker.line.width = 3
        fig.data[1].marker.line.color = 'white'

        plotar1 = plot(figure_or_data=fig, output_type='div', include_plotlyjs=False)

        return plotar1

    context2 = {'plottrafos': dashboard}

    return render(request, 'template/monitoramento-trafos.html', context2)
