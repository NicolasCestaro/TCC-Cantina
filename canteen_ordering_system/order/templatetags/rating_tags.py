from django import template

register = template.Library()

@register.filter
def pseudo_rating(food):
    """
    Gera um rating pseudo-dinâmico e determinístico baseado no id do objeto.
    Retorna um float entre 3.5 e 5.0 arredondado em 0.5.
    Serve quando não há campo de avaliação no modelo.
    """
    try:
        fid = int(getattr(food, 'id', 0) or 0)
        base = 3.5
        # variação determinística (0,0.3,0.6,0.9,1.2) -> 3.5 .. 4.7 -> truncado a 5.0
        add = (fid % 5) * 0.3
        rating = base + add
        # arredonda para meio (0.5)
        rating = round(min(rating, 5.0) * 2) / 2.0
        return rating
    except Exception:
        return 4.0


@register.filter
def star_list(rating):
    """
    Converte um rating float (ex: 4.5) em lista de 5 strings: 'full', 'half' ou 'empty'.
    Exemplo: 4.5 -> ['full','full','full','full','half']
    """
    try:
        r = float(rating)
    except Exception:
        r = 0.0
    full = int(r)
    half = 1 if (r - full) >= 0.5 else 0
    empty = 5 - full - half
    result = ['full'] * full
    if half:
        result.append('half')
    result.extend(['empty'] * empty)
    return result
