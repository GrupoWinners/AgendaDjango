import json
from datetime import date

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Evento


def resposta(evento):
    return {
        "id": evento.id,
        "titulo": evento.titulo,
        "descricao": evento.descricao,
        "data": evento.data.isoformat(),
        "local": evento.local,
    }


def ler_json(request):
    try:
        dados = json.loads(request.body)
        return dados if isinstance(dados, dict) else None
    except (ValueError, UnicodeDecodeError):
        return None


def validar(dados):
    if dados is None:
        return None, "Envie um objeto JSON válido."

    for campo in ("titulo", "data", "local"):
        valor = dados.get(campo)
        if not isinstance(valor, str) or not valor.strip():
            return None, f"O campo {campo} é obrigatório."

    titulo = dados["titulo"].strip()
    local = dados["local"].strip()
    descricao = dados.get("descricao", "")

    if len(titulo) > 120 or len(local) > 120:
        return None, "Título e local devem ter até 120 caracteres."

    if not isinstance(descricao, str):
        return None, "A descrição deve ser um texto."

    try:
        data_evento = date.fromisoformat(dados["data"])
    except ValueError:
        return None, "Data inválida. Utilize AAAA-MM-DD."

    return {
        "titulo": titulo,
        "descricao": descricao,
        "data": data_evento,
        "local": local,
    }, None


@csrf_exempt
def lista_eventos(request):
    if request.method == "GET":
        eventos = Evento.objects.order_by("data", "id")
        return JsonResponse(
            [resposta(e) for e in eventos],
            safe=False
        )

    if request.method == "POST":
        dados, erro = validar(ler_json(request))
        if erro:
            return JsonResponse({"erro": erro}, status=400)

        evento = Evento.objects.create(**dados)
        return JsonResponse(resposta(evento), status=201)

    return JsonResponse(
        {"erro": "Método não permitido."}, status=405
    )


@csrf_exempt
def detalhe_evento(request, id):
    evento = Evento.objects.filter(id=id).first()

    if evento is None:
        return JsonResponse(
            {"erro": "Evento não encontrado."}, status=404
        )

    if request.method == "GET":
        return JsonResponse(resposta(evento))

    if request.method == "PUT":
        dados, erro = validar(ler_json(request))
        if erro:
            return JsonResponse({"erro": erro}, status=400)

        for campo, valor in dados.items():
            setattr(evento, campo, valor)

        evento.save()
        return JsonResponse(resposta(evento))

    if request.method == "DELETE":
        evento.delete()
        return HttpResponse(status=204)

    return JsonResponse(
        {"erro": "Método não permitido."}, status=405
    )