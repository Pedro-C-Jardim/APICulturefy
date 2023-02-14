from flask import Flask, Response
from flask_restful import Resource, Api, reqparse
import numpy as np
import random
import json

app = Flask(__name__)
api = Api(app)

empresas = {}

valores = ["Acusação","Agressividade","Ameaça/Medo","Apadrinhamento","Aversão a Riscos","Burocracia","Caos/Confusão","Cautela","Conflito","Coragem","Estabilidade Financeira","Exploração","Falta de Escrúpulos","Foco de Curto Prazo","Ganância","Individualismo/Egoísmo","Inveja","Oportunismo","Poder","Politicagem","Redução de Custos","Reputação Pessoal","Retenção de Informações","Sobrevivência","Tirar vantagem","Segurança do emprego","Conhecimento Técnico","Controle","Descuido","Disciplina","Exigência","Hierarquia","Justiça","Mentalidade de Silos/Departamentalização","Morosidade","Ordem","Permissividade","Planejamento","Respeito","Rigidez","Abertura para novas ideias","Accountability","Acúmulo de Informações","Adaptabilidade","Agilidade/Velocidade","Ambição","Aprendizado Contínuo","Aptidão a Risco","Atenção aos detalhes","Autenticidade/Originalidade","Autoconhecimento","Autonomia/Independência/Liberdade","Competição Interna","Competitividade","Consciência de Custos","Crescimento Organizacional","Crescimento Pessoal","Crescimento Profissional","Criatividade","Curiosidade","Dar o melhor de si","Eficiência/Produtividade","Entusiasmo","Excelência/Competência","Feedback","Imagem da marca","Inclinação para a ação/Iniciativa","Inovação","Longas jornadas de trabalho","Lucro","Manipulação","Meritocracia","Metas","Otimismo","Qualidade","Satisfação do Cliente","Simplicidade/Frugalidade","Status","Superficialidade","Bem Estar/Saúde e Segurança dos Colaboradores","Coaching/Mentoria","Colaboração/Trabalho em Equipe","Complementaridade de ideias","Comprometimento","Comunicação Direta","Conexão Pessoal/Amizade","Confiança","Decisão Compartilhada","Diálogo/Escuta","Equilíbrio Emocional","Equilíbrio Pessoal-Profissional","Humildade","Humor/Diversão","Integridade/Honestidade","Reconhecimento","Transparência/Clareza","Bem futuro","Consciência Ambiental","Cuidado com o Outro/Altruísmo/Empatia","Generosidade","Fazer a diferença","Imparcialidade","Interdependência","Paixão","Perspectiva de Longo Prazo","Pluralidade/Diversidade/Inclusão","Responsabilidade Social","Segurança Psicológica","Visão Compartilhada"]


class Pedido(Resource):
    def get(self, cid):

        id = cid

        if(id not in empresas):
            n = random.sample(range(0,107), 54)
            controle = np.zeros(108)

            ListaValores = []
            for i in n:
                controle[i] = 1
                ListaValores.append(valores[i])

            empresas[id] = controle
        else:
            controle = empresas.get(id)

            ListaValores = []
            for i in range(0, len(controle)):
                if(controle[i] == 0):
                    ListaValores.append(valores[i])
            
            empresas.pop(id)

        ListaDic = []
        for i in ListaValores:
            ListaDic.append({'nome': i})
        
        ListaValores = json.dumps(ListaDic)
        return Response(ListaValores, mimetype='application/json')

api.add_resource(Pedido, '/<string:cid>')

if __name__ == '__main__':
    app.run(debug=True)

